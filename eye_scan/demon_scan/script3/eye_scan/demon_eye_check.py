import numpy as np
import sys
import string
import struct
import glob
import traceback
import pyvisa
import time
import os
lib_path = os.path.dirname(os.path.abspath(__file__)) + "/.."
sys.path.append(lib_path)
from lib import peb_Mix046
from lib import lpgbt_usb

use_emphasis_vtrx = True
use_lumi = False


# instantiate lpGBT class
peb = peb_Mix046.peb(devnr = 0, gbt = 0, addr = 0x70, use_usb = True, use_serialcomm = False)
print("Timing lpGBT online.")

if(use_lumi):
    peb.lumi_add(devnr = 0, gbt = 0, addr = 0x71, use_usb = True, use_serialcomm = False)
    print("Lumi. lpGBT online.")


V_bias_current =  48  #0~127
V_modulation_enable = 1 # 0~1, always enable
V_modulation_current = 32 #0~127           
V_emphasis_amp = 0  #0~7
V_emphasis_rising_edge_enable = 0  #0~1
V_emphasis_falling_edge_enable = 0  #0~1

T_modulation_current = 40  #0~127
T_emphasis_enable = 1   #0~1, always enable
T_emphasis_short = 1    #0~1
T_emphasis_amp = 60    #0~127
   

peb.vtrxp_timing_line_driver_setup(
    bias_current = V_bias_current,
    modulation_current = V_modulation_current,
    modulation_enable = V_modulation_enable,
    emphasis_amp = V_emphasis_amp,
    emphasis_rising_edge_enable = V_emphasis_rising_edge_enable,
    emphasis_falling_edge_enable = V_emphasis_falling_edge_enable
)

peb.timing.lpgbt.line_driver_setup(
    modulation_current = T_modulation_current,
    emphasis_enable = T_emphasis_enable,
    emphasis_short = T_emphasis_short,
    emphasis_amp = T_emphasis_amp
    )


# rm = pyvisa.ResourceManager()
# Infiniium = rm.open_resource('TCPIP0::194.12.157.65::inst0::INSTR')
# Infiniium.write(":AUToscale")
