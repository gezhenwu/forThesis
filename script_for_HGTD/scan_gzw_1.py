import numbers
import os
import time
import sys
import traceback
from lib import altiroc2_Mix046
from lib import Utils

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

def main():
    if len(sys.argv) < 2:
        print ('input the value of vth')
        return 0
    else:
        vth = int(sys.argv[1])
    
    print("vth=%d is scanning"%(vth))
    for module in [6,8,9]:
        for chip in [0,1]:
            alti = altiroc2_Mix046.Altiroc2(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module, chip_id = chip)
            alti.setDacVth(vth,3)
            reg_L = alti.rd_asic_reg(0x1006,read_len=1)[0]
            reg_H = alti.rd_asic_reg(0x1007,read_len=1)[0]
            vth_value = reg_L | ((reg_H << 8) & 0x0300)
            print('module %d chip %d Finish Vth = %d'%(module,chip,vth_value))
try:
    main()
except:
    traceback.print_exc()    