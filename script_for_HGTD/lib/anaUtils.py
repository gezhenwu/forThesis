###############################################
#
###############################################
import os
import argparse
from glob import glob
import random
from math import *
from os import listdir
from os.path import isfile, join

import numpy as np
np.seterr(invalid='ignore')
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd    
import scipy

from lib import altiroc3_Mix046

###############################################
# 
###############################################

nbOfPixels = 225
nbOfColumns = 15
nbOfRows = 15

colorMap={}
colorMap[1]="dodgerblue"
colorMap[4]="tab:red"
colorMap[11]="limegreen"
colorMap[12]="darkviolet"
colorMap[25]="sandybrown"
colorMap[34]="darkgray"
colorMap[35]="tab:pink"
colorMap[47]="tab:olive"
colorMap[15]="tab:cyan"
colorMap[28]="tab:brown"
# colorMap[]="black"
# colorMap[]="hotpink"
# colorMap[]="navy"
# colorMap[]="lightsteelblue"
# colorMap[]="turquoise"
# colorMap[]="limegreen"
# colorMap[]="wheat"
# colorMap[]="lightsalmon"

###############################################
# functions
###############################################

def mean(args,data,selection=None):
    mean=np.mean(data[data>0])
    if args.altirocVersion==2 and args.onlyTZ:
        data=data[120:nbOfPixels]
        mean=np.mean(data[data>0])
    return mean

def median(args,data,selection=None,veto=None):

    if veto is not None:
        data=data[data!=veto]

    median=np.median(data[data>0])

    #print(np.median(data[data>0]),np.median(data))
    # blackList = list(set( list(range(0,60)) + list(range(0,225,15)) + list(range(1,225,15)) + list(range(2,225,15))  ))
    # goodList = [element for element in range(225) if element not in blackList]
    # indices_goodList = [element for element in range(225) if element in goodList]
    # median = np.median([data[i] for i in indices_goodList])

    if args.altirocVersion==2 and args.onlyTZ:
        data=data[120:nbOfPixels]
        if veto is not None:
            data=data[data!=veto]
        #print (data)
        median=np.median(data[data>0])
        #print (median)
    return median



def getDCPulser(dac,smallctest): #smallctest is a boolean: 1 for smallCtest and 0 for largeCtest
    dataALTIROC3Conversion = pd.read_csv(os.path.join(os.path.dirname(__file__),'SandBox/DCPulser/ALTIROC3DCpulserB1_2023_09_17.csv'))    
    #dataALTIROC3Conversion = pd.read_csv(os.path.join(os.path.dirname(__file__),'SandBox/DCPulser/ALTIROC3DCpulserB37_2024_02_22.csv'))    


    #dataALTIROC3Conversion = pd.read_csv(os.path.join(os.path.dirname(__file__),'SandBox/ALTIROC3DCpulserB15_2023_10_24.csv'))    
    dacrange="SR"
    if dac>=64:
        dac=dac-64
        dacrange="LR"
    ctestStr="LargeCtest"
    if smallctest: 
        ctestStr="SmallCtest"
    column_name=ctestStr+" "+dacrange
    if dac < min(dataALTIROC3Conversion['DAC']): return -1
    if dac > max(dataALTIROC3Conversion['DAC']): return -1
    # Perform linear interpolation
    interpolated_value = np.interp(dac, dataALTIROC3Conversion['DAC'], dataALTIROC3Conversion[column_name])
    return interpolated_value



def closest_to_target(lst, target):
    #print (lst,target)
    closest_entry = None
    min_distance = float('inf')  # Set initial distance to positive infinity

    for entry in lst:
        distance = abs(target - entry)
        if distance < min_distance:
            min_distance = distance
            closest_entry = entry
    #print (target,closest_entry)
    return closest_entry

def counterAboveThres(args,data,thres=0.05):
    #data=data[1:nbOfPixels]
    counter=np.count_nonzero(data>=thres)
    if args.altirocVersion==2 and args.onlyTZ:
        data=data[120:nbOfPixels]
        counter=np.count_nonzero(data>=thres)
    return counter




def makeHist(data,xLabel="",yLabel="",label="",outName=""):
    plt.figure(figsize = (20, 15))
    bins = np.arange(0,40, 1)
    plt.hist(data,  edgecolor='black',bins=bins)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.grid(True)
    mean = np.mean(data)
    rms = np.std(data)
    plt.text(0.95, 0.9, label, horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.text(0.95, 0.8, f'Mean: {mean:.2f}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.text(0.95, 0.7, f'RMS: {rms:.2f}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
    plt.savefig(outName)
    plt.close()

def getInfo(mystr):
    vec=mystr.replace(".csv","").replace("/","_").split("_")
    #print (mystr)
    dacCharge=-1
    Q=-1
    QForVthc=-1
    Vth=-1
    On=""
    Inj=""
    board="0"
    ts="0"
    N=0
    Ctest=-1
    Cd=-1
    Rtest=-1
    Cp=-1
    cDel=-1
    fDel=-1
    if "ts" in vec:ts=int(vec[vec.index("ts")+1])
    if "dacCharge" in vec:dacCharge=int(vec[vec.index("dacCharge")+1])
    if "Inj" in vec:Inj=vec[vec.index("Inj")+1]
    if "On" in vec:On=vec[vec.index("On")+1]
    if "Vth" in vec:Vth=int(vec[vec.index("Vth")+1])
    if "pulsed" in vec:Vth=int(vec[vec.index("pulsed")+1])
    if "Q" in vec:Q=int(vec[vec.index("Q")+1])
    if "QForVthc" in vec:QForVthc=int(vec[vec.index("QForVthc")+1])
    if "B" in vec:board=int(vec[vec.index("B")+1])
    if "N" in vec:N=int(vec[vec.index("N")+1])
    if "Cd" in vec:Cd=int(vec[vec.index("Cd")+1])
    if "Cp" in vec:Cp=int(vec[vec.index("Cp")+1])
    if "Ctest" in vec:Ctest=int(vec[vec.index("Ctest")+1])
    if "cDel" in vec:cDel=int(vec[vec.index("cDel")+1])
    if "fDel" in vec:fDel=int(vec[vec.index("fDel")+1])
    #Vth=cDel
    return dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N,Ctest,Cd,Rtest,Cp,cDel,fDel


def matplotlibConfig():

    from cycler import cycler
    color=["dodgerblue","tab:red","limegreen","darkviolet","sandybrown","darkgray","tab:pink","tab:olive","tab:cyan","tab:brown","black","hotpink","navy","lightsteelblue","turquoise","limegreen","wheat","lightsalmon"]
    #color=['red','orange','yellow','green','blue','purple']
    mpl.rcParams['axes.prop_cycle'] = cycler(color=color)

    mpl.rcParams['image.cmap']="jet" #'gist_rainbow'
    mpl.rcParams['legend.frameon'] = False
    mpl.rcParams['legend.fontsize'] = 30
    mpl.rcParams['xtick.labelsize'] = 30
    mpl.rcParams['ytick.labelsize'] = 30
    mpl.rcParams['axes.titlesize']  = 30
    mpl.rcParams['axes.labelsize']  = 30
    mpl.rcParams['lines.linewidth'] = 3

    mpl.rcParams['figure.subplot.bottom'] = 0.15
    mpl.rcParams['figure.subplot.hspace'] = 0
    #mpl.rcParams['figure.subplot.vspace'] = 0
    mpl.rcParams['figure.subplot.left'] = 0.15
    mpl.rcParams['figure.subplot.right'] = 0.98
    mpl.rcParams['figure.subplot.top'] = 0.98

   # plt.subplots_adjust(top = 0.99, bottom = 0.12, right = 0.99, left = 0.08, 
   #                     hspace = 0, wspace = 0)

def setLogx(plt,left=1,xticks=None):
    plt.gca().set_xscale('log')
    plt.xlim(left = left)
    if xticks != None:
        plt.gca().set_xticks(xticks)
    plt.gca().get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())



def compArray(yfile1,
              name1,
              yfile2,
              name2,
              xfile,
              xlabel,
              ylabel,
              outName):
    y1Array=np.load(yfile1)
    y2Array=np.load(yfile2)
    if xfile==None:
        xArray=range(0,nbOfPixels)
        xlabel="Pixel number"

    diffArray= y1Array - y2Array
    ratioArray= y1Array/y2Array
        

    #comparison
    plt.figure(figsize = (20, 10))
    plt.plot(xArray , y1Array,label=name1)
    plt.plot(xArray , y2Array,label=name2)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig(outName+"_comp.png")
    plt.close()

    #diff y 1D
    plt.figure(figsize = (20, 10))
    plt.plot(xArray , diffArray, label="Median: {:.1f} {:.1f}".format(np.median(diffArray[0:altiroc3_Mix046.lastVpaPixel]),np.median(diffArray[altiroc3_Mix046.firstTZPixel:altiroc3_Mix046.nbOfPixels] )))
    plt.ylabel(r"$\Delta$ "+str(ylabel))
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig(outName+"_diff.png")
    np.save(outName+"_diff.npy",diffArray)
    plt.close()

    #diff map
    plt.figure(figsize = (13, 10))
    asic_map(diffArray, clabel=r"$\Delta$ "+str(ylabel))
    plt.savefig(outName+"_diffMap.png")
    plt.close()


    #ratio y 1D
    plt.figure(figsize = (20, 10))
    plt.plot(xArray , ratioArray)
    plt.ylabel("ratio")
    plt.xlabel(xlabel)
    #plt.ylim(bottom=0,top=100)
    plt.legend()
    plt.savefig(outName+"_ratio.png")
    plt.close()

    #ratio map
    plt.figure(figsize = (13, 10))
    asic_map(ratioArray, clabel="ratio")
    plt.savefig(outName+"_ratioMap.png")
    plt.close()


    #cor y 1D
    plt.figure(figsize = (15, 10))
    plt.scatter(y1Array , y2Array)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.savefig(outName+"_correlation.png")
    plt.close()


def pol1fit(x,y):

    par=[9999,9999,0]
    if len(x) < 2: 
        return par
    else:
        try:
            #print ("Fit data:",x,y)
            par=np.polyfit(np.array(x), np.array(y), 1)
        except:
            print ('Failed')
            #print (x,y)
            return par
    chi2=np.sum((np.polyval(par, x) - y) ** 2)
    return par[0],par[1],chi2


def myerf(x,A,mu,sigma):
   return A*(1+ scipy.special.erf( -(x - mu)/(sqrt(2)*sigma )))



def whereclose(a, b, rtol=1e-05, atol=1e-08):
    def isclose(a, b, rtol=1e-05, atol=1e-08):
        return np.abs(a-b) <= (atol + rtol * np.abs(b))
    return np.where(isclose(a, b, rtol, atol))


def getYSlices(xArrayList,yArrayList,xList):

    sliceList=[]
    for x in xList:
        myslice=np.zeros(nbOfPixels)
        for pixel in range(nbOfPixels):
            indexList=np.isclose(np.array(xArrayList[pixel]) , x).nonzero()
            #print (xArrayList[pixel],x,            indexList)
            if len( indexList[0])>0:
                val=yArrayList[pixel][indexList[0][0]]               
                myslice[pixel]=val
        sliceList.append(myslice)

    return sliceList
    pass



def computeMeanRMS(df, xVarName, yVarName, ymax, xList=None, Nmin=5, cor=1, keepAll=False):

    if xList==None:
        xList = np.sort(df[xVarName].unique())

    yMean=[]
    yRMS=[]
    xOK=[]
    nEvents=[]

    for x in xList:
        y=df.loc[df[xVarName] == x][yVarName]
        nEvents.append(len(y))

        if len(y) >= Nmin:
            yMean.append(np.mean(y))
            yRMS.append(np.std(y))
            xOK.append(x)
        elif keepAll:
            yMean.append(0)
            yRMS.append(0)
            xOK.append(0)

    return np.array(yMean),np.array(yRMS),np.array(xOK),np.array(nEvents)



def computeAverage(dataList):

    N=min([    len(x) for x,y in dataList])
    
    return dataList[0][0][0:N],np.mean([   y[0:N]  for x,y in dataList] , axis=0)

    
   

def makeOnePlotPerPixel(dataList,basename="Plots/",ymin=None,ymax=None,txt=""):



    fig,axs = plt.subplots(nrows = altiroc3_Mix046.nbOfLines, ncols = altiroc3_Mix046.nbOfLines, figsize=(20,20))
    plt.subplots_adjust(wspace=0, hspace=0)
    for pixel in range(len(dataList)):
        x=dataList[pixel][0]
        y=dataList[pixel][1]

        col= pixel // altiroc3_Mix046.nbOfLines 
        row= altiroc3_Mix046.nbOfLines-1- pixel % altiroc3_Mix046.nbOfLines  
        axs[row,col].scatter(x,y)
        if ymin is not None: axs[row,col].set_ylim(bottom=ymin)
        if ymax is not None: axs[row,col].set_ylim(top=ymax)
        axs[row,col].set_yticklabels([])
        axs[row,col].set_xticks([])
        axs[row,col].set_yticks([])
        axs[row,col].set_xticklabels([])

    plt.text(0, ymin,txt, fontsize = 15)#,ha='right', va='bottom')
    plt.savefig(basename+".png")        


        
        
    plt.close()
    return 


def makeAll2DPlots(df,xVarName,yVarName,xedges,yedges,corArray=None,basename="Plots/",extension="png",separatedPlots=False):
   
    yMeanList=[]
    yRMSList=[]
    xList=[]
    
    #xedges = np.arange(        xMin-xStep/2.,xMax,xStep)
    #yedges = np.arange(-1/2,ymax+1,1.)  
    
    if separatedPlots:
        #for pixel in range(105,135):
        for pixel in range(0,nbOfPixels):
            dfpix=df.loc [ (( df['pixel'] == pixel))]
            if len(dfpix.index)==0: continue
            cor=1
            if corArray is not None: cor=corArray[pixel]
            
            HY, xedges, yedges = np.histogram2d(dfpix[xVarName], dfpix[yVarName], bins=(xedges, yedges))
            HY = HY.T  # Let each row list bins with common y range.
            X, Y = np.meshgrid(xedges, yedges)
            HY[HY==0]=np.nan
            #current_cmap = plt.cm.get_cmap().copy()
            #current_cmap.set_bad(color='white')
            
            locfig=plt.figure("all"+str(pixel),figsize = (13, 10))
            plt.pcolormesh(X, Y, HY,cmap=plt.cm.rainbow)
            plt.xlabel(xVarName)
            plt.ylabel(yVarName)
            #plt.plot( [xedges[0],xedges[-1]],   [95.5,95.5],color='black')
            plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+"_"+str(pixel)+"."+extension)
            plt.close()
        



    #Ugly!!!!!!!!!!!!!!!!!!!
    fig,axs = plt.subplots(nrows = altiroc3_Mix046.nbOfLines, ncols = altiroc3_Mix046.nbOfLines, figsize=(20,20))
    plt.subplots_adjust(wspace=0, hspace=0)
    for pixel in range(0,nbOfPixels):
        dfpix=df.loc [ (( df['pixel'] == pixel))]
        if len(dfpix.index)==0: continue
        cor=1
        if corArray is not None: cor=corArray[pixel]
        
        HY, xedges, yedges = np.histogram2d(dfpix[xVarName], dfpix[yVarName], bins=(xedges, yedges))
        HY = HY.T  # Let each row list bins with common y range.
        X, Y = np.meshgrid(xedges, yedges)
        HY[HY==0]=np.nan
        #current_cmap = plt.cm.get_cmap().copy()
        #current_cmap.set_bad(color='white')
        
                
        col= pixel // altiroc3_Mix046.nbOfLines 
        row= altiroc3_Mix046.nbOfLines-1- pixel % altiroc3_Mix046.nbOfLines  
        axs[row,col].pcolormesh(X, Y, HY,cmap=plt.cm.rainbow)
        axs[row,col].set_yticklabels([])
        axs[row,col].set_xticks([])
        axs[row,col].set_yticks([])
        axs[row,col].set_xticklabels([])
        #axs[row,col].plot( [xedges[0],xedges[-1]],   [95.5,95.5],color='black')


    #plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+".pdf") #mega slow 
    plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+".png")        
    #plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+"."+extension)

    plt.close()
    return 




def makeAll1DPlots(df,xVarName,xedges,corArray=None,basename="Plots/",extension="png",separatedPlots=False):
   
    if separatedPlots:
        #for pixel in range(105,135):
        for pixel in range(0,nbOfPixels):
            dfpix=df.loc [ (( df['pixel'] == pixel))]
            if len(dfpix.index)==0: continue

            cor=1
            if corArray is not None: cor=corArray[pixel]

            data=dfpix[xVarName]
            
            locfig=plt.figure("all"+str(pixel),figsize = (13, 10))
            plt.hist(data, bins=xedges)

            plt.xlabel(xVarName)
            #plt.ylabel(yVarName)
            plt.savefig(basename+"_"+xVarName+"_"+str(pixel)+"."+extension)
            plt.close()
        



    # #Ugly!!!!!!!!!!!!!!!!!!!
    # fig,axs = plt.subplots(nrows = altiroc3_Mix046.nbOfLines, ncols = altiroc3_Mix046.nbOfLines, figsize=(20,20))
    # plt.subplots_adjust(wspace=0, hspace=0)
    # for pixel in range(0,nbOfPixels):
    #     dfpix=df.loc [ (( df['pixel'] == pixel))]
    #     if len(dfpix.index)==0: continue
    #     cor=1
    #     if corArray is not None: cor=corArray[pixel]
        
    #     HY, xedges, yedges = np.histogram2d(dfpix[xVarName], dfpix[yVarName], bins=(xedges, yedges))
    #     HY = HY.T  # Let each row list bins with common y range.
    #     X, Y = np.meshgrid(xedges, yedges)
    #     HY[HY==0]=np.nan
    #     #current_cmap = plt.cm.get_cmap().copy()
    #     #current_cmap.set_bad(color='white')
        
                
    #     col= pixel // altiroc3_Mix046.nbOfLines 
    #     row= altiroc3_Mix046.nbOfLines-1- pixel % altiroc3_Mix046.nbOfLines  
    #     axs[row,col].pcolormesh(X, Y, HY,cmap=plt.cm.rainbow)
    #     axs[row,col].set_yticklabels([])
    #     axs[row,col].set_xticks([])
    #     axs[row,col].set_yticks([])
    #     axs[row,col].set_xticklabels([])
    #     # if col<=7:
    #     #     axs[row,col].set_xlim(0,100)#*    totlsbMedian)
    #     # else:
    #     #     axs[row,col].set_xlim(0,30)#*    totlsbMedian)
    # #plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+".pdf") #mega slow 
    # plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+".png")        
    # #plt.savefig(basename+"_"+yVarName+"_vs_"+xVarName+"."+extension)

    plt.close()
    return 


def getStatistics(df):

    statList=[]
   
    for pixel in range(0,nbOfPixels):
        dfpix=df.loc [ (( df['pixel'] == pixel))]
        statList.append(len(dfpix.index))
        pass
      
    return np.array(statList)


def getAllMeanRMS(df, xVarName, yVarName, ymax, corArray=None, Nmin=5, keepAll=False):

   
   yMeanList=[]
   yRMSList=[]
   xList=[]
   nEventsList=[]

   if corArray is not None:
       cor_df = pd.DataFrame(corArray, columns=['cor'], index=pd.Index(range(len(corArray)), name='pixel'))
       df = pd.merge(df, cor_df, on='pixel', how='inner')
       df[yVarName] = df[yVarName] * df['cor']

   df[yVarName] = df[yVarName].astype(float)
   df_filtered = df[(df[yVarName] < ymax) & (df[yVarName] > 0)]

   # Group by 'pixel' and 'xVarName' and aggregate
   grouped = df_filtered.groupby(['pixel', xVarName])[yVarName].agg(['mean', ('std', lambda x: x.std(ddof=0)), 'count']).reset_index().sort_values(by=['pixel', xVarName]) #panda has default ddof = 1, unmatch with np.std, so specified here

   if not keepAll:
       grouped = grouped[grouped['count'] >= Nmin]

   pixel_grouped = grouped.groupby('pixel')

   # Iterate over the grouped data
   for pixel in range(0,nbOfPixels):
       if pixel in pixel_grouped.groups:
           group = pixel_grouped.get_group(pixel)

           yMean = group['mean'] * (group['count'] >= Nmin)
           yRMS = group['std'] * (group['count'] >= Nmin)
           xOK = group[xVarName] * (group['count'] >= Nmin)
           nEvents = group['count']

           yMeanList.append(np.array(yMean))
           yRMSList.append(np.array(yRMS))
           xList.append(np.array(xOK))
           nEventsList.append(np.array(nEvents))
           #print (nEvents)

       else:
           yMeanList.append(np.array([], dtype=np.float64))
           yRMSList.append(np.array([], dtype=np.float64))
           xList.append(np.array([], dtype=np.float64))
           nEventsList.append(np.array([], dtype=np.float64))

   #print(len(nEventsList[0]),len(yMeanList[0]))
   return yMeanList,yRMSList,xList#,nEventsList




def getAllEff(df, valArray, varName="dac", effThres=0.5, doVthc=False, doInterpolation=False, NMax=-1):
    allEffList = []
    allNList = []
    thresArray = np.zeros(nbOfPixels)
    # Group by 'pixel' and 'varName' to reduce the number of DataFrame lookups
    grouped = df.groupby(['pixel', varName])

    # Pre-compute the size of each group
    group_sizes = grouped.size().unstack(fill_value=0)

    trig_nb = df.groupby(['pixel', varName])["trigger_nb"].mean()#zhenwu add
    trig_group = trig_nb.unstack(fill_value=0)#zhenwu add

    for pixel in range(nbOfPixels):
        if pixel in group_sizes.index:
            NArray = np.array([group_sizes.at[pixel, val] if val in group_sizes.columns else 0 for val in valArray])
            TrigArray = np.array([trig_group.at[pixel, val] if val in trig_group.columns else 0 for val in valArray])#zhenwu add
        else:
            NArray = np.zeros(len(valArray))
            TrigArray = np.zeros(len(valArray))#zhenwu add

        for i in range(0,len(TrigArray)):#zhenwu add
            if TrigArray[i]==0:TrigArray[i]=NMax#zhenwu add

        if NMax <= 0:
            NMax = NArray.max()
        effArray = NArray / NMax if NMax > 0 else NArray
        effArray = NArray / TrigArray#zhenwu add

        thres = getCrossingPoint(valArray, effArray, effThres, 0.5, fromTopToBottom = varName in ["dac"], doInterpolation=doInterpolation, fromRightToLeft=varName in ["dac"] and doVthc)

        thresArray[pixel] = thres

        allEffList.append(np.nan_to_num(effArray))  # nan replace by zero
        allNList.append(np.nan_to_num(NArray))  # nan replace by zero

    return allEffList, allNList, thresArray



def getThreshold(xList, yList, yMax=0.5): #ATT should rewritten using numpy utilities
    #find the value at which the efficiency is below ymax
    thres=0
    startToFindThres=False
    for i, y in enumerate(yList):
        if y>yMax: startToFindThres=True
        if startToFindThres==False: continue
        if y<yMax:    
            thres= xList[i]
            break;
    return thres




def getCrossingPoint(xArray,yArray,ythres,xMin=-1,xMax=-1,doInterpolation=False, fromRightToLeft = False, fromTopToBottom = False):    


   buggyValue=0
   if len(yArray)<2:
      return buggyValue
   

   # Create a boolean mask to identify elements smaller than 1
   mask = (yArray < 1)
   
   # Check if the neighbors are equal to 1 using numpy's "roll" function
   neighbors_equal_to_1 = (np.roll(yArray, 1) == 1) & (np.roll(yArray, -1) == 1)
   
   # Replace elements in the original array with 1 where the mask and neighbor conditions are satisfied
   yArray[mask & neighbors_equal_to_1] = 1

   xOFFSET=xArray[0]
   minIndex=0
   if xMin>0:
      minIndex=max(int((xMin-xOFFSET)),1) #how to make sure the step is 1 so the difference between xMin and xOFFSET equals to the index?
      maxIndex=len(yArray)
   if xMax>0:
      maxIndex=int((xMax-xOFFSET))+1


   if fromRightToLeft: #left low and right high
      yArray = yArray[::-1] #invert array if from right to left
      minIndex = len(yArray)-maxIndex
      maxIndex = len(yArray)-minIndex


   if fromTopToBottom:
      minIndex=max(minIndex,np.argmax(yArray>=ythres)) #start from points above the thres.
      try: index=minIndex+np.argmax(yArray[minIndex:maxIndex]<=ythres)
      except:return buggyValue
   else:
      minIndex=max(minIndex,np.argmax(yArray<=ythres))
      try: index=minIndex+np.argmax(yArray[minIndex:maxIndex]>=ythres)
      except:return buggyValue
      pass


   if fromRightToLeft:
      yArray = yArray[::-1] #revert back the array
      minIndex = len(yArray)-maxIndex
      maxIndex = len(yArray)-minIndex
      index = len(yArray)-index-1

   #print (xArray,yArray,minIndex,maxIndex,index)


   if index<=0 or index==minIndex:
      return xMin
   if index==len(yArray):
      return xArray[-1]


   if doInterpolation==False:
      return xArray[index]
   else:
      a=(yArray[index]-yArray[index+1])/(xArray[index]-xArray[index+1]) if fromRightToLeft else (yArray[index]-yArray[index-1])/(xArray[index]-xArray[index-1])
      b=yArray[index]-a*xArray[index]
      x=0
      if a!=0:
         x=(ythres-b)/a
         
   return x


def colSlice(data, fig=None, ax=None, clabel=None, vmin=None, vmax=None , nbOfLines=15, cmap = 'rainbow',ylabel="",label=""):
    # Figure and axis
    if not fig:
        fig = plt.gcf()
    if not ax:
        ax = plt.gca()


    #data[134]=40
    for col in range(8,nbOfLines):
        plt.xlabel('Row')
        plt.ylabel(ylabel)
        #plt.plot(np.arange(nbOfLines),data[col*nbOfLines:(col+1)*nbOfLines],label="col"+str(col) )

    bidim=np.array([data[col*nbOfLines:(col+1)*nbOfLines] for col in range(8,nbOfLines) ])
    #print ( np.mean(bidim,axis=0))

    plt.plot(np.arange(nbOfLines),np.median(bidim,axis=0) ,linewidth=5,label=label )

    plt.legend(fontsize=12)
    return


def quadraticDiff(a,b):
    c=np.sqrt(np.power(a,2)-np.power(b,2))
    return c

def asic_map(data, fig=None, ax=None, clabel=None, vmin=None, vmax=None , nbOfLines=15, cmap = 'rainbow',txt=""): #Stolen from LPC

    '''
    This fonction plot the 2D matrix of the 15x15 pixels array.
    `pix` must be a 1D array of 255 elements of any quantities.
    The first 15 pixels is the first column etc ...
    `clabel` is the label of the color bar.
    `vmin` and `vmax` are limit values for the color bar
    `fig` and `ax` can be specified to plot these maps on subplots.
    '''


    #if data[0]==0: data[0]=np.median(data[1:225])#UGLY HACK for ALTIROC3

    # Re-shaping of the array
    m = np.array([data[i*nbOfLines:(i+1)*nbOfLines] for i in range(0, nbOfLines)], dtype=np.float)
    m = np.swapaxes(m, 0, 1)
    m = m[::-1,]
    
    # Figure and axis
    if not fig:
        fig = plt.gcf()
    if not ax:
        ax = plt.gca()

    # white space
    plt.subplots_adjust(top = 0.98, bottom = 0.02, right = 0.98, left = 0.02, 
                        hspace = 0, wspace = 0)

    # Range of the z-axis
    #median=np.median(data[data > 0])
    #diff=max( abs(np.max(data[data > 0])-median), abs(np.min(data[data > 0])-median))
    if not vmin:
        #vmin=median-diff
        vmin=data.min()
    if not vmax:
        #vmax=median+diff
        vmax=data.max()
    # Plot
    im = ax.imshow(m, alpha=0.8, cmap=cmap)
    im.set_clim(vmin, vmax)


 
    
    # Color bar
    cbar = fig.colorbar(im, ax=ax)
    if clabel:
        cbar.set_label(clabel)
    ax.set_aspect('auto')

    # Grid
    ax.set_xticks(np.arange(m.shape[1]+1)-.5)
    ax.set_yticks(np.arange(m.shape[0]+1)-.5)
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    ax.grid(color="w", linestyle='-', linewidth=1.5, alpha=1)


    #median=np.median(data)
    median=np.median(data[data > 0])
    medianVpa=np.median(data[0:altiroc3_Mix046.lastVpaPixel])
    medianTZ=np.median(data[altiroc3_Mix046.firstTZPixel:altiroc3_Mix046.nbOfPixels])
    
    #plt.text(1.2,0.99,txt,transform = ax.transAxes, fontsize=0)
    #plt.text(1.14,0.94,"{:.2f} {:.2f}".format(medianVpa,medianTZ),transform = ax.transAxes, fontsize=20)
    plt.text(1.14,0.99,"{:.2f}".format(medianVpa),transform = ax.transAxes, fontsize=20)

    rms=np.std(data[data>0])
    rmsVpa=np.std(data[0:altiroc3_Mix046.lastVpaPixel])
    rmsTZ=np.std(data[altiroc3_Mix046.firstTZPixel:altiroc3_Mix046.nbOfPixels])
    #plt.text(1.14,0.89,"{:.2f} {:.2f}".format(rmsVpa,rmsTZ),transform = ax.transAxes, fontsize=20)
    plt.text(1.14,0.94,"{:.2f} ".format(rms),transform = ax.transAxes, fontsize=20)

    #write numbers
    for (j,i),label in np.ndenumerate(m):
        r=1
        if label<1:r=2
        plt.gca().text(i,j,str(round(label,r)),ha='center',va='center')
        

    return


def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-0.5 * ((x - mean) / stddev)**2)
