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
<<<<<<< HEAD
=======
        print("Reset: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
        alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

        alti.hard_rst()

for modules in alti_dict["Modules"]:
    module_nb = modules["module"]
    for chips in modules["chips"]:
        chip_nb = chips["chip"]
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
        chip_startfile = chips["startfile"]
        vth_thre = chips["vth_thre"]
        chip_vthcfile = chips["vthcfile"]
        print("Configure: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
        alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

        alti.setup(chip_startfile,chip_vthcfile,options)

        alti.setDacVth(vth_thre, options.dacVthRange)
 
        alti.setPulser(options.dacCharge)

        # alti.set_trig_latency(options.trigLatency)
 
        reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
        print ("Module%d, chip%d, Check PS locking: "%(module_nb,chip_nb),reg,bin(reg))
<<<<<<< HEAD
alti.byebye()

elinkConfigFile = options.elinkFile
if elinkConfigFile is None:
    print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
    sys.exit()
alti.felixcfg(elinkConfigFile)
alti.decode8b10b(1)
alti.idle3(3)
# alti.nIdle(options.nIdle)
# alti.nIdle(4)
alti.cmdtrigger(options.triggerFre)  # Send a given number sequence {cal + (idle)*5 + L1}
alti.cmdgbrst()


# alti.cmdtrigger(0)
# alti.byebye()
# del alti
=======
        if(reg!=127):
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PS not locked!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            alti.tune_PS()
alti.byebye()

# elinkConfigFile = options.elinkFile
# if elinkConfigFile is None:
#     print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
#     sys.exit()
# alti.felixcfg(elinkConfigFile)
# alti.decode8b10b(1)
# alti.idle3(3)
# alti.nIdle(options.nIdle)
# alti.nIdle(4)
# alti.cmdtrigger(options.triggerFre)  # Send a given number sequence {cal + (idle)*5 + L1}
# alti.cmdgbrst()

# alti.cmdtrigger(0)
# alti.byebye()
# del alti
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
