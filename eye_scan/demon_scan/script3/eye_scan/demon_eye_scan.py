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

# Global variables (booleans: 0 = False, 1 = True).
# ---------------------------------------------------------
debug = 0
# =========================================================
# Initialize:
# =========================================================
def initialize():
    # Clear status.
    do_command("*CLS")
    # Get and display the device's *IDN? string.
    idn_string = do_query_string("*IDN?")
    print("Identification string: '%s'" % idn_string)
    # Load the default setup.
    do_command("*RST")
# =========================================================
# Capture:
# =========================================================
def capture():
    # Set probe attenuation factor.
    do_command(":CHANnel1:PROBe 1.0")
    qresult = do_query_string(":CHANnel1:PROBe?")
    print("Channel 1 probe attenuation factor: %s" % qresult)
    # Use auto-scale to automatically set up oscilloscope.
    print("Autoscale.")
    do_command(":AUToscale")
    # Set trigger mode.
    do_command(":TRIGger:MODE EDGE")
    qresult = do_query_string(":TRIGger:MODE?")
    print("Trigger mode: %s" % qresult)
    # Set EDGE trigger parameters.
    do_command(":TRIGger:EDGE:SOURce CHANnel1")
    qresult = do_query_string(":TRIGger:EDGE:SOURce?")
    print("Trigger edge source: %s" % qresult)
    do_command(":TRIGger:LEVel CHANnel1,330E-3")
    qresult = do_query_string(":TRIGger:LEVel? CHANnel1")
    print("Trigger level, channel 1: %s" % qresult)
    do_command(":TRIGger:EDGE:SLOPe POSitive")
    qresult = do_query_string(":TRIGger:EDGE:SLOPe?")
    print("Trigger edge slope: %s" % qresult)
    # Save oscilloscope setup.
    setup_bytes = do_query_ieee_block(":SYSTem:SETup?")
    f = open("setup.set", "wb")
    f.write(setup_bytes)
    f.close()
    print("Setup bytes saved: %d" % len(setup_bytes))
    # Change oscilloscope settings with individual commands:
    # Set vertical scale and offset.
    do_command(":CHANnel1:SCALe 0.1")
    qresult = do_query_number(":CHANnel1:SCALe?")
    print("Channel 1 vertical scale: %f" % qresult)
    do_command(":CHANnel1:OFFSet 0.0")
    qresult = do_query_number(":CHANnel1:OFFSet?")
    print("Channel 1 offset: %f" % qresult)
    # Set horizontal scale and offset.
    do_command(":TIMebase:SCALe 200e-6")
    qresult = do_query_string(":TIMebase:SCALe?")
    print("Timebase scale: %s" % qresult)
    do_command(":TIMebase:POSition 0.0")
    qresult = do_query_string(":TIMebase:POSition?")
    print("Timebase position: %s" % qresult)
    # Set the acquisition mode.
    do_command(":ACQuire:MODE RTIMe")
    qresult = do_query_string(":ACQuire:MODE?")
    print("Acquire mode: %s" % qresult)
    # Or, set up oscilloscope by loading a previously saved setup.
    setup_bytes = ""
    f = open("setup.set", "rb")
    setup_bytes = f.read()
    f.close()
    do_command_ieee_block(":SYSTem:SETup", setup_bytes)
    print("Setup bytes restored: %d" % len(setup_bytes))
    # Set the desired number of waveform points,
    # and capture an acquisition.
    do_command(":ACQuire:POINts 32000")
    do_command(":DIGitize")
# =========================================================
# Analyze:
# =========================================================
def analyze():
    # Make measurements.
    # --------------------------------------------------------
    do_command(":MEASure:SOURce CHANnel1")
    qresult = do_query_string(":MEASure:SOURce?")
    print("Measure source: %s" % qresult)
    do_command(":MEASure:FREQuency")
    qresult = do_query_string(":MEASure:FREQuency?")
    print("Measured frequency on channel 1: %s" % qresult)
    do_command(":MEASure:VAMPlitude")
    qresult = do_query_string(":MEASure:VAMPlitude?")
    print("Measured vertical amplitude on channel 1: %s" % qresult)
    # Download the screen image.
    # --------------------------------------------------------
    screen_bytes = do_query_ieee_block(":DISPlay:DATA? PNG")
    # Save display data values to file.
    f = open("screen_image.png", "wb")
    f.write(screen_bytes)
    f.close()
    print("Screen image written to screen_image.png.")
    # Download waveform data.
    # --------------------------------------------------------
    # Get the waveform type.
    qresult = do_query_string(":WAVeform:TYPE?")
    print("Waveform type: %s" % qresult)
    # Get the number of waveform points.
    qresult = do_query_string(":WAVeform:POINts?")
    print("Waveform points: %s" % qresult)
    # Set the waveform source.
    do_command(":WAVeform:SOURce CHANnel1")
    qresult = do_query_string(":WAVeform:SOURce?")
    print("Waveform source: %s" % qresult)
    # Choose the format of the data returned:
    do_command(":WAVeform:FORMat BYTE")
    print("Waveform format: %s" % do_query_string(":WAVeform:FORMat?"))
    # Display the waveform settings from preamble:
    wav_form_dict = {
    0 : "ASCii",
    1 : "BYTE",
    2 : "WORD",
    3 : "LONG",
    4 : "LONGLONG",
    }
    acq_type_dict = {
    1 : "RAW",
    2 : "AVERage",
    3 : "VHIStogram",
    4 : "HHIStogram",
    6 : "INTerpolate",
    10 : "PDETect",
    }
    acq_mode_dict = {
    0 : "RTIMe",
    1 : "ETIMe",
    3 : "PDETect",
    }
    coupling_dict = {
    0 : "AC",
    1 : "DC",
    2 : "DCFIFTY",
    3 : "LFREJECT",
    }
    units_dict = {
    0 : "UNKNOWN",
    1 : "VOLT",
    2 : "SECOND",
    3 : "CONSTANT",
    4 : "AMP",
    5 : "DECIBEL",
    }
    preamble_string = do_query_string(":WAVeform:PREamble?")
    (
    wav_form, acq_type, wfmpts, avgcnt, x_increment, x_origin,
    x_reference, y_increment, y_origin, y_reference, coupling,
    x_display_range, x_display_origin, y_display_range,
    y_display_origin, date, time, frame_model, acq_mode,
    completion, x_units, y_units, max_bw_limit, min_bw_limit
    ) = preamble_string.split(",")
    print("Waveform format: %s" % wav_form_dict[int(wav_form)])
    print("Acquire type: %s" % acq_type_dict[int(acq_type)])
    print("Waveform points desired: %s" % wfmpts)
    print("Waveform average count: %s" % avgcnt)
    print("Waveform X increment: %s" % x_increment)
    print("Waveform X origin: %s" % x_origin)
    print("Waveform X reference: %s" % x_reference) # Always 0.
    print("Waveform Y increment: %s" % y_increment)
    print("Waveform Y origin: %s" % y_origin)
    print("Waveform Y reference: %s" % y_reference) # Always 0.
    print("Coupling: %s" % coupling_dict[int(coupling)])
    print("Waveform X display range: %s" % x_display_range)
    print("Waveform X display origin: %s" % x_display_origin)
    print("Waveform Y display range: %s" % y_display_range)
    print("Waveform Y display origin: %s" % y_display_origin)
    print("Date: %s" % date)
    print("Time: %s" % time)
    print("Frame model #: %s" % frame_model)
    print("Acquire mode: %s" % acq_mode_dict[int(acq_mode)])
    print("Completion pct: %s" % completion)
    print("Waveform X units: %s" % units_dict[int(x_units)])
    print("Waveform Y units: %s" % units_dict[int(y_units)])
    print("Max BW limit: %s" % max_bw_limit)
    print("Min BW limit: %s" % min_bw_limit)
    # Get numeric values for later calculations.
    x_increment = do_query_number(":WAVeform:XINCrement?")
    x_origin = do_query_number(":WAVeform:XORigin?")
    y_increment = do_query_number(":WAVeform:YINCrement?")
    y_origin = do_query_number(":WAVeform:YORigin?")
    # Get the waveform data.
    do_command(":WAVeform:STReaming OFF")
    sData = do_query_ieee_block(":WAVeform:DATA?")
    # Unpack signed byte data.
    values = struct.unpack("%db" % len(sData), sData)
    print("Number of data values: %d" % len(values))
    # Save waveform data values to CSV file.
    f = open("waveform_data.csv", "w")
    for i in range(0, len(values) - 1):
        time_val = x_origin + (i * x_increment)
        voltage = (values[i] * y_increment) + y_origin
        f.write("%E, %f\n" % (time_val, voltage))
    f.close()
    print("Waveform format BYTE data written to waveform_data.csv.")
# =========================================================
# Send a command and check for errors:
# =========================================================
def do_command(command, hide_params=False):
    if hide_params:
        (header, data) = command.split(" ", 1)
        if debug:
            print("\nCmd = '%s'" % header)
    else:
        if debug:
            print("\nCmd = '%s'" % command)
    Infiniium.write("%s" % command)
    if hide_params:
        check_instrument_errors(header)
    else:
        check_instrument_errors(command)
# =========================================================
# Send a command and binary values and check for errors:
# =========================================================
def do_command_ieee_block(command, values):
    if debug:
        print("Cmb = '%s'" % command)
    Infiniium.write_binary_values("%s " % command, values, datatype='B')
    check_instrument_errors(command)
# =========================================================
# Send a query, check for errors, return string:
# =========================================================
def do_query_string(query):
    if debug:
        print("Qys = '%s'" % query)
    result = Infiniium.query("%s" % query)
    check_instrument_errors(query)
    return result
# =========================================================
# Send a query, check for errors, return floating-point value:
# =========================================================
def do_query_number(query):
    if debug:
        print("Qyn = '%s'" % query)
    results = Infiniium.query("%s" % query)
    check_instrument_errors(query)
    return float(results)
# =========================================================
# Send a query, check for errors, return binary values:
# =========================================================
def do_query_ieee_block(query):
    if debug:
        print("Qyb = '%s'" % query)
    result = Infiniium.query_binary_values("%s" % query, datatype='s', container=bytes)
    check_instrument_errors(query, exit_on_error=False)
    return result
# =========================================================
# Check for instrument errors:
# =========================================================
def check_instrument_errors(command, exit_on_error=True):
    while True:
        error_string = Infiniium.query(":SYSTem:ERRor? STRing")
        if error_string: # If there is an error string value.
            if error_string.find("0,", 0, 2) == -1: # Not "No error".
                print("ERROR: %s, command: '%s'" % (error_string, command))
                if exit_on_error:
                    print("Exited because of error.")
                    sys.exit(1)
            else: # "No error"
                break
        else: # :SYSTem:ERRor? STRing should always return string.
            print("ERROR: :SYSTem:ERRor? STRing returned nothing, command: '%s'"%command)
            print("Exited because of error.")
            sys.exit(1)


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

# def main():

if len(sys.argv) < 2:
    print ('input file name')
    sys.exit()
else:
    basefname = sys.argv[1]

screenDir = "output/"+basefname+"/"+basefname+"_"

# instantiate lpGBT class
peb = peb_Mix046.peb(devnr = 0, gbt = 0, addr = 0x70, use_usb = True, use_serialcomm = False)
print("Timing lpGBT online.")

# check output file duplicate
fname = checkSaveFileName('./output/'+basefname)

rm = pyvisa.ResourceManager()

# e36200 = rm.open_resource('TCPIP0::192.168.10.19::inst0::INSTR')
# print(e36200.query("*IDN?"), end="")
# volt_out = 11.0
# current_limit = 2.0    
# e36200.write('VOLT %.3f, (@%d)'%(volt_out, 1))
# e36200.write('CURR %.3f, (@%d)'%(current_limit, 1))
# print('CH%d: volt_set = %.3f, curr_limit = %.3f'%(1, volt_out, current_limit))
# e36200.write('OUTP 1, (@%d)'%(1))
# e36200.write('SYST:BEEP')  

Infiniium = rm.open_resource('TCPIP0::194.12.157.190::inst0::INSTR')
Infiniium.timeout = 20000
Infiniium.clear()
# Clear status.
do_command("*CLS")
# Get and display the device's *IDN? string.
idn_string = do_query_string("*IDN?")
print("Identification string: '%s'" % idn_string)
# Load the default setup.
do_command("*RST")

# set up oscilloscope by loading a previously saved setup.
setup_bytes = ""
f = open("hgtd-eye.set", "rb")
setup_bytes = f.read()
f.close()
do_command_ieee_block(":SYSTem:SETup", setup_bytes)
print("Setup bytes restored: %d" % len(setup_bytes))
do_command(":AUToscale")
# Set the desired number of waveform points,
# and capture an acquisition.
# do_command(":ACQuire:POINts 32000")
# do_command(":DIGitize")

# seutup
# Infiniium.write(":DISPlay:CGRade ON")
# Infiniium.write(":DISPlay:CGRade:SCHeme CLASsic")
# Infiniium.write(":MTESt:FOLDing ON")
# Infiniium.write(":MTESt:FOLDing:POSition -0.000")
# Infiniium.write(":MTESt:FOLDing:SCALe 2.0")
# Infiniium.write(":SYSTem:HEADer OFF") #' Response headers off.

# measurement
do_command(":MEASure:SOURce CHANnel1")

time.sleep(2)

# Download the screen image.
screen_bytes = do_query_ieee_block(":DISPlay:DATA? PNG")
# Save display data values to file.
f = open(screenDir+"0.png", "wb")
f.write(screen_bytes)
f.close()

i=0
alldata = []

try:
    for V_bias_current in range (48,49,5):    #0~127
        for V_modulation_enable in range (1,2): # 0~1, always enable
            for V_modulation_current in range (32,33,5):  #0~127           
                for V_emphasis_amp in range (0,1):  #0~7
                    for V_emphasis_rising_edge_enable in range (0,1):   #0~1
                        for V_emphasis_falling_edge_enable in range (0,1):  #0~1

                            for T_modulation_current in range (2,127,5):  #0~127
                                for T_emphasis_enable in range (1,2):   #0~1, always enable
                                    for T_emphasis_short in range (0,2):    #0~1
                                        for T_emphasis_amp in range (0,127,5):    #0~127

                                            Success = 1
                                            try:
                                                # peb.vtrxp_timing_line_driver_setup(
                                                #     bias_current = V_bias_current,
                                                #     modulation_current = V_modulation_current,
                                                #     modulation_enable = V_modulation_enable,
                                                #     emphasis_amp = V_emphasis_amp,
                                                #     emphasis_rising_edge_enable = V_emphasis_rising_edge_enable,
                                                #     emphasis_falling_edge_enable = V_emphasis_falling_edge_enable
                                                # )

                                                peb.timing.lpgbt.line_driver_setup(
                                                        modulation_current = T_modulation_current,
                                                        emphasis_enable = T_emphasis_enable,
                                                        emphasis_short = T_emphasis_short,
                                                        emphasis_amp = T_emphasis_amp
                                                    )
                                            except:
                                                Success = 0
                                                # e36200.write('OUTP 0, (@%d)'%(1))
                                                # e36200.write('SYST:BEEP')
                                                # time.sleep(1)
                                                # e36200.write('VOLT %.3f, (@%d)'%(volt_out, 1))
                                                # e36200.write('CURR %.3f, (@%d)'%(current_limit, 1))
                                                # print('CH%d: volt_set = %.3f, curr_limit = %.3f'%(1, volt_out, current_limit))
                                                # e36200.write('OUTP 1, (@%d)'%(1))
                                                # e36200.write('SYST:BEEP')
                                                # time.sleep(1)

                                            i = i+1
                                            if i>=0:
                                                print(i, V_bias_current, V_modulation_enable, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_enable, T_emphasis_short, T_emphasis_amp, Success)  

                                            # SDA820.write(r"""vbs 'app.Acquisition.Horizontal.HorScale = 0.000002 ' """)
                                            # SDA820.write(r"""vbs 'app.Acquisition.Horizontal.HorScale = 0.000010 ' """)

                                            # Infiniium.clear()  
                                            # do_command("*CLS")

                                            do_command(":AUToscale")

                                            # Set horizontal scale and offset.
                                            do_command(":TIMebase:SCALe 1.0e-7")
                                            do_command(":TIMebase:SCALe 2.0e-7")

                                            # if i%1001 == 1000:
                                            #     # set up oscilloscope by loading a previously saved setup.
                                            #     setup_bytes = ""
                                            #     f = open("hgtd-eye.set", "rb")
                                            #     setup_bytes = f.read()
                                            #     f.close()
                                            #     do_command_ieee_block(":SYSTem:SETup", setup_bytes)
                                            #     print("Setup bytes restored: %d" % len(setup_bytes))    

                                            #     do_command(":AUToscale")

                                            time.sleep(2)  

                                            # try:
                                            #     Infiniium.write(":MEASure:CGRade:DCDistortion TIME")
                                            #     DCDistortion = eval(Infiniium.query(":MEASure:CGRade:DCDistortion? PERCent"))
                                            # except:
                                            #     JDCDistortion = 999
                                                
                                            # try:
                                            #     Infiniium.write(":MEASure:CGRade:CROSsing")
                                            #     EyeCross = eval(Infiniium.query(":MEASure:CGRade:CROSsing?"))
                                            # except:
                                            #     EyeCross = 999
                                                
                                            # try:
                                            #     EyeZero = eval(Infiniium.query(":MEASure:CGRade:ZLEVel?"))
                                            # except:
                                            #     EyeZero = 999
                                                
                                            # try:
                                            #     EyeOne = eval(Infiniium.query(":MEASure:CGRade:OLEVel? "))
                                            # except:
                                            #     EyeOne = 999

                                            # try:
                                            #     Infiniium.write(":MEASure:CGRade:JITTer RMS")
                                            #     Jitter = eval(Infiniium.query(":MEASure:CGRade:JITTer? RMS"))
                                            # except:
                                            #     Jitter = 999

                                            try:
                                                Infiniium.write(":MEASure:CGRade:EHEight")
                                                EyeHeight = eval(Infiniium.query(":MEASure:CGRade:EHEight?"))
                                            except:
                                                EyeHeight = 999
                                                
                                            try:
                                                Infiniium.write(":MEASure:CGRade:EWIDth")
                                                EyeWidth = eval(Infiniium.query(":MEASure:CGRade:EWIDth?"))
                                            except:
                                                EyeWidth = 999

                                            if i>=0:    
                                                # Download the screen image.
                                                screen_bytes = do_query_ieee_block(":DISPlay:DATA? PNG")
                                                # Save display data values to file.
                                                f = open(screenDir+"%d.png"%i, "wb")
                                                f.write(screen_bytes)
                                                f.close()

                                            alldata.append([i, V_bias_current, V_modulation_enable, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_enable, T_emphasis_short, T_emphasis_amp, EyeHeight, EyeWidth, Success])

    if i>=0:
        head = "ATLAS HGTD BERT test\n\
        Data file made from Infiniium\n\
        Created at %s UTC\n\
        No., V_bias_current, V_modulation_enable, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_enable, T_emphasis_short, T_emphasis_amp, EyeHeight, EyeWidth,Success" %(
        time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        fname_new = fname+"_"+str(i)+"_"+str(time.time())+".csv"
        np.savetxt(fname_new, alldata, delimiter=',', header=head)

    Infiniium.close()
    rm.close()

except:
    head = "ATLAS HGTD BERT test\n\
    Data file made from Infiniium\n\
    Created at %s UTC\n\
    No., V_bias_current, V_modulation_enable, V_modulation_current, V_emphasis_amp, V_emphasis_rising_edge_enable, V_emphasis_falling_edge_enable, T_modulation_current, T_emphasis_enable, T_emphasis_short, T_emphasis_amp, EyeHeight, EyeWidth,Success" %(
    time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    fname_new = fname+"_"+str(i)+"_"+str(time.time())+".csv"
    np.savetxt(fname_new, alldata, delimiter=',', header=head)

    Infiniium.close()
    rm.close()    


# try:
#   main()
# except:
#   traceback.print_exc()
