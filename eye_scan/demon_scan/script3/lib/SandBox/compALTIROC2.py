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
    #figures = {}
    #figures["comp"]=plt.figure("comp",figsize = (20, 10))
    #figures["ratio"]=plt.figure("ratio",figsize = (20, 10))
    #fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize=(9,9),gridspec_kw={'height_ratios': [2, 1, 1]})
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})

    refArray=None
    #for yfile in reversed(yfileList):

    #for counter,yfile in enumerate(reversed(sorted(yfileList))):
    for counter,yfile in enumerate(sorted(yfileList)):
        #for counter,yfile in enumerate(reversed(yfileList)):
        print (yfile)

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N=anaUtils.getInfo(yfile)

        prefix=yfile.replace("_ExtDiscri_False","").replace("_delay","").replace("_thres","").replace("_vthc","").replace("_charge","").split("Scan_")[0].replace("Plots/Data_","")
        prefix=""#yfile.split("_")[6]
        name=prefix
        name+=" B"+board+" "+On+" "+Inj
        if int(QForVthc)!=0:name+=" Qvthc="+QForVthc
        if int(Vth)!=0:name+=" "+Vth
        if int(Q)!=0:name+=" Qdac="+Q
        else:name+=" Ext"
        #name=yfile.replace("Plots/Data_","").replace("vthcScan","").replace("_combined_thres.npy","").replace("_combined_thres.npy","").replace("_ExtDiscri_False","")
        #if yfile.find("reg963_2")>=0: name+=" min. current "
        #if yfile.find("10us")>=0: name+="  10us "
        #else:  name+=" 100us "

        yArray=np.load(yfile)
        median=np.median(yArray)
        yArrayVpa=yArray[0:ASICConfig.lastVpaPixel]
        medianVpa=np.median(yArrayVpa)
        yArrayTZ=yArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels]
        medianTZ=np.median(yArrayTZ)
        

        name+=" median= {:.3f} {:.3f}".format(medianVpa,medianTZ)
        #name+=" median= {:.3f}".format(median)
        rms=np.std(yArray)
        rmsVpa=np.std(yArray[0:ASICConfig.lastVpaPixel])
        rmsTZ=np.std(yArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
        #name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)
        name+=" rms= {:.3f}".format(rms)
        #name=yfile
    
        if refArray is None:
            refArray=yArray
        ratioArray=yArray/refArray
        #ratioArray[ratioArray == 1] = 0
        ratioArray=np.nan_to_num(ratioArray,nan=1)
        #ratioArray[79]==1
        diffArray=yArray-refArray


        #ax1.scatter(alvinTOT[120:224] , yArray[120:224],label=name)
        #ax1.plot(xArray , (yArray-alvinTOT)/alvinTOT,label=name)
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
            median2Vpa=np.median(ratioArray[0:ASICConfig.lastVpaPixel])
            median2TZ=np.median(ratioArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            median2Vpa=np.median(ratioArray[0:ASICConfig.lastVpaPixel])
            name=" median= {:.3f} {:.3f}".format(median2Vpa,median2TZ)
            rmsVpa=np.std(ratioArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(ratioArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)
            ax2.plot(xArray , ratioArray,label=name)
            ax2.scatter(xArray , ratioArray)
            print (name)
            ax2.legend(fontsize=15)
            plt.ylabel("Ratio")
        else:
            #if np.any(ratioArray):
            median=np.median(diffArray[diffArray!=0])
            median2Vpa=np.median(diffArray[0:ASICConfig.lastVpaPixel])
            median2TZ=np.median(diffArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            name=" median= {:.3f} {:.3f}".format(median2Vpa,median2TZ)
            #name=" median=  {:.3f}".format(median)
            rms=np.std(diffArray[diffArray!=0])
            rmsVpa=np.std(diffArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(diffArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            #name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)
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
            
        #ax2.set_ylim(bottom=-5,top=25)

        #ax3.plot(xArray , diffArray,label=name)



        #plt.figure("comp")
        #plt.plot(xArray , yArray,label=name)
        #plt.figure("ratio")
        #plt.plot(xArray , ratioArray,label=name)

        ax1.set_xlim(0,224)
        ax2.set_xlim(0,224)

        #ax1.set_xlim(120,134)
        #ax2.set_xlim(120,134)

        #np.save(outName+"_diff"+str(counter),diffArray)
        #np.save(outName+"_ratio"+str(counter),ratioArray)
        Vth=int(Vth)

    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")

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



    
    
