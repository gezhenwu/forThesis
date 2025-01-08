#!/usr/bin/env python
"""Script to compare lpGBTv0 and lpGBTv1 register maps and generate a common register map"""
# pylint: disable=anomalous-backslash-in-string

TOP = 0
REG = 1
FIELD = 2


def load_registers(fname):
    """Load registers from register map"""
    reg_map = {}
    last_reg_name = ""
    with open(fname) as fin:
        for line in fin.readlines():
            striped_line = line.rstrip()
            if striped_line.startswith("#"):
                continue
            if striped_line.lstrip().startswith("class"):
                indent = int(striped_line[: striped_line.find("class")].count(" ") / 4)
                class_name = striped_line.split()[1][:-1]
                if indent == REG:
                    if class_name == "Reg(IntEnum)":
                        break
                    last_reg_name = class_name
                    reg_map[last_reg_name] = []
                elif indent == FIELD:
                    reg_map[last_reg_name].append(class_name)
    return reg_map


def main():
    """Main function to generate common register map"""
    regmap_v0 = load_registers("lpgbt_register_map_v0.py")
    regmap_v1 = load_registers("lpgbt_register_map_v1.py")
    all_regs = set(regmap_v0.keys()) | set(regmap_v1.keys())
    identical = 0
    regmap_common = '''#!/usr/bin/env python3
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
'''
    adr_enum = "\n    @unique\n    class Reg(IntEnum):\n"
    for reg in sorted(all_regs):
        reg_in_both = reg in regmap_v0 and reg in regmap_v1
        if reg_in_both:
            fields_v0 = regmap_v0[reg]
            fields_v1 = regmap_v1[reg]

            regmap_common += "\n    class %s:\n" % reg
            regmap_common += "        address = None\n\n"

            regmap_common += "        @staticmethod\n"
            regmap_common += "        def __str__():\n"
            regmap_common += '            return ""\n\n'

            regmap_common += "        @staticmethod\n"
            regmap_common += "        def __int__():\n"
            regmap_common += "            return None\n"
            for field_name in set(fields_v0) & set(fields_v1):
                regmap_common += "\n        class %s:\n" % field_name
                regmap_common += "            offset = None\n"
                regmap_common += "            length = None\n"
                regmap_common += "            bit_mask = None\n"

                regmap_common += "\n            @staticmethod\n"
                regmap_common += "            def validate(value):\n"
                regmap_common += "                return None\n"
            adr_enum += "        %s = 0x%04X\n" % (reg, identical)
            identical += 1
        else:
            print("[%s]" % reg)
            print("    v0: %s" % (regmap_v0[reg] if reg in regmap_v0 else "-"))
            print("    v1: %s" % (regmap_v1[reg] if reg in regmap_v1 else "-"))
    print(identical, len(all_regs))
    with open("lpgbt_register_map.py", "w") as fout:
        fout.write(regmap_common)
        fout.write(adr_enum)


if __name__ == "__main__":
    main()
