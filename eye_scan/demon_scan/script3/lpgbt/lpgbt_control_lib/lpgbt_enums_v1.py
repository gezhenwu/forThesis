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

from enum import IntEnum, unique  # pylint: disable=unused-import
from .lpgbt_enums import LpgbtEnums


class LpgbtEnumsV1(LpgbtEnums):
    """Class containing any lpGBTv1-related constants"""

    READ_WRITE_FUSE_REGS = 0x100
    READ_WRITE_REGS = 0x150
    READ_ONLY_REGS = 0x9E
    NUM_REGS = 0x1EE

    READ_WRITE_FUSE_REGS_OFFSET = 0x0
    READ_WRITE_REGS_OFFSET = 0x0
    READ_ONLY_REGS_OFFSET = 0x150

    VREF_BITS = 8

    ROM_VALUE = 0xA6

    # pylint: disable=too-many-lines,too-few-public-methods
    @unique
    class PusmState(IntEnum):
        """PowerUp State Machine States"""

        RESET0 = 0
        RESET1 = 1
        WAIT_VDD_STABLE = 2
        WAIT_VDD_HIGHER_THAN_0V90 = 3
        COPY_FUSES = 4
        CALCULATE_CHECKSUM = 5
        COPY_ROM = 6
        PAUSE_FOR_PLL_CONFIG_DONE = 7
        WAIT_POWER_GOOD = 8
        RESET_PLL = 9
        WAIT_PLL_LOCK = 10
        INIT_SCRAM = 11
        RESETOUT = 12
        I2C_TRANS = 13
        PAUSE_FOR_DLL_CONFIG_DONE = 14
        RESET_DLLS = 15
        WAIT_DLL_LOCK = 16
        RESET_LOGIC_USING_DLL = 17
        WAIT_CHNS_LOCKED = 18
        READY = 19

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
        VDAC = 8
        VSSA = 9
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
        CLK40MA = 2
        CLK40MB = 3
        CLK40MC = 4
        CLK80MA = 5
        CLK80MB = 6
        CLK80MC = 7
        CLK160MA = 8
        CLK160MB = 9
        CLK160MC = 10
        CLK320MA = 11
        CLK320MB = 12
        CLK320MC = 13
        CLK640MA = 14
        CLK640MB = 15
        CLK640MC = 16
        CLK1G28A = 17
        CLK1G28B = 18
        CLK1G28C = 19
        SEUEVENT = 20
        PMCLKOUT = 21
        ENDCOUNTERREFCLK = 22
        CLKREF = 23
        INSTLOCKPLL = 24
        ENDCOUNTERVCO = 25
        FUSERAMPENABLE = 26
        FUSEPOWERSHORT = 27
        FUSEPOWERENABLE = 28
        FUSESCLK = 29
        FUSEPGM = 30
        FUSEDIN = 31
        FUSECSB = 32
        PS0DLLLOCKED = 33
        PS1DLLLOCKED = 34
        PS2DLLLOCKED = 35
        PS3DLLLOCKED = 36
        PS0DLLLATE = 37
        PS1DLLLATE = 38
        PS2DLLLATE = 39
        PS3DLLLATE = 40
        PS0DLLOUT = 41
        PS1DLLOUT = 42
        PS2DLLOUT = 43
        PS3DLLOUT = 44
        EPRX0DLLINSTLOCK = 45
        EPRX1DLLINSTLOCK = 46
        EPRX2DLLINSTLOCK = 47
        EPRX3DLLINSTLOCK = 48
        EPRX4DLLINSTLOCK = 49
        EPRX5DLLINSTLOCK = 50
        EPRX6DLLINSTLOCK = 51
        EPRX0DLLOUT = 52
        EPRX1DLLOUT = 53
        EPRX2DLLOUT = 54
        EPRX3DLLOUT = 55
        EPRX4DLLOUT = 56
        EPRX5DLLOUT = 57
        EPRX6DLLOUT = 58
        DWNFRAME60 = 59
        DWNFRAME61 = 60
        DWNFRAME62 = 61
        DWNFRAME63 = 62
        EDIN0 = 63
        EDIN1 = 64
        EDIN2 = 65
        EDIN3 = 66
        EDIN4 = 67
        EDIN5 = 68
        EDIN6 = 69
        EDIN7 = 70
        EDIN8 = 71
        EDIN9 = 72
        EDIN10 = 73
        EDIN11 = 74
        EDIN12 = 75
        EDIN13 = 76
        EDIN14 = 77
        EDIN15 = 78
        EDIN16 = 79
        EDIN17 = 80
        EDIN18 = 81
        EDIN19 = 82
        EDIN20 = 83
        EDIN21 = 84
        EDIN22 = 85
        EDIN23 = 86
        EDIN24 = 87
        EDIN25 = 88
        EDIN26 = 89
        EDIN27 = 90
        EDINEC = 91
        PORA = 92
        PORB = 93
        PORC = 94
        BORA = 95
        BORB = 96
        BORC = 97
        I2CTRANSSTART = 98
        I2CTRANSDONE = 99
        I2CM0GO = 100
        I2CM1GO = 101
        I2CM2GO = 102
        SKIPCYCLERAW = 103
        SKIPCYCLE = 104
        SCRXREADY = 105
        SCTXREADY = 106
        PLLCDRLOCKED = 107
        EPRX0DLLLOCKED = 108
        EPRX1DLLLOCKED = 109
        EPRX2DLLLOCKED = 110
        EPRX3DLLLOCKED = 111
        EPRX4DLLLOCKED = 112
        EPRX5DLLLOCKED = 113
        EPRX6DLLLOCKED = 114
        EPRX0DLLLATE = 115
        EPRX1DLLLATE = 116
        EPRX2DLLLATE = 117
        EPRX3DLLLATE = 118
        EPRX4DLLLATE = 119
        EPRX5DLLLATE = 120
        EPRX6DLLLATE = 121
        FRAMEALIGNERREADY = 122
        HEADERINPHASE = 123
        SCACTIVE = 124
        I2CSTOP = 125
        I2CSTART = 126
        I2CSDASAFE = 127
        I2CSDARISE = 128
        I2CSDAFALL = 129
        I2CSCLSAFE = 130
        I2CSCLRISE = 131
        I2CSCLFALL = 132
        I2CACTIVE = 133
        CHECKSUMREADY = 134
        CHECKSUMSTART = 135
        COPYROMENABLE = 136
        COPYROMDONE = 137
        COPYFUSESENABLE = 138
        COPYFUSESDONE = 139
        ECTXDRIVERNEEDED = 140
        ECTXDRIVERENABLE = 141

    @unique
    class VddLevel(IntEnum):
        """PUSM : power sensing levels"""

        VDD_LEVEL_0V80 = 0
        VDD_LEVEL_0V85 = 1
        VDD_LEVEL_0V90 = 2
        VDD_LEVEL_0V95 = 3
        VDD_LEVEL_1V00 = 4
        VDD_LEVEL_1V05 = 5
        VDD_LEVEL_1V10 = 6
        VDD_LEVEL_1V15 = 7
