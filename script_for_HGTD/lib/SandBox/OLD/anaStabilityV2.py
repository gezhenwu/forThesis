###############################################
#
###############################################
import os
import argparse
import random
import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd    
from os import listdir
from os.path import isfile, join
import glob
from glob import glob
    
from scripts import ASICConfig
import anaUtils
anaUtils.matplotlibConfig()

mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10
mpl.rcParams['axes.titlesize']  = 10
mpl.rcParams['axes.labelsize']  = 10

mpl.rcParams['figure.subplot.bottom'] = 0.12
mpl.rcParams['figure.subplot.hspace'] = 0
#mpl.rcParams['figure.subplot.vspace'] = 0
mpl.rcParams['figure.subplot.left'] = 0.1
mpl.rcParams['figure.subplot.right'] = 0.92
mpl.rcParams['figure.subplot.top'] = 0.98

from cycler import cycler
color=["dodgerblue","tab:red","limegreen","darkviolet","sandybrown","darkgray","tab:pink","tab:olive","tab:cyan","tab:brown","hotpink","navy","lightsteelblue","turquoise","green"]

mpl.rcParams['axes.prop_cycle'] = cycler(color=color)


missing=[]


    
###############################################
# functions
###############################################


def isBad(ts):                                      

    if ts in [

    ]:
        return 1

    return 0

def convert(tsArray):#convert time in dose
    doseArray=np.zeros(np.shape(tsArray)[0])
    for i,ts in enumerate(tsArray):
        doseArray[i]=getDose(ts)    
        #print (ts,getDose(ts))
    return doseArray




def getArrays(name,regex,ylabel,tsSelArray):
    fileList = sorted(glob(regex))
    varList=[np.array([])]*225
    tsList=[]


    #for f in sorted([line.strip() for line in sorted(os.popen(cmd).readlines())],key=lambda n:int(n.split("-")[1].replace("B",""))):
    #for f in sorted(fileList):

    for f in sorted(fileList):
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,NMax=anaUtils.getInfo(f)
        if ts not in tsSelArray and len(tsSelArray)>0: continue
        yArray=np.load(f)
        tsList.append(ts)
        for pixel,y in enumerate(yArray):
            varList[pixel]=np.append(varList[pixel],y)

    #print ("==============================================>",len(tsList),len(tsSelArray),set(sorted(tsSelArray)) - set(sorted(list(tsList))))


    for ele in list(set(sorted(tsSelArray)) - set(sorted(list(tsList)))):
        missing.append(ele)



    tsArray=np.array(tsList)
    if len (tsList)>0:
        tsArray-=np.min(tsArray)
        tsArray=tsArray/3600./24. #conversion in days
        pass
    varArray=np.array(varList)

    #order=tsArray.argsort()
    #tsArray=tsArray[order]
    #varArray=varArray[order]
    #print (varArray)
    
    return tsArray,varArray

    #return tsArray,np.array(varList)

def makePlot(tsArray,varList,name,xlabel,ylabel,pixelArray,doMedian=True,xRange=[],yRange=[],substractYMedian=False):
    #print (tsArray)
    plt.figure(figsize = (10, 5))    
    #print (name)
    #printisb (tsArray,varList)
    
    yMax=0
    yMin=99999999.
    varForMedianList=[]
    varForMeanList=[]
    for pixel,yArray in enumerate(varList):
        if pixel not in pixelArray: continue
        #print (pixel,[e for e in zip(tsArray,yArray)])
        marker="o"
        if pixel>=120:
            marker="s"
        if substractYMedian: yArray=yArray-np.median(yArray)
        #print ("==",pixel,len(tsArray),len(yArray),tsArray,yArray)
        plt.scatter(tsArray, yArray,marker=marker,label=str(pixel),s=6)
        #print (yArray)

        if len (yArray)>0:
            if np.max(yArray)>yMax:yMax=np.max(yArray)
            if np.min(yArray)<yMax:yMin=np.max(yArray)
        varForMedianList.append(yArray)
        medianArray=np.median(varForMedianList,axis=0)
        meanArray=np.mean(varForMedianList,axis=0)
        
    if doMedian and len(medianArray)>0:
        
        rel=   ( np.max(medianArray)-np.min(medianArray))/float(np.median(medianArray))
        #plt.scatter(tsArray, medianArray,marker="D",color="black",label="median")# :{:.3f}".format( rel))
        
        rel=   ( np.max(meanArray)-np.min(meanArray))/float(np.mean(meanArray))
        plt.scatter(tsArray, meanArray,marker="D",label="mean :{:.3f}".format( rel),color="black")

        plt.grid(True)#color='0.95')
        median=np.median(medianArray)
        a,b,chi2=anaUtils.pol1fit(tsArray,[median]*len(tsArray))
        #plt.plot(tsArray,a*np.array(tsArray)+b,color="blue",linestyle="dashed",label="fit")
        
        #plt.plot(tsArray,[median]*len(tsArray),color="blue",linestyle="dashed")
        


        #
        #print (median)


    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    if not substractYMedian:
        if len(yRange)==2:plt.ylim(yRange)
        if len(xRange)==2:plt.ylim(xRange)
    #plt.xlim(right=1.2*np.max(tsArray))
    box = plt.gca().get_position()
    #plt.gca().set_position([box.x0, box.y0, box.width * 1.0, box.height])
    plt.legend(fontsize=8,loc='center right',bbox_to_anchor=(1.1, 0.5))
    plt.savefig(args.outputDir+"/"+name +args.extension)
    return medianArray



def makePlot2(var1Array,var2Array,name,xlabel,ylabel,pixelArray,xRange=[],yRange=[],substractYMedian=False):
    plt.figure(figsize = (10, 5))    
    
    yMax=0
    yMin=99999999.
    varForMedianList=[]
    for pixel,data in enumerate(zip(var1Array,var2Array)):
        xArray,yArray=data
        if pixel not in pixelArray: continue
        if substractYMedian: yArray=yArray-np.median(yArray)
        plt.scatter(xArray, yArray,marker="o",label=str(pixel))
        #print (yArray)

        if len (yArray)>0:
            if np.max(yArray)>yMax:yMax=np.max(yArray)
            if np.min(yArray)<yMax:yMin=np.max(yArray)
        varForMedianList.append(yArray)
    #medianArray=np.median(varForMedianList,axis=0)
    #plt.plot(tsArray, medianArray,marker="D",label="median",color="black")
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if len(yRange)==2:plt.ylim(yRange)
    if len(xRange)==2:plt.ylim(xRange)
    #plt.ylim(bottom=yMin*0.,top=yMax*1.5)
    plt.legend(fontsize=5)

    plt.savefig(args.outputDir+"/"+name +args.extension)
    #return medianArray

###############################################
# main
###############################################



if __name__=='__main__':


    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument("-e",'--extension', help = 'figure extension (ex pdf, png,...)',default="png")
    parser.add_argument('-i', '--inputDir', help = 'Path of the input directory',default="DataStability/")#Data/TIDtest1/")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="PlotsStability/")
    parser.add_argument( "--display", type = argBool, required = False, default = False, help = "display plots on screen")
    parser.add_argument( "--advanced", type = argBool, required = False, default = 0, help = "more advanced plots ")
    parser.add_argument( "--onlyTZ", type = argBool, required = False, default = False, help = " show only TZ channels ")
    parser.add_argument( "--onlyVpa", type = argBool, required = False, default = False, help = " show only Vpa channels ")
    parser.add_argument( "--pixel", type = int, required = False, default = -1, help = " show only this pixel ")
    parser.add_argument( "--tsmin", type = int, required = False, default = -1, help = " time min ")
    parser.add_argument( "--tsmax", type = int, required = False, default = -1, help = " time max ")
    #parser.add_argument( "--rate", type = float, required = False, default = None, help = " Dose [MRad] ")
    #parser.add_argument( "--dose", type = int, required = False, default = 1, help = "timestamp converted in dose in MRads")
    parser.add_argument( "--cleaning", type = int, required = False, default = 1, help = "remove bad data")
    parser.add_argument( "--substractMedian", type = int, required = False, default = 0, help = " substract median value => measurements centered around 0 ")

    args = parser.parse_args()

    args.extension="."+args.extension

    # get list of pixels to be analyzed
    pixelArray=np.arange(120,135)
    #pixelArray=np.arange(120,225)
    if args.onlyVpa:
        pixelArray=np.arange(105,120)        
    if args.onlyTZ:
        pixelArray=np.arange(120,135)
    if args.pixel>0:
        pixelArray=[args.pixel]



    if not os.path.isdir(args.outputDir): 
        os.makedirs(args.outputDir)

    ###############################################
    # timestamo
    ###############################################

    #get list of timestamp with all measurements in order to have arrays with the same size (otherwise can't easily make difference,sum,...)
    tsSelList=[]#np.array([])
    tsSelArray=np.array([])
    if args.advanced:
        print ("====lll")
        fileList = sorted(        glob(args.inputDir+"/ts_*/Keithley/*/*all_bias*csv*"))#pixelProbeResultsDC_B8.csv
        for f in fileList:
            dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,NMax=anaUtils.getInfo(f)
            if args.tsmin>0 and ts<args.tsmin: continue
            if args.tsmax>0 and ts>args.tsmax: continue
            #print (ts, isBad(ts))
            ts=int(ts)
            if args.cleaning and isBad(ts): continue
            #print (ts)
            tsSelList.append(int(ts))
            #print (ts,  int(ts)/3600./24.-19333)

        if (len(tsSelList)==0):
            print ("No Keithley measurememts. Stop here. Try with --advanced 0")
            sys.exit()
        tsSelArray=tsSelList
    print (len(tsSelArray))

    ###############################################
    # Keithley
    ###############################################

    varNameList=[
        # "vbi_pa",
        # "vb_Rf",
        # "vb_TZ",
        # "vbo_pa",
        # "vb_dc_pa",
        # "i_offset",
        # "vbm1_disc",
        # "vb_n_fol",
        # "vb_p_fol",
        # "ibi_ref_bg",
        # "ibo_ref_bg",
        # "ibi_ota_10bdac",
        # "ibo_ota_10bdac",
        # "Vref_10bdac",
        # "Dll_ibi_ota",
        # "Dll_ibo_ota",
        # "Out_rpg_dac",
        "vtemp",
        # "Bg_I_temp1_20uA",
        # "Bg_I_temp2_20uA",
        # "Bg_I_monitor_20uA",
        # "Bg_I_pulse_10uA",
        # # "probe_dc_pa",
        # # "probe_vthc",
        # "Bg_I_dc_pa_10uA",
        # "Bg_I_vth_20uA",
        # # "Bg_I_vthc_1ÂµA",
        # "Vcasc_pa",
        # "Vcasc_disc",
        # "Vbi_disc",
        # "Vbo_disc",
        "Vbg",
        # "Vbm2_disc",
        # "PLL_ext_in_Vco",
        # "Vref_dac_RPG",
        "Vtcrl-120p-tot",
        "Vtcrl-120p_toa",
        "Vtcrl_140p-toa",
        "Vth",
        "monit_vdda",
        "monit_vddd",
        # "IN_PA_dummy"
    ]
    

    
    varMap={}
    for varName in varNameList:
        varMap[varName]=[]
        
    tsList=[]
    fileList = sorted(glob(args.inputDir+"/ts_*/Keithley/*/*all_bias*csv*"))
    #print (fileList)
    for f in fileList:
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,NMax=anaUtils.getInfo(f)
        if ts not in tsSelArray and len(tsSelArray)>0: continue
        df = pd.read_csv(f)
        tsList.append(ts)
        for varName in varNameList:
            val=df.loc [ (( df['label'] == varName))]["measured[mV]"].values[0] 
            #print (varName,val)
            varMap[varName].append(val)


    tsArray=np.array(tsList)
    print (len(tsArray))
    if len (tsList)>0:
        tsMin=np.min(tsArray)
        #tsArray-=np.min(tsArray)
        tsArray-=tsMin
        tsArray=tsArray/3600./24.
        pass

    for varName in varNameList:
        #print (varName,len(varMap[varName]))
        if len(varMap[varName])==0: continue
        plt.figure(figsize = (10, 5))    
        rel=   ( np.max(varMap[varName])-np.min(varMap[varName]))/float(np.median(varMap[varName]))
        plt.scatter(tsArray, varMap[varName],marker="o",label=" (max-min)/max :{:.5f}".format( rel))
        plt.ylabel(varName)
        plt.legend()
        plt.xlabel("Time [d]")
        
        plt.savefig(args.outputDir+"/Keithley_"+varName +args.extension)


    #toto
    ###############################################
    # Plots from npy files
    ###############################################
    

    plotInfo={}#files, label, doPlot, yRange
    plotInfo["Scope_num"]=(args.inputDir+"/ts_*/Scope/*/num.npy","Number of trigger ",True,[])
    plotInfo["Scope_noise"]=(args.inputDir+"/ts_*/Scope/*/noise.npy","Noise [mV] ",True,[])
    plotInfo["Scope_amplitude"]=(args.inputDir+"/ts_*/Scope/*/amplitude.npy","amplitude [mV] ",True,[])
    plotInfo["Keithley_Vthc"]=(args.inputDir+"/ts_*/Keithley/*/vthc.npy","Vthc [mV] ",True,[])
    plotInfo["Keithley_dcPa"]=(args.inputDir+"/ts_*/Keithley/*/dcPa.npy","dcPa [mV] ",True,[])
    plotInfo["vthScan_vth_Qdac_12"]=(args.inputDir+"/Plots/*vthScan*Q_12*thres.npy","Vth (Qdac=12) [DACU] ",True,[])
    plotInfo["vthScan_vth_Qdac_24"]=(args.inputDir+"/Plots/*vthScan*Q_24*thres.npy","Vth (Qdac=24) [DACU] ",True,[])
    plotInfo["vthcScan_vthc_Qdac_10"]=(args.inputDir+"/Plots/*Qdac10*vthcScan*thres.npy","Vthc (Qdac=10) [DACU] ",True,[])
    #plotInfo["vthcScan_vthc_Qdac_6"]=(args.inputDir+"/Plots/*Qdac6*vthcScan*thres.npy","Vthc (Qdac=6) [DACU]",True,[])
    plotInfo["vthcScan_vthc_Qdac_5"]=(args.inputDir+"/Plots/*Qdac5*vthcScan*thres.npy","Vthc (Qdac=4) [DACU]",True,[])
    plotInfo["vthScan_noise_Qdac_12"]=(args.inputDir+"/Plots/*vthScan*Q_12*noise.npy","Noise (Qdac=12) [DACU] (from Vth scan)",True,[0,4])
    plotInfo["chargeScan_toa_Q_4fC_Qthres5"]=(args.inputDir+"/Plots/*_Qdac5_*toaMean4.0.npy","TOA (Q=4fC) [DACU] ",True,[])
    plotInfo["chargeScan_toa_Q_10fC_Qthres5"]=(args.inputDir+"/Plots/*_Qdac5_*toaMean10.0.npy","TOA (Q=10fC) [DACU] ",True,[])
    plotInfo["chargeScan_toa_Q_10fC_Qthres10"]=(args.inputDir+"/Plots/*_Qdac10_*toaMean10.0.npy","TOA (Q=10fC) [DACU] ",True,[])
    plotInfo["chargeScan_tot_Q_10fC_Qthres10"]=(args.inputDir+"/Plots/*_Qdac10_*totMean10.0.npy","TOT (Q=10fC) [DACU] ",True,[])
    plotInfo["chargeScan_tot_Q_10fC_Qthres5"]=(args.inputDir+"/Plots/*_Qdac5_*totMean10.0.npy","TOT (Q=10fC) [DACU] ",True,[])

    plotInfo["chargeScan_jitter_Q_102fC_Qthres_10"]=(args.inputDir+"/Plots/*_Qdac10_*toaRMS102.0.npy","Jitter (Q=10fC) [DACU] ",True,[])
    plotInfo["chargeScan_jitter_Q_10fC_Qthres_10"]=(args.inputDir+"/Plots/*_Qdac10_*toaRMS10.0.npy","Jitter (Q=10fC) [DACU] ",True,[])
    plotInfo["chargeScan_jitter_Q_4fC_Qthres_5"]=(args.inputDir+"/Plots/*_Qdac5_*toaRMS4.0.npy","Jitter (Q=4fC) [DACU] ",True,[])
    #plotInfo["chargeScan_jitter_Q_4fC_Qthres_6"]=(args.inputDir+"/Plots/*_Qdac6_*toaRMS4.0.npy","Jitter (Q=4fC) [DACU] ",True,[])
    plotInfo["chargeScan_thres_Qthres_5"]=(args.inputDir+"/Plots/*_Qdac5_*chargeScan*thres.npy","Thres [fC] ",True,[])
    #plotInfo["chargeScan_thres_Qthres_6"]=(args.inputDir+"/Plots/*_Qdac6_*chargeScan*thres.npy","Thres [fC] ",True,[])
    plotInfo["chargeScan_thres_Qthres_10"]=(args.inputDir+"/Plots/*_Qdac10_*chargeScan*thres.npy","Thres [fC] ",True,[])
    plotInfo["chargeScan_effQ0_Qthres_5"]=(args.inputDir+"/Plots/*_Qdac5_*chargeScan*effQ0.npy","Eff ",True,[])
#    plotInfo["chargeScan_effQ0_Qthres_6"]=(args.inputDir+"/Plots/*_Qdac6_*chargeScan*effQ0.npy","Eff ",True,[])
    plotInfo["chargeScan_effQ0_Qthres_10"]=(args.inputDir+"/Plots/*_Qdac10_*chargeScan*effQ0.npy","Eff ",True,[])
    plotInfo["chargeScan_noise_Qthres_5"]=(args.inputDir+"/Plots/*_Qdac5_*chargeScan*noise.npy","Noise [fC] ",True,[0,0.5])
    #    plotInfo["chargeScan_noise_Qthres_6"]=(args.inputDir+"/Plots/*_Qdac6_*chargeScan*noise.npy","Noise [fC] ",True,[0,0.5])
    plotInfo["chargeScan_noise_Qthres_10"]=(args.inputDir+"/Plots/*_Qdac10_*chargeScan*noise.npy","Noise [fC] ",True,[0,0.5])

    plotInfo["delayScan_nbOfPoints_toa_pulser"]=(args.inputDir+"/Plots/*Qdac10_delayScan_ExtDiscri_False*nbOfPoints.npy","Number of points",True,[])#,[0,32])
    plotInfo["delayScan_lsb_toa_pulser"]=(args.inputDir+"/Plots/*Qdac10_delayScan_ExtDiscri_False*lsb.npy","TOA LSB [ps] ",True,[10,32])#,[0,32])
    plotInfo["delayScan_lsb_toa"]=(args.inputDir+"/Plots/*delayScan_ExtDiscri_True*lsb.npy","TOA LSB [ps] ",True,[10,32])#,[0,32])
    plotInfo["delayScan_nbOfPoints_toa"]=(args.inputDir+"/Plots/*delayScan_ExtDiscri_True*nbOfPoints.npy","Number of points ",True,[])#,[0,32])
    plotInfo["widthScan_lsb_tot"]=(args.inputDir+"/Plots/*widthScan*lsb.npy","TOT LSB [ps] ",True,[100,150])
    plotInfo["widthScan_nbOfPoints_tot"]=(args.inputDir+"/Plots/*widthScan*nbOfPoints.npy","Number of points ",True,[])

#    plotInfo["delayScan_lsb_toa_pulser"]=(args.inputDir+"/Plots/*Qdac10_delayScan_ExtDiscri_False*lsb.npy","TOA LSB [ps] ",True,[0,32])
#    plotInfo["delayScan_lsb_toa"]=(args.inputDir+"/Plots/*delayScan_ExtDiscri_True*lsb.npy","TOA LSB [ps] ",True,[0,32])
#    plotInfo["widthScan_lsb_tot"]=(args.inputDir+"/Plots/*widthScan*lsb.npy","TOT LSB [ps] ",True,[100,200])

    plotData={}

    xlabel="Time [d]"

    for name,info in plotInfo.items():
        #print ("=========== ",name,[])
        regex=info[0]
        ylabel=info[1]
        doPlot=info[2]
        yRange=info[3]
        tsArray,varArray=getArrays(name,regex,ylabel,tsSelArray)
        plotData[name]=(tsArray,varArray)
        #print ("TOTO",name,len(plotData[name][0]))
        # if name=="chargeScan_jitter_Q_10fC":
        #     print (np.shape(varArray),tsArray)
        #     print ( varArray[107])
        #     toto

        if doPlot:# or not args.advanced:
            #if name!="chargeScan_jitter_Q_10fC_Qthres_10": continue
            varMap[name]=makePlot(tsArray,varArray,name,xlabel,ylabel,pixelArray,yRange=yRange,substractYMedian=args.substractMedian)
            




    ###################################
    # advanced
    ##################################

    #print ("Missing data for ",set(missing))
    if args.advanced:

        #amplitude
        #print (plotData["vthScan_vth_Qdac_24"][1],plotData["vthScan_vth_Qdac_12"][1])
        #if np.array_equal(plotData["vthScan_vth_Qdac_24"][1],plotData["vthScan_vth_Qdac_12"][1]):

        
        print ("===============")
        tsList=plotData["vthScan_vth_Qdac_12"][0]
        amplitudeArray=plotData["vthScan_vth_Qdac_24"][1]-plotData["vthScan_vth_Qdac_12"][1]
        makePlot(tsList,amplitudeArray,"A_DeltaVth",xlabel,"Vth (Qdac=24) -Vth (Qdac=12) [DACU]",pixelArray,substractYMedian=args.substractMedian,yRange=[30,100])
        
        
        #SOverN
        #if np.array_equal(amplitudeArray,plotData["vthScan_noise_Qdac_12"][1]):
        SOverNArray=amplitudeArray/plotData["vthScan_noise_Qdac_12"][1]
        #makePlot(tsList,SOverNArray,"A_SOverN",xlabel,"(Vth (Qdac=24) -Vth (Qdac=12) ) / noise",pixelArray,yRange=[0,60],substractYMedian=args.substractMedian)
        
        
        #Jitter 10fC
        #if np.array_equal(plotData["chargeScan_jitter_Q_10fC"][1],plotData["delayScan_lsb_toa_pulser"][1]):
        jitterQ10fCArray=plotData["chargeScan_jitter_Q_10fC_Qthres_10"][1]*plotData["delayScan_lsb_toa"][1]
        makePlot(tsList,jitterQ10fCArray,"A_chargeScan_jitter_Q_10fC_Qthres_10_ps",xlabel,"Jitter (Q=10fC) [ps]",pixelArray,substractYMedian=args.substractMedian)

        #Jitter 102fC
        #if np.array_equal(plotData["chargeScan_jitter_Q_102fC"][1],plotData["delayScan_lsb_toa_pulser"][1]):
        jitterQ102fCArray=plotData["chargeScan_jitter_Q_102fC_Qthres_10"][1]*plotData["delayScan_lsb_toa"][1]
        makePlot(tsList,jitterQ102fCArray,"A_chargeScan_jitter_Q_102fC_Qthres10_ps",xlabel,"Jitter (Q=102fC) [ps]",pixelArray,substractYMedian=args.substractMedian)
        
        #Jitter 4fC
        #if np.array_equal( plotData["chargeScan_jitter_Q_4fC"][1],plotData["delayScan_lsb_toa_pulser"][1]):
        jitterQ4fCArray=plotData["chargeScan_jitter_Q_4fC_Qthres_5"][1]*plotData["delayScan_lsb_toa"][1]
        makePlot(tsList,jitterQ4fCArray,"A_chargeScan_jitter_Q_4fC_Qthres_5_ps",xlabel,"Jitter (Q=4fC) [ps]",pixelArray,yRange=[30,70],substractYMedian=args.substractMedian)
        #jitterQ4fCArray=plotData["chargeScan_jitter_Q_4fC_Qthres_6"][1]*plotData["delayScan_lsb_toa"][1]
        #makePlot(tsList,jitterQ4fCArray,"A_chargeScan_jitter_Q_4fC_Qthres_6_ps",xlabel,"Jitter (Q=4fC) [ps]",pixelArray,yRange=[],substractYMedian=args.substractMedian)

        #toa 10fc "chargeScan_toa_Q_10fC_Qthres10"
        toaQ10fCArray=plotData["chargeScan_toa_Q_10fC_Qthres10"][1]*plotData["delayScan_lsb_toa"][1]
        makePlot(tsList,toaQ10fCArray,"A_chargeScan_toa_Q_10fC_Qthres_10_ps",xlabel,"Toa (Q=10fC) [ps]",pixelArray,substractYMedian=args.substractMedian)


        #tot 10fc "chargeScan_tot_Q_10fC_Qthres10"
        totQ10fCArray=plotData["chargeScan_tot_Q_10fC_Qthres10"][1]*plotData["widthScan_lsb_tot"][1]
        makePlot(tsList,totQ10fCArray,"A_chargeScan_tot_Q_10fC_Qthres_10_ps",xlabel,"TOT (Q=10fC) [ps]",pixelArray,substractYMedian=args.substractMedian)#,yRange=[1500,2500])

        #tot 10fc "chargeScan_tot_Q_10fC_Qthres5"
        totQ10fCArray=plotData["chargeScan_tot_Q_10fC_Qthres5"][1]*plotData["widthScan_lsb_tot"][1]
        makePlot(tsList,totQ10fCArray,"A_chargeScan_tot_Q_10fC_Qthres_6_ps",xlabel,"TOT (Q=10fC) [ps]",pixelArray,substractYMedian=args.substractMedian)#,yRange=[2000,3000])





        # correlation plots
        #jitter vs Vth
        makePlot(varMap["vtemp"],plotData["Keithley_Vthc"][1],"C_Vthc_vs_vtemp","Vtemp [mV]","Vthc [mV]",pixelArray,doMedian=False,yRange=[],substractYMedian=True)
        # makePlot(varMap["vtemp"],plotData["vthScan_vth_Qdac_12"][1],"C_VthQ12_vs_vtemp","Vtemp [mV]","VthQ12 [DACU]",pixelArray,doMedian=False,yRange=[],substractYMedian=True)
        #makePlot(varMap["vtemp"],plotData["widthScan_lsb_tot"][1],"C_TOT_vs_vtemp","Vtemp [mV]","TOT [ps]",pixelArray,doMedian=False)#,yRange=[-0.2,0.2],substractYMedian=False)
        print (plotData["Scope_amplitude"][1][120])
#-plotData["vthScan_vth_Qdac_12"][1]
        makePlot(varMap["vtemp"],plotData["Scope_amplitude"][1],"C_Amp_vs_vtemp","Vtemp [mV]","Probe amplitude [mV]",pixelArray,doMedian=False,substractYMedian=1)
        

        makePlot(varMap["vtemp"],amplitudeArray,"C_DeltaVth_vs_vtemp","Vtemp [mV]","Vth(10fC)-Vth(5fC) [dac]",pixelArray,doMedian=1,substractYMedian=0,yRange=[30,50])

        

        makePlot2(plotData["vthcScan_vthc_Qdac_10"][1],plotData["chargeScan_toa_Q_10fC_Qthres10"][1],"C_TOA_vs_vthcQ10","Vthc [DACU]","TOA",pixelArray,substractYMedian=False)#,yRange=[])
        

        
###############################################
# 
###############################################

if args.display:
    plt.show()

