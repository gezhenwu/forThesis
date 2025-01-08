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
"""Driver implementation for lpGBTv0 (prototype) chip revision"""
# pylint: disable=too-few-public-methods,too-many-ancestors

from .lpgbt import Lpgbt, lpgbt_accessor
from .lpgbt_register_map_v0 import LpgbtRegisterMapV0
from .lpgbt_pins_v0 import LpgbtPinsV0
from .lpgbt_enums_v0 import LpgbtEnumsV0


class LpgbtV0(LpgbtPinsV0, LpgbtEnumsV0, LpgbtRegisterMapV0, Lpgbt):
    """Implementation of lpGBT driver for lpGBTv0"""

    def ctrl_pins_default(self):
        """Sets all control pins to their default values"""
        Lpgbt.ctrl_pins_default(self)
        self.set_ctrl_pin(self.CTRL_SCI2C, self.ConfigSelect.I2C)
        self.set_ctrl_pin(self.CTRL_STATEOVRD, False)
        self.set_ctrl_pin(self.CTRL_VCOBYPASS, False)

    @lpgbt_accessor
    def rstoutb_config(self, pulse_duration):
        """Configures the RSTOUTB pin"""
        assert pulse_duration in range(4), "Invalid reset pulse duration"

        self.write_reg(
            self.RESETCONFIG,
            self.RESETCONFIG.RESETOUTDRIVESTRENGTH.bit_mask
            | pulse_duration << self.RESETCONFIG.RESETOUTLENGTH.offset,
        )

    @lpgbt_accessor
    def clock_generator_setup(self):
        """Writes the default configuration for the lpGBT clock generator"""
        Lpgbt.clock_generator_setup(self)
        self.write_reg(self.PSDLLCONFIG, 0xA)

        self.write_reg(self.FAMAXHEADERFOUNDCOUNT, 0x10)
        self.write_reg(self.FAMAXHEADERFOUNDCOUNTAFTERNF, 0x10)
        self.write_reg(self.FAMAXHEADERNOTFOUNDCOUNT, 0x10)
        self.write_reg(self.FAFAMAXSKIPCYCLECOUNTAFTERNF, 0x40)

    @lpgbt_accessor
    def vref_enable(self, enable=True, tune=0):
        """Controls the bandgap reference voltage generator

        Arguments:
            enable: reference generator state
            tune: reference voltage tuning word
        """
        assert self.VREFCNTR.VREFTUNE.validate(
            tune
        ), "Invalid reference voltage tuning word"

        config = int(tune) << self.VREFCNTR.VREFTUNE.offset
        if enable:
            config |= self.VREFCNTR.VREFENABLE.bit_mask
        self.write_reg(self.VREFCNTR, config)

    @lpgbt_accessor
    def internal_voltage_monitors(
        self,
        temp_sensor_reset=True,
        vdd_mon_enable=True,
        vddtx_mon_enable=True,
        vddrx_mon_enable=True,
        vddadc_mon_enable=True,
        vddpst_mon_enable=True,
    ):
        """Configures the lpGBT voltage monitors and temperature sensor.

        Arguments:
            temp_sensor_reset: temperature sensor reset control
            vdd_mon_enable: VDD monitor state
            vddtx_mon_enable: VDDTX monitor state
            vddrx_mon_enable: VDDRX monitor state
            vddadc_mon_enable: VDDADC monitor state
            vddpst_mon_enable: VDDPST monitor state
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
        if vddpst_mon_enable:
            adcmon |= self.ADCMON.VDDPSTMONENA.bit_mask

        self.write_reg(self.ADCMON, adcmon)

    @lpgbt_accessor
    def pll_watchdog_config(self, wd_pll_enable, wd_pll_timeout):
        """Configures the PLL watchdog

        Arguments:
            wd_pll_enable: True if watchdog should be enabled (default)
            wd_pll_timeout: One of the valid POWERUP0.PUSMPLLTIMEOUTCONFIG values
        """
        assert wd_pll_timeout in range(16), "Invalid PLL watchdog timeout value"

        reg_val = self.read_reg(self.POWERUP0)
        reg_val &= ~self.POWERUP0.PUSMPLLWDOGDISABLE.bit_mask
        reg_val &= ~(0x0F << self.POWERUP0.PUSMPLLTIMEOUTCONFIG.offset)

        if not wd_pll_enable:
            reg_val |= self.POWERUP0.PUSMPLLWDOGDISABLE.bit_mask
        reg_val |= wd_pll_timeout << self.POWERUP0.PUSMPLLTIMEOUTCONFIG.offset

        self.write_reg(self.POWERUP0, reg_val)

    @lpgbt_accessor
    def get_fec_error_counter(self):
        """Returns the value of the FEC error counter"""
        regs = self.read_regs(self.DLDPFECCORRECTIONCOUNTH, read_len=2)
        value = regs[0] << 8 | regs[1]
        return value

    @lpgbt_accessor
    def log_pusm_status(self):
        """Verbosely logs current status of the power up state machine"""
        status = self.read_reg(self.PUSMSTATUS)
        status_str = "-"
        if status in self.PusmState:
            status_str = self.PusmState(status).name
        self.logger.info("PUSMSTATUS : 0x%02X (%s)", status, status_str)

        actions = self.read_reg(self.PUSMACTIONS)
        actions_list = []
        if actions & self.PUSMACTIONS.PUSMPLLTIMEOUTACTION.bit_mask:
            actions_list.append("PLLTIMEOUTACTION")

        if actions & self.PUSMACTIONS.PUSMDLLTIMEOUTACTION.bit_mask:
            actions_list.append("DLLTIMEOUTACTION")

        if actions & self.PUSMACTIONS.PUSMCHANNELSTIMEOUTACTION.bit_mask:
            actions_list.append("CHANNELSTIMEOUTACTION")

        if actions & self.PUSMACTIONS.PUSMBROWNOUTACTION.bit_mask:
            actions_list.append("BROWNOUTACTION")

        if actions & self.PUSMACTIONS.PUSMPLLWATCHDOGACTION.bit_mask:
            actions_list.append("PLLWATCHDOGACTION")

        if actions & self.PUSMACTIONS.PUSMDLLWATCHDOGACTION.bit_mask:
            actions_list.append("DLLWATCHDOGACTION")

        self.logger.info("PUSMACTIONS : 0x%02X (%s)", actions, " ".join(actions_list))

    @lpgbt_accessor
    def fec_error_counter_enable(self, enable=True):
        """Controls the FEC error counter

        Arguments:
            enable: FEC error counter state
        """
        reg_val = self.read_reg(self.PROCESSANDSEUMONITOR)
        if enable:
            reg_val |= self.PROCESSANDSEUMONITOR.DLDPFECCOUNTERENABLE.bit_mask
        else:
            reg_val &= ~self.PROCESSANDSEUMONITOR.DLDPFECCOUNTERENABLE.bit_mask
        self.write_reg(self.PROCESSANDSEUMONITOR, reg_val)

    @lpgbt_accessor
    def fec_error_counter_reset(self):
        """Resets the FEC error counter"""
        self.fec_error_counter_enable(enable=False)
        self.fec_error_counter_enable(enable=True)

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
        if data_gating_enable:
            dll_config |= self.EPRXDLLCONFIG.EPRXDATAGATINGENABLE.bit_mask
        self.write_reg(self.EPRXDLLCONFIG, dll_config)

    @lpgbt_accessor
    def eprx_ec_setup(
        self, enable=True, track_mode=2, term=True, ac_bias=False, invert=False, phase=0
    ):
        """Configures the External Control (EC) ePortRx

        Arguments:
            enable: state of the EC ePortRx
            track_mode: phase selection mode (EPORTRXMODE_FIXED, EPORTRXMODE_CONTINOUSTRACKING, ...)
            term: input termination control
            ac_bias: AC bias generation control
            invert: data inversion control
            phase: EC static phase selection
        """
        # pylint: disable=too-many-arguments
        assert track_mode in range(4), "Invalid ePortRx phase selection mode"

        control = (phase & 0xFF) << self.EPRXECCHNCNTR.EPRXECPHASESELECT.offset
        if enable:
            control |= self.EPRXECCHNCNTR.EPRXECENABLE.bit_mask
        if term:
            control |= self.EPRXECCHNCNTR.EPRXECTERM.bit_mask
        if ac_bias:
            control |= self.EPRXECCHNCNTR.EPRXECACBIAS.bit_mask
        if invert:
            control |= self.EPRXECCHNCNTR.EPRXECINVERT.bit_mask

        self.write_reg(self.EPRXECCHNCNTR, control)
        self.write_reg(self.EPRXECCONTROL, track_mode)

    @lpgbt_accessor
    def eptx_ec_setup(
        self,
        enable=True,
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

        control_val = self.read_reg(self.EPTXCONTROL)
        control_val &= ~(0xF0)
        if enable:
            control_val |= self.EPTXCONTROL.EPTXECENABLE.bit_mask
        if invert:
            control_val |= self.EPTXCONTROL.EPTXECINVERT.bit_mask
        pre_emphasis_width = (pre_emphasis_width >> 1) & 0x3
        control_val |= (
            pre_emphasis_width << self.EPTXCONTROL.EPTXECPREEMPHASISWIDTH.offset
        )
        self.write_reg(self.EPTXCONTROL, control_val)

        control_val = (
            pre_emphasis_strength << self.EPTXECCHNCNTR.EPTXECPREEMPHASISSTRENGTH.offset
            | pre_emphasis_mode << self.EPTXECCHNCNTR.EPTXECPREEMPHASISMODE.offset
            | drive_strength << self.EPTXECCHNCNTR.EPTXECDRIVESTRENGTH.offset
        )
        self.write_reg(self.EPTXECCHNCNTR, control_val)

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
        config_high, config_low = self._eclk_setup_common(
            clk_id=clk_id,
            freq=freq,
            drive_strength=drive_strength,
            preemphasis_strength=preemphasis_strength,
            preemphasis_mode=preemphasis_mode,
            preemphasis_width=preemphasis_width,
            invert=invert,
        )

        self.write_reg(self.EPCLK0CHNCNTRH.address + 2 * clk_id, config_high)
        self.write_reg(self.EPCLK0CHNCNTRL.address + 2 * clk_id, config_low)
