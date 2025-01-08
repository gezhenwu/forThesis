###############################################
#
###############################################
# import sys
# sys.path.append("./FADA/software")
# sys.path.append("./FADA/software/scripts")
# sys.path.append("./FADA/software/analysis")

# import os
# import argparse
# from glob import glob
# import random
# from math import *
# from os import listdir
# from os.path import isfile, join


# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd    
# from scipy.optimize import curve_fit


# import anaUtils
# anaUtils.matplotlibConfig()
# #import ASICConfig
# from scripts import ASICConfig

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


###############################################
# main
###############################################

if __name__=='__main__':
    
    ####################################
    # parameters
    ####################################

    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument( "--saveCSV", type = argBool, required = False, default = True, help = "save combined CSV file")
    parser.add_argument("-f",'--dfFileName', help = 'cvs for combined data frame',default=None)
    parser.add_argument("-e",'--extension', help = 'figure extension',default="png")
    parser.add_argument('-i', '--inputDir', help = 'Path of the data directory',default="thresScan_DCOutPA_1110_v0/act_row_pulsed_row_N_20_Q_12")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('--compThresWith', help = 'Compare thresholds with the one provided in a file',default=None)
    parser.add_argument('--frac', help = 'Fraction',default=0.5,type=float)
    parser.add_argument( "--debug", type = argBool, required = False, default = False, help = "debug")
    parser.add_argument( "--readAllPixels", type = argBool, required = False, default = False, help = "readAllPixels")
    parser.add_argument( "--doVthc", type = argBool, required = False, default = False, help = "for vthc scan")
    parser.add_argument( "--doPulse", type = argBool, required = False, default = False, help = "reco pulse shape (LSB should be provided)")
    parser.add_argument('--toaLSB', help = 'toa LSB File',default=None)
    parser.add_argument('--totLSB', help = 'tot LSB File',default=None)
    parser.add_argument('--vthcFile', help = "output vthc file ",default=None)



    args = parser.parse_args()

    if args.inputDir.find("vthcScan")>=0: args.doVthc=True
        
    if not os.path.isdir(args.outputDir):os.makedirs(args.outputDir)

    label='$V_{th}$ [DACU]'
    if args.doVthc:
        label='$V_{thc}$ [DACU]'





    
    ####################################
    #get data
    ####################################
    if args.dfFileName is not None:
        outName=args.outputDir+"/"+args.dfFileName.split("/")[-1].replace(".csv","")
        df=pd.read_csv(args.dfFileName)
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,Npulse=anaUtils.getInfo(args.dfFileName)
        #print (df)
        #print(len(df.index))
    else:
        df = pd. DataFrame()
        if args.inputDir[-1]!="/":args.inputDir+="/"
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,Npulse=anaUtils.getInfo(args.inputDir)
        outName=args.outputDir+"/"+args.inputDir.replace("/","_").replace("..","").replace("_outputNikola_","")#.replace("thresScan_","").replace("vthcScan_","")
        #outName=args.outputDir+"/"+args.inputDir.split("/")[-2]
        #if len(args.inputDir.split("/"))>=3:outName=args.outputDir+"/"+args.inputDir.split("/")[-3]+"_"+args.inputDir.split("/")[-2]#ATT need to check size

        #get timing files
        fileList = [y for x in os.walk(args.inputDir) for y in glob(os.path.join(x[0], '*timing*.csv'))]

        for ftiming in sorted(fileList):
            vec=ftiming.replace(".csv","").replace("/","_").split("_")
            if "pixelInj" in vec:pixelInj=vec[vec.index("pixelInj")+1]
            pixelList=ASICConfig.getPixelList(pixelInj)
            dac=0
            if args.doVthc:
                if "dacVthc" in vec:
                    dac=int(vec[vec.index("dacVthc")+1])
                    #if ftiming.find("col7")>=0 and dacVth>=200: continue
            else:
                if "dacVth" in vec:
                    dac=int(vec[vec.index("dacVth")+1])


            #get timing data
            print (ftiming,pixelInj)
            timingdf = pd.read_csv(ftiming)
            timingdf['dac']=dac
            #pixelList=[56]
            if not args.readAllPixels:timingdf=timingdf[timingdf['pixel'].isin(pixelList)]#only keep pixel with injected signals
            df=pd.concat([df,timingdf])

            #get meta data
            #fmeta=ftiming.replace("timing_data","meta_data_ch")
            #metadf = pd.read_csv(fmeta)
        if args.saveCSV: 
            df.to_csv(outName+"_combined.csv")


    if len(df.index)==0:
        print ("There is no data to analyse! stop here....")
        import sys
        sys.exit()

    pixelArray=np.sort(np.unique(df['pixel'].values))
    dacArray=np.sort(np.unique(df['dac'].values))
    if args.doVthc:
        #dacArray=np.insert(dacArray,0, np.array(range(0,np.min(dacArray))))#add values starting from 0
        ##dacArray=np.insert(dacArray,0, np.arange(0,np.min(dacArray)))#add values starting from 0
        if len(dacArray)>0:
            dacArray=np.append(np.arange(0,np.min(dacArray)),dacArray)#add values starting from 0
    else:
        if len(dacArray)>0:
            dacArray=np.append(dacArray,np.arange(np.max(dacArray)+1,np.max(dacArray)*1.2,10))#add values starting from 0
    


    if len(df.index)==0:
        print ("There is no data to analyse! stop here....")
        import sys
        sys.exit()

    ####################################
    # efficiency analysis
    ####################################

    # compute all efficiencies
    #Npulse=100  # tmp 
    allEffList,allNList,thresArray=anaUtils.getAllEff(df,dacArray,varName="dac",effThres=args.frac,doVthc=args.doVthc,doInterpolation=False,NMax=Npulse)


    # plot all eff and compute noise
    noiseArray=np.zeros(anaUtils.nbOfPixels)
    thresAltArray=np.zeros(anaUtils.nbOfPixels)
    figall=plt.figure("alleff",figsize = (20, 10))
    figgood=plt.figure("good",figsize = (20, 10))
    figbad=plt.figure("bad",figsize = (20, 10))
    for pixel in range(0,anaUtils.nbOfPixels):
        #if pixel not in [104]:continue
        plt.figure("alleff")
        if np.sum(allEffList[pixel])!=0:
            plt.plot(dacArray, allEffList[pixel],label=str(pixel))
            #plt.axvline(x=thresArray[pixel], color='b')


        if len(allEffList[pixel])>=2 and not np.any(np.isnan(allEffList[pixel])) and np.sum(allEffList[pixel])!=0:#ATT fit converge issue for vthc scan
            pinit=[0.5,thresArray[pixel],2]
            if args.doVthc: pinit=[0.5,thresArray[pixel],-0.5]
            index=np.argmax(dacArray==thresArray[pixel]) #ATT
            delta=30
            try:
                popt, pcov = curve_fit(anaUtils.myerf, dacArray[index-delta:index+delta], allEffList[pixel][index-delta:index+delta],p0=pinit)
                plt.figure("good")
                plt.plot(dacArray[index-delta:index+delta], allEffList[pixel][index-delta:index+delta])
            except: #the failed fits should be further investigated
                popt=[999,999,999]
                plt.figure("bad")
                plt.plot(dacArray[index-delta:index+delta],allEffList[pixel][index-delta:index+delta])

            
            noiseArray[pixel] = abs(popt[2])
            thresAltArray[pixel] = popt[1]
    plt.figure("alleff")
    plt.xlabel(label)
    plt.ylabel('Efficiency')
    plt.legend(fontsize=20)
    #plt.xlim([200,250])
    plt.savefig(outName +"_alleff."+args.extension)
    if args.debug:
        plt.figure("good")
        plt.xlabel(label)
        plt.ylabel('Efficiency')
        plt.savefig(outName +"_goodeff."+args.extension)
        plt.figure("bad")
        plt.xlabel(label)
        plt.ylabel('Efficiency')
        plt.savefig(outName +"_eff_failed_fit."+args.extension)

    plt.close()

    # thres map
    plt.figure(figsize = (13, 10))
    anaUtils.asic_map(thresArray, clabel=label)
    plt.savefig(outName+"_thresMap."+args.extension)

    # thres 1D
    plt.figure(figsize = (20, 10))
    #plt.grid()
    plt.plot(range(0,anaUtils.nbOfPixels) , thresArray)#, alpha=0.3)
    plt.ylabel(label)
    plt.xlabel('Pixel number')
    plt.savefig(outName+"_thres."+args.extension)
    plt.close()

    if np.sum(noiseArray)>0:
        # noise map
        plt.figure(figsize = (13, 10))
        anaUtils.asic_map(noiseArray, clabel='Noise [DACU]',vmax=6)
        plt.savefig(outName+"_noiseMap."+args.extension)
        plt.close()

        # noise 1D
        plt.figure(figsize = (20, 10))
        #plt.grid()
        plt.plot(range(0,anaUtils.nbOfPixels) , noiseArray,label="Median: {:.1f} {:.1f}".format(np.median(noiseArray[0:ASICConfig.lastVpaPixel]),np.median(noiseArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )))
        plt.ylabel('Noise [DACU]')
        plt.xlabel('Pixel number')
        plt.ylim(bottom = 0,top=6)
        plt.legend()
        plt.savefig(outName+"_noise."+args.extension)
        plt.close()

    # compute Vthc
    if not args.doVthc:
        vthMedian=int(np.median(thresArray))
        fvthc=open(outName+"_vthc_for_vth_"+str(vthMedian)+".txt","w")
        for pix,vth in enumerate(thresArray):
            vthc=int(128+(vthMedian-vth)*0.55/1.04)
            #print (pix,vth,vthc,"{0:b}".format(vthc),vthMedian)
            address=pix*4+3
            mystr="{0}     ,{1:#08b}, # vth: {2} vthMedian: {3} vthc: {4}\n ".format(address,vthc,vth,vthMedian,vthc)
            mystr=mystr.replace("0b","B'")
            fvthc.write(mystr)
        fvthc.close()
    else:
        if args.vthcFile is not None:
            name = args.vthcFile
        else:
            name = outName+"_vthc.txt"
        fvthc=open(name.replace("__","_"),"w")
        
        for pix,vthc in enumerate(thresArray):
            vthc=int(vthc)
            #if pix==0: vthc=0
            address=pix*4+3
            mystr="{0}     ,{1:#08b}, # {2} \n ".format(address,vthc,vthc)
            mystr=mystr.replace("0b","B'")
            fvthc.write(mystr)
        fvthc.close()


    #save array
    np.save(outName+"_thres",thresArray)
    np.save(outName+"_noise",noiseArray)

    
    #compare thresjolds with the ones saved in a file
    if args.compThresWith is not None:

        thresAltArray = np.load(args.compThresWith)
        diffArray = np.abs(thresArray-thresAltArray)
        diffOverNoiseArray = np.divide(diffArray,noiseArray)

        # compare thres
        plt.figure(figsize = (20, 10))
        plt.plot(range(0,225) , thresArray)#,label=name1)
        plt.plot(range(0,225) , thresAltArray)#,label=name2)
        plt.ylabel('$V_{th}$ [DACU]')
        plt.xlabel('Pixel number')
        plt.legend()
        plt.savefig(outName+"_thres_comp."+args.extension)
        plt.close()

        print(diffArray,thresAltArray)

        # diff thres 1D
        plt.figure(figsize = (20, 10))
        plt.plot(range(0,anaUtils.nbOfPixels) , diffArray)
        plt.ylabel(r'$\Delta V_{th}$ [DACU]')
        plt.xlabel('Pixel Number')
        plt.legend()
        plt.savefig(outName+"_thres_diff."+args.extension)
        plt.close()

        # diff map
        plt.figure(figsize = (13, 10))
        anaUtils.asic_map(diffArray, clabel=r'$\Delta V_{th}$  [DACU]')
        plt.savefig(outName+"_thres_diff_map."+args.extension)
        plt.close()


        # diffOverNoise thres 1D
        plt.figure(figsize = (20, 20))
        plt.plot(range(0,anaUtils.nbOfPixels) , diffOverNoiseArray)
        plt.ylabel(r'$\Delta V_{th}$/N')
        plt.xlabel('Pixel Number')

        plt.legend()
        plt.savefig(outName+"_thres_diffOverNoise."+args.extension)
        plt.close()

        # diffOverNoise map
        plt.figure(figsize = (13, 10))
        anaUtils.asic_map(diffOverNoiseArray, clabel=r'$\Delta V_{th}$/N')
        plt.savefig(outName+"_thres_diffOverNoise_map."+args.extension)
        plt.close()


    ####################################
    # Pulse Shape
    ####################################


    if args.toaLSB is not None:
        toalsbArray=np.load(args.toaLSB)
    else:
        toalsbArray=np.full(anaUtils.nbOfPixels,20)#take the nominal value

    if args.totLSB is not None:
        totlsbArray=np.load(args.totLSB)
    else:
        totlsbArray=np.full(anaUtils.nbOfPixels,120)#take the nominal value

    doPulseShape=args.doPulse
    if doPulseShape:
        toalsbMedian=np.median(toalsbArray[toalsbArray>0][120:225])#only TZ
        totlsbMedian=np.median(totlsbArray[totlsbArray>0][120:225])#only TZ

        #compute mean and RMS for TOT
        toaMeanList,toaRMSList,thresForTOAList= anaUtils.getAllMeanRMS(df,"dac","toa",ymax=127*toalsbMedian,corArray=toalsbArray,Nmin=0)
        totMeanList,totRMSList,thresForTOTList= anaUtils.getAllMeanRMS(df,"dac","tot",ymax=256*totlsbMedian,corArray=totlsbArray,Nmin=0)

        Tclock=4000

        slopeArray=np.zeros(225)
        for pixel,toaMean in enumerate(toaMeanList):
            #if pixel not in range(120,121): continue


            toaMean=toaMeanList[pixel]
            toaRMS=toaRMSList[pixel]
            totMean=totMeanList[pixel]
            totRMS=totRMSList[pixel]
            print (pixel,toaMean,toaRMS)
            ok=np.logical_and(toaMean<=126*toalsbArray[pixel],toaRMS>5)

            if(len(toaMean))==0: continue
            #print (toaMean)
            thres=thresForTOAList[pixel]
            plt.figure(figsize = (13, 10))
            #plt.grid()
            
            toaMean=            Tclock-toaMean

            okFit=np.logical_and(ok,toaRMS<150)
            
            #a,b,chi2=anaUtils.pol1fit(toaMean[okFit],thres[okFit])
            xmin=1
            xmax=len(toaMean[ok])-1
            if int(Q)>=16:
                xmin=5
                xmax=25
                if pixel>=ASICConfig.firstTZPixel:
                    xmax=40

            a,b,chi2=anaUtils.pol1fit(toaMean[okFit][xmin:xmax],thres[okFit][xmin:xmax])
            slopeArray[pixel]=a
            print (a,b,chi2)

            plt.errorbar(  toaMean[ok],thres[ok], xerr=toaRMS[ok],  marker="o",color="blue")
            plt.errorbar(  toaMean[ok]+totMean[ok], thres[ok], xerr=totRMS[ok],marker="o",color="red")
            plt.ylabel("thres.")
            plt.xlabel('TOA and TOA+TOT')
            plt.xlim([0,8000])
            if pixel>=ASICConfig.firstTZPixel:
                plt.xlim([1000,6000])
            else:
                plt.xlim([1000,20000])

            plt.plot(toaMean[okFit][xmin:xmax],a*toaMean[okFit][xmin:xmax]+b,color="m",linewidth=5,zorder=4)
            if pixel>=120:
                plt.savefig(outName+"_"+str(pixel)+"_PulseShape.png")
            plt.close()
            #if pixel==1: TOT



        plt.figure(figsize = (20, 10))
        #plt.grid()
        plt.plot(range(0,anaUtils.nbOfPixels) , slopeArray,label="Median: {:.2f} {:.2f}".format(np.median(slopeArray[0:ASICConfig.lastVpaPixel]),np.median(slopeArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )))
        plt.ylabel('Slope [DACU/ps]')
        plt.xlabel('Pixel number')
        plt.ylim(bottom = 0)#,top=8)
        plt.legend()
        plt.savefig(outName+"_slope."+args.extension)
        plt.close()


        plt.figure(figsize = (20, 10))
        anaUtils.colSlice(slopeArray, clabel=' ',ylabel='Slope [DACU/ps]')
        plt.grid()
        #plt.ylim(0,80)
        plt.savefig(outName +"_slopeVsRowNumber."+args.extension)
        plt.close()


        plt.figure(figsize = (20, 10))
        #plt.grid()
        jitterArray=np.divide(noiseArray,slopeArray)
        plt.plot(range(0,anaUtils.nbOfPixels) , jitterArray,label="Median: {:.2f} {:.2f}".format(np.median(jitterArray[0:ASICConfig.lastVpaPixel]),np.median(jitterArray[ASICConfig.firstTZPixel:ASICConfig.nbOfPixels] )))
        plt.ylabel('N/(dV/dt) [ps]')
        plt.xlabel('Pixel number')
        plt.ylim(bottom = 0)#,top=8)
        plt.legend()
        plt.savefig(outName+"_jitter."+args.extension)
        plt.close()


        np.save(outName+"_slope",slopeArray)
        np.save(outName+"_jitter",jitterArray)
