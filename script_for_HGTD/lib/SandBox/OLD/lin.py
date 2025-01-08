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
# main
###############################################



if __name__=='__main__':


    #ArgumentParser
    argBool = lambda s: s.lower() in ['true', 't', 'yes', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--outputName', help = '',default="")
    parser.add_argument('-o', '--outputDir', help = 'Path of the output directory',default="Plots/")
    parser.add_argument('-i', help = '',default="Plots/Data2022_01_24vthcScanOn_all_Inj_col_Vth_540_Q_12_combined_thres.npy", nargs='*')
    args = parser.parse_args()
    

    yfileList=args.i
    outName=args.outputDir+"/lin_"+args.outputName


    columns=["board","ch","Q","thres"]
    df = pd. DataFrame(columns=columns)

    for counter,yfile in enumerate(sorted(yfileList)):
        
        dacCharge,Q,QForVthc,Vth,On,Inj,board,ts,N=anaUtils.getInfo(yfile)


        yArray=np.load(yfile)
        for ch,y in enumerate(yArray):
        
            tempdf = pd.DataFrame(        [[int(board),int(ch),float(Q),y]],columns=columns)
            df=pd.concat([df,tempdf])


    #plt.savefig(outName+"_comp.png")


    
plt.figure(figsize = (20, 10))
for ch in range(0,15):
    tmpdf=df.loc[df["ch"] == ch]
    Q=tmpdf["Q"]
    thres=tmpdf["thres"]
    plt.scatter(Q,thres)
    a,b,chi2=anaUtils.pol1fit(Q,thres)
    print (ch,a,b)
    plt.plot(Q,a*Q+b)

plt.savefig(outName+"_lin.pdf")
