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


argBool = lambda s: s.lower() in ["true", "t", "yes", "1"]
parser = argparse.ArgumentParser()
parser.add_argument( "-b","--board", type = int, required = False, default = 8, help = "")
args = parser.parse_args()


columns=["vth","Q [fC]","eff","nNoisy","toa [ps]","jitter [ps]","jitterRMS","tot [ps]","tot RMS [ps]","Thres [fC]","noise"]






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
    "squareThree"
]

fileNameList=[]
boardList=[1,4,11,12,15,25,28,34,35,36,37,47]
#boardList=[9]
for board in boardList:
    for pattern in patternList:
        fileNameList.append("B_"+str(board)+"_On_all_Inj_"+pattern+"_Cp_0_Ctest_26_.dat")
        fileNameList.append("B_"+str(board)+"_On_all_Inj_"+pattern+"_Cp_0_Ctest_208_.dat")


for fileName in fileNameList:


    chargeMax=20
    if fileName.find("Ctest_208")>=0: chargeMax=100
    varList=[
    #("vth","nNoisy",None),
    #("Thres [fC]","nNoisy",None),
    ###("vth","eff",[370,390,0,1.1]),
    #("Q [fC]","eff",[0,chargeMax,0,1.1]),
    ("Q [fC]","jitter [ps]",[0,chargeMax,0,90]),
    ("Q [fC]","toa [ps]",[0,chargeMax,0,2500]),
    ("Q [fC]","tot [ps]",[0,chargeMax,0,5000]),
    ("tot [ps]","toa [ps]",[0,5000,0,2500]),
    ("Q [fC]","tot RMS [ps]",[0,chargeMax,0,300]),
    ("Q [fC]","rel_tot RMS [ps]",[0,chargeMax,0,0.3]),
    #("Q [fC]","jitterRMSRatio",None),
    #("Q [fC]","noise",None),    
    ]

    print ("=================================+> ",fileName)
    
    if not os.path.exists(fileName):
        print ("Skip: ",fileName )
        continue




    for var in varList:
        df=pd.read_csv(fileName, header=None,names=columns,sep=" ")
        if len(df) == 0 : continue

        #print ("=============================+> ",var)
        varX=var[0]
        varY=var[1]
        plt.figure(figsize = (12, 10))
        name=fileName+"_"+varY.replace(" ","")+"_vs_"+varX.replace(" ","")
        name=name.replace(" ","_").replace("[","").replace("]","")
        #QList=list(sorted(df["Q"].unique()))
        #minList=range(len(QList()))
        QthresList=sorted(df["Thres [fC]"].unique())
        #QthresList=[2.1936,5.2752]


        #thresRef=[2.1,4.8]
        #if fileName.find("AllPix")>=0: thresRef=[2.6,4.8]
        thresRef=[2.5 ,  3.2, 4. , 6]
        thresRef=[2.7 ,  4.0  ,   6.2 ]
        #thresRef=[3]
        #print (thresRef)
        #print (QthresList)
        thresList=[x for x in QthresList if x >= 2.]
        #QthresList= [anaUtils.closest_to_target(QthresList, i) for i in thresRef]
        QthresList= sorted(list(set(        QthresList)))
        print (QthresList)
        #toto


        # SCALE=1.2
        # smallCtest=40.*SCALE#208/5.2
        # largeCtest=208.*SCALE
        # SLOPE_LR=0.0017  #low range
        # SLOPE_HR=0.00784 #high range
        # OFFSET_LC=0.0090 #LC: Large Ctest
        # OFFSET_SC=0.0035
        
        # QCONV=SLOPE_LR*largeCtest
        # QOFFSET=OFFSET_LC*largeCtest

        # #smallCtest
        # QCONV=SLOPE_HR*smallCtest
        # QOFFSET=OFFSET_SC*smallCtest

        # x=np.arange(0,600,1)
        # xfc=(QOFFSET+x*QCONV)
        # y=1./(0.00369*x-0.02086)/xfc+10 #smallCtest
        # #y=1./(0.00382*x-0.00063)/xfc+10 #largeCtest
        # plt.plot( xfc , 1.7*y, color="black")
        # plt.plot( xfc , 2.0*y, color="black")

        for Qthres in QthresList:
            try:
                vth=int(list(df[df["Thres [fC]"]==Qthres]["vth"])[0])     
            except:
                vth=0
            #if vth not in [373,378,385,400]: continue
            #if vth not in [375]: continue
            #print (vth)
            #print (QthresList)
            #print ("=========================+> ",Qthres)
            #df=df[df["eff"]!=0]
            
            #if varY=="jitter [ps]":df=df[df["toa [ps]"]>300]
            df["jitterRMSRatio"] = df["jitterRMS"] / df["jitter [ps]"]
            df["rel_tot RMS [ps]"] = df["tot RMS [ps]"] / df["tot [ps]"]
            #print (df["eff"])
            df=df[df["Q [fC]"]>1]
            if "eff" not in [varX,varY]:
                df=df[df["eff"]>0.95]
                pass
            if "nNoisy" not in [varX,varY]:
                df=df[df["nNoisy"]<4]
                pass
            #print (df)
            x = np.array(df[df["Thres [fC]"]==Qthres][varX])
            y = np.array(df[df["Thres [fC]"]==Qthres][varY])



            if varY in ["jitter [ps]","tot [ps]","toa [ps]","tot RMS [ps]"]:
                np.savez("Plots/TOTO_"+name+"_Vth_"+str(vth)+"_.npz", array1=x, array2=y)

            sorted_indices = np.argsort(x)
            x = x[sorted_indices]            
            y = y[sorted_indices]


            #print (x,y)
            if len(x)==0: continue
            #name=fileName+"_"+str(Q)
            # plot
            #x*=1.7
            #x-=1.4
            #print ("===> ",prefix,fileName,varX,varY,Q,np.array(x),np.array(y))
            slope, intercept = 0,0#np.polyfit(x, y, 1)
            #plt.plot(x, slope*x + intercept, color="black")
            #print (fileName,slope,intercept)

            #if vth not in []
            vthStr=str(vth)
            #x=x/SCALE
            plt.plot(x,y,label="thres="+str(round(Qthres,1))+"fC (Vth="+vthStr+")",marker="o")
            #plt.plot(x,y,label="cDel="+str(round(Qthres,1)),marker="o")
            plt.ylim(bottom=0)
            # if varX=="Q [fC]":
            #     if fileName.find("SmallCtest")<0:                    
            #         var[2][1]=100
            #         plt.xscale("log")
                    
            if var[2] is not None:
                plt.xlim(var[2][0],var[2][1])
                plt.ylim(var[2][2],var[2][3])
            plt.xlabel(varX)
            plt.ylabel(varY)


            
        plt.legend(fontsize=20)
        ax=plt.gca()
        if varY=="jitter [ps]":
            for val in [25,65]:ax.axhline(val, color="gray", linewidth=0.5)
            #for val in range(4,20,4): ax.axvline(val, color="gray", linewidth=0.5)
            for val in np.arange(4.,11,6): ax.axvline(val, color="gray", linewidth=0.5)
        #plt.grid()

        plt.savefig("Plots/SummaryVsCharge_"+name+".png")
