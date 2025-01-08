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



# plt.figure()#figsize = (20, 10))
# x=np.array([10,100,200,250,500,1000])
# y=np.array([6,38,42,44,44,44])
# plt.xlabel("Pulse rate kHz")
# plt.ylim(0,50)
# plt.ylabel("Vth(10fC)-Vth(5fC)")
# plt.semilogx(1/(x/1000),y,marker="o")
# plt.savefig("Plots/pulser.png")


df=pd.read_csv("SandBox/ProbeAmplitude.csv")

varList=["DCpulser","Amplitude"]
#varList=["Amplitude"]
for var in varList:
    #plt.figure()#figsize = (20, 10))
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1 ,gridspec_kw={'height_ratios': [2, 1]})
    yRef=np.array([])
    for Ctest in [0,1]:
        for Rtest in [1]:
            print ("#############",var,Ctest,Rtest)
            sel=(df['Ctest']==Ctest) & (df['Rtest']==Rtest) & (df['DAC']>64)
            if var=="Amplitude":
                sel=sel&(df["DAC"]>0)
            seldf=df[sel]
            seldf['DAC']= seldf['DAC'] - 64
            #print (seldf)
            #print (seldf)
            x = np.array(seldf['DAC'])#-63
            y = np.array(seldf[var])
            # print ("=== ",x,y)
            #iRef=1
            #ref=y[iRef]
            # x=  np.delete(x,iRef)
            # y = np.delete(y,iRef)-ref

            if len(yRef)==0:
                yRef=y.copy()       
            else:
                yratio=np.divide(yRef,y)
                ax2.scatter(x,yratio)#,label="Ctest %d Rtest %d: a=%.2f  b=%.2f"%(Ctest,Rtest,slope,intercept))
            #print (y)
            # plot
            slope, intercept = np.polyfit(x, y, 1)
            #print (slope,intercept)
            #ax1.scatter(x,y,label="Ctest %d Rtest %d"%(Ctest,Rtest))
            ax1.scatter(x,y,label="Ctest %d Rtest %d: a=%.2f  b=%.2f"%(Ctest,Rtest,slope,intercept))
            ax1.plot(x, slope*x + intercept, color='black')
            #plt.ylim(2,7)
    ax2.set_xlabel("DAC")
    ax1.set_ylabel(var)
    ax2.set_ylabel("Ratio")
    ax1.legend()
    #plt.show()
    plt.savefig("Plots/"+var+"_vs_DAC.png")
