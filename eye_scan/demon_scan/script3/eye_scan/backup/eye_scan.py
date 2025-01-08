import numpy as np
import sys
from datetime import datetime as dt
import glob
import traceback
import pyvisa
import math
import time
# import serial
import threading
import os
lib_path = os.path.dirname(os.path.abspath(__file__)) + "/.."
sys.path.append(lib_path)
from lib import peb_Mix046
from lib import lpgbt_usb

use_emphasis_vtrx = True
use_lumi = False

##########################################################
def checkSaveFileName(basefname):
    fname = basefname
    i = 2
    while len(glob.glob(fname)) > 0:
        fname = "%s_%g"%(basefname, i)
        i = i + 1
    if i != 2:
        print ("saved file %s"%fname)
    return fname
##########################################################

def main():

    if len(sys.argv) < 2:
        print ('input file name')
        return 0
    else:
        basefname = sys.argv[1]

    # instantiate lpGBT class
    peb = peb_Mix046.peb(devnr = 0, gbt = 0, addr = 0x70, use_usb = True)
    print("Timing lpGBT online.")

    if(use_lumi):
        peb.lumi_add(devnr = 0, gbt = 0, addr = 0x71, use_usb = True)
        print("Lumi. lpGBT online.")

    # check output file duplicate
    fname = checkSaveFileName('./output/'+basefname)

    rm = pyvisa.ResourceManager()

    e36200 = rm.open_resource('TCPIP0::192.168.10.19::inst0::INSTR')
    print(e36200.query("*IDN?"), end="")
    volt_out = 11.0
    current_limit = 2.0    
    e36200.write('VOLT %.3f, (@%d)'%(volt_out, 1))
    e36200.write('CURR %.3f, (@%d)'%(current_limit, 1))
    print('CH%d: volt_set = %.3f, curr_limit = %.3f'%(1, volt_out, current_limit))
    e36200.write('OUTP 1, (@%d)'%(1))
    e36200.write('SYST:BEEP')  

    SDA820 = rm.open_resource('TCPIP0::192.168.1.119::inst0::INSTR')
    print(SDA820.query("*IDN?"), end="")

    SDA820.timeout = 5000
    SDA820.clear()
    SDA820.write("COMM_HEADER OFF")
    # SDA820.write(r"""vbs 'app.settodefaultsetup' """)

    r = SDA820.query(r"""vbs? 'return=app.WaitUntilIdle(0.1)' """)
    SDA820.write(r"""vbs 'app.acquisition.triggermode = "auto" ' """)

    SDA820.write(r"""vbs 'app.HardCopy.Destination = "File" ' """)
    SDA820.write(r"""vbs 'app.HardCopy.EnableCounterSuffix = 1' """)
    SDA820.write(r"""vbs 'app.HardCopy.GridAreaOnly = 1 ' """)
    SDA820.write(r"""vbs 'app.HardCopy.HardcopyArea = "GridAreaOnly" ' """)
    SDA820.write(r"""vbs 'app.HardCopy.HardcopyAreaToFile = "GridAreaOnly" ' """)
    SDA820.write(r"""vbs 'app.HardCopy.ImageFileFormat = "PNG" ' """)
    SDA820.write(r"""vbs 'app.HardCopy.Directory = "D:\HardCopy\" ' """)
    SDA820.write(r"""vbs 'app.Acquisition.Horizontal.HorScale = 0.000010 ' """)
    SDA820.write(r"""vbs 'app.HardCopy.PreferredFilename = "T_seven" ' """)
    time.sleep(10)
    SDA820.query(r"""vbs? 'app.HardCopy.Print' """)

    # # Send Oscilloscope Commands to Configure Screen Image Format
    # SDA820.write("HCSU DEV, JPEG, AREA, DSOWINDOW, PORT, NET")
    # SDA820.write("SCDP")
    
    i=0
    alldata = []

    for V_bias_current in range (80,81):
        for V_modulation_enable in range (1,2):# always enable
            for V_modulation_current in range (85,86):            
                for V_emphasis_amp in range (3,4):
                    for V_emphasis_rising_edge_enable in range (1,2):
                        for V_emphasis_falling_edge_enable in range (1,2):

                            for T_modulation_current in range (47,128,5):
                                for T_emphasis_enable in range (1,2):# always enable
                                    for T_emphasis_short in range (0,2):
                                        for T_emphasis_amp in range (20,101,5):

                                            Success = 1
                                            try:
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
                                            except:
                                                Success = 0
                                                e36200.write('OUTP 0, (@%d)'%(1))
                                                e36200.write('SYST:BEEP')
                                                time.sleep(1)
                                                e36200.write('VOLT %.3f, (@%d)'%(volt_out, 1))
                                                e36200.write('CURR %.3f, (@%d)'%(current_limit, 1))
                                                print('CH%d: volt_set = %.3f, curr_limit = %.3f'%(1, volt_out, current_limit))
                                                e36200.write('OUTP 1, (@%d)'%(1))
                                                e36200.write('SYST:BEEP')
                                                time.sleep(1)

                                            i = i+1
                                            if i>=0:
                                                print(i)
                                                print(V_bias_current,V_modulation_current,V_emphasis_amp,T_modulation_current,T_emphasis_short,T_emphasis_amp,Success)  

                                            # SDA820.write(r"""vbs 'app.Acquisition.Horizontal.HorScale = 0.000002 ' """)
                                            # SDA820.write(r"""vbs 'app.Acquisition.Horizontal.HorScale = 0.000010 ' """)

                                            SDA820.write(r"""vbs 'app.measure.clearall ' """)
                                            SDA820.write(r"""vbs 'app.measure.clearsweeps ' """)
                                            

                                            time.sleep(5)
                                            try:
                                                EyeAmpl = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeAmpl.Out.result.value' """))
                                            except:
                                                EyeAmpl = 999
                                                
                                            try:
                                                EyeAvgPwr = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeAvgPwr.Out.result.value' """))
                                            except:
                                                EyeAvgPwr = 999
                                                
                                            try:
                                                EyeBER = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeBER.Out.result.value' """))
                                            except:
                                                EyeBER = 999
                                                
                                            try:
                                                EyeCross = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeCross.Out.result.value' """))
                                            except:
                                                EyeCross = 999
                                                
                                            try:
                                                EyeER = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeER.Out.result.value' """))
                                            except:
                                                EyeER = 999
                                                
                                            try:
                                                EyeHeight = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeHeight.Out.result.value' """))
                                            except:
                                                EyeHeight = 999
                                                
                                            try:
                                                EyeOne = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeOne.Out.result.value' """))
                                            except:
                                                EyeOne = 999
                                                
                                            try:
                                                EyeWidth = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeWidth.Out.result.value' """))
                                            except:
                                                EyeWidth = 999
                                                
                                            try:
                                                EyeZero = eval(SDA820.query(r"""vbs? 'return=app.SDA2.EyeMeasure.Parameters.EyeZero.Out.result.value' """))
                                            except:
                                                EyeZero = 999

                                            if i>=0:    
                                                SDA820.query(r"""vbs? 'app.HardCopy.Print' """)

                                            # # Read the Binary Data
                                            # screen_data = SDA820.read_raw()
                                            # # Save the Binary Data Locally
                                            # f = open("ScreenImage.jpg", 'wb+')
                                            # f.write(screen_data)
                                            # f.close()

                                            alldata.append([i, V_bias_current, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_short, T_emphasis_amp, EyeAmpl, EyeAvgPwr, EyeBER, EyeCross, EyeER, EyeHeight, EyeOne, EyeWidth, EyeZero,Success])

                                            # print(alldata)

    if i>=0:
        head = "ATLAS HGTD BERT test\n\
        Data file made from SDA 820Zi-B\n\
        Created at %s UTC\n\
        No., V_bias_current, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_short, T_emphasis_amp, EyeAmpl, EyeAvgPwr/W, EyeBER, EyeCross, EyeER, EyeHeight/W, EyeOne/w, EyeWidth/s, EyeZero/W, Success" %(
        time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        # print(head)
        # fname_new = fname+str(time.time())
        fname_new = fname+str(i)+".csv"
        np.savetxt(fname_new, alldata, delimiter=',', header=head)

    SDA820.close()
    rm.close()

try:
  main()
except:
  traceback.print_exc()