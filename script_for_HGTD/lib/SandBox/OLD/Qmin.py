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

def getMedian(yArray):
    yArrayVpa=yArray[0:ASICConfig.lastVpaPixel]
    medianVpa=np.median(yArrayVpa)
    yArrayTZ=yArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels]
    medianTZ=np.median(yArrayTZ)
    return yArrayVpa,medianVpa,yArrayTZ,medianTZ


def Qmin():
    
    yfileList=args.inputs
    xfile=args.x
    outName=args.outputDir+"/Qmin_"+args.outputName.replace("/","")
    outName=args.outputDir+"/"+args.inputs[0].split("/")[1]+"_Qmin_"+args.outputName.replace("/","")


    if args.ylabel is not None:
        outName=outName+"_"+str(args.ylabel)
    outName=outName.replace("N/(dv/dt)","Ndvdt").replace("(","_").replace(")","_")

    if xfile==None:
        xArray=range(0,225)
        args.xlabel="Pixel number"

    #Qminarison
    #figures = {}
    #figures["Qmin"]=plt.figure("Qmin",figsize = (20, 10))
    #figures["ratio"]=plt.figure("ratio",figsize = (20, 10))
    #fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1, figsize=(9,9),gridspec_kw={'height_ratios': [2, 1, 1]})
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})

    refArray=None
    #for yfile in reversed(yfileList):

    vthList=[]
    thresList=[]
    noiseList=[]
    totRMS4List=[]
    totRMS10List=[]
    toaRMS10List=[]
    toaRMS20List=[]
    toaRMS4List=[]
    nNoisyList=[]
    for counter,yfile in enumerate(sorted(yfileList)):
        print ("=============================================")
    #for counter,yfile in enumerate(reversed(yfileList)):

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N=anaUtils.getInfo(yfile)

        prefix=yfile.replace("_ExtDiscri_False","").replace("_delay","").replace("_thres","").replace("_vthc","").replace("_charge","").split("Scan_")[0].replace("Plots/Data_","")
        prefix=""#yfile.split("_")[6]
        name=prefix
        name+=" B"+board+" "+On+" "+Inj
        if int(QForVthc)!=0:name+=" Qvthc="+QForVthc
        if int(Vth)!=0:name+=" "+Vth
        if int(Q)!=0:name+=" Qdac="+Q
        #name=yfile.replace("Plots/Data_","").replace("vthcScan","").replace("_combined_thres.npy","").replace("_combined_thres.npy","").replace("_ExtDiscri_False","")
        if yfile.find("reg963_2")>=0: name+=" min. current "

        ok=True
        yArray=np.load(yfile)
        yArrayVpa,ymedianVpa,yArrayTZ,ymedianTZ=getMedian(yArray)

        
        if yfile.find("effQ0")>=0:
            nNoisy=np.sum(yArrayTZ>0.01)
            thresArray= np.load(yfile.replace("effQ0","thres"))
            thresArrayVpa,thresmedianVpa,thresArrayTZ,thresmedianTZ=getMedian(thresArray)  
            noiseArray= np.load(yfile.replace("effQ0","noise"))
            noiseArrayVpa,noisemedianVpa,noiseArrayTZ,noisemedianTZ=getMedian(noiseArray)            


            try:
                totRMS4Array= np.load(yfile.replace("effQ0","totRMS4.0"))
                totRMS4ArrayVpa,totRMS4medianVpa,totRMS4ArrayTZ,totRMS4medianTZ=getMedian(totRMS4Array)            
            except:
                totRMS4medianVpa=0
                totRMS4medianTZ=0

            try:
                totRMS10Array= np.load(yfile.replace("effQ0","totRMS10.0"))
                totRMS10ArrayVpa,totRMS10medianVpa,totRMS10ArrayTZ,totRMS10medianTZ=getMedian(totRMS10Array)            
            except:
                totRMS10medianVpa=0
                totRMS10medianTZ=0

            try:
                toaRMS10Array= np.load(yfile.replace("effQ0","toaRMS10.0"))
                toaRMS10ArrayVpa,toaRMS10medianVpa,toaRMS10ArrayTZ,toaRMS10medianTZ=getMedian(toaRMS10Array)            
            except:
                toaRMS10medianVpa=0
                toaRMS10medianTZ=0

            #print (yfile)
            #toaRMS20Array= np.load(yfile.replace("effQ0","toaRMS20.8"))
            #toaRMS20ArrayVpa,toaRMS20medianVpa,toaRMS20ArrayTZ,toaRMS20media
            try:
                toaRMS20Array= np.load(yfile.replace("effQ0","toaRMS20.8"))
                toaRMS20ArrayVpa,toaRMS20medianVpa,toaRMS20ArrayTZ,toaRMS20medianTZ=getMedian(toaRMS20Array)            
            except:
                toaRMS20medianVpa=0
                toaRMS20medianTZ=0
            try:
                toaRMS4Array= np.load(yfile.replace("effQ0","toaRMS4.0"))
                toaRMS4ArrayVpa,toaRMS4medianVpa,toaRMS4ArrayTZ,toaRMS4medianTZ=getMedian(toaRMS4Array)            
            except:
                toaRMS4medianVpa=0
                toaRMS4medianTZ=0
            vthList.append(Vth)
            thresList.append(thresmedianTZ)
            noiseList.append(noisemedianTZ)
            nNoisyList.append(nNoisy)
            totRMS4List.append(totRMS4medianTZ)
            totRMS10List.append(totRMS10medianTZ)
            toaRMS10List.append(toaRMS10medianTZ)
            toaRMS20List.append(toaRMS20medianTZ)
            toaRMS4List.append(toaRMS4medianTZ)




        name+=" median= {:.3f} {:.3f}".format(ymedianVpa,ymedianTZ)
        rmsVpa=np.std(yArray[0:ASICConfig.lastVpaPixel])
        rmsTZ=np.std(yArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
        name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)

    
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
        if args.ylabel is not None:
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
            name=" median= {:.3f} {:.3f}".format(median2Vpa,median2TZ)
            rmsVpa=np.std(ratioArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(ratioArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)
            ax2.plot(xArray , ratioArray,label=name)
            ax2.legend(fontsize=15)
            plt.ylabel("Ratio")
        else:
            #if np.any(ratioArray):
            median2Vpa=np.median(diffArray[0:ASICConfig.lastVpaPixel])
            median2TZ=np.median(diffArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            name=" median= {:.3f} {:.3f}".format(median2Vpa,median2TZ)
            rmsVpa=np.std(diffArray[0:ASICConfig.lastVpaPixel])
            rmsTZ=np.std(diffArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels])
            name+=" rms= {:.3f} {:.3f}".format(rmsVpa,rmsTZ)
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



        #plt.figure("Qmin")
        #plt.plot(xArray , yArray,label=name)
        #plt.figure("ratio")
        #plt.plot(xArray , ratioArray,label=name)

        ax1.set_xlim(120,224)
        ax2.set_xlim(120,224)

        #np.save(outName+"_diff"+str(counter),diffArray)
        #np.save(outName+"_ratio"+str(counter),ratioArray)
        Vth=int(Vth)

    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")


    #
    vthArray=np.array(vthList)
    nNoisyArray=np.array(nNoisyList)
    thresArray=np.array(thresList)
    noiseArray=np.array(noiseList)
    totRMS4Array=np.array(totRMS4List)
    totRMS10Array=np.array(totRMS10List)
    toaRMS10Array=np.array(toaRMS10List)
    toaRMS20Array=np.array(toaRMS20List)
    toaRMS4Array=np.array(toaRMS4List)

    plt.figure(figsize = (20, 10))
    print (vthArray,nNoisyArray)
    plt.scatter(vthArray , nNoisyArray)#, '--bo')
    plt.xlabel("Vth [DAC]")
    plt.ylabel("Nb of noisy channels")
    plt.legend()
    plt.savefig(outName+"_nNoisy_vs_vth.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray , nNoisyArray)#, '--bo')
    plt.xlabel("Qthres [fC]")
    plt.ylabel("Nb of noisy channels")
    plt.legend()
    plt.savefig(outName+"_nNoisy_vs_Qthres.png")


    sel= nNoisyArray<3
    plt.figure(figsize = (20, 10))
    plt.scatter(vthArray[sel] , thresArray[sel])#, '--bo')
    plt.xlabel("Vth [DAC]")
    plt.ylabel("Thres. [fC]")
    plt.legend()
    plt.savefig(outName+"_Qthres_vs_vth.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , totRMS10Array[sel])#, '--bo')
    plt.xlabel("Threshold [fC]")
    plt.ylabel("TOT RMS 10fC")
    plt.legend()
    plt.savefig(outName+"_totRMS10_vs_Qthres.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , totRMS4Array[sel])#, '--bo')
    plt.xlabel("Threshold [fC]")
    plt.ylabel("TOT RMS 4fC")
    plt.legend()
    plt.savefig(outName+"_totRMS4_vs_Qthres.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , toaRMS10Array[sel])#, '--bo')
    plt.ylim(0,50)
    plt.xlabel("Threshold [fC]")
    plt.ylabel("Jitter at 10fC")
    plt.legend()
    plt.savefig(outName+"_toaRMS10_vs_Qthres.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , toaRMS20Array[sel])#, '--bo')
    plt.xlabel("Threshold [fC]")
    plt.ylabel("Jitter at 20fC")
    plt.legend()
    plt.savefig(outName+"_toaRMS20_vs_Qthres.png")

    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , toaRMS4Array[sel])#, '--bo')
    plt.xlabel("Threshold [fC]")
    plt.ylabel("Jitter at 4fC")
    plt.legend()
    plt.savefig(outName+"_toaRMS4_vs_Qthres.png")


    print (noiseArray)
    plt.figure(figsize = (20, 10))
    plt.scatter(thresArray[sel] , noiseArray[sel])#, '--bo')
    plt.xlabel("Threshold [fC]")
    plt.ylabel("Noise [fC]")
    plt.legend()
    plt.savefig(outName+"_noise_vs_Qthres.png")




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



    Qmin()



    
    
