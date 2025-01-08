# python3 configure.py -b 0 -N 50 --triggerFre 50 --pixelOn col0 --pixelInj col0 --dacCharge 24 -F ./config/altiroc/t0_forHV.yaml -d 0 -G 0 --elinkFile ./config/felix/t0_forHV.yelc --pattern Mix046 --dacVth 380


#=======================================================
# import
#=======================================================
import time
import sys,os
import numpy as np
import pandas as pd
from lib import Utils
import subprocess


# get parameters
(options, args) = Utils.getParser()

if options.gbt in range(0,3):
    from lib import altiroc3_Mix046
    altiroc3 = altiroc3_Mix046
    use_lumi = True
elif options.gbt in range(3,6):
    from lib import altiroc3_Mix230
    altiroc3 = altiroc3_Mix230
    use_lumi = False
elif options.gbt in range(6,9):
    from lib import altiroc3_Mix310
    altiroc3 = altiroc3_Mix310
    use_lumi =  False
else:
    print("Please input the elink Pattern you want to configure.")
    sys.exit()

# Config parameter
devnr = options.devnr
gbt = options.gbt
print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,gbt))
timing_addr = options.timingAddr
lumi_addr = options.LumiAddr
moduleConfigFile = options.ConfigFile
if moduleConfigFile is None:
    print("\n***No module is configured beacause no file is input.***\n")
    # sys.exit()

alti_dict = Utils.read_yaml_to_dict(moduleConfigFile)
for modules in alti_dict["Modules"]:
    module_nb = modules["module"]
    for chips in modules["chips"]:
        chip_nb = chips["chip"]
        chip_startfile = chips["startfile"]
        vth_thre = chips["vth_thre"]
        chip_vthcfile = chips["vthcfile"]
        print("Configure: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
        alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

        alti.hard_rst()
alti.byebye()