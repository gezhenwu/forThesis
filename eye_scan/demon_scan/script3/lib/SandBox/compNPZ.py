###############################################
#
###############################################
import os,sys
import argparse
from glob import glob
import random
curpath = os.getcwd()
sys.path.insert(0,curpath)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd    
from os import listdir
from os.path import isfile, join

#from scripts import ASICConfig
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
    outName=args.outputDir+"/compNPZ_"+args.outputName.replace("/","")
    if args.folded:    outName+="folded"
    if args.ylabel is not None:
        outName=outName+"_"+str(args.ylabel)
    outName=outName.replace("N/(dv/dt)","Ndvdt").replace("(","_").replace(")","_")

   

    #print (args.xlabel,"====",args.folded)

    f=open(outName+".dat","w")
    f.write("On,Inj,board,Ctest,Cd,Rtest,Cp,median,rms\n")

    #comparison
    #fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})
    fig, (ax1) = plt.subplots(nrows = 1, ncols = 1, figsize=(13,9))

    refArray=None
    sortedList=sorted(yfileList)
    if args.reversed:
        sortedList=reversed(sortedList)
    xList=[]
    yList=[]
    sortedList = sorted(yfileList, key=lambda x: int(x.split('_B_')[1].split('_')[0]))
    
    for counter,yfile in enumerate(sortedList):
        print (yfile)

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(yfile)
        prefix=yfile.replace("Plots/Jitter_B_1_SmallCtestOnAll","").replace("Cp0.dat_jitter_ps_vs_Q_fC_375.npz","").replace("Plots/TOTO_B_1_SmallCtestOnAll","").replace("Plots/TOTO_B_1_SmallCtestOnAll","").replace("Cp0.dat_"," ")
        #basename=prefix
        #prefix=""#yfile.split("_")[6]
        basename=""
        #board="X"
        basename+=" B"+str(board)+" "+On+" "+Inj#+" "+Inj
        if int(QForVthc)>0:basename+=" Qvthc="+str(QForVthc)
        if int(Vth)>0:basename+=" "+str(Vth)
        if int(Q)>0:basename+=" Qdac="+str(Q)
        if int(Ctest)>=0:basename+=" "+str(Ctest)
        #if int(Ctest)>=0:basename+=" Ctest="+str(Ctest)
        if int(Cd)>=0:basename+=" Cd="+str(Cd)
        #if int(Cp)>=0:basename+=" Cp="+str(Cp)
        #if int(cDel)>=0:basename+=" cDel="+str(cDel)
        #if int(fDel)>=0:basename+=" fDel="+str(fDel)
        #else:basename+=" Ext"
        #basename=yfile.split("/")[1].replace("Plots/Data3_","")
        basename=basename.replace("Fifteen","15").replace("Nine","9").replace("Five","5").replace("Three","3")
        print (board,basename)

        npzfile=np.load(yfile)
        xArray=npzfile['array1']
        yArray=npzfile['array2']
        #yArray=yArray[args.xmin:args.xmax]

        
        median=np.median(yArray)
        rms=np.std(yArray)
        #xList.append(cDel*1.562)

        print ("=====",xArray,yArray)
        print ("=====",len(xArray),len(yArray))

        
        
        #print (type(On),type(Inj),type(board),type(Ctest),type(Cd),type(Rtest),type(Cp),type(median),type(rms))



        name=basename#+" median= {:.3f}".format(median)
        rms=np.std(yArray)
        #xname+=" rms= {:.3f}".format(rms)
    
        print(xArray)
        ax1.plot(xArray , yArray,label=name)#,        color=anaUtils.colorMap[board])
        ax1.scatter(xArray , yArray)


        if args.ylabel is not None:
            #print (args.ylabel)
            ax1.set_ylabel(args.ylabel)
        if args.ymax is not None:
            ax1.set_ylim(top=args.ymax)
        if args.ymin is not None:
            ax1.set_ylim(bottom=args.ymin)
        if args.xmax is not None:
            ax1.set_xlim(right=args.xmax)
        if args.xmin is not None:
            ax1.set_xlim(left=args.xmin)
        #else:

        ax1.legend(fontsize=15)
        ax1.grid()    
        plt.grid()

        # yArray=yArray
        # xArray=xArray
        # if refArray is None:
        #     refArray=yArray
        # else:

        #     ratioArray=yArray/refArray
        #     ratioArray=np.nan_to_num(ratioArray,nan=1)
        #     diffArray=yArray-refArray
            
        #     if not args.doDiff:
        #         #if np.any(ratioArray):
        #         median=np.median(ratioArray)
        #         name=basename#+" median= {:.2f}".format(median)
        #         rms=np.std(ratioArray)
        #         name+=" rms= {:.2f}".format(rms)
        #         if counter==1:ax2.plot(xArray , ratioArray, markersize=1)#ugly hack
        #         ax2.plot(xArray , ratioArray,label=name)#,        color=anaUtils.colorMap[board])
        #         #ax2.scatter(xArray , ratioArray)

        #         #ax2.legend(fontsize=15)
        #         plt.ylabel("Ratio")
        #     else:
        #         #if np.any(ratioArray):
        #         median=np.median(diffArray[diffArray!=0])
        #         name=basename+" median=  {:.2f}".format(median)
        #         rms=np.std(diffArray[diffArray!=0])
        #         name+=" rms= {:.2f}".format(rms)
        #         if counter==1: ax2.plot(xArray , diffArray, markersize=1)#ugly hack
        #         ax2.plot(xArray , diffArray,label=name)#,        color=anaUtils.colorMap[board])
        #         ax2.legend(fontsize=15)
        #         plt.ylabel("Difference")
        #         np.save(outName+"_diff.npy",diffArray)
    


        if args.xlabel is not None:
            plt.xlabel(args.xlabel)

        # if args.y2max is not None:
        #     ax2.set_ylim(top=args.y2max)
        # if args.y2min is not None:
        #     ax2.set_ylim(bottom=args.y2min)

        # if args.xmax is not None:
        #     ax2.set_xlim(right=args.xmax)
        # if args.xmin is not None:
        #     ax2.set_xlim(left=args.xmin)


        #ax1.set_xlim(3,20)            
        #ax2.set_xlim(3,20)            
        #ax1.set_xlim(0,max(xArray)-1)
        #ax2.set_xlim(0,max(xArray)-1)

        if args.version==2:
            ax1.set_xlim(120,max(xArray)-1)
            #ax2.set_xlim(120,max(xArray)-1)
    

        #if varY=="jitter [ps]":
        #for val in [25,65]:ax1.axhline(val, color="gray", linewidth=0.5)
        #for val in range(4,20,4): ax.axvline(val, color="gray", linewidth=0.5)
        #for val in np.arange(4.,11,6): ax1.axvline(val, color="gray", linewidth=0.5)
    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")
    f.close()






###############################################
# main
###############################################


if __name__=='__main__':


    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--version", type = int, required = False, default = 3, help = "ALTIROC version")
    parser.add_argument('-n', '--outputName', help = '',default="")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('-i',"--inputs", help = '',default="Plots/Data2022_01_24vthcScanOn_all_Inj_col_Vth_540_Q_12_combined_thres.npy", nargs='*')
    parser.add_argument('--xmax', help = '',default=225,type=float)
    parser.add_argument('--xmin', help = '',default=0,type=float)
    parser.add_argument('--ymax', help = '',default=None,type=float)
    parser.add_argument('--ymin', help = '',default=None,type=float)
    parser.add_argument('--y2max', help = '',default=None,type=float)
    parser.add_argument('--y2min', help = '',default=None,type=float)
    parser.add_argument('--ylabel', help = '',default=None)
    parser.add_argument('--xlabel', help = '',default=None)
    parser.add_argument('-x', help = '',default=None)
    #parser.add_argument('--nx', help = '',default="Pixel Number")
    #parser.add_argument('--ny', help = '',default="")
    parser.add_argument( "--doDiff", type = argBool, required = False, default = False, help = "compute difference")
    parser.add_argument( "--reversed", type = argBool, required = False, default = False, help = "reversed list order")
    parser.add_argument( "-f","--folded", type = argBool, required = False, default = False, help = "reversed list order")
    args = parser.parse_args()
    
    print (args.inputs)



    comp()


# plt.figure()#figsize = (20, 10))
# plt.scatter([15, 15,15,15,9,3,1 ], [46.4, 53.3, 56.2, 54.6, 56.9, 59.5, 62.3])
# plt.ylabel('Jitter [ps]')
# plt.xlabel('Number of pixels')
# plt.savefig("Plots/toto.png")
# plt.close()



    
    
