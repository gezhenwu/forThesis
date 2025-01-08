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

    peb.timing.lpgbt.vdac_setup(2500)

    # read the probe signals of front-end modules
    # for module in [9,10,11,12,13]:
    #     for chip in [0,1]:
    #         # if module == 11 and chip ==1: continue
    #         i = 0
    #         for reg_value in range(96,128):
    #             for reg in [0x1015]:
    #                 peb.module_i2c_write(
    #                     module_id = module,
    #                     chip_id = chip,
    #                     reg_address = reg,
    #                     data = reg_value
    #                 )
    #                 # temp = peb.module_i2c_read(
    #                 #     module_id = module,
    #                 #     chip_id = chip,
    #                 #     reg_address = reg,
    #                 #     read_len = 1
    #                 # )
    #                 # print('module %d chip %d REG %d: %d'%(module,chip,reg,temp[0]))            
    #             if i == 0:
    #                 for muxChannel in range ((module-4)*6,(module-4)*6+5):
    #                     peb.mux_select(channel = muxChannel)
    #                     adcChannel = 0
    #                     peb.adc_select(channel = adcChannel, inn=8, gain=0)
    #                     ADC_value = peb.adc_value(adcChannel)
    #                     if muxChannel < (module-4)*6+3:
    #                         print("Module %d asic %d Bias_No. %d muxChannel %d ADC_value %d"%(module, chip, reg_value&0b0011111,muxChannel,ADC_value))                        
    #                     if chip == 0 and muxChannel == (module-4)*6+3:
    #                         print("Module %d asic %d Bias_No. %d muxChannel %d ADC_value %d"%(module, chip, reg_value&0b0011111,muxChannel,ADC_value))
    #                     if chip == 1 and muxChannel == (module-4)*6+4:
    #                         print("Module %d asic %d Bias_No. %d muxChannel %d ADC_value %d"%(module, chip, reg_value&0b0011111,muxChannel,ADC_value))

    #             else:
    #                 if chip==0:
    #                     for muxChannel in range ((module-4)*6+3,(module-4)*6+4):
    #                         peb.mux_select(channel = muxChannel)
    #                         adcChannel = 0
    #                         peb.adc_select(channel = adcChannel, inn=8, gain=0)
    #                         ADC_value = peb.adc_value(adcChannel)
    #                         print("Module %d asic %d Bias_No. %d muxChannel %d ADC_value %d"%(module, chip, reg_value&0b0011111,muxChannel,ADC_value))
    #                 if chip==1:
    #                     for muxChannel in range ((module-4)*6+4,(module-4)*6+5):
    #                         peb.mux_select(channel = muxChannel)
    #                         adcChannel = 0
    #                         peb.adc_select(channel = adcChannel, inn=8, gain=0)
    #                         ADC_value = peb.adc_value(adcChannel)
    #                         print("Module %d asic %d Bias_No. %d muxChannel %d ADC_value %d"%(module, chip, reg_value&0b0011111,muxChannel,ADC_value))
    #             i+=1


    # read the NTC sensor of the front-end module 
    #for module in [9,10,11,12,13]:
    #    for chip in [0,1]: 
    #        for muxChannel in range ((module-4)*6+5,(module-4)*6+6):
    #            try:
    #                peb.mux_select(channel = muxChannel)
    #                adcChannel = 0
    #                peb.adc_select(channel = adcChannel, inn=15, gain=0)
    #                ADC_value = peb.adc_value(adcChannel)
    #                time.sleep(1)
    #                print("Module %d asic %d muxChannel %d ADC_value %d"%(module, chip, muxChannel,ADC_value)) 
    #            except:
    #                print("Module %d asic %d muxChannel %d ADC_value %d not pass"%(module, chip, muxChannel,ADC_value))


    for muxChannel in range (5,65,12):
        try:
            peb.mux_select(channel = muxChannel)
            adcChannel = 0
            peb.adc_select(channel = adcChannel, inn=15, gain=0)
            ADC_value = peb.adc_value(adcChannel)
            time.sleep(1)
            print("muxChannel %d ADC_value %d"%(muxChannel,ADC_value)) 
        except:
            print("muxChannel %d ADC_value %d"%(muxChannel,ADC_value)) 






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


    # # read the temperature from PEB 
    # peb.mux_select(channel = 63)
    # adcChannel = 0
    # peb.adc_select(channel = adcChannel, inn=15, gain=0)
    # ADC_value = peb.adc_value(adcChannel)
    # time.sleep(1)
    # print("PEB NTC sensor readout: %d"%ADC_value) 

    # # read the temperature from lpGBT
    # adcChannel = 14
    # peb.adc_select(channel = adcChannel, inn=15, gain=0)
    # ADC_value = peb.adc_value(adcChannel)
    # time.sleep(1)
    # print("lpGBT NTC sensor readout: %d"%ADC_value) 

    # # read the temperature from VTRX
    # adcChannel = 2
    # peb.adc_select(channel = adcChannel, inn=15, gain=0)
    # ADC_value = peb.adc_value(adcChannel)
    # time.sleep(1)
    # print("VTRX+ NTC sensor readout: %d"%ADC_value) 



try:
    main()
except:
    traceback.print_exc()
