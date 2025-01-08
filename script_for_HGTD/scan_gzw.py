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

    for module in [7,10]:
        print("module%d"%(module))
        os.system("fttcemu -n")
        #close all pixel
        # for pixel in range (0,225):
        #     peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 0,
        #         reg_address = (pixel*4+1),
        #         data = 0x00     #???
        #     )
        #     peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 1,
        #         reg_address = (pixel*4+1),
        #         data = 0x00     #???
        #     )
        # print("turn off all pixels")
        # #set vthc=0
        # for pixel in range (0,225):
        #     peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 0,
        #         reg_address = (pixel*4+3),
        #         data = 0x00     
        #     )
        #     peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 1,
        #         reg_address = (pixel*4+3),
        #         data = 0x00     
        #     )
        # print("set vthc = 0")
        #vth scan
        for vth in range(1,2):
            print("vth=%d is scanning"%(vth))
            peb.module_i2c_write(
            module_id = module,
            chip_id = 0,
            reg_address = 965,
            data = (vth%256)     
            )
            peb.module_i2c_write(
            module_id = module,
            chip_id = 1,
            reg_address = 965,
            data = (vth%256)     
            )
            peb.module_i2c_write(
            module_id = module,
            chip_id = 0,
            reg_address = 966,
            data = (4+vth//256)     
            )
            peb.module_i2c_write(
            module_id = module,
            chip_id = 1,
            reg_address = 966,
            data = (4+vth//256)    
            ) 

            temp = peb.module_i2c_read(
                    module_id = module,
                    chip_id = 0,
                    reg_address = 965,
                    read_len = 1     
                    )
            print("vth_965 = %d"%(temp[0]))
            os.system("fttcemu -f 100")
            time.sleep(1)
            os.system("fdaq -t 1 module%d_vth%d -T"%(module,vth))
            time.sleep(1)
            if module==7:
                os.system("fcheck module%d_vth%d-1.dat -F 1000 -e 00b >> module%d_vth%d_00b.txt"%(module,vth,module,vth))
                os.system("fcheck module%d_vth%d-1.dat -F 1000 -e 00f >> module%d_vth%d_00f.txt"%(module,vth,module,vth))
            if module==10:
                os.system("fcheck module%d_vth%d-1.dat -F 1000 -e 012 >> module%d_vth%d_012.txt"%(module,vth,module,vth))
                os.system("fcheck module%d_vth%d-1.dat -F 1000 -e 016 >> module%d_vth%d_016.txt"%(module,vth,module,vth))
            # os.system("rm *.dat")
            os.system("fttcemu -n")
            time.sleep(1)
            print("vth=%d finish scanning"%(vth))





        




        #col scan
        # for col in range(0,15):
        #     print("scan col%d: "%(col))
        #     #turn on all pixels in the current col
        #     for pixel in range (col,col+15):
        #         peb.module_i2c_write(
        #             module_id = module,
        #             chip_id = 0,
        #             reg_address = (pixel*4+1),
        #             data = 0xb0     #???
        #         )
        #         peb.module_i2c_write(
        #             module_id = module,
        #             chip_id = 1,
        #             reg_address = (pixel*4+1),
        #             data = 0xb0     #???
        #         )

        #     #vth scan
        #     for vth in range(0,1024):            
        #         peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 0,
        #         reg_address = 965,
        #         data = (vth%256)     
        #         )
        #         peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 1,
        #         reg_address = 965,
        #         data = (vth%256)     
        #         )
        #         peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 0,
        #         reg_address = 966,
        #         data = (4+vth//256)     
        #         )
        #         peb.module_i2c_write(
        #         module_id = module,
        #         chip_id = 1,
        #         reg_address = 966,
        #         data = (4+vth//256)    
        #         ) 
        #         os.system("fttcemu -f 100")
        #         time.sleep(1)
        #         os.system("fdaq -t 1 module%d_scan_col%d_vth%d -T"%(module,col,vth))
        #         time.sleep(1)
        #         if module==7:
        #             os.system("fcheck module%d_scan_col%d_vth%d-1.dat -F 1000 -e 00b >> module%d_scan_col%d_vth%d_00b.txt"%(module,col,vth,module,col,vth))
        #             os.system("fcheck module%d_scan_col%d_vth%d-1.dat -F 1000 -e 00f >> module%d_scan_col%d_vth%d_00f.txt"%(module,col,vth,module,col,vth))
        #         if module==10:
        #             os.system("fcheck module%d_scan_col%d_vth%d-1.dat -F 1000 -e 012 >> module%d_scan_col%d_vth%d_012.txt"%(module,col,vth,module,col,vth))
        #             os.system("fcheck module%d_scan_col%d_vth%d-1.dat -F 1000 -e 016 >> module%d_scan_col%d_vth%d_016.txt"%(module,col,vth,module,col,vth))
        #         # os.system("rm *.dat")
        #         os.system("fttcemu -n")
        #         time.sleep(1)


try:
    main()
except:
    traceback.print_exc()
