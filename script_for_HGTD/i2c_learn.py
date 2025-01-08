# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import time
import sys
import traceback
from lib import peb_Mix046
from lib import Utils

(options, args) = Utils.getParser()

# Config parameter
devnr = options.devnr
gbt = options.gbt
print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,gbt))
timing_addr = options.timingAddr
lumi_addr = options.LumiAddr

def main():
    # instantiate lpGBT class
    peb = peb_Mix046.peb(devnr = devnr,gbt = gbt, addr = timing_addr)
    peb.lumi_add(devnr = devnr, gbt = gbt, addr = lumi_addr)
                    
    # for muxChannel in range (0,64):        
    #     peb.mux_select(channel = muxChannel)
    #     adcChannel = 0
    #     peb.adc_select(channel = adcChannel, inn=15, gain=0)
    #     print("muxChannel %d: %d"%(muxChannel,peb.adc_value(adcChannel)))


    # peb.adc_select(channel=1, inn=15, gain=0)
    # print("Read RSSI from VTRx+: %d"%peb.adc_value(1))
    # peb.adc_select(channel=2, inn=15, gain=0)
    # print("Read VTRX_TEMP from VTRx+: %d"%peb.adc_value(2))
    # peb.adc_select(channel=3, inn=15, gain=0)
    # print("MON_12V0: %d"%peb.adc_value(3))
    # peb.adc_select(channel=4, inn=15, gain=0)
    # print("MON_1V2_neighbour: %d"%peb.adc_value(4))
    # peb.adc_select(channel=5, inn=15, gain=0)
    # print("MON_2V5_neighbour: %d"%peb.adc_value(5))
    # peb.adc_select(channel=6, inn=15, gain=0)
    # print("MON_T0/1/2_PT_1V2: %d"%peb.adc_value(6))
    # peb.adc_select(channel=7, inn=15, gain=0)
    # print("MON_T0/1/2_PT_2V5: %d"%peb.adc_value(7))
    # peb.adc_select(channel=16, inn=15, gain=0)
    # print("PTA_G0: %d"%peb.adc_value(16))
    # peb.adc_select(channel=17, inn=15, gain=0)
    # print("PTD_G0: %d"%peb.adc_value(17))
    # peb.adc_select(channel=18, inn=15, gain=0)
    # print("PTA_G1: %d"%peb.adc_value(18))
    # peb.adc_select(channel=19, inn=15, gain=0)
    # print("PTD_G1: %d"%peb.adc_value(19))
    # peb.adc_select(channel=20, inn=15, gain=0)
    # print("PTA_G2: %d"%peb.adc_value(20))
    # peb.adc_select(channel=21, inn=15, gain=0)
    # print("PTD_G2: %d"%peb.adc_value(21))
    # peb.adc_select(channel=22, inn=15, gain=0)
    # print("PTA_G3: %d"%peb.adc_value(22))
    # peb.adc_select(channel=23, inn=15, gain=0)
    # print("PTD_G3: %d"%peb.adc_value(23))    
#####################################################
    for module in [9,10,11,12,13]:
        for chip in range(0,2):
            #Timing
            if module < 7:
                for reg in range(914,915):
                    peb.module_i2c_write(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        data = 50
                    )
                    temp = peb.module_i2c_read(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        read_len = 1
                    )
                    print('module %d chip %d REG %d: %d'%(module,chip,reg,temp[0]))
            else:
                for reg in range(914,915):
                    peb.module_i2c_write(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        data = 49
                    )
                    temp = peb.module_i2c_read(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        read_len = 1
                    )
                    print('module %d chip %d REG %d: %d'%(module,chip,reg,temp[0]))
            # #Lumi
            # if module < 5:
            #     for reg in range(908,909):
            #         peb.module_i2c_write(
            #             module_id = module,
            #             chip_id = chip,
            #             reg_address = reg,
            #             data = 10
            #         )
            #         temp = peb.module_i2c_read(
            #             module_id = module,
            #             chip_id = chip,
            #             reg_address = reg,
            #             read_len = 1
            #         )
            #         print('module %d chip %d REG %d: %d'%(module,chip,reg,temp[0]))
            # else:
            #     for reg in range(908,909):
            #         peb.module_i2c_write(
            #             module_id = module,
            #             chip_id = chip,
            #             reg_address = reg,
            #             data = 11
            #         )
            #         temp = peb.module_i2c_read(
            #             module_id = module,
            #             chip_id = chip,
            #             reg_address = reg,
            #             read_len = 1
            #         )
            #         print('module %d chip %d REG %d: %d'%(module,chip,reg,temp[0]))    
#####################################################
try:
    main()
except:
    traceback.print_exc()