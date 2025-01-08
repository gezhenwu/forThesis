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
anaUtils.matplotlibConfig()
#import ASICConfig
from scripts import ASICConfig


argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
parser = argparse.ArgumentParser()
parser.add_argument( "-b","--board", type = int, required = False, default = 8, help = "")
args = parser.parse_args()

columns=["vth","Q [fC]","eff","nNoisy","toa [ps]","jitter [ps]","jitterRMS","tot [ps]","tot RMS [ps]","Thres [fC]","noise"]
#columns=["vth","Q [fC]","eff","nNoisy","toa","jitter","jitterRMS","tot","tot RMS","Thres [fC]","noise"]


patternList=[
    "col",
    "pix",
    "rndFifteen",
    "rndFive",
    "rndNine",
    "rndThree",
    "row",
    "sparseFifteen",
    "squareFive",
    "squareThree"]

fileNameList=[]
for board in [1,4,11,12,15,25,28,34,35,36,37,47]:
    for pattern in patternList:
        fileNameList.append("B_"+str(board)+"_On_all_Inj_"+pattern+"_Cp_0_Ctest_26_.dat")
        fileNameList.append("B_"+str(board)+"_On_all_Inj_"+pattern+"_Cp_0_Ctest_208_.dat")

for fileName in fileNameList:


    thresMax=8
    if fileName.find("Ctest_208")>=0: thresMax=16
    varList=[
        ("vth","Thres [fC]",None),
        #("vth","nNoisy",None), 
        #("Thres [fC]","nNoisy",None), 
        #("vth","eff",(370,390,0,1.1)),
        #("Thres [fC]","eff",(0,thresMax,0,1.1)),
        ("Thres [fC]","jitter [ps]",(0,thresMax,0,90)),
        ("Thres [fC]","toa [ps]",(0,thresMax,0,2500)),
        ("Thres [fC]","tot [ps]",(0,thresMax,0,10000)),
        ("Thres [fC]","tot RMS [ps]",(0,thresMax,0,250)),
        ("Thres [fC]","rel_totRMS",(0,thresMax,0,0.2)),
        #("Thres [fC]","jitterRMSRatio",None),
        ("Thres [fC]","noise",(0,thresMax,0,0.8)),    
    ]


    print ("=================================+> ",fileName)
    
    if not os.path.exists(fileName):
        print ("Skip: ",fileName )
        continue


    for var in varList:
        df=pd.read_csv(fileName, header=None,names=columns,sep=' ')
        if len(df) == 0 : continue
        #print ("=============================+> ",var)
        varX=var[0]
        varY=var[1]
        plt.figure(figsize = (12, 10))
        name=fileName+"_"+varY+"_vs_"+varX
        QList=sorted(df['Q [fC]'].unique())
        QRef=[4.2,5.2,10,20,40,100]
        #QRef=[10,20,30,40]
        QList= [anaUtils.closest_to_target(QList, i) for i in QRef]
        print (QList)
        #time.sleep(10)
        for Q in QList:
            #print ("=========================+> ",Q)
            #df=df[df["eff"]!=0]
            #df=df[df["Thres [fC]"]>2]

            #if varY=="jitter":df=df[df["toa"]>300]
            #df['jitterRMSRatio'] = df['jitterRMS'] / df['jitter']
            df['rel_totRMS'] = df['tot RMS [ps]'] / df['tot [ps]']

            df=df[df["Q [fC]"]>1]
            df=df[df["Thres [fC]"]>2.]
            if "nNoisy" not in [varX,varY]:
                df=df[df["nNoisy"]<4]
            if "eff" not in [varX,varY]:
                df=df[df["eff"]>0.95]                

            x = np.array(df[df["Q [fC]"]==Q][varX])
            y = np.array(df[df["Q [fC]"]==Q][varY])
            #print (Q,x,y)
            if len(y)==0: continue

            #name=fileName+"_"+str(Q)
            # plot
            #x*=1.7
            #x-=1.4
            #print ("===> ",prefix,fileName,varX,varY,Q,np.array(x),np.array(y))
            slope, intercept = 0,0#np.polyfit(x, y, 1)
            #plt.plot(x, slope*x + intercept, color='black')
            #print (fileName,slope,intercept)
            #print (y)
            label="Q="+str(round(Q,1))+"fC "
            # if varY in ["jitter"]:
            #     iMin=np.argmin(y)
            #     #print (iMin)
            #     yMin=y[iMin]
            #     xAtMin=x[iMin]
            #     label+=str(round(yMin,1))+" "+str(round(xAtMin,1))
            # if varY in ["noise"]:
            #     #print (Q,y,round(np.median(y),2))
            #     label+=str(round(np.median(y),2))

            plt.plot(x,y,label=label,marker="o")
            #plt.ylim(bottom=0)
            if var[2] is not None:                
                plt.xlim(var[2][0],var[2][1])
                plt.ylim(var[2][2],var[2][3])
            plt.xlabel(varX)
            plt.ylabel(varY)
        plt.legend()
        plt.grid()
        plt.savefig("Plots/SummaryVsThres_"+name+".png")
