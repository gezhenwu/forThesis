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
"""lpGBT configuration pins"""
from enum import IntEnum, unique


class LpgbtPins:
    """Class containing definitions of lpGBT configuration pins (common to v0 and v1)"""

    # pylint: disable=too-few-public-methods

    # control pin definitions (associated constants are irrelevant)
    CTRL_RSTB = 0x1000
    CTRL_LOCKMODE = 0x1002
    CTRL_PORDIS = 0x1004
    CTRL_ADDR0 = 0x1006
    CTRL_ADDR1 = 0x1007
    CTRL_ADDR2 = 0x1008
    CTRL_ADDR3 = 0x1009
    CTRL_MODE0 = 0x100A
    CTRL_MODE1 = 0x100B
    CTRL_MODE2 = 0x100C
    CTRL_MODE3 = 0x100D
    CTRL_READY = 0x100E
    CTRL_RSTOUTB = 0x100F

    CTRL_OUT_PINS = [
        CTRL_RSTB,
        CTRL_LOCKMODE,
        CTRL_PORDIS,
        CTRL_ADDR0,
        CTRL_ADDR1,
        CTRL_ADDR2,
        CTRL_ADDR3,
        CTRL_MODE0,
        CTRL_MODE1,
        CTRL_MODE2,
        CTRL_MODE3,
    ]

    CTRL_IN_PINS = [
        CTRL_READY,
        CTRL_RSTOUTB,
    ]

    @unique
    class LockMode(IntEnum):
        """CDR locking mode"""

        REFERENCE = 0
        REFERENCELESS = 1

    @unique
    class LpgbtMode(IntEnum):
        """lpGBT modes of operation"""

        OFF_5G_FEC5 = 0
        TX_5G_FEC5 = 1
        RX_5G_FEC5 = 2
        TRX_5G_FEC5 = 3
        OFF_5G_FEC12 = 4
        TX_5G_FEC12 = 5
        RX_5G_FEC12 = 6
        TRX_5G_FEC12 = 7
        OFF_10G_FEC5 = 8
        TX_10G_FEC5 = 9
        RX_10G_FEC5 = 10
        TRX_10G_FEC5 = 11
        OFF_10G_FEC12 = 12
        TX_10G_FEC12 = 13
        RX_10G_FEC12 = 14
        TRX_10G_FEC12 = 15
