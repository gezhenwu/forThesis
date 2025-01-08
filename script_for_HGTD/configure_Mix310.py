#python3 configure_Mix310.py --dacChargeMax 100 --pixelOn all --pixelInj col0 --smallCtest -F ./config/altiroc/Mix310.yaml -d 0 -G 1 --elinkFile ./config/felix/fourModule.yelc

#!/usr/bin/env python3
#sudo python3 scripts/test0.py  -o ~/Measures


#=======================================================
# import
#=======================================================
import time
import sys,os
import numpy as np
import pandas as pd
from lib import altiroc3_Mix310
from lib import Utils
import subprocess


# get parameters
(options, args) = Utils.getParser()

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
        alti = altiroc3_Mix310.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

        alti.setup(chip_startfile,chip_vthcfile,options)

        alti.setDacVth(vth_thre, options.dacVthRange)
 
        alti.setPulser(options.dacCharge)

        # alti.set_trig_latency(options.trigLatency)
 
        reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
        print ("Module%d, chip%d, Check PS locking: "%(module_nb,chip_nb),reg,bin(reg))
alti.byebye()

# elinkConfigFile = options.elinkFile
# if elinkConfigFile is None:
#     print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
#     sys.exit()
# alti.felixcfg(elinkConfigFile)
# alti.decode8b10b(1)
# alti.idle3(3)
# # alti.nIdle(options.nIdle)
# alti.nIdle(4)
# alti.cmdtrigger(options.triggerFre)  # Send a given number sequence {cal + (idle)*5 + L1}
# alti.cmdgbrst()


# # alti.cmdtrigger(0)
# alti.byebye()
del alti