import numbers
import os
import time
import sys
import traceback
from lib import modular_peb

I2C_ID_LUMI     = 1
I2C_ADDR_LUMI   = 0x71


#initial emulator7 and digital module10
#turn on all pixels and set vth=0, vthc=0
#set ALTIROC K-Char
#disable TTC
# os.system("bash scan.sh")
def main():
    peb = modular_peb.modular_peb()

    if len(sys.argv) < 2:
        print ('input the value of vth')
        return 0
    else:
        vth = int(sys.argv[1])
    
    print("vth=%d is scanning"%(vth))
    for modu in range (5,11):        
        peb.module_i2c_write(
        module_id = modu,
        chip_id = 0,
        reg_address = 965,
        data = (vth%256)     
        )
        peb.module_i2c_write(
        module_id = modu,
        chip_id = 1,
        reg_address = 965,
        data = (vth%256)     
        )
        peb.module_i2c_write(
        module_id = modu,
        chip_id = 0,
        reg_address = 966,
        data = (4+vth//256)     
        )
        peb.module_i2c_write(
        module_id = modu,
        chip_id = 1,
        reg_address = 966,
        data = (4+vth//256)    
        ) 

try:
    main()
except:
    traceback.print_exc()    