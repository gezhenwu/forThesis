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


pixelOn="all"
pixelInjList=[    "col",
                  "pix",
                  "rndFifteen",
                  "rndFive",
                  "rndNine",
                  "rndThree",
                  "row",
                  "sparseFifteen",
                  "squareFive",
                  "squareThree"]

Cp=0
CtestList=[26,208]

boardList=[1,4,9,11,12,15,25,28,34,35,36,37,47]

for board in boardList:
    for pixelInj in pixelInjList:
        for Ctest in CtestList:
            cmd="cat Plots/Data3*_B_"+str(board)+"_*On_"+pixelOn+"_Inj_"+pixelInj+"*Cp_"+str(Cp)+"*Ctest_"+str(Ctest)+"*summary.dat  > B_"+str(board)+"_On_"+pixelOn+"_Inj_"+pixelInj+"_Cp_"+str(Cp)+"_Ctest_"+str(Ctest)+"_.dat"
            print (cmd)
