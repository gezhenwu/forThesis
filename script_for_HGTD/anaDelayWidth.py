###############################################
#
###############################################

import os,sys
import argparse
from glob import glob
import random
from math import *
from os import listdir
from os.path import isfile, join

curpath = os.getcwd()
sys.path.insert(0,curpath)
import time

import numpy as np
import matplotlib; 
matplotlib.use('Agg') 
matplotlib.use('pdf') 
import matplotlib.pyplot as plt
import pandas as pd    
from scipy.optimize import curve_fit


from lib import anaUtils
anaUtils.matplotlibConfig()

#import ASICConfig
from lib import altiroc3_Mix046


###############################################
# main
###############################################

def getDelay(cdelay,fdelay,altirocVersion):
    cdelay1=cdelay
    if altirocVersion==3:
        if fdelay==14 : cdelay1=cdelay1-1
        if fdelay==15 : cdelay1=cdelay1-1
    delay=cdelay1*altiroc3_Mix046.coarseDelayDacToPs+fdelay*altiroc3_Mix046.fineDelayDacToPs
    return delay

if __name__=='__main__':
    startTime0 = time.time()
    
    ####################################
    # parameters
    ####################################

    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument( "-v","--altirocVersion", type = int, required = False, default = 3, help = "2 or 3")
    parser.add_argument( "--saveCSV", type = argBool, required = False, default = False, help = "save combined CSV file")
    parser.add_argument("-f",'--dfFileName', help = 'cvs for combined data frame',default=None)
    parser.add_argument("-e",'--extension', help = 'figure extension',default="png")
    parser.add_argument('-i', '--inputDir', help = 'Path of the data directory',default="thresScan_DCOutPA_1110_v0/act_row_pulsed_row_N_20_Q_12")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('--compThresWith', help = 'Compare thresholds with the one provided in a file',default=None)
    parser.add_argument( "--debug", type = argBool, required = False, default = False, help = "debug")
    parser.add_argument( "-q","--quarter", type = int, required = False, default = 0, help = "")
    parser.add_argument( "--readAllPixels", type = argBool, required = False, default = False, help = "readAllPixels")
    parser.add_argument("-x",'--xvar', help = 'delay or width',default=None)
    parser.add_argument("-y",'--yvar', help = 'toa or tot',default=None)
    parser.add_argument('--xval', help = 'x values used to make additionnal plots',default=None)
    parser.add_argument('--blackList', help = ' blackList',default=None)#in fC
    args = parser.parse_args()

    if args.inputDir.find("FastFADA_ALTIROC2")>=0 or args.inputDir.find("Data2")>=0 :
        print ("ALTIROC VERSION 2")
        args.altirocVersion=2
        
    if not os.path.isdir(args.outputDir):os.makedirs(args.outputDir)

    if args.xvar==None:
        if args.inputDir.find("widthScan")>=0:
            args.xvar="width"
        else:
            args.xvar="delay"
            
    xvar=args.xvar
    yvar=args.yvar
    if args.yvar==None:
        if args.xvar=="delay":
            yvar="toa"
            
        elif args.xvar=="width":
            yvar="tot"

    label=""
    if args.xvar=="width":
        label='Width [ps]'
    else:
        label='Delay [ps]'


    if yvar=="toa":
        ymax=127
    elif yvar=="tot":
        ymax=256

    if args.xval is None:
        xvalList=[]#[12884]#,13854]
        if xvar=="width":
            xvalList=[]#[9375]
    else:
        xvalList= [float(x) for x in args.xval.split(",")]


    if args.blackList is not None:
        blackList=[float(i) for i in args.blackList.split(",")]#(0,67)

    ####################################
    # get data
    ####################################
    print ("Get Data")
    if args.dfFileName is not None:
        outName=args.outputDir+"/"+args.dfFileName.split("/")[-1].replace(".csv","")
        df=pd.read_csv(args.dfFileName)
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(args.dfFileName)

    else:
        df = pd. DataFrame()
        if args.inputDir[-1]!="/":args.inputDir+="/"
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel=anaUtils.getInfo(args.inputDir)

        outName=args.outputDir+"/"+args.inputDir.replace("/","_").replace("..","").replace("_outputNikola_","")#.replace("thresScan_","").replace("vthcScan_","")
        if args.quarter>0:
            outName+="_Quarter_"+str(args.quarter)
        
        #if len(args.inputDir.split("/"))>=3:outName=args.outputDir+"/"+args.inputDir.split("/")[-3]+"_"+args.inputDir.split("/")[-2]#ATT need to check size

        #get timing files
        fileList = [y for x in os.walk(args.inputDir) for y in glob(os.path.join(x[0], '*timing*.csv'))]

        allDF=[]
        for ftiming in sorted(fileList):
            #print (ftiming)
            vec=ftiming.replace(".csv","").replace("/","_").split("_")


            cdelay=0
            fdelay=0
            if "cdelay" in vec:cdelay=int(vec[vec.index("cdelay")+1])
            if "fdelay" in vec:fdelay=int(vec[vec.index("fdelay")+1])
            delay=getDelay(cdelay,fdelay,args.altirocVersion)
            #print (cdelay,fdelay,delay)
            if "extDelay" in vec:delay=int(vec[vec.index("extDelay")+1])*10
            #if fdelay!=2: continue



            width=0
            if "width" in vec:width=int(vec[vec.index("width")+1])
            width=width*altiroc3_Mix046.widthDacToPs


            if "pixelInj" in vec:pixelInj=vec[vec.index("pixelInj")+1]
            pixelList=altiroc3_Mix046.getPixelList(pixelInj)
            #print (cdelay,fdelay,delay)
            #if args.debug:print (ftiming,pixelInj)

            #if xvar=="delay" and  (delay<5000  or  delay>27000) : continue #ATT
            if args.altirocVersion==3:
                if xvar=="width" and  (width>6000) : continue #ATT ugly
                #if xvar=="delay" and  (delay<5000  or  delay>27000) : continue #ATT
            #if args.inputDir.find("DataStability")>=0 and  args.inputDir.find("delayScan_ExtDiscri_False")>=0:# or args.altirocVersion==2:
            #    if xvar=="delay" and  (delay<10000  or  delay>27000) : continue #ATT

            
            #get timing data
            try:
                timingdf = pd.read_csv(ftiming)
            except:
                print ("can't read ",ftiming)
                #timingdf = allDF[-1]#ATT not nice
                continue


            if args.blackList is not None:
                pixelList = [e for e in pixelList if e not in blackList]

            timingdf['delay']=delay
            timingdf['width']=width
            if not args.readAllPixels:timingdf=timingdf[timingdf['pixel'].isin(pixelList)]#only keep pixel with injected signals   
            #timingdf=timingdf[timingdf['toa']<127]#only keep pixel with injected signals   
            #print (timingdf)
            #print (len(timingdf))
            allDF.append(timingdf)


        df=pd.concat(allDF)


        if args.saveCSV: 
            df.to_csv(outName+"_combined.csv")
    
        

    if len(df.index)==0:
        print ("There is no data to analyse! stop here....")
        import sys
        sys.exit()

    print ("Get Data %3.3f sec" %(time.time() - startTime0))
    
    info="b"+str(board)
    ####################################
    # analysis
    ####################################
    print ("Analysis Cells")

    if args.quarter==4:
        df=df[ df["toa"]>=96 ]
    elif args.quarter==3:
        df=df[ (df["toa"]<96) & (df["toa"]>=64) ]
    elif args.quarter==2:
        df=df[ (df["toa"]<64) & (df["toa"]>=32) ]
    elif args.quarter==1:
        df=df[ (df["toa"]<32) & (df["toa"]>=0) ]


    if args.debug:
        anaUtils.makeAll2DPlots(df,"delay",yvar, np.arange(4000,12000,100),np.arange(0,127,1),corArray=None,basename=outName,extension=args.extension,separatedPlots=0)

    #pixelArray=np.sort(np.unique(df['pixel'].values))
    #delayArray=np.sort(np.unique(df['delay'].values))

    #compute mean and RMS for VAR
    varMeanList,varRMSList,delayForVARList =  anaUtils.getAllMeanRMS(df,xvar,yvar,ymax=ymax)

    # #get rid off zero events
    # for pixel in range(anaUtils.nbOfPixels):
    #     print (len(varMeanList[pixel]),   len(nEventsList[pixel]))
    #     varMeanList[pixel]=        varMeanList[pixel][nEventsList[pixel]>0]
    #     delayForVARList[pixel]=        delayForVARList[pixel][nEventsList[pixel]>0]
    #     varRMSList[pixel]=        varRMSList[pixel][nEventsList[pixel]>0]

    # bin_width = 16
    # min_value = 0
    # max_value = 127
    # bins = np.arange(min_value, max_value + bin_width, bin_width)
    # tmpdf=df
    # #tmpdf = tmpdf[tmpdf['pixel'] == pixel]
    # tmpdf = tmpdf[tmpdf['toa'] <127]
    # tmpdf = tmpdf[tmpdf['toa'] >0]
    # #tmpdf = tmpdf[tmpdf['pixel'] ==0]
    # plt.figure()#figsize = (20, 10))
    # tmpdf.hist(column = 'toa',bins=bins)
    # plt.savefig(outName+"_VARhist_pixel.png")


    # # Calculate mean delay for each unique 'toa' value
    # mean_delay = tmpdf.groupby('toa')['delay'].mean().reset_index()

    # # Create a figure with two subplots
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # # Scatter plot with linear fit
    # ax1.scatter(mean_delay['toa'], mean_delay['delay'], c='red', marker='o', label='Mean Delay')
    
    # # Perform linear regression
    # x = mean_delay['toa']
    # y = mean_delay['delay']
    # coefficients = np.polyfit(x, y, 1)
    # poly = np.poly1d(coefficients)
    # ax1.plot(x, poly(x), 'b--', label='Linear Fit')
    
    # # Set titles and labels for the scatter plot
    # ax1.set_title('Linear Fit of Mean Delay vs TOA')
    # ax1.set_xlabel('toa')
    # ax1.set_ylabel('delay')
    # ax1.legend()
    
    # # Calculate residuals
    # residuals = y - poly(x)
    
    # # Residuals plot
    # ax2.plot(x, residuals, color='green')
    # ax2.set_xlabel('toa')
    # ax2.set_ylabel('Residuals')
    # ax2.set_title('Residuals of Linear Fit')
    
    # # Adjust layout and display the plots
    # plt.tight_layout()
    # plt.savefig(outName+"_delay_vs_toa.png")

    print ("Analysis Cells %3.3f sec" %(time.time() - startTime0))



    print ("Compute LSB and Make Plots")

    # plot varMean and compute lsb
    nbOfPointsArray=np.zeros(anaUtils.nbOfPixels)
    lsbArray=np.zeros(anaUtils.nbOfPixels)
    chi2Array=np.zeros(anaUtils.nbOfPixels)
    figgood=plt.figure("good",figsize = (20, 10))
    figresiduals=plt.figure("residuals",figsize = (20, 10))
    figbad=plt.figure("bad",figsize = (20, 10))
    residualsList=[]
    nBad=0
    for pixel in range(0,anaUtils.nbOfPixels):
        nbOfPointsArray[pixel]=len(varMeanList[pixel])
        #print (pixel,varMeanList[pixel])
        #if pixel not in [224]: continue
        #print (varMeanList[pixel])
        residuals=np.array([])
        shifted_x=np.array([])
        okForFit=np.logical_and(np.array(varMeanList[pixel])>=1,delayForVARList[pixel]>0)

        iMin=0
        iMax=len(varMeanList)
        if len(varMeanList[pixel][okForFit])>3:
            #if pixel in [224]: iMin=5
            slope,intercept,chi2=anaUtils.pol1fit(delayForVARList[pixel][okForFit][iMin:iMax],varMeanList[pixel][okForFit][iMin:iMax])
            # if pixel in [0,1]:
            #     chi2=100000
            #     slope,intercept,chi2=anaUtils.pol1fit(delayForVARList[pixel][okForFit][1:8],varMeanList[pixel][okForFit][1:8])
            #     print (delayForVARList[pixel][okForFit],varMeanList[pixel][okForFit],slope)
        else:
            slope,intercept,chi2=anaUtils.pol1fit(delayForVARList[pixel][okForFit],varMeanList[pixel][okForFit])



        chi2Array[pixel]=chi2
        #print ("chi2: ",pixel,chi2)
        if chi2>5000:
            nBad+=1
            #print (delayForVARList[pixel],varMeanList[pixel],okForFit)
            plt.figure("bad")
            plt.plot(delayForVARList[pixel][okForFit], varMeanList[pixel][okForFit],label=str(pixel),marker="o")



        else:
            #print ("lsb:",pixel,lsbArray[pixel])
            plt.figure("good")
            x=delayForVARList[pixel][okForFit][iMin:iMax]
            y=varMeanList[pixel][okForFit][iMin:iMax]
            plt.plot(x,y,label=str(pixel),marker="o")
            lsb=0
            if slope!=0:
                lsb=1/slope
            #if pixel in range(15,30):
            lsbArray[pixel]=abs(lsb)
            plt.figure("residuals")
            if len(x)>0:
                residuals=y-(slope*x+intercept)
                shifted_x=x#-np.min(x)
                plt.plot(shifted_x,residuals,label=str(pixel),marker="o",zorder=1)
        residualsList.append((shifted_x,residuals))
        #plt.close()


    plt.figure("bad")
    plt.legend(fontsize=15)
    plt.xlabel(label)
    plt.ylabel("<"+yvar+"> [DACU]")
    #if args.debug:
    if (nBad>0): plt.savefig(outName +"_varMeanVsXXXBad."+args.extension)

    plt.figure("good")
    #plt.legend(fontsize=15)
    plt.xlabel(label)
    plt.ylabel("<"+yvar+"> [DACU]")
    for cdelay in range(0,16):

        x=cdelay*altiroc3_Mix046.coarseDelayDacToPs
        if  yvar=="tot":
            aa=16
            bb=20
        else:
            aa=0
            bb=100
        #plt.plot([x,x],[aa,bb],color="black",linestyle="dashed",linewidth=1)
    plt.savefig(outName +"_varMeanVsXXXGood."+args.extension)



    figresiduals=plt.figure("residualsmean",figsize = (20, 10))
    x,y=anaUtils.computeAverage(residualsList)    
    plt.scatter(x,y,s=100, c='black', marker='o',zorder=2)
    plt.ylim(bottom=-1.5)
    plt.ylim(top=+1.5)
    #plt.savefig(outName +"_varMeanVsXXXResidualsMean."+args.extension)
    
    plt.figure("residuals")
    #plt.scatter(x,y,s=200, c='yellow', marker='o',zorder=2)
    #plt.legend(fontsize=15)
    plt.xlabel(label)
    plt.ylim(bottom=-2)
    plt.ylim(top=+2)
    plt.ylabel("Residuals [DACU]")
    if args.debug:plt.savefig(outName +"_varMeanVsXXXResiduals."+args.extension)

    if args.debug:
        # plot of residuals
        anaUtils.makeOnePlotPerPixel(residualsList,basename=outName+"_Residuals",ymin=-2,ymax=2,txt=info)


    plt.close()
    np.save(outName+"_lsb",lsbArray)
    np.save(outName+"_nbOfPoints",nbOfPointsArray)


    # plot lsb map
    plt.figure(figsize = (13, 10))
    anaUtils.asic_map(lsbArray, clabel=yvar+' LSB [ps]',txt=info)
    plt.savefig(outName +"_lsbMap."+args.extension)
    plt.close()

    # plot lsb vs rowNumber
    plt.figure(figsize = (13, 10))
    anaUtils.colSlice(lsbArray, clabel=yvar+' LSB [ps]')
    #if args.debug:
    plt.savefig(outName +"_lsbVsRowNumber."+args.extension)
    plt.close()

    # plot lsb
    plt.figure(figsize = (20, 10))
    plt.plot(range(0,anaUtils.nbOfPixels), lsbArray,label="Mean: {:.1f}".format(np.mean(lsbArray)))
    plt.xlabel('Pixel Number')
    plt.ylabel(yvar+' LSB [ps]')
    if xvar=="toa":
        plt.ylim(bottom = 0,top=50)
    plt.legend()
    plt.savefig(outName +"_lsbVsPixelNumber."+args.extension)
    plt.close()



    # plot nbOfPoints
    plt.figure(figsize = (20, 10))
    plt.plot(range(0,anaUtils.nbOfPixels), nbOfPointsArray,label="Mean: {:.1f}".format(np.mean(nbOfPointsArray)))
    plt.xlabel('Pixel Number')
    plt.ylabel(yvar+' NBOFPOINTS')
    plt.legend()
    if args.debug:plt.savefig(outName +"_nbOfPointsVsPixelNumber."+args.extension)
    plt.close()



    # plot nbOfPoints map
    plt.figure(figsize = (13, 10))
    anaUtils.asic_map(nbOfPointsArray, clabel=yvar+' NBOFPOINTS [ps]',txt=info)
    if args.debug:plt.savefig(outName +"_nbOfPointsMap."+args.extension)
    plt.close()


    # plot chi2 map
    plt.figure(figsize = (13, 10))
    anaUtils.asic_map(chi2Array, clabel=r'$\chi^{2}$',txt=info)
    plt.savefig(outName +"_chi2Map."+args.extension)
    plt.close()


    # plot all varRMS and compute rms
    plt.figure(figsize = (20, 10))
    rmsArray=np.zeros(anaUtils.nbOfPixels)
    for pixel in range(anaUtils.nbOfPixels):
        #print (pixel,varRMSList)
        non_zero_rms = varRMSList[pixel][varRMSList[pixel]>0]
        if non_zero_rms.size > 0:
            rmsArray[pixel] = np.max(non_zero_rms) * lsbArray[pixel]
        #rmsArray[pixel]=np.max(varRMSList[pixel][varRMSList[pixel]>0])*lsbArray[pixel]
        plt.plot(delayForVARList[pixel], varRMSList[pixel])#, alpha=0.3)
    plt.xlabel(label)
    plt.ylabel(yvar+' RMS [ps]')
    if xvar=="toa":
        plt.ylim(bottom = 0,top=10)
    #plt.xlim(left = 0)
    if args.debug:plt.savefig(outName +"_varRMSVsXXX."+args.extension)
    plt.close()


    # plot rms map
    plt.figure(figsize = (13, 10))
    anaUtils.asic_map(rmsArray, clabel="max("+yvar+' rms) [ps]',txt=info)
    if args.debug:plt.savefig(outName +"_rmsMap."+args.extension)
    plt.close()

    # plot rms
    plt.figure(figsize = (20, 10))
    plt.plot(range(0,anaUtils.nbOfPixels), rmsArray,label="Median: {:.1f}".format(np.median(rmsArray)))
    plt.xlabel('Pixel Number')
    plt.ylabel(yvar+' rms [ps]')
    if xvar=="toa":
        plt.ylim(bottom = 0,top=50)
    plt.legend()
    if args.debug:plt.savefig(outName +"_rmsVsPixelNumber."+args.extension)
    plt.close()

    if args.debug:
        # compute 1D var slices
        varMeanSliceList=anaUtils.getYSlices(delayForVARList,varMeanList,xvalList)
        varRMSSliceList=anaUtils.getYSlices(delayForVARList,varRMSList,xvalList)


        # plot varMean
        for counter,varArray in enumerate(varMeanSliceList):
            plt.figure(figsize = (13, 10))
            varCorArray=varArray*lsbArray
            #varCorArray[varCorArray == 0] = np.median(varCorArray[varCorArray > 0])# replace 0 by median
            anaUtils.asic_map(varCorArray, clabel=yvar+' mean [ps]',txt=info)
            plt.savefig(outName +"_varCorMeanMap_var"+str(xvalList[counter])+"."+args.extension)
            plt.close()


        # plot varRMS
        for counter,varArray in enumerate(varRMSSliceList):
            plt.figure(figsize = (13, 10))
            varCorArray=varArray*lsbArray
            #varCorArray[varCorArray == 0] = np.median(varCorArray[varCorArray > 0])# replace 0 by median
            anaUtils.asic_map(varCorArray, clabel=yvar+' mean [ps]',txt=info)
            plt.savefig(outName +"_varCorRMSMap_var"+str(xvalList[counter])+"."+args.extension)
            plt.close()


        # plot varMean slices
        plt.figure(figsize = (20, 10))
        for counter,varArray in enumerate(varMeanSliceList):
            okLSB=lsbArray>0
            varCorArray=varArray*lsbArray
            plt.plot(np.arange(0,anaUtils.nbOfPixels)[okLSB],varCorArray[okLSB] ,label="RMS: {:.1f}".format(np.std(varCorArray)))
            varNoCorArray=varArray*np.median(lsbArray[lsbArray>0])
            plt.plot(np.arange(0,anaUtils.nbOfPixels)[okLSB],varNoCorArray[okLSB] ,label="RMS: {:.1f}".format(np.std(varNoCorArray))+" (using median LSB)")
            np.save(outName+"_mean"+str(xvalList[counter]),varCorArray)

        plt.xlabel('Pixel Number')
        plt.ylabel(yvar+' mean [ps]')
        #plt.ylim(bottom = 0,top=127)
        plt.legend()
        plt.savefig(outName +"_varCorMeanVsPixelNb."+args.extension)
        plt.close()



        # plot varRMS slices
        plt.figure(figsize = (20, 10))
        for counter,varArray in enumerate(varRMSSliceList):
            okLSB=lsbArray>0
            varCorArray=varArray*lsbArray
            plt.plot(np.arange(0,anaUtils.nbOfPixels)[okLSB],varCorArray[okLSB] ,label="RMS: {:.1f}".format(np.std(varCorArray)))
            varNoCorArray=varArray*np.median(lsbArray[lsbArray>0])
            plt.plot(np.arange(0,anaUtils.nbOfPixels)[okLSB],varNoCorArray[okLSB] ,label="RMS: {:.1f}".format(np.std(varNoCorArray))+" (using median LSB)")
            np.save(outName+"_rms"+str(xvalList[counter]),varCorArray)

        plt.xlabel('Pixel Number')
        plt.ylabel(yvar+' rms [ps]')
        #plt.ylim(bottom = 0,top=127)
        plt.legend()
        plt.savefig(outName +"_varCorRMSVsPixelNb."+args.extension)
        plt.close()




    # statistics
    if args.debug:
        #np.min(dacChargeArray)+dacChargeArray
        statArray=anaUtils.getStatistics(df)
        
        
        # plot stat map
        plt.figure(figsize = (13, 10))
        anaUtils.asic_map(statArray, clabel=yvar+' STAT ',txt=info)
        plt.savefig(outName +"_statMap."+args.extension)
        plt.close()            


    # if args.doDeltaT: # ATT ugly and slow, should do better

    #     #compute deltaT between pixels for each events
    #     #pixelArray=np.arange(4)#anaUtils.nbOfPixels)
    #     #print (pixelArray)
    #     deltadf= pd.DataFrame(columns = ["delay","pixel1","pixel2","delta"])
    #     timestampArray=np.sort(np.unique(df['timestamp'].values))
    #     df=df.loc [  (df['delay'] >= 12000) &  (df['delay'] <= 15000) ]
    #     for timestamp in timestampArray:
    #         dfts=df.loc [  df['timestamp'] == timestamp]
    #         #print (dfts)
    #         tmppixelArray=pixelArray#np.sort(np.unique(dfts['pixel'].values))
    #         for pixel1 in tmppixelArray:
    #             delay=np.array(dfts.loc[dfts["pixel"] == pixel1] ["delay"]   )
    #             if len(delay)!=1: continue
    #             var1=np.array(dfts.loc[dfts["pixel"] == pixel1] ["var"]*lsbArray[pixel1]   )
    #             if len(var1)!=1: continue
    #             if var1[0]==127*lsbArray[pixel1]: continue
    #             for pixel2 in tmppixelArray:
    #                 if pixel2<pixel1: continue
    #                 #print (pixel1,pixel2)
    #                 var2=np.array(dfts.loc[dfts["pixel"] == pixel2] ["var"]*lsbArray[pixel2]   )
    #                 if len(var2)!=1: continue
    #                 if var2[0] ==127*lsbArray[pixel1]: continue
    #                 delta=var1[0]-var2[0]
    #                 if pixel2==pixel1: delta=var1[0]
    #                 deltadf=deltadf.append(pd.Series({"delay":delay[0],"pixel1":pixel1,"pixel2":pixel2,"delta":delta}, name=str(timestamp)))
    #                 #print (timestamp,delay,pixel1,pixel2,var1,var2,delta)
    #                 pass
    #     print ("=======================")
    #     #print (deltadf)

    #     #deltaArray=np.zeros(len(pixelArray)*len(pixelArray))
    #     deltaArray=np.zeros((anaUtils.nbOfPixels,anaUtils.nbOfPixels))
    #     #deltaArray=np.zeros((15,15))
    #     #deltaArray=np.zeros((anaUtils.nbOfPixels,anaUtils.nbOfPixels))
    #     #compute the rms of the deltaT
    #     for pixel1 in pixelArray:
    #         for pixel2 in pixelArray:
    #             if pixel2<=pixel1: continue
    #             rmsList=[]
    #             for delay in delayArray:
    #                 delta = deltadf.loc[  (deltadf["pixel1"] == pixel1) & (deltadf["pixel2"] == pixel2) & (deltadf["delay"] == delay)     ] ["delta"]
    #                 #print (pixel1,pixel2,delay,len(delta))
    #                 if len(delta)>=5:#need enough stat to compute a rms
    #                     rmsList.append(np.std(delta))

    #             medianrms=np.median(rmsList)
    #             if pixel1!=pixel2: medianrms/=sqrt(2)
    #             deltaArray[pixel1][pixel2]=medianrms
    #             #deltaArray[pixel2][pixel1]=medianrms
    #             print (pixel1,pixel2,medianrms)
    #             print (deltaArray)



    #     # plot delta map
    #     #import matplotlib as mpl
    #     #mpl.rcParams['image.cmap']='bwr'
    #     plt.figure(figsize = (13, 10))
    #     median=np.median(deltaArray[deltaArray > 0])
    #     diff=max( abs(np.max(deltaArray[deltaArray > 0])-median), abs(np.min(deltaArray[deltaArray > 0])-median))
    #     deltaArray[deltaArray == 0] = np.median(deltaArray[deltaArray > 0])# replace 0 by median
    #     im = plt.imshow(deltaArray,cmap='seismic')#, interpolation='none')
    #     ax = plt.gca()
    #     fig = plt.gcf()
    #     #ax.invert_yaxis()
    #     cbar = fig.colorbar(im, ax=ax)
    #     #cbar.set_label("RMS [ps]")
    #     cbar.set_label(r'RMS(t1-t2)/$\sqrt{2}$ [ps]')
    #     ax.set_aspect('auto')
    #     #ax.grid(color="w", linestyle='-', linewidth=1.5, alpha=1)
    #     im.set_clim(median-diff,median+diff)
    #     ax.set_xticks(np.arange(deltaArray.shape[1]+1)-.5)
    #     ax.set_yticks(np.arange(deltaArray.shape[0]+1)-.5)
    #     ax.xaxis.set_ticklabels([])
    #     ax.yaxis.set_ticklabels([])
    #     plt.xlabel('Pixel 1')
    #     plt.ylabel('Pixel 2')
    #     plt.savefig(outName +"_deltaMap."+args.extension )
    #     plt.savefig(outName +"_deltaMap.png")
    #     plt.close()

    print ("Compute LSB and Make Plots %3.3f sec" %(time.time() - startTime0))
