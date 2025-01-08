#!/usr/bin/env python3
###############################################################################
#                                                                             #
#        _        _____ ____ _______                                          #
#       | |      / ____|  _ \__   __|                                         #
#       | |_ __ | |  __| |_) | | |                                            #
#       | | '_ \| | |_ |  _ <  | |                                            #
#       | | |_) | |__| | |_) | | |                                            #
#       |_| .__/ \_____|____/  |_|                                            #
#         | |                                                                 #
#         |_|                                                                 #
#                                                                             #
#  Copyright (C) 2020-2021 lpGBT Team, CERN                                   #
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
""" Lpgbt Constants"""
# pylint: disable=too-many-lines,too-few-public-methods,missing-class-docstring
# pylint: disable=empty-docstring,line-too-long,invalid-name
# pylint: disable=missing-function-docstring, unused-argument

from enum import IntEnum, unique


class LpgbtRegisterMap:
    """Class containing lpGBT-related constants common to lpGBTv0 and lpGBTv1.

    The class definitions below are included only for static code checking and the assigned
    values (or lack of there of) renders this class unusable. Please always use LpgbtV0 or LpgbtV1
    instead.
    """

    class ADCCAL0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2SEHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2SELOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN8DIFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL11:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN8DIRFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCCALGAIN8DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL12:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN16DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL13:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN16DIFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL14:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN16DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCCALGAIN16DIRFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2SEHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCCALGAIN2SELOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2DIFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN2DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCCALGAIN2DIRFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN4DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN4DIFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN4DIRFLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCCALGAIN4DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCAL9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCALGAIN8DIFHIGH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCCONVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCGAINSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCMON:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class VDDMONENA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class VDDANMONENA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class VDDRXMONENA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TEMPSENSRESET:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class VDDTXMONENA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCSELECT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCINNSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCINPSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCSTATUSH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCBUSY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ADCVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ADCSTATUSL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ADCVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTMEASTIME:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BERTSTART:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class SKIPDISABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTDATAPATTERN0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTDATAPATTERN1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTDATAPATTERN2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTDATAPATTERN3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTRESULT0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTERRORCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTRESULT1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTERRORCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTRESULT2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTERRORCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTRESULT3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTERRORCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTRESULT4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTERRORCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTSOURCE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTSOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class BERTSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BERTPRBSERRORFLAG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BERTDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BERTBUSY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CHIPCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class HIGHSPEEDDATAOUTINVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CHIPADDRESSBAR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class HIGHSPEEDDATAININVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CHIPID0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CHIPID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CHIPID1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CHIPID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CHIPID2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CHIPID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CHIPID3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CHIPID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCDRFFPROPCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGCDRFEEDFORWARDPROPCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCDRFEEDFORWARDPROPCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCDRINTCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGCDRINTCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCDRINTCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCDRPROPCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGCDRPROPCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCDRPROPCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCNTOVERRIDE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CDRCOENABLECDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCODISDESVBIASGEN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCOREFCLKSEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCOENABLEFD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCOOVERRIDEVC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCODISDATACOUNTERREF:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCOCONNECTPLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCOENABLEPLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCONFIG0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGCALIBRATIONENDOFCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGBIASGENCONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGCONFIG1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGVCODAC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGVCORAILMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCONTROLOVERRIDEENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCDRRES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGDISABLEFRAMEALIGNERLOCKCONTROL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGFFCAP:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGFEEDFORWARDCAPWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGFEEDFORWARDCAP:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCAPBANKOVERRIDEENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CDRCOCONNECTCDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGFLLINTCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGFLLINTCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGFLLINTCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGLFCONFIG0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGLOCKFILTERENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGCAPBANKSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGLOCKFILTERLOCKTHRCOUNTER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGLFCONFIG1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGLOCKFILTERRELOCKTHRCOUNTER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGLOCKFILTERUNLOCKTHRCOUNTER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGOVERRIDECAPBANK:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGCAPBANKSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGPLLINTCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGPLLINTCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGPLLINTCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGPLLPROPCUR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGPLLPROPCUR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGPLLPROPCURWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGPLLRES:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGPLLRES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGPLLRESWHENLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_PLL_R_CONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONFIG_I_PLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_CONFIG_I_FLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONFIG_I_CDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_CONFIG_P_FF_CDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONFIG_P_CDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_LFLOSSOFLOCKCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_BIASGEN_CONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONFIG_P_PLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_VCOCAPSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_VCODAC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_VCOCAPSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_DATAMUXCFG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_OVERRIDEVC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONNECTCDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_ENABLEPLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_ENABLEFD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_ENABLECDR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_DISDATACOUNTERREF:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_REFCLKSEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONNECTPLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_LFLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_ENABLE_CDR_R:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_CONFIG_FF_CAP:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_LFINSTLOCK:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_SMLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_VCORAILMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGSTATUS9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKG_LFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKG_SMSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKGWAITTIME:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKGWAITPLLTIME:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKGWAITCDRTIME:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CLKTREE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CLKTREEADISABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKTREEMAGICNUMBER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKTREECDISABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class CLKTREEBDISABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CONFIGERRORCOUNTERH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CONFIGERRORCOUNTER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CONFIGERRORCOUNTERL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CONFIGERRORCOUNTER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CONFIGPINS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class LPGBTMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class LOCKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CURDACCALH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CURDACCAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CURDACCALL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CURDACCAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CURDACCHN:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CURDACCHNENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class CURDACVALUE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CURDACSELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DACCAL0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DACCALMINCODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DACCAL1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DACCALMAXCODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DACCAL2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DACCALMAXCODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DACCALMINCODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DACCONFIGH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class CURDACENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class VOLDACENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class VOLDACVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DACCONFIGL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class VOLDACVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DATAPATH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ULDPBYPASSFECCODER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLDPBYPASDEINTERLEVEAR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULDPBYPASSINTERLEAVER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLDPBYPASSDESCRAMBLER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLDPBYPASFECDECODER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULDPBYPASSSCRAMBLER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DPDATAPATTERN0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DPDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DPDATAPATTERN1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DPDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DPDATAPATTERN2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DPDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class DPDATAPATTERN3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DPDATAPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCONFIGH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMENDOFCOUNTSEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EOMSTART:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EOMBYPASSPHASEINTERPOLATOR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EOMENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCONFIGL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMPHASESEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCOUNTER40MH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMCOUNTER40M:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCOUNTER40ML:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMCOUNTER40M:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCOUTERVALUEH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMCOUNTERVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMCOUTERVALUEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMCOUNTERVALUE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMBUSY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EOMEND:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EOMSMSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EOMVOFSEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EOMVOFSEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK0CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK0FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK0INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK0DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK0CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK0PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK0PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK0PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK10CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK10FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK10INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK10DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK10CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK10PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK10PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK10PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK11CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK11DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK11INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK11FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK11CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK11PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK11PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK11PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK12CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK12INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK12FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK12DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK12CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK12PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK12PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK12PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK13CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK13INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK13FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK13DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK13CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK13PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK13PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK13PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK14CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK14INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK14DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK14FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK14CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK14PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK14PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK14PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK15CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK15FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK15INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK15DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK15CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK15PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK15PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK15PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK16CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK16DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK16INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK16FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK16CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK16PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK16PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK16PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK17CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK17INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK17DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK17FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK17CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK17PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK17PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK17PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK18CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK18FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK18INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK18DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK18CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK18PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK18PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK18PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK19CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK19DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK19INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK19FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK19CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK19PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK19PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK19PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK1CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK1DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK1INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK1FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK1CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK1PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK1PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK1PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK20CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK20INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK20DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK20FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK20CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK20PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK20PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK20PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK21CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK21DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK21INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK21FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK21CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK21PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK21PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK21PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK22CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK22DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK22INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK22FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK22CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK22PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK22PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK22PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK23CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK23INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK23FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK23DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK23CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK23PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK23PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK23PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK24CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK24DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK24FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK24INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK24CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK24PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK24PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK24PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK25CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK25INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK25DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK25FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK25CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK25PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK25PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK25PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK26CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK26FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK26INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK26DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK26CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK26PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK26PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK26PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK27CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK27INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK27DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK27FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK27CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK27PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK27PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK27PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK28CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK28DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK28INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK28FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK28CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK28PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK28PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK28PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK2CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK2FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK2INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK2DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK2CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK2PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK2PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK2PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK3CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK3DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK3INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK3FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK3CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK3PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK3PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK3PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK4CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK4DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK4INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK4FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK4CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK4PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK4PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK4PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK5CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK5INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK5FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK5DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK5CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK5PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK5PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK5PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK6CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK6INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK6DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK6FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK6CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK6PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK6PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK6PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK7CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK7FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK7DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK7INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK7CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK7PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK7PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK7PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK8CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK8DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK8FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK8INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK8CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK8PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK8PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK8PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK9CHNCNTRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK9INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK9FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK9DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPCLK9CHNCNTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPCLK9PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK9PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPCLK9PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX00CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX00ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX01CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX01EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX02CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX02EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX02TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX02ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX02INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX02PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX03CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX03ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX0CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX00ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX02ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX0CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX0CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX0CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX0CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX0DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX0DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX0LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX0STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX10CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX10EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX11CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX11EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX12CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX12INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX13CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX13TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX1CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX12ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX1CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX1CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX1CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX1CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX1DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX1DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX1LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX1CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX1STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX20CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX20EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX21CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX21EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX22CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX22PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX23CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX23TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX2CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX2DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX2CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX2CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX2CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX2CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX2DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX2DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX2LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX2CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX30CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX30EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX31CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX31INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX32CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX32EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX33CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX33PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX3CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX33ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX3CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX3CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX3CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX3CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX3DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX3DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX3LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX3CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX3STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX40CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX40EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX41CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX41EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX42CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX42ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX43CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX43INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX4CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX4DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX4CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX4CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX4CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX4CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX4DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX4DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX4LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX4CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX50CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX50EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX51CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX51EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX52CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX52TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX53CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX53PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX5CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX53ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX5CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX5CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX5CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX5CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX5DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX5DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX5LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX5CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX5STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX60CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX60PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX61CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX61TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX62CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX62EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX62ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX62PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX62INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX62TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX63CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX63EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63TERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63ACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63PHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX6CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX61ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6TRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX62ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX6CURRENTPHASE10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX6CURRENTPHASE1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6CURRENTPHASE0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX6CURRENTPHASE32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX6CURRENTPHASE3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6CURRENTPHASE2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX6DLLSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX6DLLLFSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6DLLLOLCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6DLLLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRX6LOCKED:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX6STATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX6CHNLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXDLLCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRXDLLFSMCLKALWAYSON:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXDLLCURRENT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXDLLCOARSELOCKDETECTION:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXENABLEREINIT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXDLLCONFIRMCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXECCHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRXECACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXECTERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXECPHASESELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXECINVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXECCONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRXECTRACKMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXECCURRENTPHASE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRXECCURRENTPHASE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXEQ10CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX02EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXEQ32CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX30EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX32EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXEQ54CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX41EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX40EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXEQ6CONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX62EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63EQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXLOCKFILTER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRXRELOCKTHRESHOLD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXLOCKTHRESHOLD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXPRBS0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX02PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX11PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX10PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX00PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX12PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX03PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX13PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX01PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXPRBS1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX32PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX20PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX22PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX21PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX31PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX23PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX33PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX30PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXPRBS2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX40PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX53PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX41PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX52PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX51PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX43PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX42PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX50PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXPRBS3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX62PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX63PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRXECPRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX61PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX60PRBSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXTRAIN10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX1TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX0TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXTRAIN32:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX3TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX2TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXTRAIN54:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX5TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPRX4TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPRXTRAINEC6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPRX6TRAIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX00CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX00DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX00PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX00PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX01CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX01DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX01PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX01PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX01_00CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX00INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX01PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX01INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX00PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX02CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX02PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX02PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX02DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX03CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX03PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX03PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX03DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX03_02CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX03INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX02INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX03PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX02PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX10CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX10PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX10PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX10DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX10ENABLE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX11ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX02ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX01ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX03ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX13ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX00ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX12ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX10ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX11CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX11DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX11PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX11PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX11_10CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX11INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX11PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX10INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX10PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX12CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX12DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX12PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX12PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX13CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX13PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX13PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX13DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX13_12CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX12INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX12PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX13INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX13PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX20CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX20DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX20PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX20PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX21CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX21PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX21DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX21PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX21_20CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX20INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX21PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX20PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX21INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX22CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX22DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX22PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX22PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX23CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX23DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX23PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX23PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX23_22CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX22INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX22PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX23INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX23PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX30CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX30PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX30PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX30DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX31CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX31PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX31PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX31DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX31_30CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX30INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX30PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX31INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX31PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX32CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX32PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX32PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX32DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX32ENABLE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX32ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX33ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX21ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX22ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX23ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX31ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX30ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX20ENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX33CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX33DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX33PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX33PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTX33_32CHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX33PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX32PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX33INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX32INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTXCONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX2MIRRORENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX3MIRRORENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX0MIRRORENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX1MIRRORENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTXDATARATE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTX2DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX1DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX3DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EPTX0DATARATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EPTXECCHNCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EPTXECDRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EQCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EQATTENUATION:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EQCAP:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class EQRES:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class EQRES2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EQRES3:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EQRES1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class EQRES0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FAMAXHEADERFOUNDCOUNT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FAMAXHEADERFOUNDCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FAMAXHEADERFOUNDCOUNTAFTERNF:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FAMAXHEADERFOUNDCOUNTAFTERNF:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FAMAXHEADERNOTFOUNDCOUNT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FAMAXHEADERNOTFOUNDCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FASTATE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FASTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FORCEENABLE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class LDFORCEENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FORCETXENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CMCLKALWAYSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PSFSMCLKALWAYSON:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FORCERXENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWADDH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWADDL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWDATAA:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWDATAB:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWDATAC:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEBLOWDATAD:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOWDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSECONTROL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEBLOW:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FUSEREAD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FUSEBLOWPULSELENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEMAGIC:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEMAGICNUMBER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSESTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class FUSEDATAVALID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FUSEBLOWBUSY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FUSEBLOWERROR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class FUSEBLOWDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEVALUESA:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SELECTEDFUSEVALUES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEVALUESB:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SELECTEDFUSEVALUES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEVALUESC:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SELECTEDFUSEVALUES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class FUSEVALUESD:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SELECTEDFUSEVALUES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0ADDRESS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0ADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0CMD:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0CMD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0ADDRESSEXT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM0SCLPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM0SDAPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM0SDADRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM0SCLDRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0CTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0CTRL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0DATA0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0DATA1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0DATA2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0DATA3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0MASK:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0MASK:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ11:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ12:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ13:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ14:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ15:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READ9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0READBYTE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0READBYTE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0STATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0STATUS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM0TRANCNT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM0TRANCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1ADDRESS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1ADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1CMD:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1CMD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1SDADRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM1ADDRESSEXT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM1SCLPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM1SDAPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM1SCLDRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1CTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1CTRL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1DATA0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1DATA1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1DATA2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1DATA3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1MASK:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1MASK:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ11:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ12:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ13:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ14:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ15:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READ9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1READBYTE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1READBYTE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1STATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1STATUS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM1TRANCNT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM1TRANCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2ADDRESS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2ADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2CMD:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2CMD:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2ADDRESSEXT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM2SCLPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM2SCLDRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM2SDADRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CM2SDAPULLUPENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2CTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2CTRL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2DATA0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2DATA1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2DATA2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2DATA3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2DATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2MASK:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2MASK:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ11:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ12:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ13:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ14:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ15:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READ9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2READBYTE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2READBYTE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2STATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2STATUS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CM2TRANCNT:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CM2TRANCNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSADDRESS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSADDRESS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSCHANNEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CMTRANSENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class I2CMTRANSADDRESSEXT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSCTRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSCTRL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA10:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA11:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA12:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA13:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA14:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA15:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA6:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA7:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA8:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CMTRANSDATA9:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class I2CMTRANSDATA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class I2CSLAVEADDRESS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ASICCONTROLADR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class LDCONFIGH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class LDEMPHASISENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class LDMODULATIONCURRENT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class LDCONFIGL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class LDEMPHASISSHORT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class LDEMPHASISAMP:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PGCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PGENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PGDELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PGLEVEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIODIRH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIODIR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIODIRL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIODIR:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIODRIVESTRENGTHH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIODRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIODRIVESTRENGTHL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIODRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOINH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOINL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOIN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOOUTH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOOUT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOOUTL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOOUT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOPULLENAH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOPULLENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOPULLENAL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOPULLENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOUPDOWNH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOUPDOWN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PIOUPDOWNL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PIOUPDOWN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PMFREQA:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PMFREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PMFREQB:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PMFREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PMFREQC:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PMFREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PORBOR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PORA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BODB:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BODC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PORC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PORB:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BODA:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class POWERUP0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PUSMREADYWHENCHNSLOCKED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PUSMPLLTIMEOUTCONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class POWERUP1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PUSMCHANNELSTIMEOUTCONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PUSMDLLTIMEOUTCONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class POWERUP2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DLLCONFIGDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PLLCONFIGDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class POWERUP3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PUSMFORCESTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PUSMSTATEFORCED:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class POWERUP4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PUSMFORCEMAGIC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PROCESSANDSEUMONITOR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PMCHANNEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class SEUENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PMENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PROCESSMONITORSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PMDONE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PMBUSY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS0CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS0FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0ENABLEFINETUNE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS0DELAY:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS0DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS0OUTDRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS0PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS1CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS1ENABLEFINETUNE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS1DELAY:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS1DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS1OUTDRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS1PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS2CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS2ENABLEFINETUNE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS2DELAY:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS2DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS2OUTDRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS2PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS3CONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS3DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS3ENABLEFINETUNE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS3FREQ:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS3DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS3DELAY:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS3DELAY:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PS3OUTDRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS3PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS3PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS3PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PSDLLCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PSDLLCURRENTSEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PSDLLCONFIRMCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PSSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PS3DLLINITSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS1DLLINITSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS2DLLINITSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class PS0DLLINITSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class PUSMSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class PUSMSTATE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class REFCLK:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class REFCLKFORCEENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class REFCLKACBIAS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class REFCLKTERM:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class RESERVED1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

    class RESETCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class BODENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class BODLEVEL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ROM:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ROMREG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class RST0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class RSTFUSES:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTI2CM1:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTPLLDIGITAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTI2CM0:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTI2CM2:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTCONFIG:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTTXLOGIC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTRXLOGIC:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class RST1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class RSTFRAMEALIGNER:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX3DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX5DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX1DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX4DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX6DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX2DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTEPRX0DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class RST2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class RSTPS0DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTPS2DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RESETOUTFORCEACTIVE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTPS1DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class RSTPS3DLL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class SKIPFORCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class SCCONFIG:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SCPARITYCHECKDISABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class SCSTATUS:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SCPARITYVALID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class SEUCOUNTH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SEUCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class SEUCOUNTL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class SEUCOUNT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TEMPCALH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TEMPCAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TEMPCALL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TEMPCAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO0SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO0SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO1SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO1SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO2SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO2SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO3SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO3SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO4DRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO4PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO4DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO4PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO4SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO4SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO5DRIVER:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO5PREEMPHASISSTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO5DRIVESTRENGTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO5PREEMPHASISMODE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TO5SEL:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO5SELECT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TODRIVINGSTRENGTH:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO0DS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO3DS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO1DS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO2DS:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TOPREEMP:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TO5INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO5PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO4PREEMPHASISWIDTH:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class TO4INVERT:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class TOVALUE:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class TOVAL:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ULSERTESTPATTERN:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULECDATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class LDDATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULG1DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULG0DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ULG3DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULG2DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ULG5DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULG4DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE4:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class ULG6DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLECDATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class ULICDATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class ULDATASOURCE5:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class DLG0DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLG1DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLG3DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

        class DLG2DATASOURCE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class USERID0:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class USERID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class USERID1:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class USERID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class USERID2:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class USERID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class USERID3:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class USERID:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    class VREFCNTR:
        address = None

        @staticmethod
        def __str__():
            return ""

        @staticmethod
        def __int__():
            return None

        class VREFENABLE:
            offset = None
            length = None
            bit_mask = None

            @staticmethod
            def validate(value):
                return None

    @unique
    class Reg(IntEnum):
        ADCCAL0 = 0x0000
        ADCCAL1 = 0x0001
        ADCCAL10 = 0x0002
        ADCCAL11 = 0x0003
        ADCCAL12 = 0x0004
        ADCCAL13 = 0x0005
        ADCCAL14 = 0x0006
        ADCCAL2 = 0x0007
        ADCCAL3 = 0x0008
        ADCCAL4 = 0x0009
        ADCCAL5 = 0x000A
        ADCCAL6 = 0x000B
        ADCCAL7 = 0x000C
        ADCCAL8 = 0x000D
        ADCCAL9 = 0x000E
        ADCCONFIG = 0x000F
        ADCMON = 0x0010
        ADCSELECT = 0x0011
        ADCSTATUSH = 0x0012
        ADCSTATUSL = 0x0013
        BERTCONFIG = 0x0014
        BERTDATAPATTERN0 = 0x0015
        BERTDATAPATTERN1 = 0x0016
        BERTDATAPATTERN2 = 0x0017
        BERTDATAPATTERN3 = 0x0018
        BERTRESULT0 = 0x0019
        BERTRESULT1 = 0x001A
        BERTRESULT2 = 0x001B
        BERTRESULT3 = 0x001C
        BERTRESULT4 = 0x001D
        BERTSOURCE = 0x001E
        BERTSTATUS = 0x001F
        CHIPCONFIG = 0x0020
        CHIPID0 = 0x0021
        CHIPID1 = 0x0022
        CHIPID2 = 0x0023
        CHIPID3 = 0x0024
        CLKGCDRFFPROPCUR = 0x0025
        CLKGCDRINTCUR = 0x0026
        CLKGCDRPROPCUR = 0x0027
        CLKGCNTOVERRIDE = 0x0028
        CLKGCONFIG0 = 0x0029
        CLKGCONFIG1 = 0x002A
        CLKGFFCAP = 0x002B
        CLKGFLLINTCUR = 0x002C
        CLKGLFCONFIG0 = 0x002D
        CLKGLFCONFIG1 = 0x002E
        CLKGOVERRIDECAPBANK = 0x002F
        CLKGPLLINTCUR = 0x0030
        CLKGPLLPROPCUR = 0x0031
        CLKGPLLRES = 0x0032
        CLKGSTATUS0 = 0x0033
        CLKGSTATUS1 = 0x0034
        CLKGSTATUS2 = 0x0035
        CLKGSTATUS3 = 0x0036
        CLKGSTATUS4 = 0x0037
        CLKGSTATUS5 = 0x0038
        CLKGSTATUS6 = 0x0039
        CLKGSTATUS7 = 0x003A
        CLKGSTATUS8 = 0x003B
        CLKGSTATUS9 = 0x003C
        CLKGWAITTIME = 0x003D
        CLKTREE = 0x003E
        CONFIGERRORCOUNTERH = 0x003F
        CONFIGERRORCOUNTERL = 0x0040
        CONFIGPINS = 0x0041
        CURDACCALH = 0x0042
        CURDACCALL = 0x0043
        CURDACCHN = 0x0044
        CURDACVALUE = 0x0045
        DACCAL0 = 0x0046
        DACCAL1 = 0x0047
        DACCAL2 = 0x0048
        DACCONFIGH = 0x0049
        DACCONFIGL = 0x004A
        DATAPATH = 0x004B
        DPDATAPATTERN0 = 0x004C
        DPDATAPATTERN1 = 0x004D
        DPDATAPATTERN2 = 0x004E
        DPDATAPATTERN3 = 0x004F
        EOMCONFIGH = 0x0050
        EOMCONFIGL = 0x0051
        EOMCOUNTER40MH = 0x0052
        EOMCOUNTER40ML = 0x0053
        EOMCOUTERVALUEH = 0x0054
        EOMCOUTERVALUEL = 0x0055
        EOMSTATUS = 0x0056
        EOMVOFSEL = 0x0057
        EPCLK0CHNCNTRH = 0x0058
        EPCLK0CHNCNTRL = 0x0059
        EPCLK10CHNCNTRH = 0x005A
        EPCLK10CHNCNTRL = 0x005B
        EPCLK11CHNCNTRH = 0x005C
        EPCLK11CHNCNTRL = 0x005D
        EPCLK12CHNCNTRH = 0x005E
        EPCLK12CHNCNTRL = 0x005F
        EPCLK13CHNCNTRH = 0x0060
        EPCLK13CHNCNTRL = 0x0061
        EPCLK14CHNCNTRH = 0x0062
        EPCLK14CHNCNTRL = 0x0063
        EPCLK15CHNCNTRH = 0x0064
        EPCLK15CHNCNTRL = 0x0065
        EPCLK16CHNCNTRH = 0x0066
        EPCLK16CHNCNTRL = 0x0067
        EPCLK17CHNCNTRH = 0x0068
        EPCLK17CHNCNTRL = 0x0069
        EPCLK18CHNCNTRH = 0x006A
        EPCLK18CHNCNTRL = 0x006B
        EPCLK19CHNCNTRH = 0x006C
        EPCLK19CHNCNTRL = 0x006D
        EPCLK1CHNCNTRH = 0x006E
        EPCLK1CHNCNTRL = 0x006F
        EPCLK20CHNCNTRH = 0x0070
        EPCLK20CHNCNTRL = 0x0071
        EPCLK21CHNCNTRH = 0x0072
        EPCLK21CHNCNTRL = 0x0073
        EPCLK22CHNCNTRH = 0x0074
        EPCLK22CHNCNTRL = 0x0075
        EPCLK23CHNCNTRH = 0x0076
        EPCLK23CHNCNTRL = 0x0077
        EPCLK24CHNCNTRH = 0x0078
        EPCLK24CHNCNTRL = 0x0079
        EPCLK25CHNCNTRH = 0x007A
        EPCLK25CHNCNTRL = 0x007B
        EPCLK26CHNCNTRH = 0x007C
        EPCLK26CHNCNTRL = 0x007D
        EPCLK27CHNCNTRH = 0x007E
        EPCLK27CHNCNTRL = 0x007F
        EPCLK28CHNCNTRH = 0x0080
        EPCLK28CHNCNTRL = 0x0081
        EPCLK2CHNCNTRH = 0x0082
        EPCLK2CHNCNTRL = 0x0083
        EPCLK3CHNCNTRH = 0x0084
        EPCLK3CHNCNTRL = 0x0085
        EPCLK4CHNCNTRH = 0x0086
        EPCLK4CHNCNTRL = 0x0087
        EPCLK5CHNCNTRH = 0x0088
        EPCLK5CHNCNTRL = 0x0089
        EPCLK6CHNCNTRH = 0x008A
        EPCLK6CHNCNTRL = 0x008B
        EPCLK7CHNCNTRH = 0x008C
        EPCLK7CHNCNTRL = 0x008D
        EPCLK8CHNCNTRH = 0x008E
        EPCLK8CHNCNTRL = 0x008F
        EPCLK9CHNCNTRH = 0x0090
        EPCLK9CHNCNTRL = 0x0091
        EPRX00CHNCNTR = 0x0092
        EPRX01CHNCNTR = 0x0093
        EPRX02CHNCNTR = 0x0094
        EPRX03CHNCNTR = 0x0095
        EPRX0CONTROL = 0x0096
        EPRX0CURRENTPHASE10 = 0x0097
        EPRX0CURRENTPHASE32 = 0x0098
        EPRX0DLLSTATUS = 0x0099
        EPRX0LOCKED = 0x009A
        EPRX10CHNCNTR = 0x009B
        EPRX11CHNCNTR = 0x009C
        EPRX12CHNCNTR = 0x009D
        EPRX13CHNCNTR = 0x009E
        EPRX1CONTROL = 0x009F
        EPRX1CURRENTPHASE10 = 0x00A0
        EPRX1CURRENTPHASE32 = 0x00A1
        EPRX1DLLSTATUS = 0x00A2
        EPRX1LOCKED = 0x00A3
        EPRX20CHNCNTR = 0x00A4
        EPRX21CHNCNTR = 0x00A5
        EPRX22CHNCNTR = 0x00A6
        EPRX23CHNCNTR = 0x00A7
        EPRX2CONTROL = 0x00A8
        EPRX2CURRENTPHASE10 = 0x00A9
        EPRX2CURRENTPHASE32 = 0x00AA
        EPRX2DLLSTATUS = 0x00AB
        EPRX2LOCKED = 0x00AC
        EPRX30CHNCNTR = 0x00AD
        EPRX31CHNCNTR = 0x00AE
        EPRX32CHNCNTR = 0x00AF
        EPRX33CHNCNTR = 0x00B0
        EPRX3CONTROL = 0x00B1
        EPRX3CURRENTPHASE10 = 0x00B2
        EPRX3CURRENTPHASE32 = 0x00B3
        EPRX3DLLSTATUS = 0x00B4
        EPRX3LOCKED = 0x00B5
        EPRX40CHNCNTR = 0x00B6
        EPRX41CHNCNTR = 0x00B7
        EPRX42CHNCNTR = 0x00B8
        EPRX43CHNCNTR = 0x00B9
        EPRX4CONTROL = 0x00BA
        EPRX4CURRENTPHASE10 = 0x00BB
        EPRX4CURRENTPHASE32 = 0x00BC
        EPRX4DLLSTATUS = 0x00BD
        EPRX4LOCKED = 0x00BE
        EPRX50CHNCNTR = 0x00BF
        EPRX51CHNCNTR = 0x00C0
        EPRX52CHNCNTR = 0x00C1
        EPRX53CHNCNTR = 0x00C2
        EPRX5CONTROL = 0x00C3
        EPRX5CURRENTPHASE10 = 0x00C4
        EPRX5CURRENTPHASE32 = 0x00C5
        EPRX5DLLSTATUS = 0x00C6
        EPRX5LOCKED = 0x00C7
        EPRX60CHNCNTR = 0x00C8
        EPRX61CHNCNTR = 0x00C9
        EPRX62CHNCNTR = 0x00CA
        EPRX63CHNCNTR = 0x00CB
        EPRX6CONTROL = 0x00CC
        EPRX6CURRENTPHASE10 = 0x00CD
        EPRX6CURRENTPHASE32 = 0x00CE
        EPRX6DLLSTATUS = 0x00CF
        EPRX6LOCKED = 0x00D0
        EPRXDLLCONFIG = 0x00D1
        EPRXECCHNCNTR = 0x00D2
        EPRXECCONTROL = 0x00D3
        EPRXECCURRENTPHASE = 0x00D4
        EPRXEQ10CONTROL = 0x00D5
        EPRXEQ32CONTROL = 0x00D6
        EPRXEQ54CONTROL = 0x00D7
        EPRXEQ6CONTROL = 0x00D8
        EPRXLOCKFILTER = 0x00D9
        EPRXPRBS0 = 0x00DA
        EPRXPRBS1 = 0x00DB
        EPRXPRBS2 = 0x00DC
        EPRXPRBS3 = 0x00DD
        EPRXTRAIN10 = 0x00DE
        EPRXTRAIN32 = 0x00DF
        EPRXTRAIN54 = 0x00E0
        EPRXTRAINEC6 = 0x00E1
        EPTX00CHNCNTR = 0x00E2
        EPTX01CHNCNTR = 0x00E3
        EPTX01_00CHNCNTR = 0x00E4
        EPTX02CHNCNTR = 0x00E5
        EPTX03CHNCNTR = 0x00E6
        EPTX03_02CHNCNTR = 0x00E7
        EPTX10CHNCNTR = 0x00E8
        EPTX10ENABLE = 0x00E9
        EPTX11CHNCNTR = 0x00EA
        EPTX11_10CHNCNTR = 0x00EB
        EPTX12CHNCNTR = 0x00EC
        EPTX13CHNCNTR = 0x00ED
        EPTX13_12CHNCNTR = 0x00EE
        EPTX20CHNCNTR = 0x00EF
        EPTX21CHNCNTR = 0x00F0
        EPTX21_20CHNCNTR = 0x00F1
        EPTX22CHNCNTR = 0x00F2
        EPTX23CHNCNTR = 0x00F3
        EPTX23_22CHNCNTR = 0x00F4
        EPTX30CHNCNTR = 0x00F5
        EPTX31CHNCNTR = 0x00F6
        EPTX31_30CHNCNTR = 0x00F7
        EPTX32CHNCNTR = 0x00F8
        EPTX32ENABLE = 0x00F9
        EPTX33CHNCNTR = 0x00FA
        EPTX33_32CHNCNTR = 0x00FB
        EPTXCONTROL = 0x00FC
        EPTXDATARATE = 0x00FD
        EPTXECCHNCNTR = 0x00FE
        EQCONFIG = 0x00FF
        EQRES = 0x0100
        FAMAXHEADERFOUNDCOUNT = 0x0101
        FAMAXHEADERFOUNDCOUNTAFTERNF = 0x0102
        FAMAXHEADERNOTFOUNDCOUNT = 0x0103
        FASTATE = 0x0104
        FORCEENABLE = 0x0105
        FUSEBLOWADDH = 0x0106
        FUSEBLOWADDL = 0x0107
        FUSEBLOWDATAA = 0x0108
        FUSEBLOWDATAB = 0x0109
        FUSEBLOWDATAC = 0x010A
        FUSEBLOWDATAD = 0x010B
        FUSECONTROL = 0x010C
        FUSEMAGIC = 0x010D
        FUSESTATUS = 0x010E
        FUSEVALUESA = 0x010F
        FUSEVALUESB = 0x0110
        FUSEVALUESC = 0x0111
        FUSEVALUESD = 0x0112
        I2CM0ADDRESS = 0x0113
        I2CM0CMD = 0x0114
        I2CM0CONFIG = 0x0115
        I2CM0CTRL = 0x0116
        I2CM0DATA0 = 0x0117
        I2CM0DATA1 = 0x0118
        I2CM0DATA2 = 0x0119
        I2CM0DATA3 = 0x011A
        I2CM0MASK = 0x011B
        I2CM0READ0 = 0x011C
        I2CM0READ1 = 0x011D
        I2CM0READ10 = 0x011E
        I2CM0READ11 = 0x011F
        I2CM0READ12 = 0x0120
        I2CM0READ13 = 0x0121
        I2CM0READ14 = 0x0122
        I2CM0READ15 = 0x0123
        I2CM0READ2 = 0x0124
        I2CM0READ3 = 0x0125
        I2CM0READ4 = 0x0126
        I2CM0READ5 = 0x0127
        I2CM0READ6 = 0x0128
        I2CM0READ7 = 0x0129
        I2CM0READ8 = 0x012A
        I2CM0READ9 = 0x012B
        I2CM0READBYTE = 0x012C
        I2CM0STATUS = 0x012D
        I2CM0TRANCNT = 0x012E
        I2CM1ADDRESS = 0x012F
        I2CM1CMD = 0x0130
        I2CM1CONFIG = 0x0131
        I2CM1CTRL = 0x0132
        I2CM1DATA0 = 0x0133
        I2CM1DATA1 = 0x0134
        I2CM1DATA2 = 0x0135
        I2CM1DATA3 = 0x0136
        I2CM1MASK = 0x0137
        I2CM1READ0 = 0x0138
        I2CM1READ1 = 0x0139
        I2CM1READ10 = 0x013A
        I2CM1READ11 = 0x013B
        I2CM1READ12 = 0x013C
        I2CM1READ13 = 0x013D
        I2CM1READ14 = 0x013E
        I2CM1READ15 = 0x013F
        I2CM1READ2 = 0x0140
        I2CM1READ3 = 0x0141
        I2CM1READ4 = 0x0142
        I2CM1READ5 = 0x0143
        I2CM1READ6 = 0x0144
        I2CM1READ7 = 0x0145
        I2CM1READ8 = 0x0146
        I2CM1READ9 = 0x0147
        I2CM1READBYTE = 0x0148
        I2CM1STATUS = 0x0149
        I2CM1TRANCNT = 0x014A
        I2CM2ADDRESS = 0x014B
        I2CM2CMD = 0x014C
        I2CM2CONFIG = 0x014D
        I2CM2CTRL = 0x014E
        I2CM2DATA0 = 0x014F
        I2CM2DATA1 = 0x0150
        I2CM2DATA2 = 0x0151
        I2CM2DATA3 = 0x0152
        I2CM2MASK = 0x0153
        I2CM2READ0 = 0x0154
        I2CM2READ1 = 0x0155
        I2CM2READ10 = 0x0156
        I2CM2READ11 = 0x0157
        I2CM2READ12 = 0x0158
        I2CM2READ13 = 0x0159
        I2CM2READ14 = 0x015A
        I2CM2READ15 = 0x015B
        I2CM2READ2 = 0x015C
        I2CM2READ3 = 0x015D
        I2CM2READ4 = 0x015E
        I2CM2READ5 = 0x015F
        I2CM2READ6 = 0x0160
        I2CM2READ7 = 0x0161
        I2CM2READ8 = 0x0162
        I2CM2READ9 = 0x0163
        I2CM2READBYTE = 0x0164
        I2CM2STATUS = 0x0165
        I2CM2TRANCNT = 0x0166
        I2CMTRANSADDRESS = 0x0167
        I2CMTRANSCONFIG = 0x0168
        I2CMTRANSCTRL = 0x0169
        I2CMTRANSDATA0 = 0x016A
        I2CMTRANSDATA1 = 0x016B
        I2CMTRANSDATA10 = 0x016C
        I2CMTRANSDATA11 = 0x016D
        I2CMTRANSDATA12 = 0x016E
        I2CMTRANSDATA13 = 0x016F
        I2CMTRANSDATA14 = 0x0170
        I2CMTRANSDATA15 = 0x0171
        I2CMTRANSDATA2 = 0x0172
        I2CMTRANSDATA3 = 0x0173
        I2CMTRANSDATA4 = 0x0174
        I2CMTRANSDATA5 = 0x0175
        I2CMTRANSDATA6 = 0x0176
        I2CMTRANSDATA7 = 0x0177
        I2CMTRANSDATA8 = 0x0178
        I2CMTRANSDATA9 = 0x0179
        I2CSLAVEADDRESS = 0x017A
        LDCONFIGH = 0x017B
        LDCONFIGL = 0x017C
        PGCONFIG = 0x017D
        PIODIRH = 0x017E
        PIODIRL = 0x017F
        PIODRIVESTRENGTHH = 0x0180
        PIODRIVESTRENGTHL = 0x0181
        PIOINH = 0x0182
        PIOINL = 0x0183
        PIOOUTH = 0x0184
        PIOOUTL = 0x0185
        PIOPULLENAH = 0x0186
        PIOPULLENAL = 0x0187
        PIOUPDOWNH = 0x0188
        PIOUPDOWNL = 0x0189
        PMFREQA = 0x018A
        PMFREQB = 0x018B
        PMFREQC = 0x018C
        PORBOR = 0x018D
        POWERUP0 = 0x018E
        POWERUP1 = 0x018F
        POWERUP2 = 0x0190
        POWERUP3 = 0x0191
        POWERUP4 = 0x0192
        PROCESSANDSEUMONITOR = 0x0193
        PROCESSMONITORSTATUS = 0x0194
        PS0CONFIG = 0x0195
        PS0DELAY = 0x0196
        PS0OUTDRIVER = 0x0197
        PS1CONFIG = 0x0198
        PS1DELAY = 0x0199
        PS1OUTDRIVER = 0x019A
        PS2CONFIG = 0x019B
        PS2DELAY = 0x019C
        PS2OUTDRIVER = 0x019D
        PS3CONFIG = 0x019E
        PS3DELAY = 0x019F
        PS3OUTDRIVER = 0x01A0
        PSDLLCONFIG = 0x01A1
        PSSTATUS = 0x01A2
        PUSMSTATUS = 0x01A3
        REFCLK = 0x01A4
        RESERVED1 = 0x01A5
        RESETCONFIG = 0x01A6
        ROM = 0x01A7
        RST0 = 0x01A8
        RST1 = 0x01A9
        RST2 = 0x01AA
        SCCONFIG = 0x01AB
        SCSTATUS = 0x01AC
        SEUCOUNTH = 0x01AD
        SEUCOUNTL = 0x01AE
        TEMPCALH = 0x01AF
        TEMPCALL = 0x01B0
        TO0SEL = 0x01B1
        TO1SEL = 0x01B2
        TO2SEL = 0x01B3
        TO3SEL = 0x01B4
        TO4DRIVER = 0x01B5
        TO4SEL = 0x01B6
        TO5DRIVER = 0x01B7
        TO5SEL = 0x01B8
        TODRIVINGSTRENGTH = 0x01B9
        TOPREEMP = 0x01BA
        TOVALUE = 0x01BB
        ULDATASOURCE0 = 0x01BC
        ULDATASOURCE1 = 0x01BD
        ULDATASOURCE2 = 0x01BE
        ULDATASOURCE3 = 0x01BF
        ULDATASOURCE4 = 0x01C0
        ULDATASOURCE5 = 0x01C1
        USERID0 = 0x01C2
        USERID1 = 0x01C3
        USERID2 = 0x01C4
        USERID3 = 0x01C5
        VREFCNTR = 0x01C6
