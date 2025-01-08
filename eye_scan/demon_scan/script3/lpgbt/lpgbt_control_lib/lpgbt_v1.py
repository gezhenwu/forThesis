#!/usr/bin/env python3
###############################################################################
#                                                                             #
#  Copyright (C) 2021 lpGBT Team, CERN                                        #
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
"""Driver implementation for lpGBTv1 chip revision"""
# pylint: disable=too-few-public-methods,too-many-ancestors

import zlib
import array
from .lpgbt import Lpgbt, u32_to_bytes, lpgbt_accessor
from .lpgbt_register_map_v1 import LpgbtRegisterMapV1
from .lpgbt_pins_v1 import LpgbtPinsV1
from .lpgbt_enums_v1 import LpgbtEnumsV1


def calculate_crc32(protected_registers):
    """Calculate value of CRC32"""

    protected_registers_as_bytes = array.array("B", protected_registers).tobytes()
    crc = zlib.crc32(protected_registers_as_bytes) & 0xFFFFFFFF
    crc_inverted = crc ^ 0xFFFFFFFF
    return crc_inverted


class LpgbtV1(LpgbtPinsV1, LpgbtEnumsV1, LpgbtRegisterMapV1, Lpgbt):
    """Implementation of lpGBT driver for lpGBTv1"""

    def ctrl_pins_default(self):
        """Sets all control pins to their default values"""
        Lpgbt.ctrl_pins_default(self)
        self.set_bootcnf_pins(self.BootConfig.NO_INIT)
        self.set_ctrl_pin(self.CTRL_EDINECTERM, False)

    def set_bootcnf_pins(self, boot_config):
        """Sets BOOTCNF pins

        Arguments:
            boot_config: boot config
        """
        assert boot_config in range(4), "Bootcnf has only 2 bits (0-3)"

        self.set_ctrl_pin(self.CTRL_BOOTCNF0, boot_config & 0x01)
        self.set_ctrl_pin(self.CTRL_BOOTCNF1, boot_config & 0x02)

    @lpgbt_accessor
    def get_fec_error_counter(self):
        """Returns the value of the FEC error counter"""
        regs = self.read_regs(self.DLDPFECCORRECTIONCOUNT0, read_len=4)
        value = regs[0] << 24 | regs[1] << 16 | regs[2] << 8 | regs[3] << 0
        return value

    @lpgbt_accessor
    def fec_error_counter_enable(self, enable=True):
        """Controls the FEC error counter

        Arguments:
            enable: FEC error counter state
        """
        reg_val = self.read_reg(self.DATAPATH)
        if enable:
            reg_val |= self.DATAPATH.DLDPFECCOUNTERENABLE.bit_mask
        else:
            reg_val &= ~self.DATAPATH.DLDPFECCOUNTERENABLE.bit_mask
        self.write_reg(self.DATAPATH, reg_val)

    @lpgbt_accessor
    def fec_error_counter_reset(self):
        """Resets the FEC error counter"""
        self.write_reg(self.DLDPFECCORRECTIONCOUNT0, 0x0)

    @lpgbt_accessor
    def vref_enable(self, enable=True, tune=0):
        """Controls the bandgap reference voltage generator

        Arguments:
            enable: reference generator state
            tune: reference voltage tuning word
        """
        assert self.VREFTUNE.VREFTUNE.validate(
            tune
        ), "Invalid reference voltage tuning word"

        cntr = 0
        if enable:
            cntr |= self.VREFCNTR.VREFENABLE.bit_mask
        self.write_reg(self.VREFCNTR, cntr)
        self.write_reg(self.VREFTUNE, int(tune) << self.VREFTUNE.VREFTUNE.offset)

    @lpgbt_accessor
    def eclk_setup(
        self,
        clk_id,
        freq=0,
        drive_strength=4,
        preemphasis_strength=0,
        preemphasis_mode=0,
        preemphasis_width=0,
        invert=False,
        low_res=False,
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
            low_res: decreases the power supply filter resistance
        """
        # pylint: disable=too-many-arguments
        config_high, config_low = self._eclk_setup_common(
            clk_id=clk_id,
            freq=freq,
            drive_strength=drive_strength,
            preemphasis_strength=preemphasis_strength,
            preemphasis_mode=preemphasis_mode,
            preemphasis_width=preemphasis_width,
            invert=invert,
        )

        if low_res:
            config_high |= self.EPCLK0CHNCNTRH.EPCLK0LOWRES.bit_mask

        self.write_reg(self.EPCLK0CHNCNTRH.address + 2 * clk_id, config_high)
        self.write_reg(self.EPCLK0CHNCNTRL.address + 2 * clk_id, config_low)

    @lpgbt_accessor
    def log_pusm_status(self):
        """Verbosely logs current status of the power up state machine"""
        (
            status,
            pusm_pll_watchdog,
            pusm_dll_watchdog,
            pusm_csum_watchdog,
            pusm_brownout_watchdog,
            pusm_pll_timeout,
            pusm_dll_timeout,
            pusm_channels_timeout,
            crc0,
            crc1,
            crc2,
            crc3,
            failed_crc,
        ) = self.read_regs(self.PUSMSTATUS, 13)

        status_str = self.PusmState(status).name
        self.logger.info("Power Up State Machine")
        self.logger.info("  State  : 0x%02X (%s)", status, status_str)
        self.logger.info("  Watchdog action counters")
        self.logger.info("    PLL  : %d", pusm_pll_watchdog)
        self.logger.info("    DLL  : %d", pusm_dll_watchdog)
        self.logger.info("    CSUM : %d", pusm_csum_watchdog)
        self.logger.info("  Brownout action flag : %d", pusm_brownout_watchdog)
        self.logger.info("  Timeout action counters")
        self.logger.info("    PLL  : %d", pusm_pll_timeout)
        self.logger.info("    DLL  : %d", pusm_dll_timeout)
        self.logger.info("    CSUM : %d", pusm_channels_timeout)
        self.logger.info("  CRC")
        self.logger.info("    Value: 0x%02X%02X%02X%02X", crc3, crc2, crc1, crc0)
        self.logger.info("    Invalid cycles: %d", failed_crc)

    @lpgbt_accessor
    def write_crc32(self, value):
        """Write 32bit value of CRC"""

        self.write_regs(self.CRC0, list(reversed(u32_to_bytes(value))))

    @lpgbt_accessor
    def calculate_and_write_crc32(self, protected_registers):
        """Update value of CRC32"""
        crc = calculate_crc32(protected_registers)
        self.write_crc32(crc)

    @lpgbt_accessor
    def ready_pin_setup(
        self, chns_enable=False, dll_enable=False, clkg_enable=False, pusm_disable=False
    ):
        """Configure the behavior of READY pin.

        Arguments:
            chns_enable:  When true, the READY signal will go low when one of
                          the ePortRx channels is unlocked. Not recommended.
            dll_enable:   When true, the READY signal will go low when one of
                          the DLLs declares a temporary loss of lock. Not recommended.
            clkg_enable:  When set, the READY signal will go low when the clock
                          generator (or frame aligner) declares a temporary
                          loss of lock. Not recommended.
            pusm_disable: When set, the READY signal will not depend on PUSM state.
                          Not recommended.
        """

        reg_val = 0
        if chns_enable:
            reg_val |= self.READY.READYCHNSENABLE.bit_mask

        if dll_enable:
            reg_val |= self.READY.READYDLLSENABLE.bit_mask

        if clkg_enable:
            reg_val |= self.READY.READYCLKGENABLE.bit_mask

        if pusm_disable:
            reg_val |= self.READY.READYPUSMDISABLE.bit_mask

        self.write_reg(self.READY, reg_val)

    @lpgbt_accessor
    def internal_voltage_monitors(
        self,
        temp_sensor_reset=True,
        vdd_mon_enable=True,
        vddtx_mon_enable=True,
        vddrx_mon_enable=True,
        vddadc_mon_enable=True,
    ):
        """Configures the lpGBT voltage monitors and temperature sensor.

        Arguments:
            temp_sensor_reset: temperature sensor reset control
            vdd_mon_enable: VDD monitor state
            vddtx_mon_enable: VDDTX monitor state
            vddrx_mon_enable: VDDRX monitor state
            vddadc_mon_enable: VDDADC monitor state
        """
        # pylint: disable=too-many-arguments

        adcmon = 0
        if temp_sensor_reset:
            adcmon |= self.ADCMON.TEMPSENSRESET.bit_mask
        if vdd_mon_enable:
            adcmon |= self.ADCMON.VDDMONENA.bit_mask
        if vddtx_mon_enable:
            adcmon |= self.ADCMON.VDDTXMONENA.bit_mask
        if vddrx_mon_enable:
            adcmon |= self.ADCMON.VDDRXMONENA.bit_mask
        if vddadc_mon_enable:
            adcmon |= self.ADCMON.VDDANMONENA.bit_mask

        self.write_reg(self.ADCMON, adcmon)

    @lpgbt_accessor
    def config_watchdog(
        self,
        pll_watchdog_enable=True,
        dll_watchdog_enable=True,
        checksum_watchdog_enable=False,
    ):
        """Configure watchdog

        Arguments:
            pll_watchdog_enable: enables PLL watchdog
            dll_watchdog_enable: enables DLL watchdog
            checksum_watchdog_enable: enables checksum watchdog
        """

        reg_val = 0x0
        if not pll_watchdog_enable:
            reg_val |= self.WATCHDOG.PUSMPLLWDOGDISABLE.bit_mask
        if not dll_watchdog_enable:
            reg_val |= self.WATCHDOG.PUSMDLLWDOGDISABLE.bit_mask
        if checksum_watchdog_enable:
            reg_val |= self.WATCHDOG.PUSMCHECKSUMWDOGENABLE.bit_mask
        self.write_reg(self.WATCHDOG, reg_val)

    @lpgbt_accessor
    def reset_brownout_watchdog_flag(self):
        """Resets PUSMbrownoutActionFlag"""

        self.write_reg(self.PUSMBROWNOUTWATCHDOG, 0x0)

    @lpgbt_accessor
    def brownout_config(self, enable=True, level=LpgbtEnumsV1.VddLevel.VDD_LEVEL_0V90):
        """Resets PUSMbrownoutActionFlag"""
        reg_value = level << self.RESETCONFIG.BODLEVEL.offset
        if enable:
            reg_value |= self.RESETCONFIG.BODENABLE.bit_mask
        self.write_reg(self.RESETCONFIG, reg_value)

    @lpgbt_accessor
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
        # pylint: disable= too-many-arguments

        dll_config = self._eprx_general_config(
            dll_current=dll_current,
            dll_confirm_count=dll_confirm_count,
            coarse_lock_detection=coarse_lock_detection,
            fsm_clk_always_on=fsm_clk_always_on,
            reinit_enable=reinit_enable,
        )
        if not data_gating_enable:
            dll_config |= self.EPRXDLLCONFIG.EPRXDATAGATINGDISABLE.bit_mask
        self.write_reg(self.EPRXDLLCONFIG, dll_config)

    @lpgbt_accessor
    def eprx_ec_setup(
        self,
        enable=True,
        term=True,
        ac_bias=False,
        invert=False,
        phase=0,
        pull_up_enable=True,
        track_mode=0,
        auto_phase_reset_disable=False,
    ):
        """Configures the External Control (EC) ePortRx

        Arguments:
            enable: state of the EC ePortRx
            term: input termination control
            ac_bias: AC bias generation control
            invert: data inversion control
            phase: EC static phase selection
            pull_up_enable: enable pull up
            track_mode: phase tracking mode for the EC channel
            auto_phase_reset_disable: disable the automatic phase reset
                in between transactions.
        """
        # pylint: disable=too-many-arguments

        assert self.EPRXECCHNCNTR.EPRXECPHASESELECT.validate(phase), "Invalid phase"

        chn_cntr = phase << self.EPRXECCHNCNTR.EPRXECPHASESELECT.offset
        if term:
            chn_cntr |= self.EPRXECCHNCNTR.EPRXECTERM.bit_mask
        if ac_bias:
            chn_cntr |= self.EPRXECCHNCNTR.EPRXECACBIAS.bit_mask
        if invert:
            chn_cntr |= self.EPRXECCHNCNTR.EPRXECINVERT.bit_mask
        if pull_up_enable:
            chn_cntr |= self.EPRXECCHNCNTR.EPRXECPULLUPENABLE.bit_mask
        self.write_reg(self.EPRXECCHNCNTR, chn_cntr)

        ec_control = 0x0
        if enable:
            ec_control |= self.EPRXECCONTROL.EPRXECENABLE.bit_mask
        if auto_phase_reset_disable:
            ec_control |= self.EPRXECCONTROL.EPRXECAUTOPHASERESETDISABLE.bit_mask
        if track_mode:
            ec_control |= self.EPRXECCONTROL.EPRXECTRACKMODE.bit_mask
        self.write_reg(self.EPRXECCONTROL, ec_control)

    @lpgbt_accessor
    def eptx_ec_setup(
        self,
        enable=True,
        tri_state=False,
        drive_strength=4,
        pre_emphasis_mode=0,
        pre_emphasis_strength=0,
        pre_emphasis_width=0,
        invert=False,
    ):
        """Configures the External Control (EC) ePortTx

        Arguments:
            enable: EC ePortTx state
            drive_strength: output driver strength
            tri_state: enable tri-state operation of EC channel output in
                simplex modes.
            pre_emphasis_mode: output driver pre-emphasis mode
            pre_emphasis_strength: output driver pre-emphasis strength
            pre_emphasis_width: output driver pre-emphasis width
            invert: output data inversion control
        """
        # pylint: disable=too-many-arguments
        assert drive_strength in range(8), "Invalid drive strength configuration"
        assert pre_emphasis_strength in range(8), "Invalid preemphasis strength"
        assert pre_emphasis_mode in range(4), "Invalid preemphasis mode"
        assert pre_emphasis_width in range(4), "Invalid preemphasis width"

        ec_chn_cntr = drive_strength << self.EPTXECCHNCNTR.EPTXECDRIVESTRENGTH.offset
        if enable:
            ec_chn_cntr |= self.EPTXECCHNCNTR.EPTXECENABLE.bit_mask
        if invert:
            ec_chn_cntr |= self.EPTXECCHNCNTR.EPTXECINVERT.bit_mask
        if tri_state:
            ec_chn_cntr |= self.EPTXECCHNCNTR.EPTXECTRISTATE.bit_mask
        self.write_reg(self.EPTXECCHNCNTR, ec_chn_cntr)

        ec_chn_cntr2 = (
            pre_emphasis_width << self.EPTXECCHNCNTR2.EPTXECPREEMPHASISWIDTH.offset
        )
        ec_chn_cntr2 |= (
            pre_emphasis_mode << self.EPTXECCHNCNTR2.EPTXECPREEMPHASISMODE.offset
        )
        ec_chn_cntr2 |= (
            pre_emphasis_strength
            << self.EPTXECCHNCNTR2.EPTXECPREEMPHASISSTRENGTH.offset
        )
        self.write_reg(self.EPTXECCHNCNTR2, ec_chn_cntr2)

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
        low_res=False,
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
            low_res: decreases the power supply filter resistance
        """
        # pylint: disable=too-many-arguments
        # pylint: disable=arguments-differ

        Lpgbt.eptx_channel_config(
            self,
            group_id=group_id,
            channel_id=channel_id,
            drive_strength=drive_strength,
            pre_emphasis_mode=pre_emphasis_mode,
            pre_emphasis_strength=pre_emphasis_strength,
            pre_emphasis_width=pre_emphasis_width,
            invert=invert,
        )
        reg_address = self.EPTXLOWRES0.address + int(group_id / 2)
        bit_address = group_id % 2 * 4 + channel_id

        reg_val = self.read_reg(reg_address)
        if low_res:
            reg_val |= 1 << bit_address
        else:
            reg_val &= ~(1 << bit_address)
        self.write_reg(reg_address, reg_val)
