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

if options.pattern == "Mix046":
    from lib import peb_Mix046
    peb_1f = peb_Mix046
    use_lumi = True
elif options.pattern == "Mix230":
    from lib import peb_Mix230
    peb_1f = peb_Mix230
    use_lumi = False
elif options.pattern == "Mix310":
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
T_modulation_current = 115
T_emphasis_enable = True
T_emphasis_short = False
T_emphasis_amp = 65

# Lumi lpGBT pre_emphasis config
use_lumi_emphasis = True
L_modulation_current = 115
L_emphasis_enable = True
L_emphasis_short = False
L_emphasis_amp = 65

# VTRx+ Pre_emphasis config
use_vtrx_emphasis = True
vtrx_bias_current = 80
vtrx_modulation_current = 30  #85
vtrx_emphasis_amp = 7 #3
vtrx_rising_edge_enable = True
vtrx_falling_edge_enable = True


def main():

    if use_timing_emphasis:
        print("***************** Debug Info. *************************")
        # Configure the line driver when the link is unreliable
        ldconfig_h = (T_modulation_current & 0x7F) | (T_emphasis_enable << 7)
        ldconfig_l = (T_emphasis_amp & 0x7F) | (T_emphasis_short << 7)
        for x in range(2):
            subprocess.run("fice -1 -d %d -G %d -I 0x%x -a 0x3A 0x%x"%(devnr, gbt, timing_addr, ldconfig_l), shell=True)
            time.sleep(1)
            subprocess.run("fice -1 -d %d -G %d -I 0x%x -a 0x39 0x%x"%(devnr, gbt, timing_addr, ldconfig_h), shell=True)
            time.sleep(1)
        print("*******************************************************")
        print('')

    # instantiate lpGBT class
    peb = peb_1f.peb(devnr = devnr, gbt = gbt, addr = timing_addr,
        use_usb = use_usb, use_fice = use_fice, use_serialcomm = use_serialcomm)

    if use_timing_emphasis:
        peb.timing_init(modulation_current = T_modulation_current,
                        emphasis_enable = T_emphasis_enable,
                        emphasis_amp = T_emphasis_amp,
                        emphasis_short = T_emphasis_short)
    print("Timing lpGBT online.")

    if use_vtrx_emphasis:
        peb.vtrxp_timing_line_driver_setup(
            bias_current = vtrx_bias_current,
            modulation_current = vtrx_modulation_current,
            emphasis_amp = vtrx_emphasis_amp,
            emphasis_rising_edge_enable = vtrx_rising_edge_enable,
            emphasis_falling_edge_enable = vtrx_falling_edge_enable
        )

    peb.timing.lpgbt.adc_config(inp=1, inn=15, gain=0)
    print("Read RSSI from VTRx+: %d"%peb.timing.lpgbt.adc_convert(1))

    if(use_lumi):
        peb.lumi_add(devnr = devnr, gbt = gbt, addr = lumi_addr)
        if use_lumi_emphasis:        
            peb.lumi_init(modulation_current = L_modulation_current,
                            emphasis_enable = L_emphasis_enable,
                            emphasis_amp = L_emphasis_amp,
                            emphasis_short = L_emphasis_short)
        print("Lumi. lpGBT online.")
        peb.vtrxp_lumi_enable()

    sync = sync_felix2lpgbt.Sync_Elink(pebConfigFile)
    enable_timing, speed_timing = sync.module_on(0)
    enable_lumi, speed_lumi = sync.module_on(1)

    print("-----------Timing lpGBT setup-------------")
    peb.module_setup(module_id = 0, enable = enable_timing[0], reset = True, eprx_data_rate = speed_timing[0])
    peb.module_setup(module_id = 1, enable = enable_timing[1], reset = True, eprx_data_rate = speed_timing[0])
    peb.module_setup(module_id = 2, enable = enable_timing[2], reset = True, eprx_data_rate = speed_timing[0])
    peb.module_setup(module_id = 3, enable = enable_timing[3], reset = True, eprx_data_rate = speed_timing[0])
    peb.module_setup(module_id = 4, enable = enable_timing[4], reset = True, eprx_data_rate = speed_timing[1])
    peb.module_setup(module_id = 5, enable = enable_timing[5], reset = True, eprx_data_rate = speed_timing[1])
    peb.module_setup(module_id = 6, enable = enable_timing[6], reset = True, eprx_data_rate = speed_timing[1])
    peb.module_setup(module_id = 7, enable = enable_timing[7], reset = True, eprx_data_rate = speed_timing[1])
    peb.module_setup(module_id = 8, enable = enable_timing[8], reset = True, eprx_data_rate = speed_timing[2])
    peb.module_setup(module_id = 9, enable = enable_timing[9], reset = True, eprx_data_rate = speed_timing[2])
    peb.module_setup(module_id = 10, enable = enable_timing[10], reset = True, eprx_data_rate = speed_timing[2])
    peb.module_setup(module_id = 11, enable = enable_timing[11], reset = True, eprx_data_rate = speed_timing[2])
    peb.module_setup(module_id = 12, enable = enable_timing[12], reset = True, eprx_data_rate = speed_timing[3])
    peb.module_setup(module_id = 13, enable = enable_timing[13], reset = True, eprx_data_rate = speed_timing[3])

    if(use_lumi):
        print('')
        print("-----------Lumi. lpGBT setup-------------")
        peb.module_setup_lumi(module_id = 0, enable = enable_lumi[0])
        peb.module_setup_lumi(module_id = 1, enable = enable_lumi[1])
        peb.module_setup_lumi(module_id = 2, enable = enable_lumi[2])
        peb.module_setup_lumi(module_id = 3, enable = enable_lumi[3])
        peb.module_setup_lumi(module_id = 4, enable = enable_lumi[4])
        peb.module_setup_lumi(module_id = 5, enable = enable_lumi[5])
        peb.module_setup_lumi(module_id = 6, enable = enable_lumi[6])
        peb.module_setup_lumi(module_id = 7, enable = enable_lumi[7])
        peb.module_setup_lumi(module_id = 8, enable = enable_lumi[8])
        peb.module_setup_lumi(module_id = 9, enable = enable_lumi[9])
        peb.module_setup_lumi(module_id = 10, enable = enable_lumi[10])
        peb.module_setup_lumi(module_id = 11, enable = enable_lumi[11])
        peb.module_setup_lumi(module_id = 12, enable = enable_lumi[12])
        peb.module_setup_lumi(module_id = 13, enable = enable_lumi[13])

    print("Successful configuration")
    peb.serialcomm.clear()

####################################################################################

try:
    main()
except:
    traceback.print_exc()
