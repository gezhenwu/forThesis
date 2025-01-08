#!/usr/bin/env python3
#sudo python3 scripts/test0.py  -o ~/Measures


#=======================================================
# import
#=======================================================
import time
import sys,os
import numpy as np
import pandas as pd
from lib import Utils
import subprocess


# get parameters
(options, args) = Utils.getParser()

if options.gbt in range(0,3):
    from lib import altiroc3_Mix046
    altiroc3 = altiroc3_Mix046
    use_lumi = True
elif options.gbt in range(3,6):
    from lib import altiroc3_Mix230
    altiroc3 = altiroc3_Mix230
    use_lumi = False
elif options.gbt in range(6,9):
    from lib import altiroc3_Mix310
    altiroc3 = altiroc3_Mix310
    use_lumi =  False
else:
    print("Please input the elink Pattern you want to configure.")
    sys.exit()

# Config parameter
devnr = options.devnr
gbt = options.gbt
print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,gbt))
timing_addr = options.timingAddr
lumi_addr = options.LumiAddr
moduleConfigFile = options.ConfigFile
if moduleConfigFile is None:
    print("\n***No module is configured beacause no file is input.***\n")
    # sys.exit()

alti_dict = Utils.read_yaml_to_dict(moduleConfigFile)
# for modules in alti_dict["Modules"]:
#     module_nb = modules["module"]
#     for chips in modules["chips"]:
#         chip_nb = chips["chip"]
#         chip_startfile = chips["startfile"]
#         vth_thre = chips["vth_thre"]
#         chip_vthcfile = chips["vthcfile"]
#         print("Configure: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
#         alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

#         alti.setup(chip_startfile,chip_vthcfile,options)   

#         alti.setDacVth(vth_thre, options.dacVthRange)

#         alti.setPulser(options.dacCharge)
#         print(alti.rd_asic_reg(0x2011,1)[0])
#         # alti.set_trig_latency(options.trigLatency)
        
#         # print("Turning off all discriminators")
#         # alti.setDiscriOffCol("all")        
        
#         reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
#         print ("Module%d, chip%d, Check PS locking: "%(module_nb,chip_nb),reg,bin(reg))
# alti.byebye()

# elinkConfigFile = options.elinkFile
# if elinkConfigFile is None:
#     print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
#     sys.exit()
# alti.felixcfg(elinkConfigFile)
# alti.decode8b10b(1)
# alti.idle3(3)
# # alti.nIdle(options.nIdle)
# alti.nIdle(4)

# output dir -----------------------------------------
outputbasedir = options.outputDir
if not os.path.isdir(outputbasedir):
    os.makedirs(outputbasedir)

for col in range(options.startCol,options.endCol+1,options.stepCol):

    if options.dacChargeMin<0 and options.dacChargeMax<0:
        dacChargeList  =list(range(0,14))
        dacChargeList +=list(range(14,28,1))
        dacChargeList += list(range(28,64,8))
        dacChargeList +=list(range(84,128,8))
        #dacChargeList +=[25,50]#10fC and 20fC amd 102fC
        dacChargeList +=[124]
        dacChargeList = list(set(dacChargeList))# re;ove duplicate
        #dacChargeList =[20]
    else:
        dacChargeList = reversed(list(range(options.dacChargeMin,options.dacChargeMax+1,options.dacChargeStep)))

    cnt = 0
    sizeList=[]
    dataFrameList=[]
    data_size_all = []
    for dacCharge in dacChargeList:
        for modules in alti_dict["Modules"]:
            module_nb = modules["module"]
            for chips in modules["chips"]:
                chip_nb = chips["chip"]
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)
                if cnt ==0:                    
                    options.pixelInj = "col"+str(col) 
                    # if col != options.startCol:
                        # alti.turnOffCol("col"+str(col-1))
                        # alti.disInjCol("col"+str(col-1),options)
                    # else:
                    #     alti.setDiscriOffCol("col"+str(options.endCol))
                    #     alti.disInjCol("col"+str(options.endCol),options)                        
                    # alti.turnOnCol("col"+str(col))
                    # alti.injCol("col"+str(col),options) 
                
                # alti.setPulser(dacCharge)    

        cnt+=1
        alti.byebye()    

        # alti.cmdtrigger(options.triggerFre)  
        # alti.cmdgbrst()
        tmpdat = outputbasedir+'/Rawdat_charge/col_'+str(col)+'_Q_'+str(dacCharge)
        # alti.extract_data(tmpdat)
        # alti.cmdtrigger(0)
        # alti.felixcfg('ic_ec_only.yelc')

        csv_len_scan = []
        for modules in alti_dict["Modules"]:
            module_nb = modules["module"]
            tick = 0
            for chips in modules["chips"]:
                chip_nb = chips["chip"]
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)
                finaltxt = outputbasedir +"/M"+str(module_nb + 14*gbt)+"C"+str(chip_nb)+"/chargeScan"+options.suffix+"/"+Utils.getOutName(options)
                if not os.path.isdir(finaltxt):
                    os.makedirs(finaltxt)
                prefix = finaltxt            
                tmptxt = prefix+'txt_data_'+'dacCharge_' + str(dacCharge) + '.txt'
                # os.system('rm'+tmptxt)
                suffix='dacCharge_' + str(dacCharge) + '_.csv'
                #metaFN   = prefix+ '/meta_data_'+suffix
                timingFN = prefix+'timing_data_'+suffix
                if tick == 0:
                    if os.path.isfile(timingFN):
                        os.system("rm " + timingFN)                   
                extractOK = alti.analyse_data(tmpdat,tmptxt,timingFN,chip_nb)
                tick+=1

                if options.autoStop:
                    if extractOK==1:
                        csv_len_scan.append(Utils.get_total_rows(timingFN))

        if options.autoStop:
            data_size_all.append(csv_len_scan) 
            if len(data_size_all) > 5 and Utils.is_all_zero(data_size_all[-6])==False:
                if Utils.is_all_zero(data_size_all[-5]) & Utils.is_all_zero(data_size_all[-4]) & Utils.is_all_zero(data_size_all[-3]) & Utils.is_all_zero(data_size_all[-2]) & Utils.is_all_zero(data_size_all[-1]):
                    print("Stop scan at %d for column %d"%(dacCharge,col))
                    break  

del alti
