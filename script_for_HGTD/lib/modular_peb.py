#!/usr/bin/env python
#encoding: utf-8
# Company:  IHEP.CAS
# Engineer:  Jie Zhang
# 2022-06-12 created
import os
import sys
from lib import lpgbt_timing
from lib import lpgbt_lumi
from lib import lpgbt_usb
from lib import serial_comm
import time

###############################################
# MUX64
# Module 0~12
MON_GND     = 0
MON_VDDA    = 1
MON_VDDD    = 2
MON_PROBE0  = 3
MON_PROBE1  = 4

###############################################
# lpGBT

# I2C
I2C_Freq_100KHZ = 0
I2C_Freq_200KHZ = 1
I2C_Freq_400KHZ = 2
I2C_Freq_1MHZ   = 3

# I2C address
I2C_ID_VTRX   = 2
I2C_ADDR_VTRX = 0x50

# ADC
ADC_MUX         = 0
ADC_VTRX_RSSI   = 1
ADC_VTRX_TEMP   = 2
ADC_12V0        = 3
ADC_1V2         = 4
ADC_2V5         = 5
ADC_TEMP0       = 6
ADC_TEMP1       = 7
# ADC_NTC       = 8

ADC_GAIN_X2     = 0
ADC_GAIN_X8     = 1
ADC_GAIN_X16    = 2
ADC_GAIN_X32    = 3

# GPIO
# Low bits
PIN_MUX_S0    = 0b00000001  # out
PIN_MUX_S1    = 0b00000010  # out
PIN_MUX_S2    = 0b00000100  # out
PIN_MUX_S3    = 0b00001000  # out
PIN_MUX_S4    = 0b00010000  # out
PIN_MUX_S5    = 0b00100000  # out
PIN_PEN_0_1   = 0b01000000  # out
PIN_PEN_2_4   = 0b10000000  # out
# High bits
PIN_PEN_5_6   = 0b00000001  # out
PIN_PEN_7_9   = 0b00000010  # out
PIN_PEN_10_13 = 0b00000100  # out
PIN_RST_0_1   = 0b00001000  # out
PIN_RST_2_4   = 0b00010000  # out
PIN_RST_5_6   = 0b00100000  # out
PIN_RST_7_9   = 0b01000000  # out
PIN_RST_10_13 = 0b10000000  # out
# GPIO position
BIT_MUX_S0    = 0
BIT_MUX_S1    = 1
BIT_MUX_S2    = 2
BIT_MUX_S3    = 3
BIT_MUX_S4    = 4
BIT_MUX_S5    = 5
BIT_PEN_0_1   = 6
BIT_PEN_2_4   = 7
BIT_PEN_5_6   = 8
BIT_PEN_7_9   = 9
BIT_PEN_10_13 = 10
BIT_RST_0_1   = 11
BIT_RST_2_4   = 12
BIT_RST_5_6   = 13
BIT_RST_7_9   = 14
BIT_RST_10_13 = 15

# PSCLK
PSFREQ_40MHZ  = 1
PSFREQ_320MHZ = 4

# EPCLK
EPCLK_NONE   = 0
EPCLK_40MHZ  = 1
EPCLK_320MHZ = 4
EPCLK_640MHZ = 5
EPCLK_1280MHZ = 6

clk_freq = EPCLK_40MHZ
# clk_freq = EPCLK_320MHZ
# clk_freq = EPCLK_640MHZ

# EPRX
EPRX_DATA_RATE_DISABLE   = 0
EPRX_DATA_RATE_320MBPS   = 1
EPRX_DATA_RATE_640MBPS   = 2
EPRX_DATA_RATE_1280MBPS  = 3

EPRXMODE_FIXED      = 0
EPRXMODE_INIT       = 1
EPRXMODE_CONT       = 2
EPRXMODE_INIT_CONT  = 3

EPRXEQ_NONE = 0
EPRXEQ_5DB  = 1
EPRXEQ_8DB  = 2
EPRXEQ_11DB = 3

# EPTX
EPTX_NONE    = 0
EPTX_320MBPS = 3

# eport config list:
    # enable,
    # epclk_id,
        # drive_strength, preemphasis_strength, preemphasis_mode, preemphasis_width, invert,
    # eptx_group, eptx_channel,
        # drive_strength, preemphasis_strength, preemphasis_mode, preemphasis_width,
    # eprx_group0, eprx_channel0, eprx_group1, eprx_channel1,
        # eprx_data_rate, eprx_track_mode, eprx_term, eprx_ac_bias, eprx_equalizer

class ep_module(object):
    def __init__(self,
        enable = 0,
        # epclk
        epclk_id = 0,
        epclk_drive_strength = 4,
        epclk_preemphasis_strength = 4,
        epclk_preemphasis_mode = 0,
        epclk_preemphasis_width = 0,
        epclk_invert = False,
        # eptx
        eptx_group = 0,
        eptx_channel = 0,
        eptx_drive_strength = 4,
        eptx_preemphasis_strength = 4,
        eptx_preemphasis_mode = 0,
        eptx_preemphasis_width = 0,
        # eprx
        eprx_group0 = 0,
        eprx_channel0 = 0,
        eprx_group1 = 1,
        eprx_channel1 = 0,
        eprx_data_rate = 320,                       # share in the same group
        eprx_track_mode = EPRXMODE_INIT_CONT,       # share in the same group
        eprx_term = True,
        eprx_ac_bias = True,
        eprx_equalizer = EPRXEQ_NONE
    ):
        self.enable = enable
        self.epclk_id = epclk_id
        self.epclk_drive_strength = epclk_drive_strength
        self.epclk_preemphasis_strength = epclk_preemphasis_strength
        self.epclk_preemphasis_mode = epclk_preemphasis_mode
        self.epclk_preemphasis_width = epclk_preemphasis_width
        self.epclk_invert = epclk_invert
        # eptx
        self.eptx_group = eptx_group
        self.eptx_channel = eptx_channel
        self.eptx_drive_strength = eptx_drive_strength
        self.eptx_preemphasis_strength = eptx_preemphasis_strength
        self.eptx_preemphasis_mode = eptx_preemphasis_mode
        self.eptx_preemphasis_width = eptx_preemphasis_width
        # eprx
        self.eprx_group0 = eprx_group0
        self.eprx_channel0 = eprx_channel0
        self.eprx_group1 = eprx_group1
        self.eprx_channel1 = eprx_channel1
        self.eprx_data_rate = eprx_data_rate
        self.eprx_track_mode = eprx_track_mode
        self.eprx_term = eprx_term
        self.eprx_ac_bias = eprx_ac_bias
        self.eprx_equalizer = eprx_equalizer

class modular_peb(object):
    def __init__(self, card = 0, dev = 0, addr = 0x70, use_usb = False, use_fice = False, use_serialcomm = True):

        if (use_serialcomm):
            self.serialcomm = serial_comm.SerialComm(card = card)
        else:
            self.serialcomm = None

        if use_usb:
            self.timing = lpgbt_usb.lpgbt(usbnr = dev, addr = addr)
        else:
            self.timing = lpgbt_timing.lpgbt(self.serialcomm, dev = dev, addr = addr, use_fice = use_fice)

        self.ep_config = []
        # module 0
        self.ep_config.append(
            ep_module(epclk_id = 0, eptx_group = 0, eptx_channel = 0,
                eprx_group0 = 0, eprx_channel0 = 0, eprx_group1 = 1, eprx_channel1 = 0))
        # module 1
        self.ep_config.append(
            ep_module(epclk_id = 1, eptx_group = 0, eptx_channel = 1,
                eprx_group0 = 0, eprx_channel0 = 1, eprx_group1 = 1, eprx_channel1 = 1))
        # module 2
        self.ep_config.append(
            ep_module(epclk_id = 2, eptx_group = 0, eptx_channel = 2,
                eprx_group0 = 0, eprx_channel0 = 2, eprx_group1 = 1, eprx_channel1 = 2))
        # module 3
        self.ep_config.append(
            ep_module(epclk_id = 3, eptx_group = 0, eptx_channel = 3,
                eprx_group0 = 0, eprx_channel0 = 3, eprx_group1 = 1, eprx_channel1 = 3))
        # module 4
        self.ep_config.append(
            ep_module(epclk_id = 4, eptx_group = 1, eptx_channel = 0,
                eprx_group0 = 2, eprx_channel0 = 0, eprx_group1 = 3, eprx_channel1 = 0))
        # module 5
        self.ep_config.append(
            ep_module(epclk_id = 5, eptx_group = 1, eptx_channel = 1,
                eprx_group0 = 2, eprx_channel0 = 1, eprx_group1 = 3, eprx_channel1 = 1))
        # module 6
        self.ep_config.append(
            ep_module(epclk_id = 6, eptx_group = 1, eptx_channel = 2,
                eprx_group0 = 2, eprx_channel0 = 2, eprx_group1 = 3, eprx_channel1 = 2))
        # module 7
        self.ep_config.append(
            ep_module(epclk_id = 7, eptx_group = 1, eptx_channel = 3,
                eprx_group0 = 2, eprx_channel0 = 3, eprx_group1 = 3, eprx_channel1 = 3))
        # module 8
        self.ep_config.append(
            ep_module(epclk_id = 8, eptx_group = 2, eptx_channel = 0,
                eprx_group0 = 4, eprx_channel0 = 0, eprx_group1 = 5, eprx_channel1 = 0))
        # module 9
        self.ep_config.append(
            ep_module(epclk_id = 9, eptx_group = 2, eptx_channel = 1,
                eprx_group0 = 4, eprx_channel0 = 1, eprx_group1 = 5, eprx_channel1 = 1))
        # module 10
        self.ep_config.append(
            ep_module(epclk_id = 10, eptx_group = 2, eptx_channel = 2,
                eprx_group0 = 4, eprx_channel0 = 2, eprx_group1 = 5, eprx_channel1 = 2))
        # module 11
        self.ep_config.append(
            ep_module(epclk_id = 11, eptx_group = 2, eptx_channel = 3,
                eprx_group0 = 4, eprx_channel0 = 3, eprx_group1 = 5, eprx_channel1 = 3))
        # module 12
        self.ep_config.append(
            ep_module(epclk_id = 12, eptx_group = 3, eptx_channel = 0,
                eprx_group0 = 6, eprx_channel0 = 0, eprx_group1 = 6, eprx_channel1 = 2))
        # module 13
        self.ep_config.append(
            ep_module(epclk_id = 13, eptx_group = 3, eptx_channel = 1,
                eprx_group0 = 6, eprx_channel0 = 1, eprx_group1 = 6, eprx_channel1 = 3))

    def timing_init(self, modulation_current = 115, emphasis_amp = 65):
        # Configure the line driver when the link is unreliable
        self.timing.lpgbt.line_driver_setup(
            modulation_current = modulation_current,
            emphasis_enable = True,
            emphasis_short = False,
            emphasis_amp = emphasis_amp)
        # Indicates completion of PLL/DLL config to PUSM, wait for READY state
        try:
            self.timing.lpgbt.config_done_and_wait_for_ready()
        except Exception as e:
            print(e)
            return False
        # clear all gpio
        self.timing.lpgbt.gpio_set_out(0)
        # drive high current
        # self.timing.lpgbt.gpio_set_drive(PIN_RST_0_1|PIN_RST_2_4|PIN_RST_5_6|PIN_RST_7_9|PIN_RST_10_13|
        #     PIN_PEN_0_1|PIN_PEN_2_4|PIN_PEN_5_6|PIN_PEN_7_9|PIN_PEN_10_13)
        # set as output
        self.timing.lpgbt.gpio_set_dir(0xFFFF)
        # enable the bandgap reference voltage generator
        self.timing.lpgbt.vref_enable()
        # enable EC
        self.timing.lpgbt.eptx_ec_setup(
       		drive_strength=7,
        	pre_emphasis_mode=3,
        	pre_emphasis_strength=7,
        	pre_emphasis_width=3
       	)
        self.timing.lpgbt.eprx_ec_setup(track_mode = 1)
        # enable I2C
        self.timing.lpgbt.i2c_master_config(
            master_id = 0,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )
        self.timing.lpgbt.i2c_master_config(
            master_id = 1,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )
        self.timing.lpgbt.i2c_master_config(
            master_id = 2,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )
        # enable PSCLK
        self.timing.lpgbt.phase_shifter_setup(
            channel_id = 1,
            freq = PSFREQ_40MHZ,
            drive_strength=7,
            preemphasis_strength=7,
            preemphasis_mode=3,
            preemphasis_width=7
        )
        self.timing.lpgbt.phase_shifter_setup(
            channel_id = 2,
            freq = PSFREQ_40MHZ,
            drive_strength=7,
            preemphasis_strength=7,
            preemphasis_mode=3,
            preemphasis_width=7
        )
        return True

    def module_reset(self, module_id):
        if (module_id<0) or (module_id>13):
            print("Input valid module id (0~13)")
            return
        if module_id == 0:
            temp = BIT_RST_0_1
            text = "0, 1"
        if module_id == 1:
            temp = BIT_RST_0_1
            text = "0, 1"
        if module_id == 2:
            temp = BIT_RST_2_4
            text = "2, 3, 4"
        if module_id == 3:
            temp = BIT_RST_2_4
            text = "2, 3, 4"
        if module_id == 4:
            temp = BIT_RST_2_4
            text = "2, 3, 4"
        if module_id == 5:
            temp = BIT_RST_5_6
            text = "5, 6"
        if module_id == 6:
            temp = BIT_RST_5_6
            text = "5, 6"
        if module_id == 7:
            temp = BIT_RST_7_9
            text = "7, 8, 9"
        if module_id == 8:
            temp = BIT_RST_7_9
            text = "7, 8, 9"
        if module_id == 9:
            temp = BIT_RST_7_9
            text = "7, 8, 9"
        if module_id == 10:
            temp = BIT_RST_10_13
            text = "10, 11, 12, 13"
        if module_id == 11:
            temp = BIT_RST_10_13
            text = "10, 11, 12, 13"
        if module_id == 12:
            temp = BIT_RST_10_13
            text = "10, 11, 12, 13"
        if module_id == 13:
            temp = BIT_RST_10_13
            text = "10, 11, 12, 13"
        self.timing.lpgbt.gpio_set_out_bit(temp, 0)
        time.sleep(0.1)
        self.timing.lpgbt.gpio_set_out_bit(temp, 1)
        print("Reset module "+text)

    def module_power(self, module_id, enable):
        if (module_id<0) or (module_id>13):
            print("Input valid module id (0~13)")
            return
        if enable:
            if module_id == 0:
                temp = BIT_PEN_0_1
                text = "0, 1"
            if module_id == 1:
                temp = BIT_PEN_0_1
                text = "0, 1"
            if module_id == 2:
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 3:
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 4:
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 5:
                temp = BIT_PEN_5_6
                text = "5, 6"
            if module_id == 6:
                temp = BIT_PEN_5_6
                text = "5, 6"
            if module_id == 7:
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 8:
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 9:
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 10:
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 11:
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 12:
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 13:
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            self.timing.lpgbt.gpio_set_out_bit(temp, 1)
            print("Power on module "+text)
        else:
            text = ""
            if module_id == 0:
                if self.ep_config[1].enable:
                    return
                temp = BIT_PEN_0_1
                text = "0, 1"
            if module_id == 1:
                if self.ep_config[0].enable:
                    return
                temp = BIT_PEN_0_1
                text = "0, 1"
            if module_id == 2:
                if self.ep_config[3].enable:
                    return
                if self.ep_config[4].enable:
                    return
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 3:
                if self.ep_config[2].enable:
                    return
                if self.ep_config[4].enable:
                    return
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 4:
                if self.ep_config[2].enable:
                    return
                if self.ep_config[3].enable:
                    return
                temp = BIT_PEN_2_4
                text = "2, 3, 4"
            if module_id == 5:
                if self.ep_config[6].enable:
                    return
                temp = BIT_PEN_5_6
                text = "5, 6"
            if module_id == 6:
                if self.ep_config[5].enable:
                    return
                temp = BIT_PEN_5_6
                text = "5, 6"
            if module_id == 7:
                if self.ep_config[8].enable:
                    return
                if self.ep_config[9].enable:
                    return
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 8:
                if self.ep_config[7].enable:
                    return
                if self.ep_config[9].enable:
                    return
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 9:
                if self.ep_config[7].enable:
                    return
                if self.ep_config[8].enable:
                    return
                temp = BIT_PEN_7_9
                text = "7, 8, 9"
            if module_id == 10:
                if self.ep_config[11].enable:
                    return
                if self.ep_config[12].enable:
                    return
                if self.ep_config[13].enable:
                    return
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 11:
                if self.ep_config[10].enable:
                    return
                if self.ep_config[12].enable:
                    return
                if self.ep_config[13].enable:
                    return
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 12:
                if self.ep_config[10].enable:
                    return
                if self.ep_config[11].enable:
                    return
                if self.ep_config[13].enable:
                    return
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            if module_id == 13:
                if self.ep_config[10].enable:
                    return
                if self.ep_config[11].enable:
                    return
                if self.ep_config[12].enable:
                    return
                temp = BIT_PEN_10_13
                text = "10, 11, 12, 13"
            self.timing.lpgbt.gpio_set_out_bit(temp, 0)
            print("Power off module "+text)

    def module_setup(self,
        module_id,
        enable,
        reset = False,
        # epclk
        epclk_drive_strength = 7,
        epclk_preemphasis_strength = 7,
        epclk_preemphasis_mode = 3,
        epclk_preemphasis_width = 7,
        epclk_invert = False,
        # eptx
        eptx_drive_strength = 7,
        eptx_preemphasis_strength = 7,
        eptx_preemphasis_mode = 3,
        eptx_preemphasis_width = 7,
        # eprx
        eprx_data_rate = 320,                       # share in the same group
        eprx_track_mode = EPRXMODE_INIT_CONT,       # share in the same group
        eprx_term = True,
        eprx_ac_bias = True,
        eprx_equalizer = EPRXEQ_NONE
    ):
        if (module_id<0) or (module_id>13):
            print("Input valid module id (0~13)")
            return
        self.ep_config[module_id].enable = enable
        self.ep_config[module_id].epclk_drive_strength = epclk_drive_strength
        self.ep_config[module_id].epclk_preemphasis_strength = epclk_preemphasis_strength
        self.ep_config[module_id].epclk_preemphasis_mode = epclk_preemphasis_mode
        self.ep_config[module_id].epclk_preemphasis_width = epclk_preemphasis_width
        self.ep_config[module_id].epclk_invert = epclk_invert
        self.ep_config[module_id].eptx_drive_strength = eptx_drive_strength
        self.ep_config[module_id].eptx_preemphasis_strength = eptx_preemphasis_strength
        self.ep_config[module_id].eptx_preemphasis_mode = eptx_preemphasis_mode
        self.ep_config[module_id].eptx_preemphasis_width = eptx_preemphasis_width
        self.ep_config[module_id].eprx_data_rate = eprx_data_rate
        self.ep_config[module_id].eprx_track_mode = eprx_track_mode
        self.ep_config[module_id].eprx_term = eprx_term
        self.ep_config[module_id].eprx_ac_bias = eprx_ac_bias
        self.ep_config[module_id].eprx_equalizer = eprx_equalizer
        """
        Module uplink data speed supports
        +-----------+-----------+----------+-----------+
        | Module id | 1280 Mbps | 640Mbps  | 320 Mbps  |
        +===========+===========+==========+===========+
        | Module 0  | Yes       | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 1  | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 2  | No        | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 3  | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 4  | Yes       | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 5  | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 6  | No        | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 7  | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 8  | Yes       | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 9  | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 10 | No        | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 11 | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 12 | No        | Yes      | Yes       |
        +-----------+-----------+----------+-----------+
        | Module 13 | No        | No       | Yes       |
        +-----------+-----------+----------+-----------+
        """
        # check the parameter
        if module_id in [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13]:
            if self.ep_config[module_id].enable and (self.ep_config[module_id].eprx_data_rate == 1280):
                self.ep_config[module_id].enable = 0
                print("Module %d can't run at 1280 Mbps, close this module."%module_id)
        if module_id in [1, 3, 5, 7, 9, 11, 13]:
            if self.ep_config[module_id].enable and (self.ep_config[module_id].eprx_data_rate == 640):
                self.ep_config[module_id].enable = 0
                print("Module %d can't run at 640 Mbps, close this module."%(module_id))

        if self.ep_config[module_id].enable:
            # copy the parameter to the group
            if module_id in [0, 4, 8]:
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+3].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+3].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [1, 5, 9]:
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [2, 6, 10]:
                self.ep_config[module_id-2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [3, 7, 11]:
                self.ep_config[module_id-3].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-3].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id == 12:
                self.ep_config[13].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[13].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id == 13:
                self.ep_config[12].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[12].eprx_track_mode = self.ep_config[module_id].eprx_track_mode

            # config eclk
            if clk_freq == EPCLK_40MHZ:
                text = "40 MHz"
            else:
                text = "320 MHz"
            self.timing.lpgbt.eclk_setup(
                clk_id = self.ep_config[module_id].epclk_id,
                freq = clk_freq,
                drive_strength = self.ep_config[module_id].epclk_drive_strength,
                preemphasis_strength = self.ep_config[module_id].epclk_preemphasis_strength,
                preemphasis_mode = self.ep_config[module_id].epclk_preemphasis_mode,
                preemphasis_width = self.ep_config[module_id].epclk_preemphasis_width,
                invert = self.ep_config[module_id].epclk_invert
            )
            print("  Enable %s eclk for module %d"%(text,module_id))

            # config eptx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            if self.ep_config[module_id].eprx_data_rate == 1280:
                chn0_enable = True
            if self.ep_config[module_id].eprx_data_rate == 640:
                if module_id in [0, 4, 8]:
                    chn0_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn2_enable = True
                if module_id in [2, 6, 10]:
                    chn2_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn0_enable = True
                if module_id == 12:
                    chn0_enable = True
            if self.ep_config[module_id].eprx_data_rate == 320:
                if module_id in [0, 4, 8]:
                    chn0_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn1_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn2_enable = True
                    if self.ep_config[module_id+3].enable:
                        chn3_enable = True
                if module_id in [1, 5, 9]:
                    chn1_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn0_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn2_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn3_enable = True
                if module_id in [2, 6, 10]:
                    chn2_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn0_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn1_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn3_enable = True
                if module_id in [3, 7, 11]:
                    chn3_enable = True
                    if self.ep_config[module_id-3].enable:
                        chn0_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn1_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn2_enable = True
                if module_id == 12:
                    chn0_enable = True
                    if self.ep_config[13].enable:
                        chn1_enable = True
                if module_id == 13:
                    chn1_enable = True
                    if self.ep_config[12].enable:
                        chn0_enable = True
            self.timing.lpgbt.eptx_group_setup(
                group_id = self.ep_config[module_id].eptx_group,
                data_rate = EPTX_320MBPS,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
                mirror = True
            )
            self.timing.lpgbt.eptx_channel_config(
                group_id = self.ep_config[module_id].eptx_group,
                channel_id = self.ep_config[module_id].eptx_channel,
                drive_strength = self.ep_config[module_id].eptx_drive_strength,
                pre_emphasis_mode = self.ep_config[module_id].eptx_preemphasis_mode,
                pre_emphasis_strength = self.ep_config[module_id].eptx_preemphasis_strength,
                pre_emphasis_width = self.ep_config[module_id].eptx_preemphasis_width,
                invert = False
            )
            print("  Enable 320 Mbps eptx for module %d"%module_id)

            # power on
            self.module_power(module_id, 1)

            # reset
            if(reset):
                self.module_reset(module_id)

            # config eprx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            if self.ep_config[module_id].eprx_data_rate == 1280:
                chn0_enable = True
            if self.ep_config[module_id].eprx_data_rate == 640:
                if module_id in [0, 4, 8]:
                    chn0_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn2_enable = True
                if module_id in [2, 6, 10]:
                    chn2_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn0_enable = True
                if module_id == 12:
                    chn0_enable = True
                    chn2_enable = True
            if self.ep_config[module_id].eprx_data_rate == 320:
                if module_id in [0, 4, 8]:
                    chn0_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn1_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn2_enable = True
                    if self.ep_config[module_id+3].enable:
                        chn3_enable = True
                if module_id in [1, 5, 9]:
                    chn1_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn0_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn2_enable = True
                    if self.ep_config[module_id+2].enable:
                        chn3_enable = True
                if module_id in [2, 6, 10]:
                    chn2_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn0_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn1_enable = True
                    if self.ep_config[module_id+1].enable:
                        chn3_enable = True
                if module_id in [3, 7, 11]:
                    chn3_enable = True
                    if self.ep_config[module_id-3].enable:
                        chn0_enable = True
                    if self.ep_config[module_id-2].enable:
                        chn1_enable = True
                    if self.ep_config[module_id-1].enable:
                        chn2_enable = True
                if module_id == 12:
                    chn0_enable = True
                    chn2_enable = True
                    if self.ep_config[13].enable:
                        chn1_enable = True
                        chn3_enable = True
                if module_id == 13:
                    chn1_enable = True
                    chn3_enable = True
                    if self.ep_config[12].enable:
                        chn0_enable = True
                        chn2_enable = True
            if self.ep_config[module_id].eprx_data_rate == 1280:
                data_rate = EPRX_DATA_RATE_1280MBPS
            elif self.ep_config[module_id].eprx_data_rate == 640:
                data_rate = EPRX_DATA_RATE_640MBPS
            else:
                data_rate = EPRX_DATA_RATE_320MBPS
            self.timing.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group0,
                data_rate = data_rate,
                track_mode = self.ep_config[module_id].eprx_track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.timing.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group1,
                data_rate = data_rate,
                track_mode = self.ep_config[module_id].eprx_track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.timing.lpgbt.eprx_channel_config(
                group_id = self.ep_config[module_id].eprx_group0,
                channel_id = self.ep_config[module_id].eprx_channel0,
                term = self.ep_config[module_id].eprx_term,
                ac_bias = self.ep_config[module_id].eprx_ac_bias,
                invert = False,
                phase = 0,
                equalizer = self.ep_config[module_id].eprx_equalizer
            )
            self.timing.lpgbt.eprx_channel_config(
                group_id = self.ep_config[module_id].eprx_group1,
                channel_id = self.ep_config[module_id].eprx_channel1,
                term = self.ep_config[module_id].eprx_term,
                ac_bias = self.ep_config[module_id].eprx_ac_bias,
                invert = False,
                phase = 0,
                equalizer = self.ep_config[module_id].eprx_equalizer
            )
            print("  Enable %d Mbps eprx for module %d"%(self.ep_config[module_id].eprx_data_rate, module_id))

        # disable
        else:
            # dsable eprx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            if module_id in [0, 4, 8]:
                if self.ep_config[module_id+1].enable:
                    if self.ep_config[module_id+1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id+2].enable:
                    if self.ep_config[module_id+2].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+2].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+2].eprx_track_mode
                    chn2_enable = True
                if self.ep_config[module_id+3].enable:
                    if self.ep_config[module_id+3].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+3].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+3].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable and not self.ep_config[module_id+3].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id+2].eprx_data_rate = 320
                    self.ep_config[module_id+3].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+3].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [1, 5, 9]:
                if self.ep_config[module_id-1].enable:
                    if self.ep_config[module_id-1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id+1].enable:
                    if self.ep_config[module_id+1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn2_enable = True
                if self.ep_config[module_id+2].enable:
                    if self.ep_config[module_id+2].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+2].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+2].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id+2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+2].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [2, 6, 10]:
                if self.ep_config[module_id-2].enable:
                    if self.ep_config[module_id-2].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-2].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-2].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id-1].enable:
                    if self.ep_config[module_id-1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id+1].enable:
                    if self.ep_config[module_id+1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id+1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id-2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [3, 7, 11]:
                if self.ep_config[module_id-3].enable:
                    if self.ep_config[module_id-3].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-3].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-3].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id-2].enable:
                    if self.ep_config[module_id-2].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-2].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-2].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id-1].enable:
                    if self.ep_config[module_id-1].eprx_data_rate == 1280:
                        data_rate = EPRX_DATA_RATE_1280MBPS
                    elif self.ep_config[module_id-1].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn2_enable = True
                if not self.ep_config[module_id-3].enable and not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-3].eprx_data_rate = 320
                    self.ep_config[module_id-2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id-3].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id == 12:
                if self.ep_config[13].enable:
                    data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[13].eprx_track_mode
                    chn1_enable = True
                    chn3_enable = True
                else:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id == 13:
                if self.ep_config[12].enable:
                    if self.ep_config[12].eprx_data_rate == 640:
                        data_rate = EPRX_DATA_RATE_640MBPS
                    else:
                        data_rate = EPRX_DATA_RATE_320MBPS
                    track_mode = self.ep_config[12].eprx_track_mode
                    chn0_enable = True
                    chn2_enable = True
                else:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
            self.timing.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group0,
                data_rate = data_rate,
                track_mode = track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.timing.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group1,
                data_rate = data_rate,
                track_mode = track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            print("  Disable eprx for module %d"%module_id)

            # disable eptx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            data_rate = EPTX_320MBPS
            if module_id in [0, 4, 8]:
                if self.ep_config[module_id+1].enable:
                    chn1_enable = True
                if self.ep_config[module_id+2].enable:
                    chn2_enable = True
                if self.ep_config[module_id+3].enable:
                    chn3_enable = True
                if not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable and not self.ep_config[module_id+3].enable:
                    data_rate = EPTX_NONE
            if module_id in [1, 5, 9]:
                if self.ep_config[module_id-1].enable:
                    chn0_enable = True
                if self.ep_config[module_id+1].enable:
                    chn2_enable = True
                if self.ep_config[module_id+2].enable:
                    chn3_enable = True
                if not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable:
                    data_rate = EPTX_NONE
            if module_id in [2, 6, 10]:
                if self.ep_config[module_id-2].enable:
                    chn0_enable = True
                if self.ep_config[module_id-1].enable:
                    chn1_enable = True
                if self.ep_config[module_id+1].enable:
                    chn3_enable = True
                if not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable:
                    data_rate = EPTX_NONE
            if module_id in [3, 7, 11]:
                if self.ep_config[module_id-3].enable:
                    chn0_enable = True
                if self.ep_config[module_id-2].enable:
                    chn1_enable = True
                if self.ep_config[module_id-1].enable:
                    chn2_enable = True
                if not self.ep_config[module_id-3].enable and not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable:
                    data_rate = EPTX_NONE
            if module_id == 12:
                if self.ep_config[13].enable:
                    chn1_enable = True
                else:
                    data_rate = EPTX_NONE
            if module_id == 13:
                if self.ep_config[12].enable:
                    chn0_enable = True
                else:
                    data_rate = EPTX_NONE
            self.timing.lpgbt.eptx_group_setup(
                group_id = self.ep_config[module_id].eptx_group,
                data_rate = data_rate,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
                mirror = True
            )
            print("  Disable eptx for module %d"%module_id)

            # config eclk
            self.timing.lpgbt.eclk_setup(
                clk_id = self.ep_config[module_id].epclk_id,
                freq = EPCLK_NONE
            )
            print("  Disable eclk for module %d"%module_id)

            # power off
            self.module_power(module_id, 0)

    def module_setup_lumi(self,
        module_id,
        enable,
        # eprx
        eprx_data_rate = 640,                       # share in the same group
        eprx_track_mode = EPRXMODE_INIT_CONT,       # share in the same group
        eprx_term = True,
        eprx_ac_bias = True,
        eprx_equalizer = EPRXEQ_NONE
    ):
        # lumi will only config rprx, adn will not participate in power on/off/reset
        if (module_id<0) or (module_id>13):
            print("Input valid module id (0~13)")
            return
        self.ep_config[module_id].enable = enable
        self.ep_config[module_id].eprx_data_rate = eprx_data_rate
        self.ep_config[module_id].eprx_track_mode = eprx_track_mode
        self.ep_config[module_id].eprx_term = eprx_term
        self.ep_config[module_id].eprx_ac_bias = eprx_ac_bias
        self.ep_config[module_id].eprx_equalizer = eprx_equalizer
        """
        Module uplink data speed supports
        Lumi speed is fixed at 640 Mbps at present
        +-----------+-----------+
        | Module id | 640Mbps   |
        +===========+===========+
        | Module 0  | Yes       |
        +-----------+-----------+
        | Module 1  | No        |
        +-----------+-----------+
        | Module 2  | Yes       |
        +-----------+---- ------+
        | Module 3  | No        |
        +-----------+---- ------+
        | Module 4  | Yes       |
        +-----------+---- ------+
        | Module 5  | No        |
        +-----------+---- ------+
        | Module 6  | Yes       |
        +-----------+---- ------+
        | Module 7  | No        |
        +-----------+---- ------+
        | Module 8  | Yes       |
        +-----------+---- ------+
        | Module 9  | No        |
        +-----------+---- ------+
        | Module 10 | Yes       |
        +-----------+---- ------+
        | Module 11 | No        |
        +-----------+---- ------+
        | Module 12 | Yes       |
        +-----------+---- ------+
        | Module 13 | No        |
        +-----------+-----------+
        """
        # check the parameter
        if module_id in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
            if self.ep_config[module_id].enable and (self.ep_config[module_id].eprx_data_rate == 1280):
                self.ep_config[module_id].enable = 0
                print("Module %d can't run at 1280 Mbps for lumi data, close this module."%module_id)
            if self.ep_config[module_id].enable and (self.ep_config[module_id].eprx_data_rate == 320):
                self.ep_config[module_id].enable = 0
                print("Module %d can't run at 320 Mbps for lumi data, close this module."%(module_id))
        if module_id in [1, 3, 5, 7, 9, 11, 13]:
            if self.ep_config[module_id].enable and (self.ep_config[module_id].eprx_data_rate == 640):
                self.ep_config[module_id].enable = 0
                print("Module %d can't run at 640 Mbps for lumi data, close this module."%(module_id))

        if self.ep_config[module_id].enable:
            # copy the parameter to the group
            if module_id in [0, 4, 8]:
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+3].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+3].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [1, 5, 9]:
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [2, 6, 10]:
                self.ep_config[module_id-2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id+1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id+1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id in [3, 7, 11]:
                self.ep_config[module_id-3].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-2].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-1].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[module_id-3].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-2].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
                self.ep_config[module_id-1].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id == 12:
                self.ep_config[13].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[13].eprx_track_mode = self.ep_config[module_id].eprx_track_mode
            if module_id == 13:
                self.ep_config[12].eprx_data_rate  = self.ep_config[module_id].eprx_data_rate
                self.ep_config[12].eprx_track_mode = self.ep_config[module_id].eprx_track_mode

            # config eprx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            if module_id in [0, 4, 8]:
                chn0_enable = True
                if self.ep_config[module_id+2].enable:
                    chn2_enable = True
            if module_id in [2, 6, 10]:
                chn2_enable = True
                if self.ep_config[module_id-2].enable:
                    chn0_enable = True
            if module_id == 12:
                chn0_enable = True
                chn2_enable = True
            self.lumi.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group0,
                data_rate = EPRX_DATA_RATE_640MBPS,
                track_mode = self.ep_config[module_id].eprx_track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.lumi.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group1,
                data_rate = EPRX_DATA_RATE_640MBPS,
                track_mode = self.ep_config[module_id].eprx_track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.lumi.lpgbt.eprx_channel_config(
                group_id = self.ep_config[module_id].eprx_group0,
                channel_id = self.ep_config[module_id].eprx_channel0,
                term = self.ep_config[module_id].eprx_term,
                ac_bias = self.ep_config[module_id].eprx_ac_bias,
                invert = False,
                phase = 0,
                equalizer = self.ep_config[module_id].eprx_equalizer
            )
            self.lumi.lpgbt.eprx_channel_config(
                group_id = self.ep_config[module_id].eprx_group1,
                channel_id = self.ep_config[module_id].eprx_channel1,
                term = self.ep_config[module_id].eprx_term,
                ac_bias = self.ep_config[module_id].eprx_ac_bias,
                invert = False,
                phase = 0,
                equalizer = self.ep_config[module_id].eprx_equalizer
            )
            print("  Enable %d Mbps eprx for module %d"%(self.ep_config[module_id].eprx_data_rate, module_id))

        # disable
        else:
            # dsable eprx
            chn0_enable = False
            chn1_enable = False
            chn2_enable = False
            chn3_enable = False
            if module_id in [0, 4, 8]:
                if self.ep_config[module_id+1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id+2].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+2].eprx_track_mode
                    chn2_enable = True
                if self.ep_config[module_id+3].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+3].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable and not self.ep_config[module_id+3].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id+2].eprx_data_rate = 320
                    self.ep_config[module_id+3].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+3].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [1, 5, 9]:
                if self.ep_config[module_id-1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id+1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn2_enable = True
                if self.ep_config[module_id+2].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+2].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable and not self.ep_config[module_id+2].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id+2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+2].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [2, 6, 10]:
                if self.ep_config[module_id-2].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-2].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id-1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id+1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id+1].eprx_track_mode
                    chn3_enable = True
                if not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable and not self.ep_config[module_id+1].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id+1].eprx_data_rate = 320
                    self.ep_config[module_id-2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id+1].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id in [3, 7, 11]:
                if self.ep_config[module_id-3].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-3].eprx_track_mode
                    chn0_enable = True
                if self.ep_config[module_id-2].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-2].eprx_track_mode
                    chn1_enable = True
                if self.ep_config[module_id-1].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[module_id-1].eprx_track_mode
                    chn2_enable = True
                if not self.ep_config[module_id-3].enable and not self.ep_config[module_id-2].enable and not self.ep_config[module_id-1].enable:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-3].eprx_data_rate = 320
                    self.ep_config[module_id-2].eprx_data_rate = 320
                    self.ep_config[module_id-1].eprx_data_rate = 320
                    self.ep_config[module_id].eprx_data_rate = 320
                    self.ep_config[module_id-3].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-2].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id-1].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[module_id].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id == 12:
                data_rate = EPRX_DATA_RATE_DISABLE
                track_mode = EPRXMODE_INIT_CONT
                self.ep_config[12].eprx_data_rate = 320
                self.ep_config[12].eprx_data_rate = 320
                self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
                self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
            if module_id == 13:
                if self.ep_config[12].enable:
                    data_rate = EPRX_DATA_RATE_640MBPS
                    track_mode = self.ep_config[12].eprx_track_mode
                    chn0_enable = True
                    chn2_enable = True
                else:
                    data_rate = EPRX_DATA_RATE_DISABLE
                    track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[12].eprx_data_rate = 320
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
                    self.ep_config[13].eprx_track_mode = EPRXMODE_INIT_CONT
            self.lumi.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group0,
                data_rate = data_rate,
                track_mode = track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            self.lumi.lpgbt.eprx_group_setup(
                group_id = self.ep_config[module_id].eprx_group1,
                data_rate = data_rate,
                track_mode = track_mode,
                chn0_enable = chn0_enable,
                chn1_enable = chn1_enable,
                chn2_enable = chn2_enable,
                chn3_enable = chn3_enable,
            )
            print("  Disable eprx for module %d"%module_id)

    def mux_select(self, module_id = 0, channel = 0):
        if (module_id<0) or (module_id>12):
            print("Input a valid module id (0~12)")
            return
        if (channel<0) or (channel>4):
            print("Input a valid channel id (0~4)")
            return
        mux_channel = module_id * 5 + channel
        if mux_channel > 63:
            print("No connection for channel 4 for module 12")
        gpio = self.timing.lpgbt.gpio_get_out()
        # clear MUX control bits
        gpio &= ~(PIN_MUX_S0|PIN_MUX_S1|PIN_MUX_S2|PIN_MUX_S3|PIN_MUX_S4|PIN_MUX_S5)
        # set MUX control bits
        gpio |= mux_channel
        # print("%x"%gpio)
        self.timing.lpgbt.gpio_set_out(gpio)

    def adc_select(self, channel = 0):
        if channel in range(16):
            self.timing.lpgbt.adc_config(inp=channel, inn=9, gain=ADC_GAIN_X32)

    def module_i2c_write(self, module_id, chip_id, reg_address, data):
        print ("module_id = ", module_id)
        print ("reg_address = ", reg_address)
        print ("data = ", data)
        # lpGBT I2C master selection
        if module_id in range(0, 5):
            master_id = 2
        elif module_id in range(5, 10):
            master_id = 1
        else:
            master_id = 0
        # I2C device address set
        if module_id in (0,5,10):
            peb_address = 0x1
        elif module_id in (1,6,11):
            peb_address = 0x2
        elif module_id in (2,7,12):
            peb_address = 0x3
        elif module_id in (3,8,13):
            peb_address = 0x4
        elif module_id in (4,9):
            peb_address = 0x5
        MSB3 = 0
        slave_address = (MSB3 << 4) | (peb_address << 1) | (chip_id & 1)
        # Internal address: MSB first, swap byte order
        # reg_address = ((reg_address << 8) & 0xFF00) | ((reg_address >> 8) & 0xFF)

        try:
            data_list = list(data)
        except TypeError:
            data_list = list((data,))

        # Maximum write length = 2(reg_address_width) + 14(data_width)
        data_list = [data_list[i:i+14] for i in range(0, len(data_list), 14)]

        i = 0
        for temp in data_list:
            self.timing.lpgbt.i2c_master_write(
                master_id = master_id,
                slave_address = slave_address,
                reg_address_width = 2,
                reg_address = (((reg_address+i) << 8) & 0xFF00) | (((reg_address+i) >> 8) & 0xFF),
                data = temp
            )
            i += 14

    def module_i2c_read(self, module_id, chip_id, reg_address, read_len):
        # lpGBT I2C master selection
        if module_id in range(0, 5):
            master_id = 2
        elif module_id in range(5, 10):
            master_id = 1
        else:
            master_id = 0
        # print (master_id)
        # I2C device address set
        if module_id in (0,5,10):
            peb_address = 0x1
        elif module_id in (1,6,11):
            peb_address = 0x2
        elif module_id in (2,7,12):
            peb_address = 0x3
        elif module_id in (3,8,13):
            peb_address = 0x4
        elif module_id in (4,9):
            peb_address = 0x5
        MSB3 = 0
        slave_address = (MSB3 << 4) | (peb_address << 1) | (chip_id & 1)
        # Internal address: MSB first, swap byte order
        # reg_address = ((reg_address << 8) & 0xFF00) | ((reg_address >> 8) & 0xFF)

        temp = []
        for i in range(int(read_len/16)+1):
            if i == int(read_len/16):
                len = read_len%16
            else:
                len = 16
            temp += self.timing.lpgbt.i2c_master_read(
                master_id = master_id,
                slave_address = slave_address,
                read_len = len,
                reg_address_width = 2,
                reg_address = (((reg_address +16*i) << 8) & 0xFF00) | (((reg_address +16*i) >> 8) & 0xFF)
            )
        return temp

    def vtrxp_lumi_enable(self):
        if self.vtrx_version == '1.3':
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0,
                data = 0x3
            )
            print("Enable VTRx+ channel for lumi.")
        else:
            print("Lumi channel is enabled by default by VTRx+.")


    def vtrxp_timing_line_driver_setup(
        self,
        bias_current = 0x30,
        modulation_current = 0x20,
        modulation_enable = True,
        emphasis_amp = 0,
        emphasis_rising_edge_enable = True,
        emphasis_falling_edge_enable = True
    ):
        # delay = 0.1
        assert bias_current in range(128), "Invalid bias current value"
        assert modulation_current in range(128), "Invalid modulation current value"
        assert emphasis_amp in range(8), "Invalid emphasis amplitude value"
        bias_current &=  0x7F
        modulation_current &= 0x7F
        emphasis_amp &= 0x07       
        vtrx_version = self.timing.lpgbt.i2c_master_read(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x15,
                read_len = 1
            )[0]        
        if(vtrx_version == 0x15): #10101
            self.vtrx_version = '1.3'
        else:
            self.vtrx_version = '1.2'
        print("Checked VTRx+ version: "+ self.vtrx_version)

        if self.vtrx_version == '1.3':
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x3,
                data = bias_current)
            # time.sleep(delay)
            if modulation_enable:
                modulation_current |= 0x80
                self.timing.lpgbt.i2c_master_write(
                    master_id = I2C_ID_VTRX,
                    slave_address = I2C_ADDR_VTRX,
                    reg_address_width = 1,
                    reg_address = 0x4,
                    data = modulation_current)
                # time.sleep(delay)
            if (emphasis_rising_edge_enable | emphasis_falling_edge_enable):
                emphasis_amp |= (emphasis_rising_edge_enable << 3 | emphasis_falling_edge_enable << 4)
                self.timing.lpgbt.i2c_master_write(
                    master_id = I2C_ID_VTRX,
                    slave_address = I2C_ADDR_VTRX,
                    reg_address_width = 1,
                    reg_address = 0x5,
                    data = emphasis_amp)
                # time.sleep(delay)

        else: # VTRx+ V1.2
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x5,
                data = bias_current)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x6,
                data = modulation_current)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x7,
                data = emphasis_amp)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x4,
                data = emphasis_rising_edge_enable << 4 | emphasis_falling_edge_enable << 5 | modulation_enable << 3 | 0x7)
            # time.sleep(delay)

    def vtrxp_lumi_line_driver_setup(
        self,
        bias_current = 0x30,
        modulation_current = 0x20,
        modulation_enable = True,
        emphasis_amp = 0,
        emphasis_rising_edge_enable = True,
        emphasis_falling_edge_enable = True
    ):
        # delay = 0.1
        assert bias_current in range(128), "Invalid bias current value"
        assert modulation_current in range(128), "Invalid modulation current value"
        assert emphasis_amp in range(8), "Invalid emphasis amplitude value"
        bias_current &=  0x7F
        modulation_current &= 0x7F
        emphasis_amp &= 0x07

        vtrx_version = self.timing.lpgbt.i2c_master_read(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x15,
                read_len = 1
            )[0]
        if(vtrx_version == 0x15): #10101
            self.vtrx_version = '1.3'
        else:
            self.vtrx_version = '1.2'
        # print("Checked VTRx+ version: "+ self.vtrx_version)

        if self.vtrx_version == '1.3':
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x6,
                data = bias_current)
            # time.sleep(delay)
            if modulation_enable:
                modulation_current |= 0x80
                self.timing.lpgbt.i2c_master_write(
                    master_id = I2C_ID_VTRX,
                    slave_address = I2C_ADDR_VTRX,
                    reg_address_width = 1,
                    reg_address = 0x7,
                    data = modulation_current)
                # time.sleep(delay)
            if (emphasis_rising_edge_enable | emphasis_falling_edge_enable):
                emphasis_amp |= (emphasis_rising_edge_enable << 3 | emphasis_falling_edge_enable << 4)
                self.timing.lpgbt.i2c_master_write(
                    master_id = I2C_ID_VTRX,
                    slave_address = I2C_ADDR_VTRX,
                    reg_address_width = 1,
                    reg_address = 0x8,
                    data = emphasis_amp)
                # time.sleep(delay)

        else: # VTRx+ V1.2
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x9,
                data = bias_current)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0xA,
                data = modulation_current)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0xB,
                data = emphasis_amp)
            # time.sleep(delay)
            self.timing.lpgbt.i2c_master_write(
                master_id = I2C_ID_VTRX,
                slave_address = I2C_ADDR_VTRX,
                reg_address_width = 1,
                reg_address = 0x8,
                data = emphasis_rising_edge_enable << 4 | emphasis_falling_edge_enable << 5 | modulation_enable << 3 | 0x7)
            # time.sleep(delay)

    def lumi_add(self, dev = 0, addr = 0x71, use_usb = False, use_fice = False):
        if use_usb:
            self.lumi = lpgbt_usb.lpgbt(dev = dev, addr = addr)
        else:
            self.lumi = lpgbt_lumi.lpgbt(self.serialcomm, dev = dev, addr = addr, use_fice = use_fice)

    def lumi_init(self, modulation_current = 115, emphasis_amp = 65):
        # Configure the line driver when the link is unreliable
        self.lumi.lpgbt.line_driver_setup(
            modulation_current = modulation_current,
            emphasis_enable = True,
            emphasis_short = False,
            emphasis_amp = emphasis_amp)

        # Indicates completion of PLL/DLL config to PUSM, wait for READY state
        try:
            self.lumi.lpgbt.config_done_and_wait_for_ready()
        except Exception as e:
            print(e)
            return False
        # clear all gpio
        self.lumi.lpgbt.gpio_set_out(0)
        # drive high current
        # self.lumi.lpgbt.gpio_set_drive(PIN_RST_0_1|PIN_RST_2_4|PIN_RST_5_6|PIN_RST_7_9|PIN_RST_10_13|
        #     PIN_PEN_0_1|PIN_PEN_2_4|PIN_PEN_5_6|PIN_PEN_7_9|PIN_PEN_10_13)
        # set as input for PG
        self.lumi.lpgbt.gpio_set_dir(0x0)
        # enable the bandgap reference voltage generator
        self.lumi.lpgbt.vref_enable()
        # enable EC
        # self.lumi.lpgbt.eptx_ec_setup()
        # self.lumi.lpgbt.eprx_ec_setup(track_mode = 1)
        # enable PSCLK1
        self.lumi.lpgbt.phase_shifter_setup(channel_id = 1, freq = PSFREQ_40MHZ)
        # enable I2C
        self.lumi.lpgbt.i2c_master_config(
            master_id = 0,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )
        self.lumi.lpgbt.i2c_master_config(
            master_id = 1,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )
        self.lumi.lpgbt.i2c_master_config(
            master_id = 2,
            clk_freq=0,
            scl_drive=False,
            scl_pullup=True,
            scl_drive_strength=1,
            sda_pullup=True,
            sda_drive_strength=1
        )

        return True
