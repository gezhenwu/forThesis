import argparse
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import glob

smallCtest=40.#208/4.2
largeCtest=208.
QOFFSET=0.0077*largeCtest
QCONV=0.0017*largeCtest
HIGHLOWRATIO=7.84/1.7
#if args.smallCtest:
QCONV=QCONV*smallCtest/largeCtest#0.4*26./200
QOFFSET=0.0035*smallCtest

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Generate a distribution of TOA for a specific pixel in a CSV file.')

# Add the file name argument
#parser.add_argument("-f",'--file_name', type=str, help='the name of the CSV file',default="ALTIROC3Data/B_4_2023_05_16/chargeScan/B_4_On_all_Inj_col_N_100_Vth_382_Ctest_26_/pixelOn_all_pixelInj_col0/timing_data_dacCharge_35_.csv")

# Add the channel number argument
parser.add_argument('-p','--pixel', type=int, help='the channel number to filter',default=120)

# Parse the command-line arguments
args = parser.parse_args()


var="tot"


file_pattern = "ALTIROC3Data/B_1_2023_05_19/chargeScan/B_1_On_all_Inj_col_N_100_Vth_*_Ctest_26_/pixelOn_all_pixelInj_col0/timing_data_dacCharge_53_.csv"
file_pattern = "Data3/B_9_2023_07_06_setup1_IBNoNumber_reg1005_10/chargeScan/B_9_On_all_Inj_pix_N_100_Vth_378_Cd_3_Cp_0_cDel_0_fDel_7_Ctest_26_/pixelOn_all_pixelInj_127/*80*csv"
file_pattern = "Data3/BX_test1ASIC_2023_12_XX//B_1_test1ASIC_all_col/chargeScan/B_1_On_all_Inj_col_N_100_Vth_385_Cd_-1_Cp_0_cDel_0_fDel_9_Ctest_26_/*/*dacCharge_80*csv"

fileNameList = glob.glob(file_pattern)

for fileName in fileNameList:
    print (fileName)

    plt.figure()#figsize = (20, 10))
    # Read the CSV file into a pandas DataFrame
    try:
        df = pd.read_csv(fileName)
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
        sys.exit(1)

    if len(df)==0: continue
    
    # Filter the data for the specified channel number
    df = df[df['pixel'] == args.pixel]

    if len(df)==0: continue

    #print (df)
    dfNOVARSAT = df[df[var] < 127]

    # Set up the bins based on the desired width and range
    bin_width = 1
    min_value = df[var].min()
    max_value = df[var].max()
    bins = np.arange(min_value, max_value + bin_width, bin_width)

    # Create a histogram of the VAR values
    plt.hist(df[var], bins=bins, edgecolor='black')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of VAR for Pixel {args.pixel}')
    plt.grid(True)
    # Calculate mean and RMS
    mean = dfNOVARSAT[var].mean()
    #rms = np.sqrt(np.mean(np.square(dfNOVARSAT[var])))
    rms = np.std(dfNOVARSAT[var])
    dacCharge = -1
    match = re.search(r"dacCharge_(\d+)", fileName)
    if match:
        dacCharge = int(match.group(1))
    Vth = -1
    match = re.search(r"Vth_(\d+)", fileName)
    if match:
        Vth = int(match.group(1))
    if dacCharge<=63:charge=QOFFSET+dacCharge*QCONV#in fact it is not anymore a dacCharge
    else:charge=QOFFSET+(dacCharge-64)*HIGHLOWRATIO*QCONV
    charge=round(charge,1)
    # Add mean and RMS to the plot
    plt.text(0.95, 0.9, f'charge: {dacCharge} DACU {charge} fC', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.text(0.95, 0.8, f'Mean: {mean:.2f}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.text(0.95, 0.7, f'RMS: {rms:.2f}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.savefig("Plots/debug_"+str(args.pixel)+"_"+str(Vth)+".png")
