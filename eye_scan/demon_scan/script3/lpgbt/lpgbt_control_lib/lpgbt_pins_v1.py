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

from enum import IntEnum, unique  # pylint: disable=unused-import
from .lpgbt_pins import LpgbtPins


class LpgbtPinsV1(LpgbtPins):
    """Class containing definitions of lpGBTv0 configuration pins"""

    # pylint: disable=too-few-public-methods

    # control pin definitions (associated constants are irrelevant)
    CTRL_BOOTCNF1 = 0x1001
    CTRL_EDINECTERM = 0x1003
    CTRL_BOOTCNF0 = 0x1005

    CTRL_OUT_PINS = [
        LpgbtPins.CTRL_RSTB,
        CTRL_BOOTCNF1,
        LpgbtPins.CTRL_LOCKMODE,
        CTRL_EDINECTERM,
        LpgbtPins.CTRL_PORDIS,
        CTRL_BOOTCNF0,
        LpgbtPins.CTRL_ADDR0,
        LpgbtPins.CTRL_ADDR1,
        LpgbtPins.CTRL_ADDR2,
        LpgbtPins.CTRL_ADDR3,
        LpgbtPins.CTRL_MODE0,
        LpgbtPins.CTRL_MODE1,
        LpgbtPins.CTRL_MODE2,
        LpgbtPins.CTRL_MODE3,
    ]

    CTRL_IN_PINS = [
        LpgbtPins.CTRL_READY,
        LpgbtPins.CTRL_RSTOUTB,
    ]

    @unique
    class BootConfig(IntEnum):
        """Boot config"""

        LOAD_FUSES_CRC = 0
        LOAD_ROM = 1
        LOAD_FUSES_NO_CRC = 2
        NO_INIT = 3
