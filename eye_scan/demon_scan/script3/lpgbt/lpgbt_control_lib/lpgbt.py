#!/usr/bin/env python3
###############################################################################
#                                                                             #
#  Copyright (C) 2018 lpGBT Team, CERN                                        #
#                                                                             #
#  This IP block is free for HEP experiments and other scientific research    #
#  purposes. Commercial exploitation of a chip containing the IP is not       #
#  permitted.  You can not redistribute the IP without written permission     #
#  from the authors. Any modifications of the IP have to be communicated back #
#  to the authors. The use of the IP should be acknowledged in publications,  #
#  public presentations, user manual, and other documents.                    #
#                                                                             #
#  This IP is distributed in the hope that it will be useful, but WITHOUT ANY #
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS  #
#  FOR A PARTICULAR PURPOSE.                                                  #
#                                                                             #
###############################################################################
"""lpGBT driver code common to all chip revisions"""
# pylint: disable=too-many-lines, too-many-branches

import time
import inspect
import numpy as np
import matplotlib.pyplot as plt
from .lpgbt_enums import LpgbtEnums
from .lpgbt_pins import LpgbtPins
from .lpgbt_register_map import LpgbtRegisterMap
from .lpgbt_exceptions import (
    LpgbtTimeoutError,
    LpgbtI2CMasterBusError,
    LpgbtI2CMasterTransactionError,
    LpgbtFuseError,
)


def u32_to_bytes(val):
    """Converts u32 to 4 bytes"""
    byte3 = (val >> 24) & 0xFF
    byte2 = (val >> 16) & 0xFF
    byte1 = (val >> 8) & 0xFF
    byte0 = (val >> 0) & 0xFF
    return (byte3, byte2, byte1, byte0)


def lpgbt_accessor(method):
    """Decorator for methods accessing the lpGBT via its register interfaces

    This decorator handles the communication interface management.
    Any decorated method may be called with a 'comm_intf' argument, specifying
    the communication interface to be used for execution of this command.
    """
    # pylint: disable=protected-access
    def decorator(self, *args, **kwargs):
        comm_intf = kwargs.pop("comm_intf", None)

        # sanitize comm_intf if supplied
        if comm_intf is not None and comm_intf not in self._comm_intfs:
            raise KeyError("Invalid communication interface specified.")

        # fail in case two methods on the call stack try to force a specific interface
        if comm_intf is not None and self._current_comm_intf is not None:
            raise RuntimeError(
                "Conflicting communication interface overrides specified."
            )

        # apply an interface override if specified
        if self._current_comm_intf is None and comm_intf:
            self._current_comm_intf = comm_intf

        # call the original method, clear interface override in case of comms errors and re-raise
        try:
            retval = method(self, *args, **kwargs)
        except Exception as error:
            self._current_comm_intf = None
            raise error

        # in case we were the ones forcing a specific interface, reset it after we're done
        if comm_intf is not None:
            self._current_comm_intf = None

        return retval

    return decorator


class Lpgbt(LpgbtPins, LpgbtEnums, LpgbtRegisterMap):
    """Implementation of lpGBT driver code common to all chip revisions"""

    # pylint: disable=too-many-public-methods

    def __init__(self, logger):
        self.logger = logger
        self._comm_intfs = {}
        self._default_comm_intf = None
        self._current_comm_intf = None
        self._ctrl_pin_methods = None

    #
    # Register Access
    #

    def decode_reg_addr(self, reg_addr):
        """Decode reg_addr to int"""

        if inspect.isclass(reg_addr):
            reg_addr = reg_addr.address
        return reg_addr

    def register_comm_intf(self, name, write_regs, read_regs, default=False):
        """Registers a new communications interface.

        Arguments:
            name: arbitrary string, used to reference this interface for read/writes
            write_regs: method reference for writing N registers, must accept two named parameters
                reg_addr: first write register address
                reg_vals: list of values to write
            read_regs: method reference for reading N registers, must accept two named parameters
                reg_addr: first read register address
                read_len: number of registers to read
                must return a list of register values read
        """
        if name in self._comm_intfs:
            raise KeyError("Interface with same name already registered.")

        self._comm_intfs[name] = {"write_regs": write_regs, "read_regs": read_regs}

        if default:
            self._default_comm_intf = name

    @lpgbt_accessor
    def write_reg(self, reg_addr, reg_val):
        """Writes a single register via selected control interface

        Arguments:
            reg_addr: register address
            reg_val: register value to write
        """

        reg_addr = self.decode_reg_addr(reg_addr)

        self.logger.debug("[%s] = 0x%02x", self.Reg(reg_addr).name, int(reg_val))

        self.write_regs(reg_addr, [reg_val])


    @lpgbt_accessor
    def write_regs(self, reg_addr, reg_vals):
        """Writes multiple registers via selected control interface

        Arguments:
            reg_addr: register address
            reg_vals: register values to write
        """

        reg_addr = self.decode_reg_addr(reg_addr)

        comm_intf = self._current_comm_intf or self._default_comm_intf

        self._comm_intfs[comm_intf]["write_regs"](reg_addr=reg_addr, reg_vals=reg_vals)


    @lpgbt_accessor
    def read_reg(self, reg_addr):
        """Reads a single register via selected control interface

        Arguments:
            reg_addr: register address

        Returns:
            Register value
        """

        reg_addr = self.decode_reg_addr(reg_addr)
        reg_val = self.read_regs(reg_addr, 1)[0]
        self.logger.debug("[%s] = 0x%02x", self.Reg(reg_addr).name, int(reg_val))
        return reg_val

    @lpgbt_accessor
    def read_regs(self, reg_addr, read_len):
        """Reads multiple registers via selected control interface

        Arguments:
            reg_addr: register address
            read_len: number of registers to read

        Returns:
            Register values
        """
        reg_addr = self.decode_reg_addr(reg_addr)
        comm_intf = self._current_comm_intf or self._default_comm_intf
        data = self._comm_intfs[comm_intf]["read_regs"](
            reg_addr=reg_addr, read_len=read_len
        )
        return data

    #
    # Control Pin Access
    #
    def register_ctrl_pin_access(self, write_pin, read_pin):
        """Register methods for control pin access.

        Arguments:
            write_pin: method for writing a single control pin, using two parameters
                pin_name: name of the control pin to write
                value: value to write to the pin (bool)
            read_pin: method for reading a single control pin, using one parameter
                pin_name: name of the control pin to read
                must return value of the control pin
        """
        self._ctrl_pin_methods = {"write": write_pin, "read": read_pin}

    def set_ctrl_pin(self, pin_name, value):
        """Sets a single control pin using the registered implementation

        Arguments:
            pin_name: control pin to set (see lpgbt_constants)
            value: boolean value to write
        """
        if self._ctrl_pin_methods is None:
            raise RuntimeError("No write method for control pins defined.")
        if pin_name not in self.CTRL_OUT_PINS:
            raise ValueError("Invalid control pin name provided.")

        self._ctrl_pin_methods["write"](pin_name, bool(value))

    def get_ctrl_pin(self, pin_name):
        """Reads a single control pin using the registered implementation

        Arguments:
            pin_name: control pin to read (see lpgbt_constants)

        Returns:
            Control pin state
        """
        if self._ctrl_pin_methods is None:
            raise RuntimeError("No read method for control pins defined.")
        if pin_name not in self.CTRL_IN_PINS:
            raise ValueError("Invalid control pin name provided.")

        return self._ctrl_pin_methods["read"](pin_name)

    def set_mode_pins(self, mode):
        """Sets the mode of operation using the MODE pins

        Arguments:
            mode: operation mode to set (sett lpgbt_constants)
        """
        assert mode in range(16), "Mode only has 4 bits (0-15)"

        self.set_ctrl_pin(self.CTRL_MODE0, mode & 0x01)
        self.set_ctrl_pin(self.CTRL_MODE1, mode & 0x02)
        self.set_ctrl_pin(self.CTRL_MODE2, mode & 0x04)
        self.set_ctrl_pin(self.CTRL_MODE3, mode & 0x08)

    def set_address_pins(self, address):
        """Sets LSB of the lpGBT address using the ADDR pins

        Arguments:
            address: lpGBT address LSBs
        """
        assert address in range(16), "Address has only 4 bits (0-15)"

        self.set_ctrl_pin(self.CTRL_ADDR0, address & 0x01)
        self.set_ctrl_pin(self.CTRL_ADDR1, address & 0x02)
        self.set_ctrl_pin(self.CTRL_ADDR2, address & 0x04)
        self.set_ctrl_pin(self.CTRL_ADDR3, address & 0x08)

    def ctrl_pins_default(self):
        """Sets all control pins to their default values"""
        self.set_ctrl_pin(self.CTRL_RSTB, True)
        self.set_ctrl_pin(self.CTRL_LOCKMODE, self.LockMode.REFERENCELESS)
        self.set_address_pins(0)
        self.set_mode_pins(self.LpgbtMode.TX_5G_FEC5)
        self.set_ctrl_pin(self.CTRL_PORDIS, False)

    def ready(self):
        """Returns state of READY pin"""
        return self.get_ctrl_pin(self.CTRL_READY)

    def generate_reset_pulse(self, pulse_width=0.001):
        """Generates a reset pulse of given length"""
        self.set_ctrl_pin(self.CTRL_RSTB, False)
        time.sleep(pulse_width)
        self.set_ctrl_pin(self.CTRL_RSTB, True)

    #
    # Helpers for register configuration
    #
    @lpgbt_accessor
    def read_mode(self):
        """Returns the lpGBT mode from the CONFIGPINS register"""
        configpins = self.read_reg(self.CONFIGPINS)
        return configpins >> self.CONFIGPINS.LPGBTMODE.offset

    @lpgbt_accessor
    def clock_generator_setup(self):
        """Writes the default configuration for the lpGBT clock generator"""
        self.write_reg(
            self.REFCLK,
            self.REFCLK.REFCLKACBIAS.bit_mask | self.REFCLK.REFCLKTERM.bit_mask,
        )

        self.write_reg(
            self.CLKGCONFIG0,
            (
                0x0E << self.CLKGCONFIG0.CLKGCALIBRATIONENDOFCOUNT.offset
                | 0x08 << self.CLKGCONFIG0.CLKGBIASGENCONFIG.offset
            ),
        )
        self.write_reg(
            self.CLKGCONFIG1,
            (
                self.CLKGCONFIG1.CLKGCDRRES.bit_mask
                | self.CLKGCONFIG1.CLKGVCORAILMODE.bit_mask
                | 8 << self.CLKGCONFIG1.CLKGVCODAC.offset
            ),
        )
        self.write_reg(
            self.CLKGPLLINTCUR,
            (
                9 << self.CLKGPLLINTCUR.CLKGPLLINTCURWHENLOCKED.offset
                | 9 << self.CLKGPLLINTCUR.CLKGPLLINTCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGPLLPROPCUR,
            (
                9 << self.CLKGPLLPROPCUR.CLKGPLLPROPCURWHENLOCKED.offset
                | 9 << self.CLKGPLLPROPCUR.CLKGPLLPROPCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGPLLRES,
            (
                2 << self.CLKGPLLRES.CLKGPLLRESWHENLOCKED.offset
                | 2 << self.CLKGPLLRES.CLKGPLLRES.offset
            ),
        )
        self.write_reg(
            self.CLKGFFCAP,
            (
                3 << self.CLKGFFCAP.CLKGFEEDFORWARDCAPWHENLOCKED.offset
                | 3 << self.CLKGFFCAP.CLKGFEEDFORWARDCAP.offset
            ),
        )
        self.write_reg(
            self.CLKGCDRINTCUR,
            (
                5 << self.CLKGCDRINTCUR.CLKGCDRINTCURWHENLOCKED.offset
                | 5 << self.CLKGCDRINTCUR.CLKGCDRINTCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGFLLINTCUR,
            (
                5 << self.CLKGFLLINTCUR.CLKGFLLINTCURWHENLOCKED.offset
                | 5 << self.CLKGFLLINTCUR.CLKGFLLINTCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGCDRPROPCUR,
            (
                5 << self.CLKGCDRPROPCUR.CLKGCDRPROPCURWHENLOCKED.offset
                | 5 << self.CLKGCDRPROPCUR.CLKGCDRPROPCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGCDRFFPROPCUR,
            (
                6 << self.CLKGCDRFFPROPCUR.CLKGCDRFEEDFORWARDPROPCURWHENLOCKED.offset
                | 6 << self.CLKGCDRFFPROPCUR.CLKGCDRFEEDFORWARDPROPCUR.offset
            ),
        )
        self.write_reg(
            self.CLKGLFCONFIG0,
            (
                self.CLKGLFCONFIG0.CLKGLOCKFILTERENABLE.bit_mask
                | 15 << self.CLKGLFCONFIG0.CLKGLOCKFILTERLOCKTHRCOUNTER.offset
            ),
        )
        self.write_reg(
            self.CLKGLFCONFIG1,
            (
                15 << self.CLKGLFCONFIG1.CLKGLOCKFILTERRELOCKTHRCOUNTER.offset
                | 15 << self.CLKGLFCONFIG1.CLKGLOCKFILTERUNLOCKTHRCOUNTER.offset
            ),
        )
        self.write_reg(
            self.CLKGWAITTIME,
            (8 << self.CLKGWAITTIME.CLKGWAITCDRTIME.offset)
            | 8 << self.CLKGWAITTIME.CLKGWAITPLLTIME.offset,
        )

        self.eprx_general_config()

    def _eprx_general_config(
        self,
        dll_current=1,
        dll_confirm_count=2,
        coarse_lock_detection=True,
        fsm_clk_always_on=False,
        reinit_enable=False,
    ):
        """General configuration for ePortRxGroups

        Arguments:
            dll_current: Current for the DLL charge pump
            dll_confirm_count: Number of clock cycles (in the 40 MHz clock domain) to
                               confirm locked state
            coarse_lock_detection: Use coarse detector for the DLL lock condition
            reinit_enable: Allow re-initialization in ePortRxGroup when the tuning is out of range.
        """
        # pylint: disable=too-many-arguments
        assert dll_current in range(4), "Invalid dll_current"
        assert dll_confirm_count in range(4), "Invalid dll_confirm_count"

        dll_config = dll_current << self.EPRXDLLCONFIG.EPRXDLLCURRENT.offset
        dll_config |= dll_confirm_count << self.EPRXDLLCONFIG.EPRXDLLCONFIRMCOUNT.offset
        if coarse_lock_detection:
            dll_config |= self.EPRXDLLCONFIG.EPRXDLLCOARSELOCKDETECTION.bit_mask
        if fsm_clk_always_on:
            dll_config |= self.EPRXDLLCONFIG.EPRXDLLFSMCLKALWAYSON.bit_mask
        if reinit_enable:
            dll_config |= self.EPRXDLLCONFIG.EPRXENABLEREINIT.bit_mask
        return dll_config

    def eprx_general_config(
        self,
        dll_current=1,
        dll_confirm_count=2,
        coarse_lock_detection=True,
        data_gating_enable=True,
        fsm_clk_always_on=False,
        reinit_enable=False,
    ):
        """General configuration for ePortRxGroups

        Arguments:
            dll_current: Current for the DLL charge pump
            dll_confirm_count: Number of clock cycles (in the 40 MHz clock domain) to
                               confirm locked state
            coarse_lock_detection: Use coarse detector for the DLL lock condition
            data_gating_enable: Enable data gating.
            reinit_enable: Allow re-initialization in ePortRxGroup when the tuning is out of range.
        """
        # pylint: disable=too-many-arguments, unused-argument
        raise NotImplementedError("eprx_general_config is not implemented in Lpgbt")

    @lpgbt_accessor
    def high_speed_io_invert(self, invert_data_out=False, invert_data_in=False):
        """Configures the high-speed link inversion feature

        Arguments:
            invert_data_out: controls uplink data inversion
            invert_data_in: controls downlink data inversion
        """
        cnf = self.read_reg(self.CHIPCONFIG)
        cnf &= ~(
            self.CHIPCONFIG.HIGHSPEEDDATAOUTINVERT.bit_mask
            | self.CHIPCONFIG.HIGHSPEEDDATAININVERT.bit_mask
        )
        if invert_data_out:
            cnf |= self.CHIPCONFIG.HIGHSPEEDDATAOUTINVERT.bit_mask
        if invert_data_in:
            cnf |= self.CHIPCONFIG.HIGHSPEEDDATAININVERT.bit_mask
        self.write_reg(self.CHIPCONFIG, cnf)

    @lpgbt_accessor
    def line_driver_setup(
        self,
        modulation_current=64,
        emphasis_enable=False,
        emphasis_short=False,
        emphasis_amp=32,
    ):

        """Configures the line driver

        Arguments:
            emphasis_enable: line driver pre-emphasis
            modulation_current: line driver modulation current:
                                Im = 137 uA * modulation_current
            emphasis_short: duration of the pre-emphasis pulse;
                            pre-emphasis has to be enabled for this
                            field to have any impact.
            emphasis_amp: line driver pre-emphasis current:
                          Ipre = 137 uA * LDEmphasisAmp
                          pre-emphasis has to be enabled for this
                          field to have any impact.
        """
        assert modulation_current in range(128), "Invalid modulation current value"

        assert emphasis_amp in range(
            128
        ), "Invalid modulation pre-emphasis current value"


        modulation_current = int(modulation_current) & 0x7F
        ldconfig_h = modulation_current << self.LDCONFIGH.LDMODULATIONCURRENT.offset
        if emphasis_enable:
            ldconfig_h |= self.LDCONFIGH.LDEMPHASISENABLE.bit_mask

        ldconfig_l = emphasis_amp << self.LDCONFIGL.LDEMPHASISAMP.offset
        if emphasis_short:
            ldconfig_l |= self.LDCONFIGL.LDEMPHASISSHORT.bit_mask

        self.write_reg(self.LDCONFIGH, ldconfig_h)

        self.write_reg(self.LDCONFIGL, ldconfig_l)

    @lpgbt_accessor
    def serializer_set_data_source(self, source):
        """Sets the serialier data source

        Arguments:
            source: serializer input data source
        """
        assert source in range(16), "Invalid serializer data source"

        self.write_reg(self.ULDATASOURCE0, source)

    @lpgbt_accessor
    def line_driver_set_data_source(self, source):
        """Sets the line driver data source

        Arguments:
            source: line driver input data source
        """
        assert source in range(4), "Invalid line driver data source"

        self.write_reg(
            self.ULDATASOURCE1, source << self.ULDATASOURCE1.LDDATASOURCE.offset
        )

    @lpgbt_accessor
    def uplink_set_constant_pattern(self, constant_pattern):
        """Sets the constant uplink pattern. Constant pattern transmission
        must still be manually enabled by use of line_driver_set_data_source
        or serializer_set_data_source.

        Arguments:
            constant_pattern: 32 bit constant pattern value
        """
        frame = u32_to_bytes(constant_pattern)
        self.write_reg(self.DPDATAPATTERN3, frame[3])  # pattern for group 3
        self.write_reg(self.DPDATAPATTERN2, frame[2])  # pattern for group 2
        self.write_reg(self.DPDATAPATTERN1, frame[1])  # pattern for group 1
        self.write_reg(self.DPDATAPATTERN0, frame[0])  # pattern for group 0

    @lpgbt_accessor
    def phase_shifter_setup(
        self,
        channel_id,
        freq,
        delay=0,
        enable_fine_tune=False,
        drive_strength=4,
        preemphasis_strength=0,
        preemphasis_mode=0,
        preemphasis_width=0,
    ):
        """Configures a phase shifter channel

        Arguments:
            channel_id: channel ID (0-3)
            freq: output frequency (PS_CLK40M, PS_CLK80M, ...)
            delay: delay in ~50ps steps (requires enable_fine_tune=True)
            enable_fine_tune: enables fine tuning feature
            drive_strength: output driver strength (0-7)
            preemphasis_strength: output driver preemphasis strength (0-7)
            preemphasis_mode: output driver preemphasis mode
            preemphasis_width: output driver preemphasis width (0-7)
        """
        # pylint: disable=too-many-arguments
        assert channel_id in range(4), "Invalid phase shifter channel ID"
        assert freq in range(7), "Invalid phase shifter frequency"
        assert delay in range(512), "Invalid phase shift configuration"
        assert drive_strength in range(8), "Invalid drive strength configuration"
        assert preemphasis_strength in range(8), "Invalid preemphasis strength"
        assert preemphasis_mode in range(4), "Invalid preemphasis mode"
        assert preemphasis_width in range(8), "Invalid preemphasis width"

        config = freq | drive_strength << self.PS0CONFIG.PS0DRIVESTRENGTH.offset
        if enable_fine_tune:
            config |= self.PS0CONFIG.PS0ENABLEFINETUNE.bit_mask
        if delay & 0x100:
            config |= self.PS0CONFIG.PS0DELAY.bit_mask
        self.write_reg(self.PS0CONFIG.address + 3 * channel_id, config)

        delay &= 0xFF
        self.write_reg(self.PS0DELAY.address + 3 * channel_id, delay)

        driver = preemphasis_strength << self.PS0OUTDRIVER.PS0PREEMPHASISSTRENGTH.offset
        driver |= preemphasis_mode << self.PS0OUTDRIVER.PS0PREEMPHASISMODE.offset
        driver |= preemphasis_width << self.PS0OUTDRIVER.PS0PREEMPHASISWIDTH.offset
        self.write_reg(self.PS0OUTDRIVER.address + 3 * channel_id, driver)

    @lpgbt_accessor
    def phase_shifter_status(self, channel_id):
        """Generates a verbose phase shifter status report.

        Arguments:
            channel_id: phase shifter channel to report

        Returns a list of strings containing information about a given
        phase shifter channel.
        """
        assert channel_id in range(4), "Invalid phase shifter channel ID"

        config = self.read_reg(self.PS0CONFIG.address + 3 * channel_id)
        freq = config & 0x7
        drive_strength = (config >> self.PS0CONFIG.PS0DRIVESTRENGTH.offset) & 0x7

        enable_fine_tune = bool(config & self.PS0CONFIG.PS0ENABLEFINETUNE.bit_mask)

        delay = self.read_reg(self.PS0DELAY.address + 3 * channel_id)
        delay |= int(bool(config & self.PS0CONFIG.PS0DELAY.bit_mask)) << 8

        driver = self.read_reg(self.PS0OUTDRIVER.address + 3 * channel_id)
        preemphasis_strength = (
            driver >> self.PS0OUTDRIVER.PS0PREEMPHASISSTRENGTH.offset
        ) & 0x7
        preemphasis_mode = (driver >> self.PS0OUTDRIVER.PS0PREEMPHASISMODE.offset) & 0x3
        preemphasis_width = (
            driver >> self.PS0OUTDRIVER.PS0PREEMPHASISWIDTH.offset
        ) & 0x7

        dll_status = (self.read_reg(self.PSSTATUS) >> 2 * channel_id) & 0x3
        ret = [f"PS{channel_id}"]
        ret.append(f"  Freq: {self.EclockFrequency(freq).name} ({freq})")
        ret.append(f"  Delay: {delay}")
        ret.append(f"  Fine tune: {enable_fine_tune}")
        ret.append(
            f"  DriveStrength: {drive_strength} "
            f"PreemphasisWidth: {preemphasis_width} "
            f"PreemphasisMode: {preemphasis_mode} "
            f"PreemphasisStrength: {preemphasis_strength}"
        )
        ret.append(
            f"  DLL status: {self.EportRxDllStatus(dll_status).name} ({dll_status})"
        )
        return ret

    @lpgbt_accessor
    def eprx_prbs_gen_enable(self, group_id, channel_id, enable=True):
        """Enables PRBS generator attached to a ePortRx group/channel input.
        The PRBS feature requires that phase shifter clock 0 is enabled
        and set to an appropriate frequency.

        Arguments:
            group_id: ePortRx group to configure
            channel_id: ePortRx channel to configure
            enable: PRBS generator state
        """
        assert group_id in range(7), "Invalid ePortRx group"
        assert channel_id in range(4), "Invalid ePortRx channel"

        offset = channel_id + group_id * 4
        reg = self.EPRXPRBS0.address - int(offset / 8)
        bit = offset % 8

        value = self.read_reg(reg)
        if enable:
            value |= 1 << bit
        else:
            value &= ~(1 << bit)
        self.write_reg(reg, value)

    @lpgbt_accessor
    def eprx_group_setup(
        self,
        group_id,
        data_rate=0,
        track_mode=1,
        chn0_enable=True,
        chn1_enable=True,
        chn2_enable=True,
        chn3_enable=True,
    ):
        """Configures one ePortRx group

        Arguments:
            group_id: group ID (0-6)
            data_rate: data rate (EPORTRXHS_X8, EPORTRXLS_X4, ...)
            track_mode: phase selection mode (EPORTRXMODE_FIXED, EPORTRXMODE_CONTINOUSTRACKING, ...)
            chn0_enable: state of channel 0
            chn1_enable: state of channel 1
            chn2_enable: state of channel 2
            chn3_enable: state of channel 3
        """
        # pylint: disable=too-many-arguments
        assert group_id in range(7), "Invalid ePortRx group"
        assert data_rate in range(4), "Invalid ePortRx data rate"
        assert track_mode in range(4), "Invalid ePortRx phase selection mode"

        control = (
            data_rate << self.EPRX0CONTROL.EPRX0DATARATE.offset
            | track_mode << self.EPRX0CONTROL.EPRX0TRACKMODE.offset
        )
        if chn0_enable:
            control |= self.EPRX0CONTROL.EPRX00ENABLE.bit_mask
        if chn1_enable:
            control |= self.EPRX0CONTROL.EPRX01ENABLE.bit_mask
        if chn2_enable:
            control |= self.EPRX0CONTROL.EPRX02ENABLE.bit_mask
        if chn3_enable:
            control |= self.EPRX0CONTROL.EPRX03ENABLE.bit_mask

        self.write_reg(self.EPRX0CONTROL.address + group_id, control)

    @lpgbt_accessor
    def eprx_channel_config(
        self,
        group_id,
        channel_id,
        term=True,
        ac_bias=False,
        invert=False,
        phase=0,
        equalizer=0,
    ):
        """Configures an ePortRx channel

        Arguments:
            group_id: ePortRx group to configure
            channel_id: channel in the ePortRx to configure
            term: input termination control
            ac_bias: AC bias generation control
            invert: data inversion control
            phase: static data phase control
            equalizer: input equalizer control
        """
        # pylint: disable=too-many-arguments
        assert group_id in range(7), "Invalid ePortRx group"
        assert channel_id in range(4), "Invalid ePortRx channel"
        assert phase in range(16), "Invalid ePortRX phase"
        assert equalizer in range(4), "Invalid ePortRX equalizer configuration"

        reg = self.EPRX00CHNCNTR.address + group_id * 4 + channel_id

        reg_val = phase << self.EPRX00CHNCNTR.EPRX00PHASESELECT.offset

        if invert:
            reg_val |= self.EPRX00CHNCNTR.EPRX00INVERT.bit_mask

        if term:
            reg_val |= self.EPRX00CHNCNTR.EPRX00TERM.bit_mask

        if ac_bias:
            reg_val |= self.EPRX00CHNCNTR.EPRX00ACBIAS.bit_mask

        if equalizer & 0x2:
            reg_val |= self.EPRX00CHNCNTR.EPRX00EQ.bit_mask

        self.write_reg(reg, reg_val)

        req_eq = self.EPRXEQ10CONTROL.address + int(group_id / 2)
        reg_val = self.read_reg(req_eq)

        chan_mask = 1 << (group_id * 4 + channel_id) % 8
        reg_val &= chan_mask
        if equalizer & 0x1:
            reg_val |= chan_mask
        self.write_reg(req_eq, reg_val)

    @lpgbt_accessor
    def eprx_retrain_all_channel(self):
        """Performs training on all channels of all ePortRx groups"""
        self.write_reg(self.EPRXTRAIN10, 0xFF)
        self.write_reg(self.EPRXTRAIN32, 0xFF)
        self.write_reg(self.EPRXTRAIN54, 0xFF)
        self.write_reg(self.EPRXTRAINEC6, 0xFF)
        self.write_reg(self.EPRXTRAIN10, 0x00)
        self.write_reg(self.EPRXTRAIN32, 0x00)
        self.write_reg(self.EPRXTRAIN54, 0x00)
        self.write_reg(self.EPRXTRAINEC6, 0x00)

    @lpgbt_accessor
    def eprx_retrain_channel(self, group_id, channel_id):
        """Performs training on a single channel of a given ePortRx group

        Arguments:
            group_id: ePortRx group to train
            channel_id: channel in the ePortRx to train
        """
        assert group_id in range(7), "Invalid ePortRx group"
        assert channel_id in range(4), "Invalid ePortRx channel"

        reg_addr = self.EPRXTRAIN10.address + int(group_id / 2)
        reg_val_old = self.read_reg(reg_addr)

        chan_offsetfset = (group_id * 4 + channel_id) % 8
        reg_val = reg_val_old | (1 << chan_offsetfset)

        self.write_reg(reg_addr, reg_val)  # enable training
        self.write_reg(reg_addr, reg_val_old)  # disable training

    @lpgbt_accessor
    def eprx_channel_locked(self, group_id, channel_id):
        """Returns true if a given ePortRx channel is locked

        Arguments:
            group_id: ePortRx group to train
            channel_id: channel in the ePortRx to train
        """
        assert group_id in range(7), "Invalid ePortRx group"
        assert channel_id in range(4), "Invalid ePortRx channel"

        locked = self.read_reg(self.EPRX0LOCKED.address + 3 * group_id)
        return bool(
            locked & (1 << (self.EPRX0LOCKED.EPRX0CHNLOCKED.offset + channel_id))
        )

    @lpgbt_accessor
    def eprx_all_channels_locked(self, group_id):
        """Returns true if all channels in a given ePortRx group are locked

        Arguments:
            group_id: ePortRx group to train
        """
        assert group_id in range(7), "Invalid ePortRx group"

        locked = self.read_reg(self.EPRX0LOCKED.address + 3 * group_id)
        locked_channels = locked & self.EPRX0LOCKED.EPRX0CHNLOCKED.bit_mask
        return locked_channels == self.EPRX0LOCKED.EPRX0CHNLOCKED.bit_mask

    @lpgbt_accessor
    def eprx_channel_phase(self, group_id, channel_id):
        """Returns the selected phase of a given ePortRx channel

        Arguments:
            group_id: ePortRx group to train
            channel_id: channel in the ePortRx to train
        """
        assert group_id in range(7), "Invalid ePortRx group"
        assert channel_id in range(4), "Invalid ePortRx channel"

        reg_offset = channel_id / 2
        chn_pos = channel_id % 2
        phases = self.read_reg(
            self.EPRX0CURRENTPHASE10.address + int(3 * group_id + reg_offset)
        )
        phase = (phases >> (chn_pos * 4)) & 0xF
        return phase

    @lpgbt_accessor
    def eptx_group_setup(
        self,
        group_id,
        data_rate=0,
        chn0_enable=True,
        chn1_enable=True,
        chn2_enable=True,
        chn3_enable=True,
        mirror=False,
    ):
        """Configures an ePortTx group

        Arguments:
            group_id: ePortTx group (0-3)
            data_rate: data rate (EPORTTX_X2, EPORTTX_X4, ...)
            chn0_enable: state of channel 0
            chn1_enable: state of channel 1
            chn2_enable: state of channel 2
            chn3_enable: state of channel 3
            mirror: mirror function control
        """
        # pylint: disable=too-many-arguments
        assert group_id in range(4), "Invalid ePortTx group"
        assert data_rate in range(4), "Invalid ePortTx data rate"

        data_rate_reg_val = self.read_reg(self.EPTXDATARATE)
        data_rate_reg_val &= ~(0x3 << (group_id * 2))
        data_rate_reg_val |= data_rate << (group_id * 2)
        self.write_reg(self.EPTXDATARATE, data_rate_reg_val)

        enable_reg = self.EPTX10ENABLE.address + int(group_id / 2)
        enable_reg_val = self.read_reg(enable_reg)
        enable_reg_val &= ~(0xF << (group_id % 2) * 4)
        enable_reg_mask = 0
        if chn0_enable:
            enable_reg_mask |= self.EPTX10ENABLE.EPTX00ENABLE.bit_mask
        if chn1_enable:
            enable_reg_mask |= self.EPTX10ENABLE.EPTX01ENABLE.bit_mask
        if chn2_enable:
            enable_reg_mask |= self.EPTX10ENABLE.EPTX02ENABLE.bit_mask
        if chn3_enable:
            enable_reg_mask |= self.EPTX10ENABLE.EPTX03ENABLE.bit_mask

        enable_reg_val |= enable_reg_mask << (group_id % 2) * 4
        self.write_reg(enable_reg, enable_reg_val)

        mirror_reg_val = self.read_reg(self.EPTXCONTROL)
        if mirror:
            mirror_reg_val |= 1 << group_id
        else:
            mirror_reg_val &= ~(1 << group_id)
        self.write_reg(self.EPTXCONTROL, mirror_reg_val)

    @lpgbt_accessor
    def eptx_channel_config(
        self,
        group_id,
        channel_id,
        drive_strength=4,
        pre_emphasis_mode=0,
        pre_emphasis_strength=0,
        pre_emphasis_width=0,
        invert=False,
    ):
        """Configures an ePortTx channel

        Arguments:
            group_id: ePortTx group
            channel_id: ePortTx group channel
            drive_strength: output driver strength
            pre_emphasis_mode: output driver pre-emphasis mode
            pre_emphasis_strength: output driver pre-emphasis strength
            pre_emphasis_width: output driver pre-emphasis width
            invert: output data inversion control
        """
        # pylint: disable=too-many-arguments
        assert group_id in range(4), "Invalid ePortTx group"
        assert channel_id in range(4), "Invalid ePortTx channel"
        assert drive_strength in range(8), "Invalid drive strength configuration"
        assert pre_emphasis_strength in range(8), "Invalid preemphasis strength"
        assert pre_emphasis_mode in range(4), "Invalid preemphasis mode"
        assert pre_emphasis_width in range(8), "Invalid preemphasis width"

        primary_reg_adr = self.EPTX00CHNCNTR.address + group_id * 4 + channel_id
        primary_reg_val = (
            drive_strength << self.EPTX00CHNCNTR.EPTX00DRIVESTRENGTH.offset
        )
        primary_reg_val |= (
            pre_emphasis_mode << self.EPTX00CHNCNTR.EPTX00PREEMPHASISMODE.offset
        )
        primary_reg_val |= (
            pre_emphasis_strength << self.EPTX00CHNCNTR.EPTX00PREEMPHASISSTRENGTH.offset
        )
        self.write_reg(primary_reg_adr, primary_reg_val)

        secondary_reg_adr = (
            self.EPTX01_00CHNCNTR.address + group_id * 2 + int(channel_id / 2)
        )
        secondary_reg_val = self.read_reg(secondary_reg_adr)
        secondary_reg_val &= ~(0xF << 4 * (channel_id % 2))
        secondary_msk = pre_emphasis_width
        if invert:
            secondary_msk |= self.EPTX01_00CHNCNTR.EPTX00INVERT.bit_mask
        secondary_reg_val |= secondary_msk << 4 * (channel_id % 2)
        self.write_reg(secondary_reg_adr, secondary_reg_val)

    @lpgbt_accessor
    def vdac_setup(self, code, enable=True):
        """Configuration of the lpGBT voltage DAC

        Arguments:
            code: DAC output code
            enable: voltage DAC state
        """
        assert code in range(4096), "Invalid voltage DAC code"

        dach = self.read_reg(self.DACCONFIGH)
        dach = code >> 8 & 0xF
        if enable:
            dach |= self.DACCONFIGH.VOLDACENABLE.bit_mask
        else:
            dach &= (
                ~self.DACCONFIGH.VOLDACENABLE.bit_mask  # pylint: disable=invalid-unary-operand-type
            )

        dacl = code & 0xFF
        self.write_regs(self.DACCONFIGH, [dach, dacl])

    @lpgbt_accessor
    def cdac_setup(self, code, chns, enable=True):
        """Configuration of the lpGBT current DAC

        Arguments:
            code: DAC output code
            enable: current DAC state
            chns: ADC channels to connect to current DAC (8 bit mask)
                  (0x01 -> ADC0, 0x02 -> ADC1, ..., 0x80 -> ADC7)
        """
        assert code in range(256), "Invalid current DAC code"

        config = self.read_reg(self.DACCONFIGH)
        if enable:
            config |= self.DACCONFIGH.CURDACENABLE.bit_mask
        else:
            config &= (
                ~self.DACCONFIGH.CURDACENABLE.bit_mask  # pylint: disable=invalid-unary-operand-type
            )
        self.write_reg(self.DACCONFIGH, config)

        self.write_reg(self.CURDACVALUE, code)
        self.write_reg(self.CURDACCHN, chns)

    @lpgbt_accessor
    def eprx_group_status(self, group_id):
        """Generates a verbose ePortRx group status report. This report contains
        status information about its master DLL and all channels.

        Arguments:
            group_id: ePortRx group to report

        Returns a list of strings containing information about a given
        ePortRx group.
        """
        # pylint: disable=too-many-locals
        assert group_id in range(7), "Invalid ePortRx group"

        ret = []
        ret.append(f"EPRX{group_id}")
        control_reg = self.read_reg(self.EPRX0CONTROL.address + group_id)
        enabled = [
            bool(control_reg & 0x10),
            bool(control_reg & 0x20),
            bool(control_reg & 0x40),
            bool(control_reg & 0x80),
        ]
        data_rate = (control_reg >> self.EPRX0CONTROL.EPRX0DATARATE.offset) & 0x3
        track_mode = (control_reg) & 0x3

        tx_data_rate = bool(self.read_mode() & 0x08)
        tx_data_rate_str = self.eport_rx_data_rate_to_str(
            tx_data_rate=tx_data_rate,
            eprx_data_rate=data_rate,
        )
        ret.append(f"  Data rate : {tx_data_rate_str} Mbps ({tx_data_rate})")
        ret.append(
            f"  Track mode : {self.EportRxPhaseSelectionMode(track_mode).name} ({track_mode})"
        )

        locked_reg = self.read_reg(self.EPRX0LOCKED.address + 3 * group_id)
        locked = [
            bool(locked_reg & 0x10),
            bool(locked_reg & 0x20),
            bool(locked_reg & 0x40),
            bool(locked_reg & 0x80),
        ]

        phase10 = self.read_reg(self.EPRX0CURRENTPHASE10.address + 3 * group_id)
        phase32 = self.read_reg(self.EPRX0CURRENTPHASE32.address + 3 * group_id)
        phase0 = (phase10 >> self.EPRX0CURRENTPHASE10.EPRX0CURRENTPHASE0.offset) & 0xF
        phase1 = (phase10 >> self.EPRX0CURRENTPHASE10.EPRX0CURRENTPHASE1.offset) & 0xF
        phase2 = (phase32 >> self.EPRX0CURRENTPHASE32.EPRX0CURRENTPHASE2.offset) & 0xF
        phase3 = (phase32 >> self.EPRX0CURRENTPHASE32.EPRX0CURRENTPHASE3.offset) & 0xF
        phases = [phase0, phase1, phase2, phase3]

        eq0 = self.read_reg(self.EPRXEQ10CONTROL.address + int(group_id / 2))
        eq0 >>= 4 * (group_id % 2)
        for chn in range(4):
            chn_cntr = self.read_reg(self.EPRX00CHNCNTR.address + group_id * 4 + chn)
            set_phase = chn_cntr >> self.EPRX00CHNCNTR.EPRX00PHASESELECT.offset
            invert = False
            term = False
            ac_bias = False
            if chn_cntr & self.EPRX00CHNCNTR.EPRX00INVERT.bit_mask:
                invert = True
            if chn_cntr & self.EPRX00CHNCNTR.EPRX00TERM.bit_mask:
                term = True
            if chn_cntr & self.EPRX00CHNCNTR.EPRX00ACBIAS.bit_mask:
                ac_bias = True
            ret.append(
                f"  CHN{chn} Enabled: {enabled[chn]} "
                f"Locked: {locked[chn]} "
                f"Phase: {phases[chn]:2d} "
                f"Term: {term} "
                f"Acbias: {ac_bias} "
                f"Invert: {invert} "
                f"Set_phase: {set_phase:2d}"
            )

        status = locked_reg & 0x3
        dll_status = self.read_reg(self.EPRX0DLLSTATUS.address + group_id)
        dll_locked = bool(dll_status & self.EPRX0DLLSTATUS.EPRX0DLLLOCKED.bit_mask)
        ret.append(
            f"  DLL Locked:{dll_locked} "
            f"FSMStatus: {self.EportRxDllStatus(status).name} ({status})"
        )

        lock_filter_state = (
            dll_status >> self.EPRX0DLLSTATUS.EPRX0DLLLFSTATE.offset
        ) & 0x3
        loss_of_lock = (dll_status >> self.EPRX0DLLSTATUS.EPRX0DLLLOLCNT.offset) & 0x1F
        ret.append(
            f"  Lock filter State: {lock_filter_state} Loss of lock: {loss_of_lock}"
        )
        return ret

    @lpgbt_accessor
    def log_eprx_group_status(self, group_id):
        """Logs status of an ePortRx group (see eprx_group_status)"""
        for line in self.eprx_group_status(group_id):
            self.logger.info(line)

    @lpgbt_accessor
    def log_all_eprx_groups(self):
        """Logs status information about all ePortRx groups (see eprx_group_status)"""
        for group_id in range(7):
            self.log_eprx_group_status(group_id)

    @lpgbt_accessor
    def eptx_group_status(self, group_id):
        """Generates a verbose ePortTx group status report.

        Arguments:
            group_id: ePortTx group to report

        Returns a list of strings containing information about a given
        ePortTx group.
        """
        # pylint: disable=too-many-locals
        assert group_id in range(4), "Invalid ePortTx group"

        ret = []
        ret.append(f"EPTX{group_id}")
        data_rate = (self.read_reg(self.EPTXDATARATE) >> (group_id * 2)) & 0x3
        data_rate_str = self.eport_tx_data_rate_to_mbps(data_rate)
        mirror = bool(self.read_reg(self.EPTXCONTROL) & (1 << group_id))
        ret.append(f"  Data rate: {data_rate_str} Mbps ({data_rate})")
        ret.append(f"  Mirror: {mirror}")

        enable_reg = self.read_reg(self.EPTX10ENABLE.address + int(group_id / 2))
        enable_reg >>= (int(group_id % 2)) * 4
        enabled = [
            bool(enable_reg & 0x1),
            bool(enable_reg & 0x2),
            bool(enable_reg & 0x4),
            bool(enable_reg & 0x8),
        ]

        for chn in range(4):
            primary_reg_val = self.read_reg(
                self.EPTX00CHNCNTR.address + group_id * 4 + chn
            )
            drive_strength = (
                primary_reg_val >> self.EPTX00CHNCNTR.EPTX00DRIVESTRENGTH.offset
            ) & 0x7
            pre_emphasis_mode = (
                primary_reg_val >> self.EPTX00CHNCNTR.EPTX00PREEMPHASISMODE.offset
            ) & 0x3
            pre_emphasis_strength = (
                primary_reg_val >> self.EPTX00CHNCNTR.EPTX00PREEMPHASISSTRENGTH.offset
            ) & 0x7

            secondary_reg_val = self.read_reg(
                self.EPTX01_00CHNCNTR.address + group_id * 2 + int(chn / 2)
            )
            secondary_reg_val >>= 4 * (chn % 2)
            pre_emphasis_width = secondary_reg_val & 0x7
            invert = bool(
                secondary_reg_val & self.EPTX01_00CHNCNTR.EPTX00INVERT.bit_mask
            )
            ret.append(
                f"  CHN{chn} Enabled: {enabled[chn]} "
                f"DriveStrength: {drive_strength} "
                f"PreemphasisMode: {pre_emphasis_mode:2d} "
                f"PreemphasisStrength: {pre_emphasis_strength} "
                f"PreemphasisWidth: {pre_emphasis_width} "
                f"Invert: {invert}"
            )
        return ret

    @lpgbt_accessor
    def log_eptx_group_status(self, group_id):
        """Logs status of an ePortTx group (see eptx_group_status)"""
        for line in self.eptx_group_status(group_id):
            self.logger.info(line)

    @lpgbt_accessor
    def log_all_eptx_groups(self):
        """Logs status of all ePortTx groups (see eptx_group_status)"""
        for group_id in range(4):
            self.log_eptx_group_status(group_id)

    def _eclk_setup_common(
        self,
        clk_id,
        freq=0,
        drive_strength=4,
        preemphasis_strength=0,
        preemphasis_mode=0,
        preemphasis_width=0,
        invert=False,
    ):
        """Configures a single eClock

        Arguments:
            clk_id: eClock ID to configure
            freq: frequency (EPORTCLOCKS_CLK40M, EPORTCLOCKS_CLK80M, ...)
            drive_strength: output driver strength (0-7)
            preemphasis_strength: output driver preemphasis strength (0-7)
            preemphasis_mode: output driver preemphasis mode
            preemphasis_width: output driver preemphasis width (0-7)
            invert: output clock inversion control
        """

        # pylint: disable=too-many-arguments
        assert clk_id in range(29), "Invalid eClock ID"
        assert freq in range(8), "Invalid eClock frequency"
        assert self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISSTRENGTH.validate(
            preemphasis_strength
        ), "Invalid preemphasis strength"
        assert self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISMODE.validate(
            preemphasis_mode
        ), "Invalid preemphasis mode"
        assert self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISWIDTH.validate(
            preemphasis_width
        ), "Invalid preemphasis width"

        config_high = (
            freq << self.EPCLK0CHNCNTRH.EPCLK0FREQ.offset
            | drive_strength << self.EPCLK0CHNCNTRH.EPCLK0DRIVESTRENGTH.offset
        )
        if invert:
            config_high |= self.EPCLK0CHNCNTRH.EPCLK0INVERT.bit_mask

        config_low = (
            preemphasis_width << self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISWIDTH.offset
            | preemphasis_mode << self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISMODE.offset
            | preemphasis_strength
            << self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISSTRENGTH.offset
        )

        return (config_high, config_low)

    @lpgbt_accessor
    def eclk_status(self, clk_id):
        """Generates a verbose eClock status report.

        Arguments:
            clk_id: eClock to report

        Returns a list of strings containing information about a given
        eClock.
        """
        assert clk_id in range(29), "Invalid eClock ID"

        config_high = self.read_reg(self.EPCLK0CHNCNTRH.address + 2 * clk_id)
        config_low = self.read_reg(self.EPCLK0CHNCNTRL.address + 2 * clk_id)

        freq = (config_high >> self.EPCLK0CHNCNTRH.EPCLK0FREQ.offset) & 0x7
        drive_strength = config_high >> self.EPCLK0CHNCNTRH.EPCLK0DRIVESTRENGTH.offset
        invert = bool(config_high & self.EPCLK0CHNCNTRH.EPCLK0INVERT.bit_mask)

        preemphasis_width = (
            config_low >> self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISWIDTH.offset
        ) & 0x7
        preemphasis_mode = (
            config_low >> self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISMODE.offset
        ) & 0x3
        preemphasis_strength = (
            config_low >> self.EPCLK0CHNCNTRL.EPCLK0PREEMPHASISSTRENGTH.offset
        ) & 0x7
        ret = [f"ECLK{clk_id}"]
        ret.append(f"  Freq: {self.EclockFrequency(freq).name} ({freq})")
        ret.append(f"  Invert: {invert}")
        ret.append(
            f"  DriveStrength: {drive_strength} "
            f"PreemphasisWidth: {preemphasis_width} "
            f"PreemphasisMode: {preemphasis_mode} "
            f"PreemphasisStrength: {preemphasis_strength}"
        )
        return ret

    @lpgbt_accessor
    def log_regs(self):
        """Logs a verbose report of all lpGBT register values"""
        for address in self.Reg:
            data = self.read_reg(address)
            self.logger.info(
                "[0x%03X %-28s] = 0x%02x",
                address,
                self.Reg(address).name,
                data,
            )

    @lpgbt_accessor
    def log_pusm_status(self):
        """Verbosely logs current status of the power up state machine"""

        raise NotImplementedError("log_pusm_status is not implemented in Lpgbt")

    @lpgbt_accessor
    def bert_config(self, meas_time, source, skip_disable=False):
        """Configures the lpGBT BERT

        Arguments:
            meas_time: measurement cycle
            source: data source
            skip_disable: disable checker skipping
        """
        assert meas_time in range(16), "Invalid BERT measurement time"
        assert source in range(256), "Invalid BERT source configuration"

        self.write_reg(self.BERTSOURCE, source)
        config = meas_time << self.BERTCONFIG.BERTMEASTIME.offset
        if skip_disable:
            config |= self.BERTCONFIG.SKIPDISABLE.bit_mask
        self.write_reg(self.BERTCONFIG, config)

    @lpgbt_accessor
    def bert_run(self, ignore_no_activity=False):
        """Executes the lpGBT BERT

        Arguments:
            ignore_no_activity: disregard BERT error flag

        Raises:
            LpgbtException: if timeout or not data at the input

        Returns:
            Dictionary containing BER test information.
        """
        config = self.read_reg(self.BERTCONFIG)
        meas_time = (config >> self.BERTCONFIG.BERTMEASTIME.offset) & 0x0F
        bits = 2 ** (5 + 2 * meas_time)

        self.write_reg(self.BERTCONFIG, config | self.BERTCONFIG.BERTSTART.bit_mask)
        timeout = 1  # should be computed based on meas_time
        timeout_time = time.time() + timeout
        status = 0
        no_data = False
        while True:
            status = self.read_reg(self.BERTSTATUS)

            if status & self.BERTSTATUS.BERTDONE.bit_mask:
                break

            if (
                not ignore_no_activity
                and status & self.BERTSTATUS.BERTPRBSERRORFLAG.bit_mask
            ):
                self.logger.warning(
                    "BERT error flag (there was not data on the input?)"
                )
                no_data = True
                break

            if time.time() > timeout_time:
                self.write_reg(self.BERTCONFIG, config)  # stop measurement and fail
                raise LpgbtTimeoutError("Timeout while waiting for BERT to finish")

        if no_data:
            errors = bits / 2
        else:
            errors = (
                self.read_reg(self.BERTRESULT0)
                | self.read_reg(self.BERTRESULT1) << 8
                | self.read_reg(self.BERTRESULT2) << 16
                | self.read_reg(self.BERTRESULT3) << 24
                | self.read_reg(self.BERTRESULT4) << 32
            )
            errors /= 3
        self.write_reg(self.BERTCONFIG, config)

        result = {
            "bits": bits,
            "errors": errors,
            "error_flag": no_data,
            "ber": errors / bits,
        }
        return result

    @lpgbt_accessor
    def bert_set_constant_pattern(self, constant_pattern):
        """Configures the BERT constant pattern checker.

        Arguments:
            constant_pattern: 32 bit constant pattern to check
        """
        frame = u32_to_bytes(constant_pattern)
        self.write_reg(self.BERTDATAPATTERN3, frame[3])  # pattern for group 3
        self.write_reg(self.BERTDATAPATTERN2, frame[2])  # pattern for group 2
        self.write_reg(self.BERTDATAPATTERN1, frame[1])  # pattern for group 1
        self.write_reg(self.BERTDATAPATTERN0, frame[0])  # pattern for group 0

    @lpgbt_accessor
    def equalizer_setup(self, attenuation=3, cap=0, res0=0, res1=0, res2=0, res3=0):
        """Configures the downlink equalizer

        Arguments:
            attenuation: input attentuator control
            cap: equalizer capacitor value
            res0: equalizer resistor 0 value
            res1: equalizer resistor 1 value
            res2: equalizer resistor 2 value
            res3: equalizer resistor 3 value
        """
        # pylint: disable=too-many-arguments
        assert attenuation in range(4), "Invalid attentuation"
        assert cap in range(4), "Invalid capacitor setting"
        assert res0 in range(4), "Invalid resistor 0 setting"
        assert res1 in range(4), "Invalid resistor 1 setting"
        assert res2 in range(4), "Invalid resistor 2 setting"
        assert res3 in range(4), "Invalid resistor 3 setting"

        eq_config = (
            attenuation << self.EQCONFIG.EQATTENUATION.offset
            | cap << self.EQCONFIG.EQCAP.offset
        )
        self.write_reg(self.EQCONFIG, eq_config)

        eq_res = (
            res3 << self.EQRES.EQRES3.offset
            | res2 << self.EQRES.EQRES2.offset
            | res1 << self.EQRES.EQRES1.offset
            | res0 << self.EQRES.EQRES0.offset
        )
        self.write_reg(self.EQRES, eq_res)

    @lpgbt_accessor
    def get_chipid_ram(self):
        """Returns the CHIPID stored in RAM as a string"""
        result = self.read_regs(self.CHIPID0, read_len=4)
        return f"{(result[0] << 24 | result[1] << 16 | result[2] << 8 | result[3]):08X}"

    @lpgbt_accessor
    def get_chipid_fuses(self):
        """Returns the CHIPID stored in the eFuse as a string"""
        return f"{self.fuses_read_bank(self.CHIPID0):08X}"

    @lpgbt_accessor
    def eye_opening_scan(self, image_file="eye.png", data_file=None, verbose=False):
        """Performs a scan using the downling Eye-Opening Monitor (EOM).

        Arguments:
            image_file: output image filename (can be None to skip image storage)
            data_file: output raw data filename (can be None to skip raw data storage)
            verbose: logging verbosity control
        """
        # pylint: disable=too-many-locals

        config = (
            7 << self.EOMCONFIGH.EOMENDOFCOUNTSEL.offset
            | self.EOMCONFIGH.EOMENABLE.bit_mask
        )

        self.write_reg(self.EOMCONFIGH, config)

        timeout = 0.1
        data_x = []
        data_y = []
        data_c = []
        for y_axis in range(1, 31):
            self.write_reg(self.EOMVOFSEL, y_axis << self.EOMVOFSEL.EOMVOFSEL.offset)
            if verbose:
                self.logger.info("%d/32", y_axis)
            for x_axis in range(64):
                self.write_reg(
                    self.EOMCONFIGL, x_axis << self.EOMCONFIGL.EOMPHASESEL.offset
                )
                self.write_reg(
                    self.EOMCONFIGH, config | self.EOMCONFIGH.EOMSTART.bit_mask
                )

                timeout_time = time.time() + timeout
                while True:
                    if self.read_reg(self.EOMSTATUS) & self.EOMSTATUS.EOMEND.bit_mask:
                        break

                    if time.time() > timeout_time:
                        # stop the measurement
                        self.write_reg(self.EOMCONFIGH, config)
                        raise LpgbtTimeoutError(
                            "Timeout while waiting for EOM to finish"
                        )

                data_x.append(x_axis)
                data_y.append(y_axis)
                data_c.append(
                    self.read_reg(self.EOMCOUTERVALUEL)
                    | self.read_reg(self.EOMCOUTERVALUEH) << 8
                )
                self.write_reg(self.EOMCONFIGH, config)
        self.write_reg(self.EOMCONFIGH, 0x0)

        if data_file is not None and data_file:
            with open(data_file, "w", encoding="utf-8") as data:
                data.write("{'X Axis':10s} {'Y Axis':10s} {'Count':10s}\n")
                for x_val, y_val, c_val in zip(data_x, data_y, data_c):
                    data.write(f"{x_val:10d} {y_val:10d} {c_val:10d}\n")

        if image_file is not None and image_file:
            plt.clf()
            plt.scatter(np.asarray(data_x), np.asarray(data_y), c=np.asarray(data_c))
            plt.colorbar()
            if verbose:
                self.logger.info("Saving plot to '%s'", image_file)
            plt.savefig(image_file)

    @lpgbt_accessor
    def eye_opening_horizontal_scan(self, vof, step=4):
        """Performs a single horizontal line measurement using the lpGBT EOM

        Arguments:
            vof: comparison threshold voltage
            step: time step size used during scan
        """
        assert vof in range(32), "Invalid EOM threshold configuration"

        config = (
            8 << self.EOMCONFIGH.EOMENDOFCOUNTSEL.offset
            | self.EOMCONFIGH.EOMENABLE.bit_mask
        )

        self.write_reg(self.EOMCONFIGH, config)

        timeout = 0.1
        results = []
        self.write_reg(self.EOMVOFSEL, vof << self.EOMVOFSEL.EOMVOFSEL.offset)
        x_range = list(range(0, 64, step))
        for x_axis in x_range:
            self.write_reg(
                self.EOMCONFIGL, x_axis << self.EOMCONFIGL.EOMPHASESEL.offset
            )
            self.write_reg(self.EOMCONFIGH, config | self.EOMCONFIGH.EOMSTART.bit_mask)

            timeout_time = time.time() + timeout
            while True:
                if self.read_reg(self.EOMSTATUS) & self.EOMSTATUS.EOMEND.bit_mask:
                    break

                if time.time() > timeout_time:
                    # stop the measurement
                    self.write_reg(self.EOMCONFIGH, config)
                    raise LpgbtTimeoutError("Timeout while waiting for EOM to finish")

            count_regs = self.read_regs(self.EOMCOUTERVALUEH, read_len=2)
            count = count_regs[0] << 8 | count_regs[1]
            results.append(count)

            self.write_reg(self.EOMCONFIGH, config)
        self.write_reg(self.EOMCONFIGH, 0x0)

        return x_range, results

    @lpgbt_accessor
    def adc_config(self, inp=0, inn=0, gain=0):
        """Configures the lpGBT ADC

        Arguments:
            inp: positive input signal selection (AdcInputSelect.EXT0, AdcInputSelect.VDD, ...)
            inn: negative input signal selection (AdcInputSelect.EXT0, AdcInputSelect.VREF2, ...)
            gain: amplifier gain (ADCGAIN_X2, ADCGAIN_X8, ...)
        """
        assert inp in range(16), "Invalid ADC channel selection"
        assert inn in range(16), "Invalid ADC channel selection"
        assert gain in range(4), "Invalid ADC gain configuration"

        config = (
            self.ADCCONFIG.ADCENABLE.bit_mask
            | gain << self.ADCCONFIG.ADCGAINSELECT.offset
        )
        self.write_reg(self.ADCCONFIG, config)

        mux = (
            inp << self.ADCSELECT.ADCINPSELECT.offset
            | inn << self.ADCSELECT.ADCINNSELECT.offset
        )
        self.write_reg(self.ADCSELECT, mux)

    @lpgbt_accessor
    def adc_convert(self, samples=1):
        """Performs one/multiple ADC conversions

        Arguments:
            samples: how many conversions to perform

        Returns:
            10 bit conversion result. In case samples is greater than one,
            returns a list of all samples collected.

        Raises:
            LpgbtException: in case the conversion timeout is exceeded
        """
        results = []
        config = self.read_reg(self.ADCCONFIG)

        for _ in range(samples):
            self.write_reg(self.ADCCONFIG, config | self.ADCCONFIG.ADCCONVERT.bit_mask)
            timeout = 0.001
            timeout_time = time.time() + timeout
            while True:
                statush, statusl = self.read_regs(self.ADCSTATUSH, 2)

                if statush & self.ADCSTATUSH.ADCDONE.bit_mask:
                    results.append(statusl | (statush & 0x3) << 8)
                    break

                if time.time() > timeout_time:
                    # stop the measurement
                    self.write_reg(self.ADCCONFIG, config)
                    raise LpgbtTimeoutError("Timeout while waiting for ADC to finish")
            self.write_reg(self.ADCCONFIG, config)

        if len(results) == 1:
            return results[0]
        return results

    @lpgbt_accessor
    def _gpio_helper_set(self, reg, value):
        reg = self.decode_reg_addr(reg)
        assert value in range(65536), "Invalid GPIO register state"
        valueh = (value >> 8) & 0xFF
        valuel = value & 0xFF
        self.write_reg(reg, valueh)
        self.write_reg(reg + 1, valuel)

    @lpgbt_accessor
    def _gpio_helper_set_bit(self, reg, bit, value):
        reg = self.decode_reg_addr(reg)
        assert bit in range(16), "Invalid GPIO ID"
        reg_value = self._gpio_helper_get(reg)
        if value:
            reg_value |= (1 << bit)
        else:
            reg_value &= ~(1 << bit)
        self._gpio_helper_set(reg, reg_value)

    @lpgbt_accessor
    def _gpio_helper_get(self, reg):
        reg = self.decode_reg_addr(reg)
        valueh = self.read_reg(reg)
        valuel = self.read_reg(reg + 1)
        return valuel | (valueh << 8)

    @lpgbt_accessor
    def _gpio_helper_get_bit(self, reg, bit):
        reg = self.decode_reg_addr(reg)
        assert bit in range(16), "Invalid GPIO ID"
        valueh = self.read_reg(reg)
        valuel = self.read_reg(reg + 1)
        value = valuel | (valueh << 8)
        return bool(value & (1 << bit))

    @lpgbt_accessor
    def gpio_set_dir(self, dir_):
        """Configures the lpGBT GPIO direction registers

        Arguments:
            dir_: 16 bit number (dir_[n]=0 pin=input, dir_[n]=1 pin=output)
        """
        self._gpio_helper_set(self.PIODIRH, dir_)

    @lpgbt_accessor
    def gpio_set_dir_bit(self, bit, value):
        """Configures the direction of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
            value: GPIO direction
        """
        self._gpio_helper_set_bit(self.PIODIRH, bit, value)

    @lpgbt_accessor
    def gpio_get_dir(self):
        """Returns the lpGBT GPIO direction register values"""
        return self._gpio_helper_get(self.PIODIRH)

    @lpgbt_accessor
    def gpio_get_dir_bit(self, bit):
        """Returns the direction of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIODIRH, bit)

    @lpgbt_accessor
    def gpio_get_in(self):
        """Returns the input state of the lpGBT GPIOs"""
        return self._gpio_helper_get(self.PIOINH)

    @lpgbt_accessor
    def gpio_get_in_bit(self, bit):
        """Returns the input state of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIOINH, bit)

    @lpgbt_accessor
    def gpio_set_out(self, out_):
        """Configures the lpGBT GPIO output registers

        Arguments:
            out_: 16 bit number (out_[n]=0 pin=low, out_[n]=1 pin=high)
        """
        self._gpio_helper_set(self.PIOOUTH, out_)

    @lpgbt_accessor
    def gpio_set_out_bit(self, bit, value):
        """Sets the output state of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
            value: output value to write
        """
        self._gpio_helper_set_bit(self.PIOOUTH, bit, value)

    @lpgbt_accessor
    def gpio_get_out(self):
        """Reads the output state of the lpGBT GPIOs"""
        return self._gpio_helper_get(self.PIOOUTH)

    @lpgbt_accessor
    def gpio_get_out_bit(self, bit):
        """Reads the output state of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIOOUTH, bit)

    @lpgbt_accessor
    def gpio_set_drive(self, drive_strength):
        """Configures the lpGBT GPIO output drive strength

        Arguments:
            drive_strength: 16 bit number (drive_strength[n]=1 high DS)
        """
        self._gpio_helper_set(self.PIODRIVESTRENGTHH, drive_strength)

    @lpgbt_accessor
    def gpio_set_drive_bit(self, bit, drive_strength):
        """Sets the drive strenth of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
            drive_strength: GPIO drive strength (1=high DS)
        """
        self._gpio_helper_set_bit(self.PIODRIVESTRENGTHH, bit, drive_strength)

    @lpgbt_accessor
    def gpio_get_drive(self):
        """Reads the drive strength setting of the lpGBT GPIOs"""
        return self._gpio_helper_get(self.PIODRIVESTRENGTHH)

    @lpgbt_accessor
    def gpio_get_drive_bit(self, bit):
        """Reads the drive strenth setting of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIODRIVESTRENGTHH, bit)

    @lpgbt_accessor
    def gpio_set_pullena(self, pullena):
        """Configures the pull-resistor switch of the lpGBT GPIOs

        Arguments:
            pullena: 16 bit number (pullena[n]=1 enables resistor)
        """
        self._gpio_helper_set(self.PIOPULLENAH, pullena)

    @lpgbt_accessor
    def gpio_set_pullena_bit(self, bit, value):
        """Configures the pull-resistor switch of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
            value: pull-resistor state (off/on)
        """

        self._gpio_helper_set_bit(self.PIOPULLENAH, bit, value)

    @lpgbt_accessor
    def gpio_get_pullena(self):
        """Reads the pull-resistor switch setting of the lpGBT GPIOs"""
        return self._gpio_helper_get(self.PIOPULLENAH)

    @lpgbt_accessor
    def gpio_get_pullena_bit(self, bit):
        """Reads the pull-resistor switch setting of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIOPULLENAH, bit)

    @lpgbt_accessor
    def gpio_set_updown(self, updown):
        """Configures the pull-resistor direction of the lpGBT GPIOs

        Arguments:
            updown: 16 bit number (updown[n]=1 selects pull-up)
        """
        self._gpio_helper_set(self.PIOUPDOWNH, updown)

    @lpgbt_accessor
    def gpio_set_updown_bit(self, bit, value):
        """Configures the pull-resistor direction of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
            value: pull-resistor direction (down/up)
        """
        self._gpio_helper_set_bit(self.PIOUPDOWNH, bit, value)

    @lpgbt_accessor
    def gpio_get_updown(self):
        """Reads the pull-resistor direction setting of the lpGBT GPIOs"""
        return self._gpio_helper_get(self.PIOUPDOWNH)

    @lpgbt_accessor
    def gpio_get_updown_bit(self, bit):
        """Reads the pull-resistor direction setting of a single lpGBT GPIO

        Arguments:
            bit: GPIO index
        """
        return self._gpio_helper_get_bit(self.PIOUPDOWNH, bit)

    @lpgbt_accessor
    def gpio_status(self):
        """Generates a verbose GPIO status report.

        Returns a list of strings containing information about
        the lpGBT GPIO configuration.
        """
        ret = ["GPIO "]
        ret.append(f"  DIR     : {self.gpio_get_dir():04x}")
        ret.append(f"  OUT     : {self.gpio_get_out():04x}")
        ret.append(f"  IN      : {self.gpio_get_in():04x}")
        ret.append(f"  PULLENA : {self.gpio_get_pullena():04x}")
        ret.append(f"  UP/DOWN : {self.gpio_get_updown():04x}")
        return ret

    @lpgbt_accessor
    def log_gpio(self):
        """Logs status of the lpGBT GPIOs (see gpio_status)"""
        for line in self.gpio_status():
            self.logger.info(line)

    @lpgbt_accessor
    def fuses_burn_bank(self, address, value_bank, pulse_length=12, timeout=0.01):
        """Burns a single bank of eFuses

        Arguments:
            address: first register address to fuse (multiple of 4)
            value_bank: 32 bit value to fuse into bank
            pulse_length: duration of burn pulse
            timeout: timeout for fusing completion
        """
        address = self.decode_reg_addr(address)
        assert 0 <= value_bank < 2 ** 32, "Invalid fuse bank value"
        assert 0 <= address < 0x100, f"Invalid address ({address})"

        assert self.FUSECONTROL.FUSEBLOWPULSELENGTH.validate(
            pulse_length
        ), "Invalid pulse_length"

        if address % 4 != 0:
            raise LpgbtFuseError(
                f"Incorrect address for burn bank! (address=0x{address:02x})"
            )
        _, _, address_high, address_low = u32_to_bytes(address)

        self.write_reg(self.FUSEBLOWADDH, address_high)
        self.write_reg(self.FUSEBLOWADDL, address_low)

        data3, data2, data1, data0 = u32_to_bytes(value_bank)
        self.write_reg(self.FUSEBLOWDATAA, data0)
        self.write_reg(self.FUSEBLOWDATAB, data1)
        self.write_reg(self.FUSEBLOWDATAC, data2)
        self.write_reg(self.FUSEBLOWDATAD, data3)

        self.write_reg(self.FUSEMAGIC, self.FUSE_MAGIC_NUMBER)

        self.write_reg(
            self.FUSECONTROL,
            pulse_length << self.FUSECONTROL.FUSEBLOWPULSELENGTH.offset
            | self.FUSECONTROL.FUSEBLOW.bit_mask,
        )

        timeout_time = time.time() + timeout

        while True:
            status = self.read_reg(self.FUSESTATUS)
            if status & self.FUSESTATUS.FUSEBLOWDONE.bit_mask:
                self.write_reg(self.FUSECONTROL, 0)
                break

            if status & self.FUSESTATUS.FUSEBLOWERROR.bit_mask:
                self.write_reg(self.FUSECONTROL, 0)
                raise LpgbtFuseError("Unexpected error during fuse burning")

            if time.time() > timeout_time:
                self.write_reg(self.FUSECONTROL, 0)
                raise LpgbtFuseError("Timeout while waiting for burning fuses")

    @lpgbt_accessor
    def fuses_read_bank(self, address, timeout=0.01):
        """Reads a single bank of eFuses

        Arguments:
            address: first register address to read (multiple of 4)
            timeout: timeout for read completion
        """
        address = self.decode_reg_addr(address)

        if address % 4 != 0:
            raise LpgbtFuseError(
                f"Incorrect address for read bank! (address=0x{address:02x})"
            )
        _, _, address_high, address_low = u32_to_bytes(address)
        self.write_reg(self.FUSEBLOWADDH, address_high)
        self.write_reg(self.FUSEBLOWADDL, address_low)
        self.write_reg(self.FUSECONTROL, self.FUSECONTROL.FUSEREAD.bit_mask)

        timeout_time = time.time() + timeout

        while True:
            status = self.read_reg(self.FUSESTATUS)
            if status & self.FUSESTATUS.FUSEDATAVALID.bit_mask:
                fuse0, fuse1, fuse2, fuse3 = self.read_regs(self.FUSEVALUESA, 4)
                value = fuse0 | fuse1 << 8 | fuse2 << 16 | fuse3 << 24
                self.write_reg(self.FUSECONTROL, 0)
                break

            if time.time() > timeout_time:
                self.write_reg(self.FUSECONTROL, 0)
                raise LpgbtTimeoutError("Timeout while waiting for reading fuses")

        return value

    @lpgbt_accessor
    def fuses_read_reg(self, reg_address):
        """Reads a single register from eFuses

        Arguments:
            reg_address: register read address
        """
        bank_address = 4 * int(reg_address / 4)
        offset = reg_address % 4
        value_bank = self.fuses_read_bank(address=bank_address)
        reg_value = (value_bank >> (8 * offset)) & 0xFF
        return reg_value

    @lpgbt_accessor
    def uplink_set_data_source(self, group_id, source):
        """Configures the uplink data source

        Arguments:
            group_id: uplink data path group number
            source: data path data source for group_id
        """
        assert group_id in range(7), "Invalid uplink data path group"
        assert source in range(8), "Invalid uplink data source"
        grp_mapping = (
            (self.ULDATASOURCE1, self.ULDATASOURCE1.ULG0DATASOURCE.offset),
            (self.ULDATASOURCE1, self.ULDATASOURCE1.ULG1DATASOURCE.offset),
            (self.ULDATASOURCE2, self.ULDATASOURCE2.ULG2DATASOURCE.offset),
            (self.ULDATASOURCE2, self.ULDATASOURCE2.ULG3DATASOURCE.offset),
            (self.ULDATASOURCE3, self.ULDATASOURCE3.ULG4DATASOURCE.offset),
            (self.ULDATASOURCE3, self.ULDATASOURCE3.ULG5DATASOURCE.offset),
            (self.ULDATASOURCE4, self.ULDATASOURCE4.ULG6DATASOURCE.offset),
        )
        reg_addr, bit_pos = grp_mapping[group_id]
        reg_val = self.read_reg(reg_addr)
        reg_val &= ~(0x7 << bit_pos)
        reg_val |= source << bit_pos
        self.write_reg(reg_addr, reg_val)

    @lpgbt_accessor
    def downlink_set_data_source(self, group_id, source):
        """Configures the downlink data source

        Arguments:
            group_id: downlink data path group number
            source: data path data source for group_id
        """
        assert group_id in range(4), "Invalid downlink data path group"
        assert source in range(4), "Invalid downlink data source"

        reg_addr = self.ULDATASOURCE5
        bit_pos = (group_id % 4) * 2
        reg_val = self.read_reg(reg_addr)
        reg_val &= ~(0x3 << bit_pos)
        reg_val |= source << bit_pos
        self.write_reg(reg_addr, reg_val)

    @lpgbt_accessor
    def pusm_get_state(self):
        """Returns the current Power-Up State Machine state"""
        return self.read_reg(self.PUSMSTATUS)

    @lpgbt_accessor
    def pusm_jump_to_state(self, state, release=True):
        """Jump to a given PUSM state

        Arguments:
            state: PUSM state to jump to
            release: allow PUSM to progress from the forced state
        """
        assert state in range(32), "Invalid PUSM state"

        self.write_reg(
            self.POWERUP3,
            self.POWERUP3.PUSMFORCESTATE.bit_mask
            | state << self.POWERUP3.PUSMSTATEFORCED.offset,
        )
        self.write_reg(self.POWERUP4, self.FORCESTATE_MAGIC_NUMBER)
        if release:
            self.write_reg(self.POWERUP3, 0)
            self.write_reg(self.POWERUP4, 0)

    @lpgbt_accessor
    def wait_pusm_state(self, state, timeout=2):
        """Wait until PUSM is in a given state

        Arguments:
            state: state to wait for
            timeout: timeout in seconds

        Raises:
            LpgbtException: if timeout is exceeded
        """
        assert state in range(32), "Invalid PUSM state"

        t_start = time.time()
        time_log = []
        status_log = []
        while True:
            time_elapsed = time.time() - t_start
            status = self.read_reg(self.PUSMSTATUS)

            time_log.append(time_elapsed)
            status_log.append(status)

            if status == state:
                return time_log, status_log

            if time_elapsed > timeout:
                self.logger.error(
                    f"Timeout while waiting for PUSM state {self.PusmState(state).name} "
                    f"(stuck in state {self.PusmState(status).name})"
                )
                self.log_pusm_status()
                raise LpgbtTimeoutError(
                    f"Timeout while waiting for PUSM state {self.PusmState(state).name} "
                    f"(stuck in state {self.PusmState(status).name})"
                )

    @lpgbt_accessor
    def chip_status(self):
        """Returns a list of strings summarizing the lpGBT configuration and status"""
        ret = []
        for group_id in range(7):
            ret += self.eprx_group_status(group_id)
        for group_id in range(4):
            ret += self.eptx_group_status(group_id)
        for clk_id in range(29):
            ret += self.eclk_status(clk_id)
        for ps_id in range(4):
            ret += self.phase_shifter_status(ps_id)
        ret += self.gpio_status()
        return ret

    @lpgbt_accessor
    def config_done(self, pll_config_done=True, dll_config_done=True):
        """Indicates completion of PLL/DLL configuration to the PUSM

        Arguments:
            pll_config_done: PLL configuration has been written
            dll_config_done: DLL configuration has been written
        """
        reg_val = 0
        if pll_config_done:
            reg_val |= self.POWERUP2.PLLCONFIGDONE.bit_mask
        if dll_config_done:
            reg_val |= self.POWERUP2.DLLCONFIGDONE.bit_mask

        self.write_reg(self.POWERUP2, reg_val)

    @lpgbt_accessor
    def config_done_and_wait_for_ready(
        self, pll_config_done=True, dll_config_done=True
    ):
        """Indicates completion of PLL/DLL config to PUSM, wait for READY state

        Arguments:
            pll_config_done: PLL configuration has been written
            dll_config_done: DLL configuration has been written
        """
        self.config_done(pll_config_done, dll_config_done)
        self.wait_pusm_state(self.PusmState.READY)

    def _i2c_master_get_reg_offsets(self, master_id):
        """Returns read and write register offsets for a given master_id
        relative to I2CM0CONFIG.

        Arguments:
            master_id: lpGBT I2C master number
        """
        assert master_id in range(3), "Invalid I2C master ID"

        offset_wr = master_id * (self.I2CM1CMD.address - self.I2CM0CMD.address)
        offset_rd = master_id * (self.I2CM1STATUS.address - self.I2CM0STATUS.address)

        return offset_wr, offset_rd

    @lpgbt_accessor
    def _i2c_master_set_slave_address(self, master_id, slave_address, addr_10bit):
        """Set I2C master slave address

        Arguments:
            master_id: lpGBT I2C master to use
            slave_address: I2C slave bus address
            addr_10bit: enable 10-bit addressing format
        """
        if addr_10bit:
            assert slave_address in range(1024), "Unsupported I2C slave address"
        else:
            assert slave_address in range(128), "Unsupported I2C slave address"

        offset_wr, _ = self._i2c_master_get_reg_offsets(master_id)

        address_low = slave_address & 0x7F
        address_high = (slave_address >> 7) & 0x07
        self.write_reg(self.I2CM0ADDRESS.address + offset_wr, address_low)

        if addr_10bit:
            config_reg_val = self.read_reg(self.I2CM0CONFIG.address + offset_wr)
            # pylint: disable=invalid-unary-operand-type
            config_reg_val &= ~self.I2CM0CONFIG.I2CM0ADDRESSEXT.bit_mask
            self.write_reg(
                self.I2CM0CONFIG.address + offset_wr,
                config_reg_val
                | address_high << self.I2CM0CONFIG.I2CM0ADDRESSEXT.offset,
            )

    @lpgbt_accessor
    def _i2c_master_issue_command(self, master_id, command, addr_10bit=False):
        """Execute I2C master read/write command

        Arguments:
            master_id: lpGBT I2C master to use
            command: command to be executed
            addr_10bit: execute 10 bit addressing version of command (R/W only)
        """
        assert master_id in range(3), "Invalid I2C master ID"

        offset_wr, _ = self._i2c_master_get_reg_offsets(master_id)

        # handle _EXT commands for 10 bit address read/write transactions
        if addr_10bit and command in [
            Lpgbt.I2cmCommand.ONE_BYTE_WRITE,
            Lpgbt.I2cmCommand.ONE_BYTE_READ,
            Lpgbt.I2cmCommand.WRITE_MULTI,
            Lpgbt.I2cmCommand.READ_MULTI,
        ]:
            command = Lpgbt.I2cmCommand[Lpgbt.I2cmCommand(command).name + "_EXT"]

        self.write_reg(self.I2CM0CMD.address + offset_wr, command)

    @lpgbt_accessor
    def _i2c_master_await_completion(self, master_id, timeout=0.1):
        """Wait until I2C master transaction is finished

        Arguments:
            master_id: lpGBT I2C master to use
            timeout: I2C write completion timeout

        Raises:
            LpgbtException: if timeout is exceeded
                            if the transaction is not acknowledged by the slave
                            if the SDA line is pulled down
        """
        _, offset_rd = self._i2c_master_get_reg_offsets(master_id)

        timeout_time = time.time() + timeout
        while True:
            status = self.read_reg(self.I2CM0STATUS.address + offset_rd)

            if status & self.I2cmStatusReg.SUCC.bit_mask:
                break

            if status & self.I2cmStatusReg.LEVEERR.bit_mask:
                raise LpgbtI2CMasterBusError(
                    "The SDA line is pulled low before initiating a transaction."
                )

            if status & self.I2cmStatusReg.NOACK.bit_mask:
                raise LpgbtI2CMasterTransactionError(
                    "The last transaction was not acknowledged by the I2C slave"
                )

            if time.time() > timeout_time:
                raise LpgbtTimeoutError(
                    f"Timeout while waiting for I2C master to finish (status:0x{status:02x})"
                )

    @lpgbt_accessor
    def i2c_master_reset(self, master_id):
        """Resets one of the lpGBT I2C masters

        Arguments:
            master_id: I2C master to reset
        """
        assert master_id in range(3), "Invalid I2C master ID"

        rst_reg_val = [
            self.RST0.RSTI2CM0.bit_mask,
            self.RST0.RSTI2CM1.bit_mask,
            self.RST0.RSTI2CM2.bit_mask,
        ]
        self.write_reg(self.RST0.address, rst_reg_val[master_id])
        self.write_reg(self.RST0.address, 0x0)

    @lpgbt_accessor
    def i2c_master_config(
        self,
        master_id,
        clk_freq=0,
        scl_drive=False,
        scl_pullup=False,
        scl_drive_strength=0,
        sda_pullup=False,
        sda_drive_strength=0,
    ):
        """General configuration register of the lpGBT I2C masters

        Arguments:
            master_id: lpGBT I2C master to use
            clk_freq: I2C master SCL frequency
            scl_drive: configure I2C master SCL as open-drain or full CMOS
            scl_pullup: Enable pull up for the I2C master SCL pin
            scl_drive_strength: SCL pin drive strength (1=high drive strength)
            sda_pullup: Enable pull up for the I2C master SDA pin
            sda_drive_strength: SDA pin drive strength (1=high drive strength)
        """
        # pylint: disable=too-many-arguments
        assert master_id in range(3), "Invalid I2C master ID"
        assert self.I2CM0CONFIG.I2CM0SCLDRIVESTRENGTH.validate(
            scl_drive_strength
        ), "Invalid scl pin drive strength"
        assert self.I2CM0CONFIG.I2CM0SDADRIVESTRENGTH.validate(
            sda_drive_strength
        ), "Invalid sda pin drive strength"
        assert clk_freq in range(4), "Invalid clock frequency"

        offset_wr, _ = self._i2c_master_get_reg_offsets(master_id)

        self.write_reg(
            self.I2CM0DATA0.address + offset_wr,
            clk_freq << self.I2cmConfigReg.FREQ.offset
            | scl_drive << self.I2cmConfigReg.SCLDRIVE.offset,
        )

        self._i2c_master_issue_command(master_id, self.I2cmCommand.WRITE_CRA)

        self.write_reg(
            self.I2CM0CONFIG.address + offset_wr,
            scl_pullup << self.I2CM0CONFIG.I2CM0SCLPULLUPENABLE.offset
            | scl_drive_strength << self.I2CM0CONFIG.I2CM0SCLDRIVESTRENGTH.offset
            | sda_pullup << self.I2CM0CONFIG.I2CM0SDAPULLUPENABLE.offset
            | sda_drive_strength << self.I2CM0CONFIG.I2CM0SDADRIVESTRENGTH.offset,
        )

    @lpgbt_accessor
    def _i2c_master_set_nbytes(self, master_id, nbytes):
        """
        Configures number of bytes used during multi-byte READ and WRITE
        transactions. Implemented as a RMW operation in order to preserve
        I2C master configuration fields.

        Arguments:
            master_id: lpGBT I2C master to use
            nbytes: Number of transaction data bytes
        """
        assert master_id in range(3), "Invalid I2C master ID"
        assert nbytes in range(17), "Invalid transaction length"

        offset_wr, offset_rd = self._i2c_master_get_reg_offsets(master_id)

        control_reg_val = self.read_reg(self.I2CM0CTRL.address + offset_rd)
        control_reg_val &= (
            ~self.I2cmConfigReg.NBYTES.bit_mask
        )  # pylint: disable=invalid-unary-operand-type
        self.write_reg(
            self.I2CM0DATA0.address + offset_wr,
            control_reg_val | nbytes << self.I2cmConfigReg.NBYTES.offset,
        )
        self._i2c_master_issue_command(master_id, self.I2cmCommand.WRITE_CRA)

    @lpgbt_accessor
    def i2c_master_write(
        self,
        master_id,
        slave_address,
        reg_address_width,
        reg_address,
        data,
        timeout=0.1,
        addr_10bit=False,
    ):
        """
        Performs a register-based write using an lpGBT I2C master.
        Register address is placed LSbyte first in the transaction data buffer,
        followed by the register contents (variable length).

        Errata note: 16 byte writes (including address and data) are only possible
        as specified in 7 bit slave addressing mode. When 10 bit addressing mode is
        used, the maximum number of bytes in a transaction is 15.

        Arguments:
            master_id: lpGBT I2C master to use
            slave_address: I2C slave bus address
            reg_address_width: length of register address in bytes
            reg_address: slave register write address
            data: data to write (single byte or list of bytes)
            timeout: I2C write completion timeout
            addr_10bit: enable 10-bit addressing format
        """
        # pylint: disable=too-many-arguments
        assert master_id in range(3), "Invalid I2C master ID"

        offset_wr, _ = self._i2c_master_get_reg_offsets(master_id)

        address_and_data = []
        for i in range(reg_address_width):
            address_and_data.append((reg_address >> (8 * i)) & 0xFF)
        try:
            data_list = list(data)
        except TypeError:
            data_list = list((data,))
        address_and_data.extend(data_list)
        if addr_10bit:
            assert len(address_and_data) in range(
                16
            ), "Maximum write length is 15 bytes in 10 bit addressing mode"
        else:
            assert len(address_and_data) in range(
                17
            ), "Maximum write length is 16 bytes in 7 bit addressing mode"

        self._i2c_master_set_nbytes(master_id, len(address_and_data))

        for i, data_byte in enumerate(address_and_data):
            self.write_reg(self.I2CM0DATA0.address + offset_wr + (i % 4), data_byte)
            if i % 4 == 3 or i == len(address_and_data) - 1:
                self._i2c_master_issue_command(
                    master_id, self.I2cmCommand.W_MULTI_4BYTE0 + (i // 4)
                )

        self._i2c_master_set_slave_address(master_id, slave_address, addr_10bit)
        self._i2c_master_issue_command(
            master_id, self.I2cmCommand.WRITE_MULTI, addr_10bit
        )

        self._i2c_master_await_completion(master_id, timeout)

    @lpgbt_accessor
    def i2c_master_read(
        self,
        master_id,
        slave_address,
        read_len,
        reg_address_width,
        reg_address,
        timeout=0.1,
        addr_10bit=False,
    ):
        """
        Performs a register-based read using an lpGBT I2C master.
        Register address pointer is written to the slave using a write
        transaction. Then, a multi-byte read transction is triggered to read
        slave register contents.

        Errata note: 16 byte reads (including address and data) are only possible
        as specified in 7 bit slave addressing mode. When 10 bit addressing mode is
        used, the maximum number of bytes in a transaction is 15.

        Arguments:
            master_id: lpGBT I2C master to use
            slave_address: I2C slave bus address
            read_len: number of bytes to read from slave
            reg_address_width: length of register address in bytes
            reg_address: slave register read address
            timeout: I2C write completion timeout
            addr_10bit: enable 10-bit addressing format
        """
        # pylint: disable=too-many-arguments
        assert master_id in range(3), "Invalid I2C master ID"
        assert reg_address_width in range(5), "Invalid register address width"

        if addr_10bit:
            assert read_len in range(
                16
            ), "Maximum read length is 15 bytes in 10 bit addressing mode"
        else:
            assert read_len in range(
                17
            ), "Maximum read length is 16 bytes in 7 bit addressing mode"

        offset_wr, offset_rd = self._i2c_master_get_reg_offsets(master_id)

        self._i2c_master_set_slave_address(master_id, slave_address, addr_10bit)
        for i in range(reg_address_width):
            self.write_reg(
                self.I2CM0DATA0.address + offset_wr + i, (reg_address >> (8 * i)) & 0xFF
            )
        self._i2c_master_issue_command(master_id, self.I2cmCommand.W_MULTI_4BYTE0)
        self._i2c_master_set_nbytes(master_id, reg_address_width)
        self._i2c_master_issue_command(
            master_id, self.I2cmCommand.WRITE_MULTI, addr_10bit
        )
        self._i2c_master_await_completion(master_id, timeout)

        self._i2c_master_set_nbytes(master_id, read_len)
        self._i2c_master_issue_command(
            master_id, self.I2cmCommand.READ_MULTI, addr_10bit
        )
        self._i2c_master_await_completion(master_id, timeout)

        read_values = []
        for i in range(read_len):
            read_values.append(self.read_reg(self.I2CM0READ15.address + offset_rd - i))
        return read_values

    @lpgbt_accessor
    def i2c_master_single_write(
        self,
        master_id,
        slave_address,
        data,
        timeout=0.1,
        addr_10bit=False,
    ):
        """
        Performs a single byte write using an lpGBT I2C masters

        Arguments:
            master_id: lpGBT I2C master to use
            slave_address: I2C slave bus address
            data: data to write
            timeout: I2C write completion timeout
            addr_10bit: enable 10-bit addressing format
        """
        # pylint: disable=too-many-arguments
        assert master_id in range(3), "Invalid I2C master ID"

        offset_wr, _ = self._i2c_master_get_reg_offsets(master_id)

        self.write_reg(self.I2CM0DATA0.address + offset_wr, data)
        self._i2c_master_set_slave_address(master_id, slave_address, addr_10bit)
        self._i2c_master_issue_command(
            master_id, self.I2cmCommand.ONE_BYTE_WRITE, addr_10bit
        )
        self._i2c_master_await_completion(master_id, timeout)

    @lpgbt_accessor
    def i2c_master_single_read(
        self,
        master_id,
        slave_address,
        timeout=0.1,
        addr_10bit=False,
    ):
        """
        Performs a single byte read using an lpGBT I2C masters

        Arguments:
            master_id: lpGBT I2C master to use
            slave_address: I2C slave bus address
            timeout: I2C write completion timeout
            addr_10bit: enable 10-bit addressing format
        """
        # pylint: disable=too-many-arguments, too-many-locals
        assert master_id in range(3), "Invalid I2C master ID"

        _, offset_rd = self._i2c_master_get_reg_offsets(master_id)

        self._i2c_master_set_slave_address(master_id, slave_address, addr_10bit)
        self._i2c_master_issue_command(
            master_id, self.I2cmCommand.ONE_BYTE_READ, addr_10bit
        )
        self._i2c_master_await_completion(master_id, timeout)

        read_value = self.read_reg(self.I2CM0READBYTE.address + offset_rd)
        return read_value

    @lpgbt_accessor
    def i2c_master_get_transaction_counter(self, master_id):
        """
        Reads the i2c master transaction counter value

        Arguments:
            master_id: lpGBT I2C master to use
        """
        assert master_id in range(3), "Invalid I2C master ID"

        _, offset_rd = self._i2c_master_get_reg_offsets(master_id)
        result = self.read_reg(self.I2CM0TRANCNT.address + offset_rd)

        return result

    @lpgbt_accessor
    def get_process_monitor(self, channel, timeout=1):
        """Enables process monitor channel and reads frequency

        Arguments:
            channel: process monitor channel to use
            timeout: measurement completion timeout
        """
        assert channel in range(4), "Invalid process monitor channel"

        reg_val_masked = self.read_reg(self.PROCESSANDSEUMONITOR) & (
            ~(
                self.PROCESSANDSEUMONITOR.PMCHANNEL.bit_mask
                + self.PROCESSANDSEUMONITOR.PMENABLE.bit_mask
            )  # pylint: disable=invalid-unary-operand-type
        )
        cntr_reg = reg_val_masked | (
            channel << self.PROCESSANDSEUMONITOR.PMCHANNEL.offset
        )
        self.write_reg(self.PROCESSANDSEUMONITOR, cntr_reg)
        cntr_reg |= self.PROCESSANDSEUMONITOR.PMENABLE.bit_mask
        self.write_reg(self.PROCESSANDSEUMONITOR, cntr_reg)
        timeout_time = time.time() + timeout
        while True:
            status = self.read_reg(self.PROCESSMONITORSTATUS)
            if status & self.PROCESSMONITORSTATUS.PMDONE.bit_mask:
                break
            if time.time() > timeout_time:
                raise LpgbtTimeoutError(
                    f"Timeout while waiting for process monitor (status: 0x{status:02x})"
                )
        results = self.read_regs(self.PMFREQA, read_len=3)
        self.write_reg(self.PROCESSANDSEUMONITOR, reg_val_masked)

        return results[0] << 16 | results[1] << 8 | results[2]

    @lpgbt_accessor
    def seu_monitor_setup(self, enable=True):
        """Configures the SEU monitor.

        Arguments:
            enable: whether SEU monitor functionality should be enabled
        """
        reg_val = self.read_reg(self.PROCESSANDSEUMONITOR)
        if enable:
            reg_val |= self.PROCESSANDSEUMONITOR.SEUENABLE.bit_mask
        else:
            reg_val &= (
                ~self.PROCESSANDSEUMONITOR.SEUENABLE.bit_mask  # pylint: disable=invalid-unary-operand-type
            )
        self.write_reg(self.PROCESSANDSEUMONITOR, reg_val)

    @lpgbt_accessor
    def seu_monitor_read(self):
        """Reads the SEU monitor counter value"""
        results = self.read_regs(self.SEUCOUNTH, read_len=2)
        return results[0] << 8 | results[1]

    @lpgbt_accessor
    def cmos_test_output_setup(
        self, chn, select: LpgbtEnums.TestOutSelect, high_drive_strength=True
    ):
        """Configures a CMOS test output

        Arguments:
            chn: test output to configure (0-3)
            select: selects a signal to be outputted
            high_drive_strength: if true, driver has high driver strength
        """

        # pylint: disable=too-many-arguments
        assert chn in range(4), "Invalid test output channel"

        driving_strength = self.read_reg(self.TODRIVINGSTRENGTH)
        if high_drive_strength:
            driving_strength |= 1 << chn
        else:
            driving_strength &= ~(1 << chn)

        self.write_reg(self.TO0SEL.address + chn, select)
        self.write_reg(self.TODRIVINGSTRENGTH, driving_strength)

    @lpgbt_accessor
    def differential_test_output_setup(
        self,
        chn,
        select: LpgbtEnums.TestOutSelect,
        drive_strength=LpgbtEnums.EtxCurrent.AMP_2MA,
        preemphasis_strength=LpgbtEnums.EtxCurrent.AMP_0MA,
        preemphasis_mode=LpgbtEnums.EtxPreEmpahasisMode.DISABLE,
        preemphasis_width=LpgbtEnums.EtxPreEmpahasisWidth.PREEMP_120PS,
        invert=False,
    ):
        """Configures a single eClock

        Arguments:
            chn: test output to configure (4-5)
            select: selects a signal to be outputted
            drive_strength: output driver strength (0-7)
            preemphasis_strength: output driver preemphasis strength (0-7)
            preemphasis_mode: output driver preemphasis mode
            preemphasis_width: output driver preemphasis width (0-7)
            invert: output clock inversion control
        """

        # pylint: disable=too-many-arguments
        assert chn in (4, 5), "Invalid test output channel"

        assert self.TO4DRIVER.TO4DRIVESTRENGTH.validate(
            drive_strength
        ), "Invalid drivestrength"
        assert self.TO4DRIVER.TO4PREEMPHASISSTRENGTH.validate(
            preemphasis_strength
        ), "Invalid preemphasis strength"
        assert self.TO4DRIVER.TO4PREEMPHASISMODE.validate(
            preemphasis_mode
        ), "Invalid preemphasis mode"
        assert self.TOPREEMP.TO4PREEMPHASISWIDTH.validate(preemphasis_width) in range(
            8
        ), "Invalid preemphasis width"

        driver_config = (
            preemphasis_strength << self.TO4DRIVER.TO4PREEMPHASISSTRENGTH.offset
            | preemphasis_mode << self.TO4DRIVER.TO4PREEMPHASISMODE.offset
            | drive_strength << self.TO4DRIVER.TO4DRIVESTRENGTH.offset
        )

        topreemp = self.read_reg(self.TOPREEMP)
        if chn == 4:
            topreemp &= 0xF0
            topreemp |= preemphasis_width << self.TOPREEMP.TO4PREEMPHASISWIDTH.offset
            if invert:
                topreemp |= self.TOPREEMP.TO4INVERT.bit_mask
        else:
            topreemp &= 0x0F
            topreemp |= preemphasis_width << self.TOPREEMP.TO5PREEMPHASISWIDTH.offset
            if invert:
                topreemp |= self.TOPREEMP.TO5INVERT.bit_mask

        self.write_reg(self.TO0SEL.address + chn, select)
        self.write_reg(self.TO4DRIVER.address + (chn - 4), driver_config)
        self.write_reg(self.TOPREEMP.address, topreemp)

    @lpgbt_accessor
    def vref_enable(self, enable=True, tune=0):
        """Controls the bandgap reference voltage generator

        Arguments:
            enable: reference generator state
            tune: reference voltage tuning word
        """
        raise NotImplementedError()

    @lpgbt_accessor
    def clkg_get_cap_bank(self):
        """Returns the value of the selected capacitor bank (0-55).
        The returned value is already decoded to monotonic binary number."""

        bank_h, bank_l = self.read_regs(self.CLKGSTATUS5, read_len=2)

        bank_l = (
            bank_l & self.CLKGSTATUS6.CLKG_VCOCAPSELECT.bit_mask
        ) >> self.CLKGSTATUS6.CLKG_VCOCAPSELECT.offset
        bank = bank_h << 1 | bank_l
        bank_bin = bank % 8
        bank_thermo = bin(bank & 0x1F8).count("1")
        bank = bank_bin + bank_thermo * 8
        return bank

    @lpgbt_accessor
    def clkg_set_cap_bank(self, bank, force=True):
        """Sets (forces) the capacitor bank value for the VCO

        Arguments:
            bank: bank to be set (0 - 55)
            force: force bank
        """
        assert bank in range(self.CLKG_CAPBANKS), f"Invalid capacitor bank ({bank})"

        bank_bin = bank % 8
        bank_thermo = 2 ** int(bank / 8) - 1
        bank = bank_bin | bank_thermo << 3
        conf0 = self.read_reg(self.CLKGLFCONFIG0)
        if bank & 0x100:
            conf0 |= self.CLKGLFCONFIG0.CLKGCAPBANKSELECT.bit_mask
        else:
            conf0 &= (
                ~self.CLKGLFCONFIG0.CLKGCAPBANKSELECT.bit_mask  # pylint: disable=invalid-unary-operand-type
            )
        self.write_reg(self.CLKGLFCONFIG0, conf0)
        self.write_reg(self.CLKGOVERRIDECAPBANK, bank & 0xFF)

        config = self.read_reg(self.CLKGFFCAP)
        if force:
            config |= self.CLKGFFCAP.CLKGCAPBANKOVERRIDEENABLE.bit_mask
        else:
            config &= (
                ~self.CLKGFFCAP.CLKGCAPBANKOVERRIDEENABLE.bit_mask  # pylint: disable=invalid-unary-operand-type
            )
        self.write_reg(self.CLKGFFCAP, config)

    @lpgbt_accessor
    def fec_error_counter_enable(self, enable=True):
        """Enables/disables the FEC error counter

        Arguments:
            enable: state of the fec error counter
        """
        raise NotImplementedError()

    @lpgbt_accessor
    def clk_tree_disable(
        self, clk_a_disable=False, clk_b_disable=False, clk_c_disable=False
    ):
        """Enables/disables one of the triplicated clock tree.
        This feature should never be exercised in production environment as it is meant
        only for production testing.

        Arguments:
            clk_a_disable: disables clock tree A
            clk_b_disable: disables clock tree B
            clk_c_disable: disables clock tree C
        """

        reg_value = 0
        if clk_a_disable or clk_b_disable or clk_c_disable:
            reg_value = self.CLK_DISABLE_MAGIC << self.CLKTREE.CLKTREEMAGICNUMBER.offset
            if clk_a_disable:
                reg_value |= self.CLKTREE.CLKTREEADISABLE.bit_mask
            if clk_b_disable:
                reg_value |= self.CLKTREE.CLKTREEBDISABLE.bit_mask
            if clk_c_disable:
                reg_value |= self.CLKTREE.CLKTREECDISABLE.bit_mask
        self.write_reg(self.CLKTREE.address, reg_value)

    @lpgbt_accessor
    def get_config_error_counter(self):
        """Get the current value of configuration error correction counter"""

        config_err_cnt_h, config_err_cnt_l = self.read_regs(self.CONFIGERRORCOUNTERH, 2)
        return config_err_cnt_h << 8 | config_err_cnt_l

    @lpgbt_accessor
    def reset_config_error_counter(self):
        """Resets the configuration error correction counter"""

        self.write_reg(self.CONFIGERRORCOUNTERH.address, 0x0)
