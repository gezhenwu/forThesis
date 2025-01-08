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
"""lpGBT related constants"""
# pylint: disable=missing-function-docstring

from enum import IntEnum, unique


class LpgbtEnums:
    """Class containing any lpGBT-related constants"""

    # pylint: disable=too-many-lines,too-few-public-methods

    EPRX_GROUPS = 7
    EPTX_GROUPS = 4
    EPCLKS = 29

    CLKG_CAPBANKS = 56

    # magic number required to disable triplicated clock tree
    CLK_DISABLE_MAGIC = 0x15

    @unique
    class PusmState(IntEnum):
        """PowerUp State Machine States"""

        RESET0 = 0
        RESET1 = 1
        WAIT_VDD_STABLE = 2
        WAIT_VDD_HIGHER_THAN_0V90 = 3
        FUSE_SAMPLING = 4
        UPDATE = 5
        PAUSE_FOR_PLL_CONFIG_DONE = 6
        WAIT_POWER_GOOD = 7
        RESETOUT = 8
        I2C_TRANS = 9
        RESET_PLL = 10
        WAIT_PLL_LOCK = 11
        INIT_SCRAM = 12
        PAUSE_FOR_DLL_CONFIG_DONE = 13
        RESET_DLLS = 14
        WAIT_DLL_LOCK = 15
        RESET_LOGIC_USING_DLL = 16
        WAIT_CHNS_LOCKED = 17
        READY = 18

    @unique
    class PowerGoodDelay(IntEnum):
        """PUSM : power good delays"""

        DELAY_OFF = 0
        DELAY_1US = 1
        DELAY_5US = 2
        DELAY_10US = 3
        DELAY_50US = 4
        DELAY_100US = 5
        DELAY_500US = 6
        DELAY_1MS = 7
        DELAY_5MS = 8
        DELAY_10MS = 9
        DELAY_20MS = 10
        DELAY_50MS = 11
        DELAY_100MS = 12
        DELAY_200MS = 13
        DELAY_500MS = 14
        DELAY_1S = 15

    @unique
    class Timeout(IntEnum):
        """PUSM : timeout values"""

        TIMEOUT_DISABLED = 15
        TIMEOUT_10US = 14
        TIMEOUT_20US = 13
        TIMEOUT_50US = 12
        TIMEOUT_100US = 11
        TIMEOUT_200US = 10
        TIMEOUT_500US = 9
        TIMEOUT_1MS = 8
        TIMEOUT_2MS = 7
        TIMEOUT_5MS = 6
        TIMEOUT_10MS = 5
        TIMEOUT_20MS = 4
        TIMEOUT_50MS = 3
        TIMEOUT_100MS = 2
        TIMEOUT_500MS = 1
        TIMEOUT_1S = 0

    # PUSM : state override magic number
    FORCESTATE_MAGIC_NUMBER = 0xA3

    @unique
    class VddLevel(IntEnum):
        """PUSM : power sensing levels"""

        VDD_LEVEL_0V70 = 0
        VDD_LEVEL_0V75 = 1
        VDD_LEVEL_0V80 = 2
        VDD_LEVEL_0V85 = 3
        VDD_LEVEL_0V90 = 4
        VDD_LEVEL_0V95 = 5
        VDD_LEVEL_1V00 = 6
        VDD_LEVEL_1V05 = 7

    @unique
    class EclockFrequency(IntEnum):
        """eClock frequencies"""

        DISABLE = 0
        CLK40M = 1
        CLK80M = 2
        CLK160M = 3
        CLK320M = 4
        CLK640M = 5
        CLK1G28 = 6
        LOOPBACK = 7

    @unique
    class PhaseShiterClockFrequency(IntEnum):
        """eClock frequencies"""

        DISABLE = 0
        CLK40M = 1
        CLK80M = 2
        CLK160M = 3
        CLK320M = 4
        CLK640M = 5
        CLK1G28 = 6
        RESERVED = 7

    @unique
    class EtxPreEmpahasisMode(IntEnum):
        """eTx PreEmphasis Mode settings"""

        DISABLE = 0
        RESERVED = 1
        SELFTIMED = 2
        CLKTIMED = 3

    @unique
    class EtxPreEmpahasisWidth(IntEnum):
        """eTx PreEmphasis pulse width setting"""

        PREEMP_120PS = 0
        PREEMP_240PS = 1
        PREEMP_360PS = 2
        PREEMP_480PS = 3
        PREEMP_600PS = 4
        PREEMP_720PS = 5
        PREEMP_840PS = 6
        PREEMP_960PS = 7

    @unique
    class EtxCurrent(IntEnum):
        """eTx current setting"""

        AMP_0MA = 0
        AMP_1MA = 1
        AMP_1MA5 = 2
        AMP_2MA = 3
        AMP_2MA5 = 4
        AMP_3MA = 5
        AMP_3MA5 = 6
        AMP_4MA = 7

    @unique
    class TxDataRate(IntEnum):
        """lpGBT hight speed serializer data rate"""

        TXDATARATE_5G = 0
        TXDATARATE_10G = 1

    @unique
    class PhaseShifterChannel(IntEnum):
        """Phase Shifter Channel"""

        CHN0 = 0
        CHN1 = 1
        CHN2 = 2
        CHN3 = 3

    @unique
    class DownLinkDataSource(IntEnum):
        """Down link data source"""

        LINK_DATA = 0
        PRBS7 = 1
        BIN_CNTR_UP = 2
        CONST_PATTERN = 3

    @unique
    class UpLinkDataSource(IntEnum):
        """Up link data source"""

        LINK_DATA = 0
        PRBS7 = 1
        BIN_CNTR_UP = 2
        BIN_CNTR_DOWN = 3
        CONST_PATTERN = 4
        CONST_PATTERN_INV = 5
        LOOPBACK = 6

    @unique
    class BertCourseSource(IntEnum):
        """4 MSB bits of dataSource signal (dataSourceGroup)"""

        DISABLED = 0x0
        ULDG0 = 0x1
        ULDG1 = 0x2
        ULDG2 = 0x3
        ULDG3 = 0x4
        ULDG4 = 0x5
        ULDG5 = 0x6
        ULDG6 = 0x7
        ULEC = 0x8
        DLDG0 = 0x9
        DLDG1 = 0xA
        DLDG2 = 0xB
        DLDG3 = 0xC
        DLEC = 0xD
        DLFRAME = 0xE

    @unique
    class BertUpLinkSource(IntEnum):
        """4 LSB bits of dataSource signal (dataSourceGroup)"""

        UL_X4_CHN0 = 0x0
        UL_X4_CHN1 = 0x1
        UL_X4_CHN2 = 0x2
        UL_X4_CHN3 = 0x3
        UL_X2_CHN0 = 0x4
        UL_X2_CHN2 = 0x5
        UL_X1_CHN0 = 0x6
        UL_FIXED = 0x7

    @unique
    class BertDownLinkSource(IntEnum):
        """4 LSB bits of dataSource signal (dataSourceGroup)"""

        DL_X4_CHN0 = 0x0
        DL_X4_CHN1 = 0x1
        DL_X4_CHN2 = 0x2
        DL_X4_CHN3 = 0x3
        DL_X2_CHN0 = 0x4
        DL_X2_CHN2 = 0x5
        DL_X1_CHN0 = 0x6
        DL_FIXED = 0x7

    @unique
    class BertOtherSource(IntEnum):
        """4 LSB bits of dataSource signal (dataSourceGroup)"""

        DLDATA_PRBS = 0x0  # 32 bit
        DLDATA_FIXED = 0x1  # 32 bit
        DLFRAME_PRBS7 = 0x2
        DLFRAME_PRBS15 = 0x3
        DLFRAME_PRBS23 = 0x4
        DLFRAME_PRBS31 = 0x5
        DLFRAME_FIXED = 0x7

    @unique
    class BertMeasurementTime(IntEnum):
        """BERT: Measurement Time (in kilo clock cycles)"""

        MT_2E5 = 0  # 3.200e+01 (8.0e-07s) BER : (1.6e-02 - 4.9e-04)
        MT_2E7 = 1  # 1.280e+02 (3.2E-06s) BER : (3.9e-03 - 1.2E-04)
        MT_2E9 = 2  # 5.120e+02 (1.3e-05s) BER : (9.8e-04 - 3.1e-05)
        MT_2E11 = 3  # 2.048e+03 (5.1e-05s) BER : (2.4e-04 - 7.6e-06)
        MT_2E13 = 4  # 8.192E+03 (2.0e-04s) BER : (6.1e-05 - 1.9e-06)
        MT_2E15 = 5  # 3.277e+04 (8.2E-04s) BER : (1.5e-05 - 4.8e-07)
        MT_2E17 = 6  # 1.311e+05 (3.3e-03s) BER : (3.8e-06 - 1.2E-07)
        MT_2E19 = 7  # 5.243e+05 (1.3e-02s) BER : (9.5e-07 - 3.0e-08)
        MT_2E21 = 8  # 2.097e+06 (5.2E-02s) BER : (2.4e-07 - 7.5e-09)
        MT_2E23 = 9  # 8.389e+06 (2.1e-01s) BER : (6.0e-08 - 1.9e-09)
        MT_2E25 = 10  # 3.355e+07 (8.4e-01s) BER : (1.5e-08 - 4.7e-10)
        MT_2E27 = 11  # 1.342E+08 (3.4e+00s) BER : (3.7e-09 - 1.2E-10)
        MT_2E29 = 12  # 5.369e+08 (1.3e+01s) BER : (9.3e-10 - 2.9e-11)
        MT_2E31 = 13  # 2.147e+09 (5.4e+01s) BER : (2.3e-10 - 7.3e-12)
        MT_2E33 = 14  # 8.590e+09 (2.1e+02s) BER : (5.8e-11 - 1.8e-12)
        MT_2E35 = 15  # 3.436e+10 (8.6e+02s) BER : (1.5e-11 - 4.5e-13)

    class EportRxDataRate(IntEnum):
        """EportRx Data Rate"""

        # ePortRx : data rates (5.12G mode, txDataRate=1'b0)
        IDLE = 0
        LS_X4 = 1
        LS_X8 = 2
        LS_X16 = 3

        # ePortRx : data rates (10.24G mode, txDataRate=1'b1)
        HS_IDLE = 0
        HS_X8 = 1
        HS_X16 = 2
        HS_X32 = 3

    @unique
    class EportRxPhaseSelectionMode(IntEnum):
        """ePortRx : phase selection mode"""

        FIXED = 0
        AUTOSTARTUP = 1
        CONTINOUSTRACKING = 2
        CONTINOUSTRACKINGINITIALPHASE = 3

    @staticmethod
    def eport_rx_data_rate_to_str(
        tx_data_rate, eprx_data_rate
    ):
        """Helper function to decode tx_data_rate and eprx_data_rate to string"""
        helper_tab = [["-", "160", "320", "640"], ["-", "320", "640", "1280"]]
        return helper_tab[tx_data_rate][eprx_data_rate]

    @unique
    class EportRxDllStatus(IntEnum):
        """EportRx DLL Status register values"""

        RESET = 0
        FORCE_DOWN = 1
        FREE_RUNNING = 2
        CONFIRM_EARLY = 3

    @unique
    class EportTxDataRate(IntEnum):
        """ePortTx : data rates"""

        IDLE = 0
        X2 = 1
        X4 = 2
        X8 = 3

    @staticmethod
    def eport_tx_data_rate_to_mbps(data_rate):
        """Helper function to decode tx_data_rate and eprx_data_rate to string"""
        helper_tab = ["-", "80", "160", "320"]
        return helper_tab[data_rate]

    @unique
    class AdcGainSelect(IntEnum):
        """ADC Gain Select"""

        X2 = 0
        X8 = 1
        X16 = 2
        X32 = 3

    # Voltage DAC
    VDAC_MAX = 4096
    CDAC_MAX = 256
    ADC_MAX = 1024
    VREF_NOMINAL = 1.0
    ADC_MAX = 1024

    # process monitor
    PROCESS_MONITOR_CHANNELS = 4

    @unique
    class TestOutSelect(IntEnum):
        """Test output select"""

        ZERO = 0
        ONE = 1

    @unique
    class I2cmCommand(IntEnum):
        """I2C Master commands"""

        WRITE_CRA = 0x0
        WRITE_MSK = 0x1
        ONE_BYTE_WRITE = 0x2
        ONE_BYTE_READ = 0x3
        ONE_BYTE_WRITE_EXT = 0x4
        ONE_BYTE_READ_EXT = 0x5
        ONE_BYTE_RMW_OR = 0x6
        ONE_BYTE_RMW_XOR = 0x7
        W_MULTI_4BYTE0 = 0x8
        W_MULTI_4BYTE1 = 0x9
        W_MULTI_4BYTE2 = 0xA
        W_MULTI_4BYTE3 = 0xB
        WRITE_MULTI = 0xC
        READ_MULTI = 0xD
        WRITE_MULTI_EXT = 0xE
        READ_MULTI_EXT = 0xF

    @unique
    class I2cmFrequency(IntEnum):
        """I2C Masters: Control Register"""

        FREQ_100K = 0
        FREQ_200K = 1
        FREQ_400K = 2
        FREQ_1M = 3

    class I2cmConfigReg:
        "Structure of I2C Master Config register"

        class FREQ:
            """Frequency"""

            offset = 0
            length = 2
            bit_mask = 3

            @staticmethod
            def validate(value):
                return value in range(4)

        class NBYTES:
            """Number of bytes"""

            offset = 2
            length = 5
            bit_mask = 0x7C

            @staticmethod
            def validate(value):
                return value in range(32)

        class SCLDRIVE:
            """Drive SCL"""

            offset = 7
            length = 1
            bit_mask = 0x80

            @staticmethod
            def validate(value):
                return value in range(2)

    class I2cmStatusReg:
        "Structure of I2C Master Status register"

        class SUCC:
            """set when the last I2C transaction was executed successfully.
            Reset by the start of the next I2C transaction."""

            bit_mask = 0x04

        class LEVEERR:
            """set if the I2C master port finds that the SDA line is pulled
            low ‘0’ before initiating a transaction. Indicates a problem with
            the I2C bus. Represents the status of the SDA line and cannot be reset."""

            bit_mask = 0x08

        class NOACK:
            """set if the last transaction was not acknowledged by the I2C slave.
            Value is valid at the end of the I2C transaction. Reset if
            a slave acknowledges the next I2C transaction."""

            bit_mask = 0x40

    # Fuses
    FUSE_MAGIC_NUMBER = 0xA3

    @unique
    class UplinkSerializerPattern(IntEnum):
        """Uplink Serializer Pattern"""

        DATA = 0  # Normal mode of operation
        PRBS7 = 1  # PRBS7 test pattern (x7 + x6 + 1)
        PRBS15 = 2  # PRBS15 test pattern (x15 + x14 + 1)
        PRBS23 = 3  # PRBS23 test pattern (x23 + x18 + 1)
        PRBS31 = 4  # PRBS31 test pattern (x31 + x28 + 1)
        CLK5G12 = (
            5  # 5.12 GHz clock pattern (in 5Gbps mode it will produce only 2.56 GHz)
        )
        CLK2G56 = 6  # 2.56 GHz clock pattern
        CLK1G28 = 7  # 1.28 GHz clock pattern
        CLK40M = 8  # 40 MHz clock pattern
        DLFRAME_10G24 = 9  # Loopback, downlink frame repeated 4 times
        DLFRAME_5G12 = (
            10  # Loopback, downlink frame repeated 2 times, each bit repeated 2 times
        )
        DLFRAME_2G56 = (
            11  # Loopback, downlink frame repeated 1 times, each bit repeated 4 times
        )
        CONST_PATTERN = 12  # 8 x DPDataPattern[31:0]
