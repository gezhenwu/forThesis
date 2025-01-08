# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import time
import sys
import traceback
from lib import Utils
from search_convention import read_convention

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
<<<<<<< HEAD
            try:            
=======
            Status = True
            try:            
                convention = read_convention(gbt,module)
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
                for reg in range(0x1000,0x1004):
                    temp = peb.module_i2c_read(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        read_len = 1
                    )
<<<<<<< HEAD
                    print('module %d chip %d Reg '%(module,chip), hex(reg), bin(temp[0]), temp[0])
=======
                    print('module %d chip %d name %s Reg '%(module,chip,convention["name"]), hex(reg), bin(temp[0]), temp[0])
                    if reg == 0x1000:
                        if temp[0] != 10: Status |= False
                    if reg == 0x1001:
                        if temp[0] != 0: Status |= False
                    if reg == 0x1002:
                        if temp[0] != 40: Status |= False
                    if reg == 0x1003:
                        if temp[0] != 36: Status |= False
                if Status == False: print("!!!!!!!!!!!!!I2C wrong number, may need configuration!!!!!!!!!!")
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
                # for reg in range(0x2000,0x2026):
                #     temp = peb.module_i2c_read(
                #         module_id = module,
                #         chip_id = chip,
                #         reg_address = reg,
                #         read_len = 1
                #     )
                #     print('module %d chip %d Reg '%(module,chip), hex(reg), bin(temp[0]), temp[0])
            except:
                print("Module %d chip %d NOT pass"%(module,chip))

    del peb

try:
    main()
except:
    traceback.print_exc()
