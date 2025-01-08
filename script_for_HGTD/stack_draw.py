import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
import argparse
import os
import sys

dataX = []
for i in range(0,225):
    dataX.append(i)


for asic in ['M9C0','M9C1','M11C0','M12C0','M12C1','M13C0','M13C1']:
    dataY1 = np.load('Plots/compare/chargeAna/Measurements_t0_HV_14ch_GND_Co_'+asic+'_chargeScan_B_0_On_col_Inj_col_N_100_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_26___noise.npy', mmap_mode='r')
    dataY2 = np.load('Plots/compare/chargeAna/Measurements_t0_HV_14ch_GND_Sk_'+asic+'_chargeScan_B_0_On_col_Inj_col_N_100_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_26___noise.npy', mmap_mode='r')

    avrY1 = np.mean(dataY1)
    avrY2 = np.mean(dataY2)

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    ax.plot(dataX, dataY1, 'g-', label='PEB GND connects with vessel. 14 HV ch. '+asic+' Noise mean = %.2f'%avrY1)
    ax.plot(dataX, dataY2, 'b-', label='PEB GND connects with cooling plate. 14 HV ch. '+asic+' Noise mean = %.2f'%avrY2)

    ax.set_xlabel('Pixel')
    ax.set_ylabel('Noise (fC)')
    ax.set_ylim([0, 0.7])
    

    ax.legend()

    plt.savefig('./Plots/compare/noise/'+asic+'_14CoVS14Sk.png', dpi=300)


for asic in ['M9C0','M9C1','M11C0','M12C0','M12C1','M13C0','M13C1']:
    dataY1 = np.load('Plots/compare/chargeAna/Measurements_t0_HV_14ch_GND_Co_'+asic+'_chargeScan_B_0_On_col_Inj_col_N_100_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_26___noise.npy', mmap_mode='r')
    dataY2 = np.load('Plots/compare/chargeAna/Measurements_t0_HV_1ch_GND_Co_'+asic+'_chargeScan_B_0_On_col_Inj_col_N_100_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_26___noise.npy', mmap_mode='r')

    avrY1 = np.mean(dataY1)
    avrY2 = np.mean(dataY2)

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    ax.plot(dataX, dataY1, 'g-', label='PEB GND connects with vessel. 14 HV ch. '+asic+' Noise mean = %.2f'%avrY1)
    ax.plot(dataX, dataY2, 'r-', label='PEB GND connects with vessel. 1 HV ch. '+asic+' Noise mean = %.2f'%avrY2)

    ax.set_xlabel('Pixel')
    ax.set_ylabel('Noise (fC)')
    ax.set_ylim([0, 0.7])   

    ax.legend()

    plt.savefig('./Plots/compare/noise/'+asic+'_14CoVS1Co.png', dpi=300)    
