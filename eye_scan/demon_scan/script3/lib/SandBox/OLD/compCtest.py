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

from scripts import ASICConfig
import anaUtils
anaUtils.matplotlibConfig()

mpl.rcParams['legend.fontsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['axes.titlesize']  = 20
mpl.rcParams['axes.labelsize']  = 20


###############################################
# Functions
###############################################

#ASICConfig.nbOfPixels=134

def comp():
    

    QFor26List=[]
    VthFor26List=[]
    QFor200List=[]
    VthFor200List=[]

    yfileList=args.inputs
    xfile=args.x
    outName=args.outputDir+"/comp_"+args.outputName.replace("/","")

    if args.ylabel is not None:
        outName=outName+"_"+str(args.ylabel)
    outName=outName.replace("N/(dv/dt)","Ndvdt").replace("(","_").replace(")","_")

    if xfile==None:
        xArray=range(0,225)
        args.xlabel="Pixel number"

    #comparison
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})

    refArray=None
    #for counter,yfile in enumerate(reversed(sorted(yfileList))):
    for counter,yfile in enumerate(sorted(yfileList)):
        print (yfile)

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N=anaUtils.getInfo(yfile)
        Q=float(Q)
        prefix=yfile.replace("_ExtDiscri_False","").replace("_delay","").replace("_thres","").replace("_vthc","").replace("_charge","").split("Scan_")[0].replace("Plots/Data_","")
        prefix=""#yfile.split("_")[6]
        name=prefix
        name+=" B"+board+" "+On+" "+Inj
        if int(QForVthc)!=0:name+=" Qvthc="+QForVthc
        if int(Vth)!=0:name+=" "+Vth
        if int(Q)>=0:name+=" Qdac="+str(Q)
        #if int(Ctest)>=0:name+=" Ctest="+Ctest
        else:name+=" Ext"
        #name=yfile.replace("Plots/ALTIROC3Data_B_1_2023_05_07_vthScan_HighCtest_","period=")

        yArray=np.load(yfile)
        median=float(np.median(yArray))
        name+=" median= {:.3f}".format(median)
        rms=np.std(yArray)
        name+=" rms= {:.3f}".format(rms)
        print ("%d %f"%(Q,median))


        #if Q in [20,40,60]:
        #if Q in [70,80]:
        if Q>0 and Q>63:# and Q<100:
            Q=Q-63
            if yfile.find("Ctest_26")>=0:
                if Q>20:
                    QFor26List.append(int(Q))
                    print ("=====",QFor26List)
                    VthFor26List.append(median)
            else:
                QFor200List.append(int(Q))
                VthFor200List.append(median)



        if refArray is None:
            refArray=yArray
        ratioArray=yArray/refArray
        #ratioArray[ratioArray == 1] = 0
        ratioArray=np.nan_to_num(ratioArray,nan=1)
        diffArray=yArray-refArray
        ax1.plot(xArray , yArray,label=name)
        ax1.scatter(xArray , yArray)
        if args.ylabel is not None:
            print (args.ylabel)
            ax1.set_ylabel(args.ylabel)
        if args.ymax is not None:
            ax1.set_ylim(top=args.ymax)
        if args.ymin is not None:
            ax1.set_ylim(bottom=args.ymin)
        #else:
        #    ax1.set_ylim(bottom=0)
        ax1.legend(fontsize=15)
        if not args.doDiff:
            #if np.any(ratioArray):
            median=np.median(ratioArray)
            name=" median= {:.3f}".format(median)
            rms=np.std(ratioArray)
            name+=" rms= {:.3f}".format(rms)
            ax2.plot(xArray , ratioArray,label=name)
            ax2.scatter(xArray , ratioArray)
            ax2.legend(fontsize=15)
            plt.ylabel("Ratio")
        else:
            #if np.any(ratioArray):
            median=np.median(diffArray[diffArray!=0])
            name=" median=  {:.3f}".format(median)
            rms=np.std(diffArray[diffArray!=0])
            name+=" rms= {:.3f}".format(rms)
            ax2.plot(xArray , diffArray,label=name)
            ax2.legend(fontsize=15)
            plt.ylabel("Difference")


    
        if args.xlabel is not None:
            plt.xlabel(args.xlabel)


        if args.y2max is not None:
            ax2.set_ylim(top=args.y2max)
        if args.y2min is not None:
            ax2.set_ylim(bottom=args.y2min)
            
        ax1.set_xlim(0,224)
        ax2.set_xlim(0,224)


    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")


    #fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})
    plt.figure(figsize = (20, 10))

    QFor26List=np.array(QFor26List)
    VthFor26List=np.array(VthFor26List)
    print ("ooooooooooooooooo======= ",QFor26List,VthFor26List)
    a26,b26,chi226=anaUtils.pol1fit(QFor26List,VthFor26List)
    print (a26,b26)
    plt.scatter(QFor26List,VthFor26List,label="26fF a=%.2f b=%.1f"%(a26,b26))
    plt.plot(QFor26List,a26*QFor26List+b26)

    QFor200List=np.array(QFor200List)
    VthFor200List=np.array(VthFor200List)
    a200,b200,chi2200=anaUtils.pol1fit(QFor200List,VthFor200List)
    print (a200,b200)
    plt.scatter(QFor200List,VthFor200List,label="200fF a=%.2f b=%.1f"%(a200,b200))
    plt.plot(QFor200List,a200*QFor200List+b200)
    
    #ratio=np.divide(VthFor200List,VthFor26List)
    #print (QFor200List,VthFor26List,ratio)
    #ax2.plot(QFor200List,ratio)

    plt.legend()
    plt.savefig(outName+"_lin.png")
    plt.savefig(outName+"_lin.pdf")



###############################################
# main
###############################################





if __name__=='__main__':


    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--outputName', help = '',default="")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('-i',"--inputs", help = '',default="Plots/Data2022_01_24vthcScanOn_all_Inj_col_Vth_540_Q_12_combined_thres.npy", nargs='*')

    parser.add_argument('--ymax', help = '',default=None,type=float)
    parser.add_argument('--ymin', help = '',default=None,type=float)
    parser.add_argument('--y2max', help = '',default=None,type=float)
    parser.add_argument('--y2min', help = '',default=None,type=float)
    parser.add_argument('--ylabel', help = '',default=None)
    parser.add_argument('--xlabel', help = '',default=None)
    parser.add_argument('-x', help = '',default=None)
    parser.add_argument('--nx', help = '',default="Pixel Number")
    parser.add_argument('--ny', help = '',default="")
    parser.add_argument( "--doDiff", type = argBool, required = False, default = False, help = "compute difference")
    args = parser.parse_args()
    
    print (args.inputs)



    comp()



    
    
