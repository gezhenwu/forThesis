import glob
import re
import csv
import pandas as pd
import numpy as np
import sys
import os.path

counter = 0
epath = ['009','00d','00a','00e','00b','00f','010','014','011','015','012','016','013','017','018','01a','019','01b']
for elink in epath:
    module = 5+counter//2
    counter += 1
    fileName = './rawData_txt/module%d'%module+'_vth0_'+elink+'.txt'
    file_exist = os.path.isfile(fileName)
    if file_exist is False:
        pass
    # elif module != 10 or elink != '012':
    #     pass
    else:
        for i in range (0,1024):
            vth_str = str(i)
            if i%256==255:
                print('elink'+elink+', '+'vth = '+vth_str)
            file = open('./rawData_txt/module%d_vth'%module+vth_str+'_'+elink+'.txt','r') 
            list = []
            pattern1= re.compile(r'ELINK')
            pattern2 = re.compile(r'Chunk')
            pattern3 = re.compile(r'OUTOFBAND')
            pattern4 = re.compile(r'File')
            pattern5 = re.compile(r'Blocksize')
            pattern6 = re.compile(r']]')                       
            pattern7 = re.compile(r'@@')
            pattern8 = re.compile(r'==> BLOCK')
            pattern9 = re.compile(r'\(sz=7\)')
            pattern10 = re.compile('<.*?\)',re.S) 
            pattern11 = re.compile('sz=.*?\)',re.S) 

            flag1 = 0
            count =0

            while 1:
                line = file.readline()
                if not line:
                    # print("Read file End or Error")
                    break
                elif pattern1.search(line) or pattern2.search(line) or pattern3.search(line) or pattern4.search(line) or pattern5.search(line) or pattern6.search(line) or pattern7.search(line):
                    pass
                elif  pattern8.search(line):
                    flag1 = 1
                    pass
                else:
                    if flag1==1:
                        line = line[9:]     
                        flag1 = 0    
                    if pattern9.search(line):
                        line = 'f0 ff ff'               
                    if pattern10.search(line):
                        line = re.sub(pattern10,'',line)  
                    if pattern11.search(line):
                        line = re.sub(pattern11,'',line)  
                    line = line.strip('\n')
                    line = line.split(' ')
                    list += line
            file.close()

            list = [x.strip() for x in list if x.strip()!='']
            # print(list)
            new_list = []
            n=3 
            for i in range(0, len(list), n):
                temp = list[i:i + n]
                temp += vth_str.split(' ')
                temp += elink.split(' ')
                new_list.append(temp)
            # print(new_list)

            column = ['pixel',"tot",'toa','dac','chipid']
            dataframe=pd.DataFrame(columns=column,data=new_list)

            dataframe.to_csv('./rawData_csv/module%d_vth'%module+vth_str+'_'+elink+'.csv',encoding='gbk')    