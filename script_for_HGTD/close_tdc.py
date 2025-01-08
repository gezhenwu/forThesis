# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import time
import sys
import traceback
from lib import Utils

(options, args) = Utils.getParser()

if options.gbt in range(0,3):
    from lib import peb_Mix046
    peb_1f = peb_Mix046
    use_lumi = True
elif options.gbt in range(3,6):
    from lib import peb_Mix230
    peb_1f = peb_Mix230
    use_lumi = False
elif options.gbt in range(6,9):
    from lib import peb_Mix310
    peb_1f = peb_Mix310
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

def main():
    # instantiate lpGBT class
    peb = peb_1f.peb(devnr = devnr,gbt = gbt, addr = timing_addr)
    peb.lumi_add(devnr = devnr, gbt = gbt, addr = lumi_addr)
                    

    for module in [0,2,4,6,8,9,10,11,12,13]:
    # for module in [9]:
        for chip in range(0,2):
            try:         
                for reg in [0x2011]:
                    temp = peb.module_i2c_write(
                        module_id = module,
                        chip_id = chip,
                        reg_address = 0x2011,
                        # data = (0b01110110)
                        data = (0b01000111)
                    ) 
                    print("module %d, chip %d, TDC on"%(module,chip))
            except:
                continue

    del peb

try:
    main()
except:
    traceback.print_exc()
