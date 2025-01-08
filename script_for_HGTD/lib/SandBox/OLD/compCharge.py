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
    outName=args.outputDir+"/comp_"+args.outputName.replace("/","")
    if args.folded:    outName+="folded"
    if args.ylabel is not None:
        outName=outName+"_"+str(args.ylabel)
    outName=outName.replace("N/(dv/dt)","Ndvdt").replace("(","_").replace(")","_")

    if xfile==None:
        args.xlabel="Pixel number"
        xArray=range(args.xmin,args.xmax)
        if args.version==2:
            xArray=range(120,args.xmax)
        if args.folded:
            xArray=range(0,15)
            args.xlabel=" Row number"

    #print (args.xlabel,"====",args.folded)

    f=open(outName+".dat","w")
    f.write("On,Inj,board,Ctest,Cd,Rtest,Cp,median,rms\n")

    #comparison
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize=(13,9),gridspec_kw={'height_ratios': [2, 1]})

    refArray=None
    sortedList=sorted(yfileList)
    if args.reversed:
        sortedList=reversed(sortedList)
    xList=[]
    yList=[]
    x2List=[]
    y2List=[]
    for counter,yfile in enumerate(sortedList):
        print (yfile)

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(yfile)
        prefix=yfile.replace("_ExtDiscri_False","").replace("_delay","").replace("_thres","").replace("_vthc","").replace("_charge","").split("Scan_")[0].replace("Plots/Data_","")
        prefix=""#yfile.split("_")[6]
        basename=prefix
        #board="X"
        basename+=" B"+str(board)+" "+On+" "+Inj
        if int(QForVthc)!=0:basename+=" Qvthc="+str(QForVthc)
        if int(Vth)!=0:basename+=" "+str(Vth)
        if int(Q)>0:basename+=" Qdac="+str(Q)
        if int(Ctest)>=0:basename+=" Ctest="+str(Ctest)
        if int(Cd)>=0:basename+=" Cd="+str(Cd)
        if int(Cp)>=0:basename+=" Cp="+str(Cp)
        if int(cDel)>=0:basename+=" cDel="+str(cDel)
        if int(fDel)>=0:basename+=" fDel="+str(fDel)
        else:basename+=" Ext"
        #basename=yfile.replace("Plots/Data3_","")

        yArray=np.load(yfile)
        yArray=yArray[args.xmin:args.xmax]
        if args.folded:
            #yArray=yArray[0:15]
            mysum=np.zeros(15)
            for col in range(0,15):
                #print (len(yArray),yArray,mysum)
                mysum=mysum+yArray[col*15:(col+1)*15]#np.sum(mysum,mysum,axis=0)
                pass
            yArray=mysum/15.

        #yArray=yArray[0:15]
        #xArray=xArray[0:15]
        #if args.inputs.find("FastFADA_ALTIROC2")>=0 or args.inputs.find("Data2")>=0 :
        #    print ("ALTIROC VERSION 2")
        #    args.altirocVersion=2

        if args.version==2:
            yArray=yArray[120:args.xmax]
        median=np.median(yArray)
        rms=np.std(yArray)
        #xList.append(cDel*1.562)

        smallCtest=1
        if Ctest>=200:
            smallCtest=0

        minSel=40#7#40#190
        maxSel=120#20#120#450
        isLowRange=1
        print (Q)
        if (Q>=0 and Q<64 and isLowRange) or (Q>=64 and Q<1000 and not isLowRange):
            x=Q
            if Q>=64:
                x=Q-64#

            x=anaUtils.getDCPulser(Q,smallCtest)
            # if smallCtest:
            #     x=x*0.026
            # else:
            #     x=x*0.208
            #if x  > 40: continue
            #if x > 20: continue
            
            if Ctest<50:
                xList.append(Vth)
                yList.append(median)
            else:
                x2List.append(Vth)
                y2List.append(median)
        #xList.append(Q)
        #yList.append(median)
        
        
        #print (type(On),type(Inj),type(board),type(Ctest),type(Cd),type(Rtest),type(Cp),type(median),type(rms))
        board=int(board)
        f.write("%s,%s,%d,%d,%d,%d,%d,%f,%f  \n"%(On,Inj,board,Ctest,Cd,Rtest,Cp,median,rms))


        name=basename+" median= {:.3f}".format(median)
        rms=np.std(yArray)
        name+=" rms= {:.3f}".format(rms)
    
        ax1.plot(xArray , yArray,label=name)
        ax1.scatter(xArray , yArray)


        if args.ylabel is not None:
            #print (args.ylabel)
            ax1.set_ylabel(args.ylabel)
        if args.ymax is not None:
            ax1.set_ylim(top=args.ymax)
        if args.ymin is not None:
            ax1.set_ylim(bottom=args.ymin)
        #else:
        #    ax1.set_ylim(bottom=0)
        ax1.legend(fontsize=15)
        

        if refArray is None:
            refArray=yArray
        else:
            ratioArray=yArray/refArray
            #ratioArray[ratioArray == 1] = 0
            ratioArray=np.nan_to_num(ratioArray,nan=1)
            diffArray=yArray-refArray
            

            if not args.doDiff:
                #if np.any(ratioArray):
                median=np.median(ratioArray)
                name=basename+" median= {:.2f}".format(median)
                rms=np.std(ratioArray)
                name+=" rms= {:.2f}".format(rms)
                if counter==1:ax2.plot(xArray , ratioArray, markersize=1)#ugly hack
                ax2.plot(xArray , ratioArray,label=name)
                #ax2.scatter(xArray , ratioArray)

                ax2.legend(fontsize=15)
                plt.ylabel("Ratio")
            else:
                #if np.any(ratioArray):
                median=np.median(diffArray[diffArray!=0])
                name=basename+" median=  {:.2f}".format(median)
                rms=np.std(diffArray[diffArray!=0])
                name+=" rms= {:.2f}".format(rms)
                if counter==1: ax2.plot(xArray , diffArray, markersize=1)#ugly hack
                ax2.plot(xArray , diffArray,label=name)
                ax2.legend(fontsize=15)
                plt.ylabel("Difference")
                np.save(outName+"_diff.npy",diffArray)
    


        if args.xlabel is not None:
            plt.xlabel(args.xlabel)

        if args.y2max is not None:
            ax2.set_ylim(top=args.y2max)
        if args.y2min is not None:
            ax2.set_ylim(bottom=args.y2min)
            
        ax1.set_xlim(0,max(xArray)-1)
        ax2.set_xlim(0,max(xArray)-1)

        if args.version==2:
            ax1.set_xlim(120,max(xArray)-1)
            ax2.set_xlim(120,max(xArray)-1)
    
    plt.savefig(outName+".png")
    plt.savefig(outName+".pdf")
    f.close()


    xArray=np.array(xList)
    yArray=np.array(yList)
    x2Array=np.array(x2List)
    y2Array=np.array(y2List)

    ind = np.argsort(xArray)
    xArray = xArray[ind]
    yArray = yArray[ind]


    doLinearity=0
    if doLinearity==1:
        fig, (ax1, ax2 , ax3) = plt.subplots(3, sharex=True,gridspec_kw={'height_ratios': [2, 1, 1]}, figsize=(12, 8))
        ax1.scatter(xArray , yArray)
        sel=np.logical_and(xArray>=minSel , xArray<=maxSel)
        print (sel)
        slope, intercept = np.polyfit(xArray[sel], yArray[sel], 1)
        print (slope,intercept)

        ax1.plot(xArray[sel], slope * xArray[sel] + intercept, linewidth=1,linestyle='-', color='red',label="a="+str(round(slope,5))+" b="+str(round(intercept,5)))
        ax1.set_ylabel("Vth")#Charge at 95% efficiency [fC]")

        axTop = ax1.twiny()
        axTop.set_xlim(ax1.get_xlim())
        #axTop.set_xticks(new_tick_locations)
        #axTop.set_xticklabels(tick_function(new_tick_locations))
        axTop.set_xlabel(r"Modified x-axis: $1/(1+X)$")

        ax2.scatter(xArray , yArray-(slope * xArray + intercept))
        ax2.set_ylabel("Residuals")#Charge at 95% efficiency [fC]")

        print 
        xArray2=[]
        aArray2=[]
        for i in range(1,len(xArray)):
            x=xArray[i]
            a=0
            #if i>=2 and i<=len(xArray)-2:
            #    a,b = np.polyfit(xArray[i-2:i+2], yArray[i-2:i+2], 1)
            if i>=1 and i<=len(xArray)-1:
                a,b = np.polyfit(xArray[i-1:i+1], yArray[i-1:i+1], 1)
            elif i==len(xArray):
                a,b = np.polyfit(xArray[i-1:i], yArray[i-1:i], 1)
            elif i==0:
                a,b = np.polyfit(xArray[0:i+1], yArray[0:i+1], 1)

            xArray2.append(x)
            aArray2.append(a)
            print (i,x,a)
        print ( np.mean( aArray2 ) )
        ax3.scatter(xArray2 , aArray2)
        ax3.set_ylabel("Local derivative")
        #ax3.set_ylim(0,0.4)

        #plt.xlabel("Q [fC]")
        #plt.xlabel("Q [dac]")
        plt.xlabel("DC pulser [mV]")
        ax1.legend()

        ax1.grid()
        ax2.grid()
        ax3.grid()
        plt.savefig(outName+"_Bonus.png")
    else:
        plt.figure()
        plt.scatter(xArray , yArray)
        plt.scatter(x2Array , y2Array)
        slope, intercept = np.polyfit(xArray, yArray, 1)
        sel=xArray>=0
        slope, intercept = np.polyfit(xArray[sel], yArray[sel], 1)
        #plt.plot(xArray[sel], slope * xArray[sel] + intercept, linestyle='--', color='red',label="a="+str(round(slope,5))+" b="+str(round(intercept,5)))
        mean=np.mean(yList)
        #plt.ylim(mean-0.5,mean+0.5)
        plt.ylabel("Vth")#Charge at 95% efficiency [fC]")
        plt.xlabel("Q [dac]")
        plt.legend()
        #plt.ylabel("Charge at 95% efficiency [fC]")
        #plt.xlabel("Delay")
        #plt.xlabel("Vth [DACU]")
        plt.savefig(outName+"_Bonus.png")
 




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
    parser.add_argument('--xmax', help = '',default=225,type=int)
    parser.add_argument('--xmin', help = '',default=0,type=int)
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



    
    
