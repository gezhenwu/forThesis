###############################################
#
###############################################
import os,sys
import argparse
from glob import glob
import random
curpath = os.getcwd()
sys.path.insert(0,curpath)
curpath = os.getcwd()
sys.path.insert(0,curpath+"/analysis/")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd    
from os import listdir
from os.path import isfile, join

#from scripts import ASICConfig
import anaUtils
anaUtils.matplotlibConfig()
import matplotlib.patches as mpatches


mpl.rcParams['legend.fontsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['axes.titlesize']  = 20
mpl.rcParams['axes.labelsize']  = 20

mpl.rcParams['figure.subplot.bottom'] = 0.2
mpl.rcParams['figure.subplot.hspace'] = 0
#mpl.rcParams['figure.subplot.vspace'] = 0
mpl.rcParams['figure.subplot.left'] = 0.1
mpl.rcParams['figure.subplot.right'] = 0.89
mpl.rcParams['figure.subplot.top'] = 0.90

from cycler import cycler
color=["dodgerblue","tab:red","limegreen","darkviolet","sandybrown","darkgray","tab:pink","tab:olive","tab:cyan","tab:brown","hotpink","navy","lightsteelblue","turquoise","green"]

mpl.rcParams['axes.prop_cycle'] = cycler(color=color)


#mpl.rcParams['legend.fontsize'] = 20
#mpl.rcParams['xtick.labelsize'] = 20
#mpl.rcParams['ytick.labelsize'] = 20
#mpl.rcParams['axes.titlesize']  = 20
#mpl.rcParams['axes.labelsize']  = 20


###############################################
# Functions
###############################################


def drawRectangle(t1,t2,yRange,tsOffset,color="red"):
    t1=convertTS(t1,tsOffset,mode=mode)
    t2=convertTS(t2,tsOffset,mode=mode)
    width=t2-t1
    bottom=yRange[0]
    height=yRange[1]  -yRange[0] 
    rect=mpatches.Rectangle((t1,bottom),width,height, 
                            #fill=False,
                            alpha=0.1,
                            facecolor=color)
    plt.gca().add_patch(rect)


def extractArrays(filename):
    npzfile=np.load(filename)        
    ts=npzfile['ts']
    var=npzfile['var']
    return ts,var

def makePlot(name,ts,var,tsOffset,xlabel,ylabel,xRange=[],yRange=[]):

    ts=convertTS(ts,tsOffset,mode=mode)

    plt.figure(name,figsize = (20, 5))    

    #print (len(ts),len(var))
    plt.scatter(ts, var,marker="o",label="median",color="black")

    plt.grid(True)#color='0.95')

    #plt.title(name.replace("_"," ").replace(".npz"," "))    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)


    if len(xRange)==2:
        plt.xlim(convertTS(np.array(xRange),tsOffset,mode=mode))
    if len(yRange)==2:
        plt.ylim(yRange)
        deltaYRange=yRange[1]-yRange[0]

    for period in periodList:
        periodName,t1,t2,color=period
        drawRectangle(t1,t2,yRange,tsOffset,color=color)

    print (mode)
    if mode=="Hours":
        print ('TITI')
        for tsTxt,txt in txtList:
            
            if len(xRange)==2:
                #print ("TOT",tsTxt,xRange)
                if tsTxt<xRange[0]: continue
                if tsTxt>xRange[1]: continue
            tsTxt=convertTS(tsTxt,tsOffset,mode=mode)
            plt.text(tsTxt, yRange[1]+0.02*deltaYRange,str(txt)+" ", fontsize = 20)

    plt.savefig(args.outputDir+"/"+name +".png")
    plt.close()
    return var



def convertTS(ts,tsOffset=0,mode="hour"):
    ts=ts-tsOffset
    #ts=ts-np.min(ts)
    if mode=="Hours":
        ts=ts/3600.
    elif mode=="days":
        ts=ts/3600./60.
    elif mode=="Mrad":
        ts=ts/3600.*1.4
    return ts




###############################################
# main
###############################################


if __name__=='__main__':

    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--version", type = int, required = False, default = 3, help = "ALTIROC version")
    #parser.add_argument('-n', '--outputName', help = '',default="")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('-i',"--inputDir", help = '',default="PlotsStabilityB35/", type=str)
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
    


    mode="Hours"
    mode="Mrad"


    xRange=[]
    startIrradB11=1696436187
    durationB11=1696938469-startIrradB11
    rateB11=1.4

    startIrradB24=1700995089
    durationB24=1700979743-1700891995
    rateB24=0.6

    startIrradB35=1700982024

    duration=int(durationB11*1.031) #could be any value
    #duration=durationB24
    thresList=[378,383,403]
    if args.inputDir.find("B24")>=0:
        xRange=[1700891995,1700891995+duration]
        #xRange=[1700891995,1700979743+1]
    elif args.inputDir.find("B11")>=0:
        thresList=[380,389]
        xRange=[startIrradB11,startIrradB11+duration]
    elif args.inputDir.find("B35")>=0:
        xRange=[startIrradB35,startIrradB35+duration]

    runTime=700
    periodList=(

# PlotsStabilityB24/ts_1700891995
# PlotsStabilityB24/ts_1700895062
# PlotsStabilityB24/ts_1700895732
# PlotsStabilityB24/ts_1700896683
# PlotsStabilityB24/ts_1700897955

        ("No",1700891995,1700897955,"Green"),
        ("No",1700898611,1700900312,"Green"),
        ("No",1700900992,1700901860,"Green"),
        ("No",1700902518,1700903422,"Green"),
        ("No",1700904058,1700905013,"Green"),
        
        ("No",1700905664,1700909315-400,"Green"),
        ("No",1700909315,1700909315+700,"Green"),
        ("No",1700910410,1700910410+700,"Green"),
        ("No",1700911398,1700911398+700,"Green"),
        ("No",1700912546,1700912546+700,"Green"),
        ("No",1700913583,1700913583+700,"Green"),


        ("No",1700917254,1700918339,"Green"),
        ("No",1700923939,1700925296,"Green"),

        ("No",1700931180,1700933786,"Green"),
        ("No",1700939299,1700942788,"Green"),
        ("No",1700968660,1700973533,"Green"),
        ("No",1700973533,1700979743,"Red"),
        ("No",1700982024,1700987471,"Blue"),
        ("No",1700987471,1700995089,"Green"),



    )

    txtList=[]
    #B11
    counter=0
    for ts in range(startIrradB11,startIrradB11+duration,int(5*3600/rateB11)):
        counter+=1
        dose=int(convertTS(ts,startIrradB11,mode=mode)*rateB11)
        if counter==1:
            txtList.append((ts,"Dose [Mrad]"))
        else:
            txtList.append((ts,dose))

    #B24
    for ts in range(startIrradB24,startIrradB24+duration,int(2*3600/rateB24)):
        dose=int(convertTS(ts,startIrradB24,mode=mode)*rateB24)
        txtList.append((ts,dose))
    txtList.append((1700982024,"Dose [Mrad]"))

    #B35
    txtList+=[
        (1700891995,"Dose [Mrad]"),
        #(1700891995,0),
        #(1700912546,1),
        (1700913583,1),
        (1700917254,2),
        (1700923939,4.2),
        (1700931180,6.5),
        (1700939299,7.4),
        (1700968660,11.7),
    ]







    modeMap={}
    modeMap["Hours"]="Hours"
    modeMap["Mrad"]="Dose [Mrad]"

    ###############################################################
    #
    ###############################################################

    

    inputDir=args.inputDir
    infoMap={}
    infoMap[inputDir+"/vthcScan_smallCtest_Qdac_35_vth.npz"]=(modeMap[mode],"Vthc [DACU]",xRange,[70,200])
    infoMap[inputDir+"/vthcScan_smallCtest_Qdac_35_noise.npz"]=(modeMap[mode],"Noise [DACU]",xRange,[0,1.5])
    infoMap[inputDir+"/widthScan_lsb_totc.npz"]=(modeMap[mode],"TOT LSB [ps]",xRange,[120,200])
    infoMap[inputDir+"/delayScan_lsb_toa.npz"]=(modeMap[mode],"TOA LSB [ps]",xRange,[0,40])
    infoMap[inputDir+"/vthScan_smallCtest_Qdac_110_noise.npz"]=(modeMap[mode],"Noise (Qdac=110) [DACU]",xRange,[0,4])
    infoMap[inputDir+"/vthScan_smallCtest_Qdac_110_vth.npz"]=(modeMap[mode],"Vth (Qdac=110) [DACU]",xRange,[0,1000])
    infoMap[inputDir+"/vthScan_smallCtest_Qdac_87_noise.npz"]=(modeMap[mode],"Noise (Qdac=87) [DACU]",xRange,[0,4])
    infoMap[inputDir+"/vthScan_smallCtest_Qdac_87_vth.npz"]=(modeMap[mode],"Vth (Qdac=87) [DACU]",xRange,[0,1000])


    for thres in thresList:
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_thres.npz"]=(modeMap[mode],"Charge at 95% efficiency  [fC]",xRange,[0,6])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_noise.npz"]=(modeMap[mode],"Noise [fC]",xRange,[0,0.5])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa.npz"]=(modeMap[mode],"TOA [DACU]",xRange,[0,127])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa_RMS.npz"]=(modeMap[mode],"Jitter @ 10fC [DACU]",xRange,[0,2])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc.npz"]=(modeMap[mode],"TOTC @ 10fC [DACU]",xRange,[0,30])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc_RMS.npz"]=(modeMap[mode],"TOTC RMS @ 10fC [DACU]",xRange,[0,2])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_thres.npz"]=(modeMap[mode],"Charge at 95% efficiency  [fC]",xRange,[0,6])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_noise.npz"]=(modeMap[mode],"Noise [fC]",xRange,[0,0.5])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa.npz"]=(modeMap[mode],"TOA [DACU]",xRange,[0,127])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa_RMS.npz"]=(modeMap[mode],"Jitter @ 4fC [DACU]",xRange,[0,3])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc.npz"]=(modeMap[mode],"TOTC @ 4fC [DACU]",xRange,[0,30])
        infoMap[inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc_RMS.npz"]=(modeMap[mode],"TOTC RMS @ 4fC [DACU]",xRange,[0,2])
        

    dataMap={}
    for filename,info in infoMap.items():
        print (filename,info)
        xlabel=info[0]
        ylabel=info[1]
        xRange=info[2]
        yRange=info[3]

        try:
            ts,var = extractArrays(filename)
        except:
            print ("Skip", filename)
            continue


        ts=ts#+runTime/2.
        tsOffset=np.min(ts)
        data=makePlot(filename.replace("/","_"),ts,var,tsOffset,xlabel=xlabel,ylabel=ylabel,xRange=xRange,yRange=yRange)
        dataMap[filename]=(ts,data)

    ###############################################################
    #
    ###############################################################

    
    

    coupleMap={}
    coupleMap[inputDir+"_vthScan_smallCtest_DeltaVth_87_110"]=(inputDir+"/vthScan_smallCtest_Qdac_110_vth.npz",inputDir+"/vthScan_smallCtest_Qdac_87_vth.npz",modeMap[mode],"deltaVth [DACU]",xRange,[0,100],"diff")

    for thres in thresList:
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa.npz",inputDir+"/delayScan_lsb_toa.npz",modeMap[mode],"TOA [ps]",xRange,[0,2000],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa_RMS_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_toa_RMS.npz",inputDir+"/delayScan_lsb_toa.npz",modeMap[mode],"TOA RMS [ps]",xRange,[0,60],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc.npz",inputDir+"/widthScan_lsb_totc.npz",modeMap[mode],"TOTC [ps]",xRange,[0,5000],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc_RMS_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_10fC_totc_RMS.npz",inputDir+"/widthScan_lsb_totc.npz",modeMap[mode],"TOTC RMS [ps]",xRange,[0,200],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa.npz",inputDir+"/delayScan_lsb_toa.npz",modeMap[mode],"TOA [ps]",xRange,[0,2000],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa_RMS_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_toa_RMS.npz",inputDir+"/delayScan_lsb_toa.npz",modeMap[mode],"TOA RMS [ps]",xRange,[0,60],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc.npz",inputDir+"/widthScan_lsb_totc.npz",modeMap[mode],"TOTC [ps]",xRange,[0,5000],"mult")
        coupleMap[inputDir+"_chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc_RMS_ps"]=(inputDir+"/chargeScan_Vth_"+str(thres)+"_smallCtest_Q_4fC_totc_RMS.npz",inputDir+"/widthScan_lsb_totc.npz",modeMap[mode],"TOTC RMS [ps]",xRange,[0,200],"mult")


    for name,info in coupleMap.items():
        print ("================+>",name)
        data1=dataMap[info[0]]
        data2=dataMap[info[1]]
        xlabel=info[2]
        ylabel=info[3]
        xRange=info[4]
        yRange=info[5]
        op=info[6]
        ts=data1[0]
        tsOffset=np.min(ts)
        ts2=data2[0]
        ts2Offset=np.min(ts2)
        print ( len(ts),len(ts2))



        try:
            if op=="diff":
                var=data1[1]-data2[1]
            elif op=="mult":
                var=data1[1]*data2[1]
        except:
            print ("PRB",np.setdiff1d(ts, ts2).astype(int),np.setdiff1d(ts2, ts).astype(int))
            continue

        data=makePlot(name,ts,var,tsOffset,xlabel=xlabel,ylabel=ylabel,xRange=xRange,yRange=yRange)

print ("before exit")
sys.exit()

    
    
