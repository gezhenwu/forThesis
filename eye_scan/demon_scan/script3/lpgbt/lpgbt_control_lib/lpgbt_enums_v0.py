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

from enum import IntEnum, unique
from .lpgbt_enums import LpgbtEnums


class LpgbtEnumsV0(LpgbtEnums):
    """Class containing any lpGBTv0-related constants"""

    # pylint: disable=too-many-lines,too-few-public-methods

    READ_WRITE_FUSE_REGS = 0x0F0
    READ_WRITE_REGS = 0x140
    READ_ONLY_REGS = 0x8F
    NUM_REGS = 0x1CF

    READ_WRITE_FUSE_REG_OFFSET = 0x0
    READ_WRITE_REG_OFFSET = 0x0
    READ_ONLY_REG_OFFSET = 0x140

    VREF_BITS = 6

    ROM_VALUE = 0xA5

    @unique
    class ResetOutLength(IntEnum):
        """PUSM : reset out pulse duration"""

        LENGTH_OFF = 0
        LENGTH_100NS = 1
        LENGTH_1US = 2
        LENGTH_10US = 3

    @unique
    class AdcInputSelect(IntEnum):
        """ADC input select"""

        EXT0 = 0
        EXT1 = 1
        EXT2 = 2
        EXT3 = 3
        EXT4 = 4
        EXT5 = 5
        EXT6 = 6
        EXT7 = 7
        EOMDAC = 8
        VDDIO = 9
        VDDTX = 10
        VDDRX = 11
        VDD = 12
        VDDA = 13
        TEMP = 14
        VREF2 = 15

    @unique
    class TestOutSelect(IntEnum):
        """Test output select"""

        ZERO = 0
        ONE = 1
        CLK40MA = 4
        CLK40MB = 5
        CLK40MC = 6
        CLK80MA = 7
        CLK80MB = 8
        CLK80MC = 9
        CLK160MA = 10
        CLK160MB = 11
        CLK160MC = 12
        CLK320MA = 13
        CLK320MB = 14
        CLK320MC = 15
        CLK640MA = 16
        CLK640MB = 17
        CLK640MC = 18
        CLK1G28A = 19
        CLK1G28B = 20
        CLK1G28C = 21
        SEUEVENT = 22
        PMCLKOUT = 23
        ENDCOUNTERREFCLKV = 24
        FROMCDR_CLKREF = 25
        FROMCDR_INSTLOCKPLL = 26
        ENDCOUNTERVCOV = 27
        FUSESRAMPENABLE = 28
        FUSESPOWERSHORT = 29
        FUSESPOWERENABLE = 30
        FUSESSCLK = 31
        FUSESPGM = 32
        FUSESDIN = 33
        FUSESCSB = 34
        PS0DLLLOCKEDV = 35
        PS1DLLLOCKEDV = 36
        PS2DLLLOCKEDV = 37
        PS3DLLLOCKEDV = 38
        PS0DLLLATEV = 39
        PS1DLLLATEV = 40
        PS2DLLLATEV = 41
        PS3DLLLATEV = 42
        PS0DLLOUTREF = 43
        PS1DLLOUTREF = 44
        PS2DLLOUTREF = 45
        PS3DLLOUTREF = 46
        EPORTRXDLLINSTANTLOCK0 = 47
        EPORTRXDLLINSTANTLOCK1 = 48
        EPORTRXDLLINSTANTLOCK2 = 49
        EPORTRXDLLINSTANTLOCK3 = 50
        EPORTRXDLLINSTANTLOCK4 = 51
        EPORTRXDLLINSTANTLOCK5 = 52
        EPORTRXDLLINSTANTLOCK6 = 53
        EPORTRXDLLOUTREF0 = 54
        EPORTRXDLLOUTREF1 = 55
        EPORTRXDLLOUTREF2 = 56
        EPORTRXDLLOUTREF3 = 57
        EPORTRXDLLOUTREF4 = 58
        EPORTRXDLLOUTREF5 = 59
        EPORTRXDLLOUTREF6 = 60
        DOWNLINKFRAME60 = 61
        DOWNLINKFRAME61 = 62
        DOWNLINKFRAME62 = 63
        DOWNLINKFRAME63 = 64
        EPORTRXDATAIN0 = 65
        EPORTRXDATAIN1 = 66
        EPORTRXDATAIN2 = 67
        EPORTRXDATAIN3 = 68
        EPORTRXDATAIN4 = 69
        EPORTRXDATAIN5 = 70
        EPORTRXDATAIN6 = 71
        EPORTRXDATAIN7 = 72
        EPORTRXDATAIN8 = 73
        EPORTRXDATAIN9 = 74
        EPORTRXDATAIN10 = 75
        EPORTRXDATAIN11 = 76
        EPORTRXDATAIN12 = 77
        EPORTRXDATAIN13 = 78
        EPORTRXDATAIN14 = 79
        EPORTRXDATAIN15 = 80
        EPORTRXDATAIN16 = 81
        EPORTRXDATAIN17 = 82
        EPORTRXDATAIN18 = 83
        EPORTRXDATAIN19 = 84
        EPORTRXDATAIN20 = 85
        EPORTRXDATAIN21 = 86
        EPORTRXDATAIN22 = 87
        EPORTRXDATAIN23 = 88
        EPORTRXDATAIN24 = 89
        EPORTRXDATAIN25 = 90
        EPORTRXDATAIN26 = 91
        EPORTRXDATAIN27 = 92
        PORA = 93
        PORB = 94
        PORC = 95
        EPORTRXDATAINEC = 96
        BODA = 97
        BODB = 98
        BODC = 99
        I2CTRANSACTIONSTARTV = 100
        I2CTRANSACTIONDONEV = 101
        I2CMASTER_GO0_V = 102
        I2CMASTER_GO1_V = 103
        I2CMASTER_GO2_V = 104
        SKIPCYCLERAW = 105
        SKIPCYCLEV = 106
        RXREADY = 107
        TXREADYV = 108
        PLLSTATEMACHINELOCKEDV = 109
        EPORTRXDLLLOCKEDV0 = 110
        EPORTRXDLLLOCKEDV1 = 111
        EPORTRXDLLLOCKEDV2 = 112
        EPORTRXDLLLOCKEDV3 = 113
        EPORTRXDLLLOCKEDV4 = 114
        EPORTRXDLLLOCKEDV5 = 115
        EPORTRXDLLLOCKEDV6 = 116
        EPORTRXDLLLATEV0 = 117
        EPORTRXDLLLATEV1 = 118
        EPORTRXDLLLATEV2 = 119
        EPORTRXDLLLATEV3 = 120
        EPORTRXDLLLATEV4 = 121
        EPORTRXDLLLATEV5 = 122
        EPORTRXDLLLATEV6 = 123
        FRAMEALIGNERREADYV = 124
