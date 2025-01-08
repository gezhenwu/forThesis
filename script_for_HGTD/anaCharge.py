###############################################
#
###############################################
import os,sys,re
import argparse
from glob import glob
import random

curpath = os.getcwd()
sys.path.insert(0,curpath)

import numpy as np
import matplotlib; 
matplotlib.use('Agg') 
matplotlib.use('pdf') 
import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd    
from os import listdir
from os.path import isfile, join
from scipy.optimize import curve_fit
import time

from lib import anaUtils
anaUtils.matplotlibConfig()
#import ASICConfig
from lib import altiroc3_Mix046

xticks=[2,4,6,8,10,20,50,100]    


###############################################
# main
###############################################


if __name__=='__main__':
    startTime0 = time.time()

    ####################################
    # parameters
    ####################################
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument( "-v","--altirocVersion", type = int, required = False, default = 3, help = "ALTIROC version")
    parser.add_argument( "--onlyEff", type = argBool, required = False, default = False, help = "")
    parser.add_argument( "--onlyTZ", type = argBool, required = False, default = True, help = "save combined Eff file")
    parser.add_argument( "--saveEff", type = argBool, required = False, default = False, help = "save combined Eff file")
    parser.add_argument( "--saveCSV", type = argBool, required = False, default = False, help = "save combined CSV file")
    parser.add_argument("-f",'--dfFileName', help = 'cvs for combined data frame',default=None)
    parser.add_argument("-e",'--extension', help = 'figure extension',default="png")
    parser.add_argument('-i', '--inputDir', help = 'Path of the data directory',default="Data/2022_01_19/chargeScan/")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument( "--make2D", type = argBool, required = False, default = False, help = "2D plots")
    parser.add_argument( "--debug", type = argBool, required = False, default = False, help = "debug")
    parser.add_argument( "--readAllPixels", type = argBool, required = False, default = False, help = "readAllPixels")
    parser.add_argument( "--smallCtest", type = argBool, required = False, default = True, help = "small Ctest")
    parser.add_argument( "--noLSBCor", type = argBool, required = False, default = False, help = "no LSB cor")
    parser.add_argument('--toaLSB', help = 'toa LSB File',default=None)
    parser.add_argument('--totLSB', help = 'tot LSB File',default=None)    
    parser.add_argument('--QList', help = ' charge values used to make additionnal plots',default=None)#in fC
    #parser.add_argument( "--more", type = argBool, required = False, default = False, help = "more")
    parser.add_argument('--blackList', help = ' pixels removed',default=None)#in fC
    parser.add_argument('--pixList', help = ' selected pixels',default=None)#in fC
    
    args = parser.parse_args()


    
    if args.inputDir.find("FastFADA_ALTIROC2")>=0 or args.inputDir.find("Data2")>=0 :
        print ("ALTIROC VERSION 2")
        args.altirocVersion=2

    if args.inputDir.find("Ctest_208")>=0:
        args.smallCtest=False

    if not os.path.isdir(args.outputDir):os.makedirs(args.outputDir)

    blackList=[]
    if args.blackList is not None:
        blackList=[float(i) for i in args.blackList.split(",")]
        pass

    #blackList=list(set( list(range(0,60)) + list(range(0,225,15)) + list(range(1,225,15)) + list(range(2,225,15)) + list(range(3,225,15))  ))
    #blackList=list(set(list(range(0,225,15)) + list(range(1,225,15)) + list(range(2,225,15))+ list(range(3,225,15)) )) #masking for B15
    #blackList=[0]
    #indices = [i for i in range(0, 225, 30)]      
    #for indice in indices:blackList.extend(list(range(225))[indice:indice+15]) #masking for FIB


    if args.pixList is not None:
        pixList=[float(i) for i in args.pixList.split(",")]





    ####################################
    # Information for DAC to fC conversion
    ####################################
    smallCtest=40#208/5.2
    largeCtest=208.
    Ctest=largeCtest
    if  args.smallCtest==True:
        Ctest=smallCtest

    if args.altirocVersion==3:
        SLOPE_LR=0.00170  #low range
        SLOPE_HR=0.00784  #high range
        HIGHLOWRATIO=SLOPE_HR/SLOPE_LR
        QCONV=SLOPE_LR*largeCtest
        OFFSET_LC=0.0090 #LC: Large Ctest
        QOFFSET=OFFSET_LC*largeCtest
        if args.smallCtest:
            QCONV=QCONV*smallCtest/largeCtest
            OFFSET_SC=0.0035
            QOFFSET=OFFSET_SC*smallCtest
    elif args.altirocVersion==2:
        QOFFSET=0.0045*largeCtest
        QCONV=0.00199*largeCtest
        HIGHLOWRATIO=7.92/1.99#1.7/0.4#7.8/1.7


    ####################################
    #get data
    ####################################
    print ("Get Data")
    if args.dfFileName is not None:

        outName=args.outputDir+"/"+args.dfFileName.split("/")[-1].replace(".csv","")
        df=pd.read_csv(args.dfFileName)        
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(args.dfFileName)

    else:

        #output name
        if args.inputDir[-1]!="/":args.inputDir+="/"
        outName=args.outputDir+"/"+args.inputDir.replace("/","_").replace("..","").replace("_outputNikola_","")#.replace("thresScan_","").replace("vthcScan_","")
        outName=outName.replace("VthcForAllChannels","").replace("_CapaRemoved","")
        outName=outName.replace("Data_","")        

        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,NMax,CtestForDataTaking,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(args.inputDir)

        #object to store all the data
        df = pd. DataFrame()

        #get timing files
        fileList = [y for x in os.walk(args.inputDir) for y in glob(os.path.join(x[0], '*timing*.csv'))]

        #get data
        allDF=[]
        for ftiming in sorted(fileList):       
            vec=ftiming.replace(".csv","").replace("/","_").split("_")
            dacCharge=0
            if "dacCharge" in vec:dacCharge=int(vec[vec.index("dacCharge")+1])
            if "pixelInj" in vec:
                pixelInj=vec[vec.index("pixelInj")+1]
            else: continue
            pixelList=altiroc3_Mix046.getPixelList(pixelStr=pixelInj)


            # for dacCharge in range(127):
            #     charge=anaUtils.getDCPulser(dacCharge,args.smallCtest)*Ctest/1000.
            #     print (dacCharge,charge)
            # toto

            #convert charge in fC
            if dacCharge in range(64,78):continue # remove points from the 2nd register overlapping with the first one
            if args.altirocVersion==3:
                charge=anaUtils.getDCPulser(dacCharge,args.smallCtest)*Ctest/1000.
                #charge=dacCharge
            else:
                if dacCharge<=63:charge=QOFFSET+dacCharge*QCONV#in fact it is not anymore a dacCharge
                else:charge=QOFFSET+(dacCharge-64)*HIGHLOWRATIO*QCONV

            #get timing data
            try:
                timingdf = pd.read_csv(ftiming)
            except:
                print ("can't read ",ftiming)
                continue
            
            timingdf['dacCharge']=dacCharge
            timingdf['charge']=charge
            if args.pixList is not None:
                pixelList=pixList
            if len(blackList)>0:
                pixelList = [e for e in pixelList if e not in blackList]

        #    print( blackList,pixelList)

            #pixelList=list(range(1,225))
            if not args.readAllPixels:
                #print (pixelList)
                timingdf=timingdf[timingdf['pixel'].isin(pixelList)]#only keep pixel with injected signals

            #get meta data
            #fmeta=ftiming.replace("timing_data","meta_data_ch")
            #metadf = pd.read_csv(fmeta)
            allDF.append(timingdf)

        #concatene all data frames
        df=pd.concat(allDF)
        # df = df[df["asic"]==3] #zhenwu add, to select the asic

        if args.saveCSV: 
            df.to_csv(outName+"_combined.csv")

    if len(df.index)==0:
        print ("There is no data to analyse! stop here....",ts)
        sys.exit()

    
    #select some charges to make plots
    chargeArray=np.sort(np.unique(df['charge'].values))
    QList= sorted(list(set([anaUtils.closest_to_target(chargeArray, i) for i in [1,3,3.5,4,4.5,5,6,7,8,9,10,12,15,20,30,40,50,60,70,80,90,100]])))
    QPlotList= sorted(list(set([anaUtils.closest_to_target(chargeArray, i) for i in [4.5,10,20,100]])))
    print ("QList:",QList)
    print("QPLotList: ",QPlotList)


    # data dictionnary to summaryze data
    dataMap={}
    for counter,Q in enumerate(QList):
        dataMap[(Vth,Q)]=[1,0,0,0,0,0,0]

    print ("Get Data %3.3f sec" %(time.time() - startTime0))

    ####################################
    # LSB
    ####################################

    LSBDIR="LSB/"
    if args.altirocVersion==2:
        LSBDIR="LSB/ALTIROC2/"

    toalsbArray=np.full(anaUtils.nbOfPixels,1)
    toaUnitStr="[DACU]"
    toalsbMedian=1
    totlsbArray=np.full(anaUtils.nbOfPixels,1)
    totUnitStr="[DACU]"
    totlsbMedian=1

    if not args.noLSBCor:
        if args.toaLSB is not None:
            toalsbArray=np.load(args.toaLSB)
            toaUnitStr="[ps]"
            toalsbMedian=anaUtils.median(args,toalsbArray[toalsbArray>1])
        else:
            try:
                print (LSBDIR+"B_"+str(board)+"_TOA_LSB_all_"+Inj+".npy")            
                toalsbArray=np.load(LSBDIR+"B_"+str(board)+"_TOA_LSB_all_"+Inj+".npy")            
                toaUnitStr="[ps]"
                toalsbMedian=anaUtils.median(args,toalsbArray[toalsbArray>1])
                toalsbMedian=25##ATT!!!!!

            except:
                print ("PRB WITH TOA LSB!")

        #print (toalsbArray)
        if args.totLSB is not None:
            totlsbArray=np.load(args.totLSB)
            totUnitStr="[ps]"
            totlsbMedian=anaUtils.median(args,totlsbArray[totlsbArray>1])
        else:
            try:
                totlsbArray=np.load(LSBDIR+"B_"+str(board)+"_TOT_LSB_all_"+Inj+".npy")            
                totUnitStr="[ps]"
                totlsbMedian=anaUtils.median(args,totlsbArray[totlsbArray>1])
                totlsbMedian=200#ATT!!!
            except:
                print ("PRB WITH TOT LSB!")

    # toalsbArray=np.full(anaUtils.nbOfPixels,20)
    # toalsbMedian=anaUtils.median(args,toalsbArray[toalsbArray>1])
    # totlsbArray=np.full(anaUtils.nbOfPixels,140)
    # totlsbMedian=200#ATT!!!

    ####################################
    # Efficiency
    ####################################
    print ("Compute Efficiency")
    effThres=0.95
    nNoisy=0
    noisyPixels= np.empty(0)

    # compute all efficiencies
    QForEffList=np.sort(np.unique(QPlotList+list(chargeArray[chargeArray<1])))
    print (QForEffList)
    allEffList,allNList,thresArray=anaUtils.getAllEff(df,chargeArray,"charge",effThres=effThres,doInterpolation=True,NMax=NMax)

    if len(chargeArray)>0:
        effSliceList=anaUtils.getYSlices([chargeArray]*anaUtils.nbOfPixels,allEffList,QForEffList)
        NSliceList=anaUtils.getYSlices([chargeArray]*anaUtils.nbOfPixels,allNList,QForEffList)


        #count the number of noisy pixels
        # plot N maps
        for counter,NArray in enumerate(NSliceList):
            Qmax=0.5# there are 16 dacCharge below 1fC and 7 below 0.5fC
            if QForEffList[counter]>Qmax: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(NArray/NMax, clabel='Noise occupancy')#,cmap='viridis')
            plt.savefig(outName +"_StatMap_Q"+str(QForEffList[counter])+"."+args.extension)
            plt.close()
            np.save(outName+"_statQ"+str(QForEffList[counter]),NArray)
            nNoisy+=np.sum(NArray)
            toto=np.where(NArray > 0)[0]
            noisyPixels = np.concatenate((noisyPixels, toto[~np.in1d(toto, noisyPixels)]))
            #nNoisy+=anaUtils.counterAboveThres(args,NArray,thres=0.005,N=1)



        effMap={}
        for counter,effArray in enumerate(effSliceList):        
            #median=anaUtils.median(args,effArray)
            mean=anaUtils.mean(args,effArray)
            #print (QForEffList)
            effMap[(Vth,QForEffList[counter])]=mean
            if QForEffList[counter] in QList:
                dataMap[(Vth,QForEffList[counter])][0]=mean
                dataMap[(Vth,QForEffList[counter])][1]=nNoisy
            #if QForEffList[counter] not in QPlotList: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(effArray, clabel='EFF ')#,cmap="viridis")
            plt.savefig(outName +"_effMap_Q"+str(QForEffList[counter])+"."+args.extension)
            np.save(outName+"_effQ"+str(QForEffList[counter]),effArray)
            plt.close()
                # # noise 1D
                # plt.figure(figsize = (20, 10))
                # #plt.grid()
                # plt.plot(range(0,anaUtils.nbOfPixels) , effArray,label="Median: {:.2f} {:.2f}".format(anaUtils.median(args,effArray[0:ASICConfig.lastVpaPixel]),anaUtils.median(args,effArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )))

                # plt.ylabel('Eff Q='+str(QForEffList[counter]))
                # plt.xlabel('Pixel number')
                # plt.ylim(bottom = 0)#,top=8)
                # plt.legend()
                # plt.savefig(outName+"_eff."+args.extension)
                # plt.close()


        # thres map
        if args.debug:
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(thresArray, clabel='Q [fC]')
            plt.savefig(outName+"_thresMap."+args.extension)
            plt.close()

        # thres 1D
        plt.figure(figsize = (20, 10))
        #plt.grid()
        #plt.plot(range(0,anaUtils.nbOfPixels) , thresArray,label="Median: {:.2f} {:.2f} RMS: {:.2f} {:.2f}".format(anaUtils.median(args,thresArray[0:ASICConfig.lastVpaPixel]),anaUtils.median(args,thresArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )  ,  np.std(thresArray[0:ASICConfig.lastVpaPixel]),np.std(thresArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )    ))
        thresMedian=anaUtils.median(args,thresArray,veto=0.5)
        #print (thresArray,thresMedian)
        #thresMedian=Vth#anaUtils.median(args,thresArray)
        plt.plot(range(0,anaUtils.nbOfPixels) , thresArray,label="Median: {:.2f} RMS: {:.2f}".format(thresMedian  ,  np.std(thresArray)))
        plt.ylabel('Q [fC]')
        plt.xlabel('Pixel Number')
        #plt.ylim(bottom=0)#,top=10)
        plt.legend()
        plt.savefig(outName+"_thres."+args.extension)
        plt.close()

        if args.debug:
            # thres 1D
            plt.figure(figsize = (13, 10))
            anaUtils.colSlice(thresArray, clabel=' Jitter '+toaUnitStr,ylabel="Threshold [fC] ",label="")            
            plt.grid()
            plt.ylim(bottom=0)#,top=5*toalsbMedian)
            plt.savefig(outName +"_thresVsRowNumber."+args.extension)
            plt.close()

        # plot all eff
        noiseArray=np.zeros(anaUtils.nbOfPixels)
        thresAltArray=np.zeros(anaUtils.nbOfPixels)
        figall=plt.figure("alleff",figsize = (10, 10))
        figgood=plt.figure("good",figsize = (20, 10))
        figbad=plt.figure("bad",figsize = (20, 10))
        for pixel in range(anaUtils.nbOfPixels):
            plt.figure("alleff")
            if args.saveEff:
                np.savez(outName+"_eff_"+str(pixel)+'.npz', array1=chargeArray, array2=allEffList[pixel])

            plt.plot(chargeArray, allEffList[pixel],marker="o")

            pinit=[0.5,thresArray[pixel],-0.3]
            popt=[999,999,999]
            noise=0
            #thres=thresArray[pixel]
            if len(chargeArray)>0:
                index=np.argmax(chargeArray==thresArray[pixel])
                delta=20

                if np.sum(allEffList[pixel])==0:
                    noise=0
                    popt[1]=0
                else:
                    try:
                        popt, pcov = curve_fit(anaUtils.myerf, chargeArray, allEffList[pixel],p0=pinit)
                        noise=abs(popt[2])
                        #compute thres from fit
                        #x=np.arange(thresArray[pixel]-1,thresArray[pixel]+1,0.01)
                        #y=anaUtils.myerf(x,popt[0],popt[1],popt[2])
                        #thres=anaUtils.getCrossingPoint(x,y,effThres,0.5, fromTopToBottom = False,doInterpolation=False)
                        #if abs(popt[2])<0.1:
                        plt.figure("good")
                        plt.plot(chargeArray, allEffList[pixel],label=str(pixel)) 
                    except: #the failed fits should be further investigated            
                        print ("Fail fit for pixel: ",pixel)
                        plt.figure("bad")
                        plt.plot(chargeArray,allEffList[pixel])#[index-delta:index+delta]

            #print (popt[2])


            ####thresArray[pixel]=thres
            noiseArray[pixel] = noise
            thresAltArray[pixel] = popt[1]

        np.save(outName+"_noise",noiseArray)
        np.save(outName+"_thres",thresArray)

        if np.sum(noiseArray)>0:
            if args.debug:
                # noise map
                plt.figure(figsize = (13, 10))
                anaUtils.asic_map(noiseArray, clabel='Noise [fC]')
                plt.savefig(outName+"_noiseMap."+args.extension)
                plt.close()

        # noise 1D
        plt.figure(figsize = (20, 10))
        #plt.grid()
        noiseMedian=anaUtils.median(args,noiseArray,veto=0.3)
        plt.plot(range(0,anaUtils.nbOfPixels) , noiseArray,label="Median: {:.2f}".format(noiseMedian))
        plt.ylabel('Noise [fC]')
        plt.xlabel('Pixel number')
        plt.ylim(bottom = 0)#,top=8)
        plt.legend()
        plt.savefig(outName+"_noise."+args.extension)
        plt.close()


        if args.debug:
            # noise 1D
            plt.figure(figsize = (13, 10))
            anaUtils.colSlice(noiseArray, clabel=' Jitter '+toaUnitStr,ylabel="Noise [fC] ",label="")            
            plt.grid()
            plt.ylim(bottom=0)
            plt.savefig(outName +"_noiseVsRowNumber."+args.extension)
            plt.close()

        plt.figure("alleff")
        plt.xlabel("Q [fC]")
        plt.ylabel('Efficiency')
        plt.ylim(0,1.1)
        plt.xlim(0,20)
        plt.legend()
        plt.savefig(outName +"_allEff."+args.extension)
        plt.xlim(0,6)
        plt.ylim(0,1.1)
        #anaUtils.setLogx(plt,1,xticks) 
        plt.grid()
        plt.legend()
        #plt.text(0.12, 1.01,"B"+str(board), fontsize = 20)#,ha='right', va='bottom')
        plt.text(0.12, 1.04,"B"+str(board)+"      vth: "+str(Vth)+"    thres: "+str(round(thresMedian,1))+"fC    noise: "+str(round(noiseMedian,2))+" fC", fontsize = 20)#,ha='right', va='bottom')
        plt.text(0.12, 1.01,str(nNoisy), fontsize = 10)#,ha='right', va='bottom')
        plt.savefig(outName +"_allEffZoom."+args.extension)
        if args.debug:
            plt.figure("good")
            plt.xlabel("Q [fC]")
            plt.ylabel('Efficiency')
            plt.xlim(0,6)
            plt.savefig(outName +"_goodeff."+args.extension)
            plt.figure("bad")
            plt.xlabel("Q [fC]")
            plt.ylabel('Efficiency')
            plt.savefig(outName +"_eff_failed_fit."+args.extension)
            plt.close()




    nNoisyPixels=len(noisyPixels)
    f=open(outName+"_noise.dat","w")
    try:
        HV = int(re.search(r'HV_(\d+)', args.inputDir).group(1))
        ILEAK = float(re.search(r'Ileak_(\d+)', args.inputDir).group(1))
    except:
        HV=0
        ILEAK=0
    f.write("%d,%d,%f,%d,%f,%d\n"%(board,HV,ILEAK,Vth,nNoisy/(NMax*225),nNoisyPixels))
    f.close()

    if args.onlyEff==True:
        exit()

    print ("Compute Efficiency %3.3f sec "%(time.time() - startTime0))
    ####################################
    # make 2D plots
    ####################################
    #anaUtils.makeAll2DPlots(df,"charge","toa", np.arange(0,20,1),np.arange(0,127,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=0)


    if args.make2D:

        anaUtils.makeAll2DPlots(df,"charge","toa", np.arange(0,20,1),np.arange(0,128,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=0)

        anaUtils.makeAll2DPlots(df,"charge","tot", np.arange(0,20,1),np.arange(0,30,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=0)

        anaUtils.makeAll2DPlots(df,"tot","toa", np.arange(0,30,1),np.arange(0,128,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=0)


        #anaUtils.makeAll1DPlots(df.loc [ (( df['charge'] == 24))],"toa", np.arange(0,100,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=1)
        pass

    ####################################
    # Compute Mean and RMS for TOA
    ####################################
    print ("Analysis TOA and TOT")
    #compute mean and RMS for TOA
    toaMeanList,toaRMSList,chargeForTOAList= anaUtils.getAllMeanRMS(df[df["toa"]<=127],"charge","toa",ymax=128*toalsbMedian,corArray=toalsbArray)
    #if args.debug:QList=list(set(list(chargeForTOAList[120])+list(chargeForTOAList[135])+list(chargeForTOAList[210])))#[::5] #ugly

    #print ("chargeForTOA for channel 1:",chargeForTOAList[1])


    # compute 1D toa slices
    #print (chargeForTOAList)
    toaMeanSliceList=anaUtils.getYSlices(chargeForTOAList,toaMeanList,QList)
    toaRMSSliceList=anaUtils.getYSlices(chargeForTOAList,toaRMSList,QList)


    # plot all toaMean    
    plt.figure(figsize = (20, 10))
    for pixel in range(anaUtils.nbOfPixels):
        plt.plot(chargeForTOAList[pixel], toaMeanList[pixel],marker="o")
        
    plt.xlabel('Q [fC]')
    plt.ylabel('TOA mean '+toaUnitStr)
    plt.ylim(bottom = 0,top=127*toalsbMedian)
    plt.xlim(left = 2.)#,right=10)
    #anaUtils.setLogx(plt,4,xticks) 
    plt.savefig(outName +"_toaMean."+args.extension)
    plt.close()

    # plot toaMean slices
    plt.figure(figsize = (20, 10))
    for counter,toaArray in enumerate(toaMeanSliceList):
        median=anaUtils.median(args,toaArray)
        rms=np.std(toaArray)
        dataMap[(Vth,QList[counter])][2]=median
        if QList[counter] not in QPlotList: continue
        plt.plot(range(0,anaUtils.nbOfPixels), toaArray,label="{:.1f}fC Median: {:.2f} RMS: {:.2f}".format(QList[counter],median,rms   ))       
        np.save(outName+"_toaMean"+str(QList[counter]),toaArray)
    plt.xlabel('Pixel Number')
    plt.ylabel('TOA mean '+toaUnitStr)
    plt.ylim(bottom = 0,top=127*toalsbMedian)
    plt.legend()
    plt.savefig(outName +"_toaMeanVsPixelNb."+args.extension)
    plt.close()

    # plot toaMean maps
    if args.debug:
        for counter,toaArray in enumerate(toaMeanSliceList):
            if QList[counter] not in QPlotList: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(toaArray, clabel='TOA '+toaUnitStr)
            plt.savefig(outName +"_toaMeanMap_Q"+str(QList[counter])+"."+args.extension)
            plt.close()



    # plot toaRMS slices
    jitterMap={}
    medianJitterList=np.zeros(len(toaRMSSliceList))
    plt.figure(figsize = (20, 10))
    for counter,toaArray in enumerate(toaRMSSliceList):
        median=anaUtils.median(args,toaArray)
        rms=np.std(toaArray)
        jitterMap[(Vth,QList[counter])]=median
        dataMap[(Vth,QList[counter])][3]=median
        dataMap[(Vth,QList[counter])][4]=rms
        TZvec=toaArray[altiroc3_Mix046.firstTZPixel:altiroc3_Mix046.nbOfPixels]
        if len(TZvec)>0:
            medianTZ=anaUtils.median(args,TZvec[TZvec>0])
        medianJitterList[counter]=medianTZ
        if QList[counter] not in QPlotList: continue
        plt.plot(range(0,anaUtils.nbOfPixels), toaArray,label="{:.1f}fC Median: {:.2f} RMS: {:.2f}".format(QList[counter],median,rms   ))
        np.save(outName+"_toaRMS"+str(QList[counter]),toaArray)

    plt.xlabel('Pixel Number')
    plt.ylabel('TOA RMS '+toaUnitStr)
    plt.ylim(bottom=0,top=80)#5*toalsbMedian)
    plt.xlim(left=0,right=225)
    #plt.xlim(left=1,right=14)
    plt.legend()
    plt.savefig(outName +"_toaRMSVsPixelNumber."+args.extension)
    #plt.savefig(outName +"_toaRMSVsPixelNumber.pdf")
    plt.close()



     # plot all toaRMS
    plt.figure(figsize = (20, 10))
    for pixel in range(anaUtils.nbOfPixels):
        #if QList[counter] not in QPlotList: continue
        #if len(toaRMSList[pixel])>0 and max(toaRMSList[pixel][5:])>150: print (pixel,toaRMSList[pixel])
        plt.plot(chargeForTOAList[pixel], toaRMSList[pixel])#, alpha=0.3)
        #print ("======+>",(chargeForTOAList[pixel]))
    if args.debug: plt.plot(QList,medianJitterList,color="black",linestyle="dashed",linewidth=5)
    plt.xlabel('Q [fC]')
    plt.ylabel('TOA RMS '+toaUnitStr)
    plt.ylim(bottom = 0,top=4*toalsbMedian)
    plt.xlim(left = 2.)#, right=40)
    #anaUtils.setLogx(plt,4,xticks)
    plt.savefig(outName +"_toaRMS."+args.extension)
    plt.close()

    # plot median toaRMS
    if args.debug:
        plt.figure(figsize = (20, 10))
        plt.plot(QList,medianJitterList,linewidth=5,label="Mean jitter")
        np.save(outName+"_toaRMSMedian_Q",QList)
        np.save(outName+"_toaRMSMedian_jitter",medianJitterList)
        plt.xlabel('Q [fC]')
        plt.grid()
        plt.ylabel('TOA RMS '+toaUnitStr)
        plt.ylim(bottom = 0,top=5*toalsbMedian)
        plt.xlim(left = 2., right=20)
        floor=0
        if len(medianJitterList[medianJitterList>0])>0:
            floor=np.min(medianJitterList[medianJitterList>0])
        plt.plot(QList,anaUtils.quadraticDiff(medianJitterList,floor),linewidth=5,label="Mean jitter floor substracted")

        plt.plot([3,20.],[floor,floor],color="black",linestyle="dashed",linewidth=2,label="floor (measured at 100fC)")
        #anaUtils.setLogx(plt,4,xticks)
        plt.legend()
        plt.savefig(outName +"_toaRMSMedian."+args.extension)
        plt.close()

    # plot toaRMS maps
    if args.debug or True:
        for counter,toaArray in enumerate(toaRMSSliceList):
            if QList[counter] not in QPlotList: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(toaArray, clabel='TOA RMS '+toaUnitStr)
            plt.savefig(outName +"_toaRMSMap_Q"+str(QList[counter])+"."+args.extension)
            plt.close()

    if args.debug:
        plt.figure(figsize = (13, 10))
        for counter,toaArray in enumerate(toaRMSSliceList):
            if QList[counter] not in QPlotList: continue
            # plot toaRMS vs rowNumber            
            anaUtils.colSlice(toaArray, clabel=' Jitter '+toaUnitStr,ylabel="Jitter "+toaUnitStr,label="Qinj="+str(QList[counter])+" fC")
            
        plt.grid()
        plt.ylim(bottom=0,top=80)#,top=5*toalsbMedian)
        #plt.savefig(outName +"_toaRMSVsRowNumber_Q"+str(QList[counter])+"."+args.extension)
        plt.savefig(outName +"_toaRMSVsRowNumber."+args.extension)
        plt.close()

    ####################################
    # Compute Mean and RMS for TOT
    ####################################

    #compute mean and RMS for TOT
    #df[df["toa"]<=127]
    totMeanList,totRMSList,chargeForTOTList= anaUtils.getAllMeanRMS(df,"charge","tot",ymax=256*totlsbMedian,corArray=totlsbArray)

    # compute 1D tot slices
    totMeanSliceList=anaUtils.getYSlices(chargeForTOTList,totMeanList,QList)
    totRMSSliceList=anaUtils.getYSlices(chargeForTOTList,totRMSList,QList)

    # plot all totMean
    plt.figure(figsize = (20, 10))
    for pixel in range(anaUtils.nbOfPixels):
        plt.plot(chargeForTOTList[pixel], totMeanList[pixel],marker="o")
    plt.xlabel('Q [fC]')
    plt.ylabel('TOT mean '+totUnitStr)
    plt.ylim(bottom=0,top=50* totlsbMedian)
    #plt.xlim(left = 2.)#,right=20)
    #anaUtils.setLogx(plt,1,xticks)
    plt.savefig(outName +"_totMean."+args.extension)
    plt.close()

    # plot totMean slices
    plt.figure(figsize = (20, 10))
    for counter,totArray in enumerate(totMeanSliceList):
        median=anaUtils.median(args,totArray)
        rms=np.std(totArray)
        dataMap[(Vth,QList[counter])][5]=median
        if QList[counter] not in QPlotList: continue
        plt.plot(range(0,anaUtils.nbOfPixels), totArray,label="{:.1f}fC Median: {:.1f} RMS: {:.1f}".format(QList[counter],anaUtils.median(args,totArray),np.std(totArray)))
        np.save(outName+"_totMean"+str(QList[counter]),totArray)
    plt.xlabel('Pixel Number')
    plt.ylabel('TOT mean '+totUnitStr)
    plt.ylim(bottom=0)#,top=5000)
    plt.xlim(left=0,right=225)
    plt.legend()
    plt.savefig(outName +"_totMeanVsPixelNumber."+args.extension)
    plt.close()

    # plot totMean maps
    if args.debug:
        for counter,totArray in enumerate(totMeanSliceList):
            if QList[counter] not in QPlotList: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(totArray, clabel='TOT '+totUnitStr)
            plt.savefig(outName +"_totMeanMap_Q"+str(QList[counter])+"."+args.extension)
            plt.close()


        plt.figure(figsize = (13, 10))
        for counter,totArray in enumerate(totMeanSliceList):
            if QList[counter] not in QPlotList: continue
            # plot totMean vs rowNumber
            anaUtils.colSlice(totArray, clabel=' TOT Mean '+totUnitStr,ylabel="TOT Mean "+totUnitStr,label="Qinj="+str(QList[counter])+"fC")
        plt.grid()
        plt.ylim(bottom=0)#,top=3*totlsbMedian)
        plt.savefig(outName +"_totMeanVsRowNumber."+args.extension)
        #plt.savefig(outName +"_totMeanVsRowNumber_Q"+str(QList[counter])+"."+args.extension)
        plt.close()


        # fig,axs = plt.subplots(nrows = ASICConfig.nbOfLines, ncols = ASICConfig.nbOfLines, figsize=(20,20))
        # plt.subplots_adjust(wspace=0, hspace=0)
        # #fig.suptitle('TOT vs Q')
        # for pixel in range(anaUtils.nbOfPixels):
        #     col= pixel // ASICConfig.nbOfLines 
        #     row= ASICConfig.nbOfLines-1- pixel % ASICConfig.nbOfLines  
        #     axs[row,col].scatter(chargeForTOTList[pixel], totMeanList[pixel],s=1)#,marker="o")
        #     axs[row,col].set_yticklabels([])
        #     axs[row,col].set_xticks([])
        #     axs[row,col].set_yticks([])
        #     axs[row,col].set_xticklabels([])
        #     if col<=7:
        #         axs[row,col].set_ylim(0,150*    totlsbMedian)
        #     else:
        #         axs[row,col].set_ylim(0,30*    totlsbMedian)
        # plt.savefig(outName+"_totMeanIndividual."+args.extension)
        # plt.savefig(outName+"_totMeanIndividual."+args.extension)


    # plot all totRMS
    plt.figure(figsize = (20, 10))
    for pixel in range(anaUtils.nbOfPixels):
        if len(chargeForTOTList[pixel])==0: continue
        plt.plot(chargeForTOTList[pixel], totRMSList[pixel],label=str(pixel))#, alpha=0.3)
        plt.xlabel('Q [fC]')
        plt.ylabel('TOT RMS '+totUnitStr)
        #plt.ylim(bottom=0)
        plt.ylim(bottom = 0,top=2*totlsbMedian)
        plt.xlim(left = 2.5,right=20)
        #anaUtils.setLogx(plt,4,xticks)
        plt.plot([thresMedian,thresMedian],[0,3*totlsbMedian],color="black",linestyle="dashed",linewidth=1)
    #plt.legend(fontsize=10)
    plt.savefig(outName +"_totRMS."+args.extension)
    plt.close()

    # plot totRMS slices
    plt.figure(figsize = (20, 10))
    totRMSMap={}
    for counter,totRMSArray in enumerate(totRMSSliceList):
        median=anaUtils.median(args,totRMSArray)
        totRMSMap[(Vth,QList[counter])]=median
        dataMap[(Vth,QList[counter])][6]=median
        if QList[counter] not in QPlotList: continue
        plt.plot(range(0,anaUtils.nbOfPixels), totRMSArray,label="{:.1f}fC Median: {:.1f}".format(QList[counter],anaUtils.median(args,totRMSArray)))
        np.save(outName+"_totRMS"+str(QList[counter]),totRMSArray)
        plt.xlabel('Pixel Number')
        plt.ylabel('TOT RMS '+totUnitStr)
        #plt.ylim(bottom=0)#,top=500)
        #plt.ylim(bottom = 0,top=3*totlsbMedian)
        plt.xlim(left=0,right=225)
    plt.legend()
    plt.savefig(outName +"_totRMSVsPixelNumber."+args.extension)
    plt.close()

    if args.debug:
        # plot totRMS maps
        for counter,totArray in enumerate(totRMSSliceList):
            if QList[counter] not in QPlotList: continue
            plt.figure(figsize = (13, 10))
            anaUtils.asic_map(totArray, clabel='TOT RMS '+totUnitStr)
            plt.savefig(outName +"_totRMSMap_Q"+str(QList[counter])+"."+args.extension)
            plt.close()

    if args.debug:
        plt.figure(figsize = (13, 10))
        for counter,totArray in enumerate(totRMSSliceList):
            if QList[counter] not in QPlotList: continue
            # plot totRMS vs rowNumber
            anaUtils.colSlice(totArray, clabel=' TOT RMS '+totUnitStr,ylabel="TOT RMS "+totUnitStr,label="Qinj="+str(QList[counter])+"fC")
        plt.grid()
        plt.ylim(bottom=0)#,top=3*totlsbMedian)
        plt.savefig(outName +"_totRMSVsRowNumber."+args.extension)
        #plt.savefig(outName +"_totRMSVsRowNumber_Q"+str(QList[counter])+"."+args.extension)
        plt.close()

    

    # ############################
    # # plot all toa vs tot Mean
    # ############################
    # #recompute mean with to have same selection
    # if args.debug:
    #     totMeanList,totRMSList,chargeForTOTList= anaUtils.getAllMeanRMS(df,"charge","tot",ymax=2560*totlsbMedian,corArray=totlsbArray,keepAll=True)
    #     toaMeanList,toaRMSList,chargeForTOAList= anaUtils.getAllMeanRMS(df,"charge","toa",ymax=1270*toalsbMedian,corArray=toalsbArray,keepAll=True)
    #     plt.figure(figsize = (20, 10))
    #     for pixel in range(anaUtils.nbOfPixels):
    #         print (pixel,len(totMeanList[pixel]), len(toaMeanList[pixel]))
    #         plt.scatter(totMeanList[pixel], toaMeanList[pixel],marker="o")
    #     plt.xlabel('TOT mean '+totUnitStr)
    #     plt.ylabel('TOA mean '+toaUnitStr)
    #     plt.ylim(bottom = 0,top=127*toalsbMedian)
    #     plt.xlim(left = 0, right=50*totlsbMedian)
    #     #anaUtils.setLogx(plt,1,xticks) 
    #     plt.savefig(outName +"_toaMeanVstotMean."+args.extension)
    #     plt.close()

    #     fig,axs = plt.subplots(nrows = ASICConfig.nbOfLines, ncols = ASICConfig.nbOfLines, figsize=(20,20))
    #     plt.subplots_adjust(wspace=0, hspace=0)
    #     #fig.suptitle('TOA vs TOT')
    #     for pixel in range(anaUtils.nbOfPixels):
    #         col= pixel // ASICConfig.nbOfLines 
    #         row= ASICConfig.nbOfLines-1- pixel % ASICConfig.nbOfLines  
    #         axs[row,col].scatter(totMeanList[pixel], toaMeanList[pixel],s=1)#,marker="o")
    #         axs[row,col].set_yticklabels([])
    #         axs[row,col].set_xticks([])
    #         axs[row,col].set_yticks([])
    #         axs[row,col].set_xticklabels([])
    #         axs[row,col].set_ylim(0,127*    toalsbMedian)
    #         #if col<=7:
    #         #    axs[row,col].set_xlim(0,100*    totlsbMedian)
    #         #else:
    #         axs[row,col].set_xlim(0,30*    totlsbMedian)
    #     plt.savefig(outName+"_toaMeanVstotMeanIndividual."+args.extension)
    #     plt.savefig(outName+"_toaMeanVstotMeanIndividual."+args.extension)




    f=open(outName+"_summary.dat","w")
    for key,info in dataMap.items():
        f.write("%f %f %f %f %f %f %f %f %f %f %f\n"%(float(key[0]),float(key[1]),float(info[0]),float(info[1]),float(info[2]),float(info[3]),float(info[4]),float(info[5]),float(info[6]),thresMedian,noiseMedian))            
    f.close()

    # f=open(outName+"_jitter.dat","w")
    # for key,info in jitterMap.items():
    #     f.write("%f %f %f %f %f\n"%(float(key[0]),float(key[1]),float(info),thresMedian,noiseMedian))            
    # f.close()

    # f=open(outName+"_eff.dat","w")
    # for key,info in effMap.items():
    #     f.write("%f %f %f %f %f\n"%(float(key[0]),float(key[1]),float(info),thresMedian,noiseMedian))            
    # f.close()

    # f=open(outName+"_totRMS.dat","w")
    # for key,info in totRMSMap.items():
    #     f.write("%f %f %f %f %f\n"%(float(key[0]),float(key[1]),float(info),thresMedian,noiseMedian))            
    # f.close()

    print ("Analysis TOA and TOT %3.3f sec "%(time.time() - startTime0))
