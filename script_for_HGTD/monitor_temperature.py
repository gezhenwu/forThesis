# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import os
import time
import sys
import traceback
import subprocess
import math
from lib import Utils
from lib import sync_felix2lpgbt
from search_convention import read_convention

Ka = 273.15

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
pebConfigFile = options.ConfigFile
if pebConfigFile is None:
    pebConfigFile = "./config/lpGBT/ic_ec_only.yelc"
    print("\n***Use the default file to configure PEB beacause no file is input.***\n")

use_usb = False
use_fice = False
use_serialcomm = True

# Timing lpGBT pre_emphasis config
use_timing_emphasis = True
T_modulation_current = 112
T_emphasis_enable = True
T_emphasis_short = False
T_emphasis_amp = 52

# Lumi lpGBT pre_emphasis config
use_lumi_emphasis = True
L_modulation_current = 112
L_emphasis_enable = True
L_emphasis_short = False
L_emphasis_amp = 52

# VTRx+ Pre_emphasis config
use_vtrx_emphasis = False
vtrx_bias_current = 48
vtrx_modulation_current = 32
vtrx_emphasis_amp = 0
vtrx_rising_edge_enable = False
vtrx_falling_edge_enable = False

def calc_temp_vtrx(voltage):
    Rp = 1
    T2 = 25.0 + Ka
    Bx = 3500.0

    V12 = 1.2
    R0 = 10
    Vt = voltage # put the output voltage of ADC here(unit:V)

    Rt = (Vt*R0)/(V12-Vt)

    temp = 1/((1/T2)+(math.log(Rt/Rp)/Bx)) - Ka

    return temp

def calc_temp_peb(voltage):
    Rp = 10
    T2 = 25.0 + Ka
    Bx = 3435.0

    V12 = 1.2
    R0 = 100
    Vt = voltage

    Rt = (Vt*R0)/(V12-Vt)

    temp = 1/((1/T2)+(math.log(Rt/Rp)/Bx)) - Ka

    return temp

def calc_temp_altiroc(voltage):
    temp = (voltage*1000 - 640)*0.16

    return temp

def main():

    # instantiate lpGBT class
    peb = peb_1f.peb(devnr = devnr, gbt = gbt, addr = timing_addr,
        use_usb = use_usb, use_fice = use_fice, use_serialcomm = use_serialcomm)
    peb.lumi_add(devnr = devnr, gbt = gbt, addr = lumi_addr)

    # peb.timing.lpgbt.vdac_setup(2500)
    peb.timing.lpgbt.auto_tune_vref()

    ####### read out ADC channel 2(vtrx+ temp)########
    print("read out ADC channel 2")
    peb.timing.lpgbt.adc_config(inp=2, inn=15, gain=0)
    adc_value= peb.timing.lpgbt.adc_convert(1)
    calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
    temp_vtrx = calc_temp_vtrx(calibrated_v)
    print("Timing ADC input 2 : "+ str(adc_value) + " voltage: " + str(calibrated_v*1000) + "temperature: " + str(temp_vtrx))
    time.sleep(0.1)
    ###########################################

    ######### read out Mon_GND, Mon_VDDA, Mon_VDDD, NTC #######
    print("read out Mon_GND, Mon_VDDA, Mon_VDDD, NTC")
    i=0
    for module in [0,2,4,6,8,9,10,11,12,13]:
        for val in [5]:
            mux_ch = val + i*6
            peb.mux_select(channel=mux_ch)
            peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
            adc_value= peb.timing.lpgbt.adc_convert(1)
            calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
            temp_peb = calc_temp_peb(calibrated_v)
            print("channel %d module %d mux channel %d, NTC: ADC: %d, voltage: %d, temperature: %d"%(options.gbt,module,mux_ch,adc_value,calibrated_v*1000,temp_peb))
            time.sleep(0.1)
        i+=1
    ############################################################

    ##############read out 1/2 1V2_peb, MON_NTC_PEB###############
    print("read out MON_NTC_PEB")
    # peb.mux_select(channel=62)
    # peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
    # adc_value= peb.timing.lpgbt.adc_convert(1)
    # calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
    # print("Read 1/2 1V2_peb: "+str(adc_value) + " voltage: " + str(calibrated_v*1000))
    # time.sleep(0.1)
    peb.mux_select(channel=63)
    peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
    adc_value= peb.timing.lpgbt.adc_convert(1)
    calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
    temp_peb = calc_temp_peb(calibrated_v)
    print("Read TEMP from PEB: "+str(adc_value) + " voltage: " + str(calibrated_v*1000)+ " temperature: " + str(temp_peb))
    time.sleep(0.1)

    ##############read out monitor signals of front-end modules###############
    print("read out monitor signals of front-end modules")
    calibrated_vc120 = 0
    if options.gbt in range(0,3):        
        i=0
        for module in [0,2,4,6,8,9,10,11,12,13]:
        # for module in [12]:
            j=0
            for chip in [0,1]:
                k=17
                try:
                    convention = read_convention(gbt,module)
                    for reg in [0x1015]:
                        peb.module_i2c_write(
                            module_id = module,
                            chip_id = chip,
                            reg_address = reg,
                            data = 113
                        )
                    mux_ch = 3+i*6+j
                    peb.mux_select(channel=mux_ch)
                    peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
                    adc_value= peb.timing.lpgbt.adc_convert(1)
                    calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
                    temp_altiroc = calc_temp_altiroc(calibrated_v)
                    print("chanel %d module %d chip %d name %s monitor_sig %d, vtemp1: ADC: %d, voltage: %d, temperature: %d"%(options.gbt,module,chip,convention["name"],k,adc_value,calibrated_v*1000, temp_altiroc))
                except:  
                    continue        
                j+=1
            i+=1

    else:
        i=0
        for module in [0,2,4,6,8,9,10,11,12,13]:
            j=0
            for chip in [0,1]:
                k=0
                try:
                    for reg_value in range(96,128):
                        for reg in [986]:
                            peb.module_i2c_write(
                                module_id = module,
                                chip_id = chip,
                                reg_address = reg,
                                data = reg_value
                            )
                        mux_ch = 3+i*6+j
                        peb.mux_select(channel=mux_ch)
                        peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
                        adc_value= peb.timing.lpgbt.adc_convert(1)
                        calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
                        print("chanel %d module %d chip %d monitor_sig %d: ADC: %d, voltage: %d"%(options.gbt,module,chip,k,adc_value,calibrated_v*1000))
                        time.sleep(0.1)
                        k+=1
                except:
                    continue        
                j+=1
            i+=1


    peb.serialcomm.clear()
#     del peb

# ####################################################################################

try:
    main()
except:
    traceback.print_exc()
