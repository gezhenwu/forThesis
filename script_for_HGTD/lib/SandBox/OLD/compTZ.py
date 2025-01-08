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
# main
###############################################



if __name__=='__main__':


    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--outputName', help = '',default="")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('-i', help = '',default="Plots/Data2022_01_24vthcScanOn_all_Inj_col_Vth_540_Q_12_combined_thres.npy", nargs='*')

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
    
    folded=1
    print (args.i)


    yfileList=args.i
    xfile=args.x
    xlabel=args.nx
    ylabel=args.ny
    outName=args.outputDir+"/comp"
    if args.ylabel is not None:
        outName=outName+"_"+str(args.ylabel)
    outName+="_"+args.outputName.replace("/","")
    outName=outName.replace("N/(dv/dt)","Ndvdt").replace("(","_").replace(")","_")


    if xfile==None:
        xArray=range(0,225)
        xArray=xArray[120:225]
        args.xlabel="Pixel number"


    if folded:
        xArray=range(0,15)
        outName+="folded"
    #comparison
    #figures = {}
    #figures["comp"]=plt.figure("comp",figsize = (20, 10))
    #figures["ratio"]=plt.figure("ratio",figsize = (20, 10))
    #fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize=(9,9),gridspec_kw={'height_ratios': [2, 1, 1]})
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})


    refArray=None
    #for yfile in reversed(yfileList):
    for counter,yfile in enumerate(sorted(yfileList)):
    #for counter,yfile in enumerate(reversed(yfileList)):

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(yfile)



        prefix=yfile.replace("_ExtDiscri_False","").replace("_delay","").replace("_thres","").replace("_vthc","").replace("_charge","").split("Scan_")[0].replace("Plots/Data_","")
        prefix=""#yfile.split("_")[6]
        name=prefix
        name+=" B"+str(board)+" "+On+" "+Inj
        if int(QForVthc)!=0:name+=" Qvthc="+QForVthc
        if int(Vth)!=0:name+=" "+str(Vth)
        print (Q)
        if int(Q)!=0:name+=" Qdac="+Q
        #name=yfile.replace("Plots/Data_","").replace("vthcScan","").replace("_combined_thres.npy","").replace("_combined_thres.npy","").replace("_ExtDiscri_False","")

        yArray=np.load(yfile)[120:225]
        if folded:
            #yArray=yArray[0:15]
            mysum=np.zeros(15)
            for col in range(0,6+1):
                mysum=mysum+yArray[col*15:(col+1)*15]#np.sum(mysum,mysum,axis=0)
                pass
            yArray=mysum/7
            print (yArray)
            #toto
        #yArray[0]=np.median(yArray)
        medianVpa=np.median(yArray[0:ASICConfig.lastVpaPixel])
        medianTZ=np.median(yArray)
        name+=" median={:.3f}".format(medianTZ)
        rmsVpa=np.std(yArray[0:ASICConfig.lastVpaPixel])
        rmsTZ=np.std(yArray)
        name+=" rms={:.2f}".format(rmsTZ)


 

        if refArray is None:
            refArray=yArray
        ratioArray=yArray/refArray
        #ratioArray[ratioArray == 1] = 0
        ratioArray=np.nan_to_num(ratioArray,nan=1)
        #ratioArray[79]==1
        diffArray=yArray-refArray

        ax1.plot(xArray , yArray,label=name)
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
        if folded:
            ax1.set_xlim(left=0,right=15)
            ax2.set_xlim(left=0,right=15)
        else:
            ax1.set_xlim(left=120,right=225)
            ax2.set_xlim(left=120,right=225)

        if args.ymax is not None and  args.ymin is not None:        
            for x in range(120,225+1,15):
                ax1.plot([x,x],[args.ymin,args.ymax],linestyle="dashed",color="black",linewidth=1)
            
        if not args.doDiff:
            #if np.any(ratioArray):
            medianVpa=np.median(ratioArray[0:ASICConfig.lastVpaPixel])
            medianTZ=np.median(ratioArray)
            name=" median={:.3f}".format(medianTZ)
            rmsVpa=np.std(ratioArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(ratioArray)
            name+=" rms={:.3f}".format(rmsTZ)
            ax2.plot(xArray , ratioArray,label=name)
            ax2.legend(fontsize=15)
            plt.ylabel("Ratio")
        else:
            #if np.any(ratioArray):
            medianVpa=np.median(diffArray[0:ASICConfig.lastVpaPixel])
            medianTZ=np.median(diffArray)
            name=" median={:.3f}".format(medianTZ)
            rmsVpa=np.std(diffArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(diffArray)
            name+=" rms={:.3f}".format(rmsTZ)
            ax2.plot(xArray , diffArray,label=name)
            ax2.legend(fontsize=15)
            plt.ylabel("Difference")

        if args.xlabel is not None:
            plt.xlabel(args.xlabel)


        if args.y2max is not None:
            ax2.set_ylim(top=args.y2max)
        if args.y2min is not None:
            ax2.set_ylim(bottom=args.y2min)
            
        #ax2.set_ylim(bottom=-5,top=25)

        #ax3.plot(xArray , diffArray,label=name)



        #plt.figure("comp")
        #plt.plot(xArray , yArray,label=name)
        #plt.figure("ratio")
        #plt.plot(xArray , ratioArray,label=name)

        np.save(outName+"_diff"+str(counter),diffArray)
        np.save(outName+"_ratio"+str(counter),ratioArray)

    ax1.grid()
    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")


    #if len(yfileList)==2:
        
    # for name,fig in figures.items():
    #     plt.figure(name)
    #     plt.ylabel(ylabel)
    #     plt.xlabel(xlabel)
    #     plt.legend()
    #     plt.savefig(outName+"_"+name+".pdf")
    #     plt.savefig(outName+"_"+name+".png")
    # plt.close()
    
    
