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
from .lpgbt_pins import LpgbtPins


class LpgbtPinsV0(LpgbtPins):
    """Class containing definitions of lpGBTv0 configuration pins"""

    # pylint: disable=too-few-public-methods

    # control pin definitions (associated constants are irrelevant)
    CTRL_SCI2C = 0x1001
    CTRL_STATEOVRD = 0x1003
    CTRL_VCOBYPASS = 0x1005

    CTRL_OUT_PINS = [
        LpgbtPins.CTRL_RSTB,
        CTRL_SCI2C,
        LpgbtPins.CTRL_LOCKMODE,
        CTRL_STATEOVRD,
        LpgbtPins.CTRL_PORDIS,
        CTRL_VCOBYPASS,
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
    class ConfigSelect(IntEnum):
        """ConfigSelect pin values"""

        SC = 0
        I2C = 1
