###############################################
#
###############################################
import os
import argparse
from glob import glob
import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd    
from os import listdir
from os.path import isfile, join
from scipy.optimize import curve_fit

import anaUtils
#anaUtils.matplotlibConfig()
#import ASICConfig
from scripts import ASICConfig
from scipy.optimize import curve_fit


import pandas as pd
import matplotlib.pyplot as plt


argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help = 'Path of the data directory',default="SandBox/ALTIROC3DCpulserB14_Omega_minus30.csv")
args = parser.parse_args()

name=args.input.split("/")[-1]
# Read the CSV file
#data = pd.read_csv('SandBox/ALTIROC3DCpulserB1_2023_09_17.csv')
#data = pd.read_csv('SandBox/ALTIROC3DCpulserB15_2023_10_24.csv')
#data = pd.read_csv('SandBox/ALTIROC3DCpulserB14_Omega_minus30.csv')
#data = pd.read_csv('SandBox/ALTIROC3DCpulserB14_Omega_plus20.csv')
data=pd.read_csv(args.input)

# Extract the column names
columns = data.columns.tolist()

# Define different hollow markers
markers = ['o', 's', 'D', '^', 'v', 'P']



def fitfcn(x,a,b,c):
   return b*x+a



fig, (ax1, ax2) = plt.subplots(2, sharex=True,gridspec_kw={'height_ratios': [2, 1]})

# Iterate over each column (excluding the first column)
counter=-1
for i, column in enumerate(columns[1:]):

    if column.find("DAC LR")>=0: continue
    #if column.find("SR")>=0: continue
    if column=="Unnamed: 5": continue
    print (column,"=")
    counter+=1
    # Extract data within the desired range
    x = data.iloc[:, 0][(data.iloc[:, 0] >= 0) & (data.iloc[:, 0] <= 63)]
    y = data[column][(data.iloc[:, 0] >= 0) & (data.iloc[:, 0] <= 63)]

    sel=x>=0
    print (x)
    # Perform linear fit
    slope, intercept = np.polyfit(x[sel], y[sel], 1)
    popt, pcov = curve_fit(fitfcn, x,y,p0=[1,1,1])

    offset=data[column][data.iloc[:, 0] == 0].values[0]
    print (column,slope,offset,intercept)
    label = f'{column} (Slope: {slope:.3f}, intercept: {intercept:.3f})'

    # Plot data and linear fit
    ax1.plot(data.iloc[:, 0], data[column], linestyle='-', label=label, marker=markers[counter])
    #intercept=8.5
    ax1.plot(x, fitfcn(x,popt[0],popt[1],popt[2]), linestyle='--', color='black')


    ax2.scatter(data.iloc[:, 0], data[column]-fitfcn(x,popt[0],popt[1],popt[2]), linestyle='-', label=label, marker=markers[counter])

# Set labels and title
#plt.ylim(0,10)
#plt.xlim(-5,10)
ax1.set_ylabel('DC pulser [mV]')
ax2.set_ylabel("Residuals")
ax2.set_xlabel(columns[0])

#plt.title('Plot of Columns as a Function of First Column')

# Add legend
ax1.legend()

# Display the plot
#plt.show()
plt.savefig("Plots/"+name+".png")



# # plt.figure()#figsize = (20, 10))
# # x=np.array([10,100,200,260,500,1000])
# # y=np.array([6,38,42,44,44,44])
# # plt.xlabel("Pulse rate kHz")
# # plt.ylim(0,50)
# # plt.ylabel("Vth(10fC)-Vth(5fC)")
# # plt.semilogx(1/(x/1000),y,marker="o")
# # plt.savefig("Plots/pulser.png")


# df=pd.read_csv("SandBox/DCpulser.csv")

# varList=["DCpulser","Amplitude"]
# #varList=["Amplitude"]
# for var in varList:
#     #plt.figure()#figsize = (20, 10))
#     fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1 ,gridspec_kw={'height_ratios': [2, 1]})
#     yRef=np.array([])
#     for Ctest in [0,1]:
#         for Rtest in [1]:
#             print ("#############",var,Ctest,Rtest)
#             sel=(df['Ctest']==Ctest) & (df['Rtest']==Rtest) & (df['DAC']>64)
#             if var=="Amplitude":
#                 sel=sel&(df["DAC"]>0)
#             seldf=df[sel]
#             seldf['DAC']= seldf['DAC'] - 64
#             #print (seldf)
#             #print (seldf)
#             x = np.array(seldf['DAC'])#-63
#             y = np.array(seldf[var])
#             # print ("=== ",x,y)
#             #iRef=1
#             #ref=y[iRef]
#             # x=  np.delete(x,iRef)
#             # y = np.delete(y,iRef)-ref

#             if len(yRef)==0:
#                 yRef=y.copy()       
#             else:
#                 yratio=np.divide(yRef,y)
#                 ax2.scatter(x,yratio)#,label="Ctest %d Rtest %d: a=%.2f  b=%.2f"%(Ctest,Rtest,slope,intercept))
#             #print (y)
#             # plot
#             slope, intercept = np.polyfit(x, y, 1)
#             #print (slope,intercept)
#             #ax1.scatter(x,y,label="Ctest %d Rtest %d"%(Ctest,Rtest))
#             ax1.scatter(x,y,label="Ctest %d Rtest %d: a=%.2f  b=%.2f"%(Ctest,Rtest,slope,intercept))
#             ax1.plot(x, slope*x + intercept, color='black')
#             #plt.ylim(2,7)
#     ax2.set_xlabel("DAC")
#     ax1.set_ylabel(var)
#     ax2.set_ylabel("Ratio")
#     ax1.legend()
#     #plt.show()
#     plt.savefig("Plots/"+var+"_vs_DAC.png")
