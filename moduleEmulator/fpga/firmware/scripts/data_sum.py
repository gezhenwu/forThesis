import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import numpy as np
import os
import traceback
import glob
import sys
import re
import csv
from scipy import interpolate
import re
from collections import OrderedDict
import seaborn as sns

def main():
    if len(sys.argv) < 2:
        print ('input file name')
        return 0
    else:
        basefname = sys.argv[1]
    files = glob.glob1('./rawData_csv/', basefname+'.csv')
    if(files==[]):
        print ('No file found')
        return 0
    
    addr = []
    index = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e']
    for i in range (0,15):
        for j in range (0,15):
            if i==0:
                addr += index[j]
            else:
                addr += (index[i]+index[j]).split(' ')    
    addr += 'f0'.split(' ')
    # print(addr)

    eff_all = []
    for filename in files:    
        module = os.path.splitext(filename)[0].split('_')[0]
        vth = os.path.splitext(filename)[0].split('_')[1].strip().strip('vth')
        elink = os.path.splitext(filename)[0].split('_')[2]

        df = pd.read_csv('./rawData_csv/'+filename)
        
        eff_vth = [int(vth)]

        for k in addr:
            try:
                eff=df.pixel.value_counts()[k]
                if k == 'f0' and (eff>105 or eff<95):
                    print(k,eff)
            except:
                eff=0
            eff_vth.append(eff)
        eff_all.append(eff_vth)        

    addr.insert(0, 'vth')
    column = addr
    dataframe = pd.DataFrame(columns=column,data=eff_all)
    dataframe.to_csv('./sum_csv/'+module+'_'+elink+'.csv',encoding='gbk') 

    raw_data = pd.read_csv(os.path.expanduser('./sum_csv/'+module+'_'+elink+'.csv'))
    raw_data.sort_values(by=['vth'], ascending=True, inplace=True)
    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)
    fig.dpi = 300
    fig.set_size_inches(16, 9)
    plt.xlabel('Threshold (DACU)',labelpad=10,fontsize=20)    
    plt.ylabel('Efficiency',labelpad=15,fontsize=20)
    # ax.set_ylim([0, max(effi_mean)+50])
    if module=='module10':
        plt.title('Threshold scan for 225 pixels of digital module',x=0.5,y=1.025,fontsize=20)
        plt.xlim([100,650])
    else:
        plt.title('Threshold scan for 225 pixels of Emulator',x=0.5,y=1.025,fontsize=20)
        plt.xlim([150,700])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    # colors = list(matplotlib.colors.XKCD_COLORS.items())
    # cmap = plt.cm.get_cmap('gist_rainbow')   

    vth_xasis = raw_data[column[0]]

    for i in range (1,226):
        efficiency_yasix = raw_data[column[i]]/(raw_data[column[226]])   
        # color = colors[i][1]
        # color = cmap(i/200)
        if i%40<10:
            colors = sns.color_palette("Paired",10)
        elif i%40<20:
            colors = sns.color_palette()
        elif i%40<30:
            colors = sns.color_palette("Set2",10)
        elif i%40<40:        
            colors = sns.color_palette("hls",10)

        color = colors[i%10]
        
        line = ax.plot(vth_xasis, efficiency_yasix, color=color, linewidth = 1)
    plt.savefig('./plots/'+module+'_'+elink+'.png', dpi=300)
    plt.savefig('./plots/'+module+'_'+elink+'.eps', dpi=300)

try:
    main()
except:
    traceback.print_exc()