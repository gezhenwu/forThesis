# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import os
import time
import sys
import traceback
import subprocess
from lib import Utils
from lib import sync_felix2lpgbt

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


def main():

    # instantiate lpGBT class
    peb = peb_1f.peb(devnr = devnr, gbt = gbt, addr = timing_addr,
        use_usb = use_usb, use_fice = use_fice, use_serialcomm = use_serialcomm)

    print(peb.timing.lpgbt.estimate_temperature_uncalib_vref()) 
    peb.timing.lpgbt.auto_tune_vref() 


    peb.timing.lpgbt.adc_config(inp=1, inn=15, gain=0)
    print("Read RSSI from VTRx+: %d"%peb.timing.lpgbt.adc_convert(1))
    print("Read RSSI from VTRx+: ",peb.timing.lpgbt.adc_get_vin())
    time.sleep(0.1)
    peb.timing.lpgbt.adc_config(inp=2, inn=15, gain=0)
    print("Read TEMP from VTRx+: %d"%peb.timing.lpgbt.adc_convert(1))
    print("Read RSSI from VTRx+: ",peb.timing.lpgbt.adc_get_vin())
    time.sleep(0.1)
    peb.mux_select(channel=63)
    peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
    print("Read TEMP from PEB: %d"%peb.timing.lpgbt.adc_convert(1))
    print("Read RSSI from VTRx+: ",peb.timing.lpgbt.adc_get_vin())
    time.sleep(0.1)
    peb.timing.lpgbt.adc_config(inp=14, inn=15, gain=0)
    print("Read TEMP from lpGBT: %d"%peb.timing.lpgbt.adc_convert(1))
    print("Read RSSI from VTRx+: ",peb.timing.lpgbt.adc_get_vin())

    peb.serialcomm.clear()
    del peb

####################################################################################

try:
    main()
except:
    traceback.print_exc()
