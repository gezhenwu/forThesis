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

if options.pattern == "Mix046":
    from lib import altiroc3_Mix046
    altiroc3 = altiroc3_Mix046
    use_lumi = True
elif options.pattern == "Mix230":
    from lib import altiroc3_Mix230
    altiroc3 = altiroc3_Mix230
    use_lumi = False
elif options.pattern == "Mix310":
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
for modules in alti_dict["Modules"]:
    module_nb = modules["module"]
    for chips in modules["chips"]:
        chip_nb = chips["chip"]
        chip_startfile = chips["startfile"]
        vth_thre = chips["vth_thre"]
        chip_vthcfile = chips["vthcfile"]
        print("Configure: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
        alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

        alti.setup(chip_startfile,chip_vthcfile,options)   

        alti.setDacVth(vth_thre, options.dacVthRange)

        alti.setPulser(options.dacCharge)
        print(alti.rd_asic_reg(0x2011,1)[0])
        # alti.set_trig_latency(options.trigLatency)        

        # print("Turning off all discriminators")
        # alti.setDiscriOffCol("all")

        reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
        
alti.byebye()

elinkConfigFile = options.elinkFile
if elinkConfigFile is None:
    print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
    sys.exit()
alti.felixcfg(elinkConfigFile)
alti.decode8b10b(1)
alti.idle3(3)
# alti.nIdle(options.nIdle)
alti.nIdle(4)

# output dir -----------------------------------------
outputbasedir = options.outputDir
if not os.path.isdir(outputbasedir):
    os.makedirs(outputbasedir)

for col in range(options.startCol,options.endCol+1,options.stepCol):
    dacVthcList = reversed(list(range(options.dacVthcMin,options.dacVthcMax+1,options.dacVthcStep)))
    cnt = 0
    sizeList=[]
    dataFrameList=[]
    data_size_all = []
    for dacVthc in dacVthcList:
        for modules in alti_dict["Modules"]:
            module_nb = modules["module"]
            for chips in modules["chips"]:
                chip_nb = chips["chip"]
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)
                if cnt ==0:                    
                    options.pixelInj = "col"+str(col) 
                    if col != options.startCol:
                        alti.turnOffCol("col"+str(col-1))
                    #    alti.disInjCol("col"+str(col-1),options)
                    # else:
                    #     alti.setDiscriOffCol("col"+str(options.endCol))
                    #     alti.disInjCol("col"+str(options.endCol),options)                        
                    alti.turnOnCol("col"+str(col))
                    alti.injCol("col"+str(col),options)       

                    alti.wr_asic_reg(0x0FF4, 0)#set vthc to zero for all channels
                for pix in alti.getPixelList(options.pixelInj):
                    baseaddr = (16*pix)+(16*(pix//15))
                    address = baseaddr + 4
                    alti.wr_asic_reg(address, dacVthc)
        cnt+=1
        alti.byebye() 

        alti.cmdtrigger(options.triggerFre)
        alti.cmdgbrst()
        tmpdat = outputbasedir+'/Rawdat_vthc/col_'+str(col)+'_Vthc_'+str(dacVthc)
        alti.extract_data(tmpdat)
        alti.cmdtrigger(0)
        # alti.felixcfg('ic_ec_only.yelc')

        csv_len_scan = []
        for modules in alti_dict["Modules"]:
            module_nb = modules["module"]
            tick = 0
            for chips in modules["chips"]:
                chip_nb = chips["chip"]
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)
                finaltxt = outputbasedir +"/M"+str(module_nb + 14*gbt)+"/vthcScan"+options.suffix+"/"+Utils.getOutName(options)
                if not os.path.isdir(finaltxt):
                    os.makedirs(finaltxt)
                prefix = finaltxt            
                tmptxt = prefix+'txt_data_'+'dacVthc_' + str(dacVthc) + '.txt'                
                suffix='dacVthc_' + str(dacVthc) + '_.csv'                
                timingFN = prefix+'timing_data_'+suffix
                if tick == 0:
                    if os.path.isfile(timingFN):
                        os.system("rm " + timingFN)                
                extractOK = alti.analyse_data(tmpdat,tmptxt,timingFN,chip_nb)
                tick+=1

                if options.autoStop and dacVthc <127:
                    if extractOK==1:
                        csv_len_scan.append(Utils.get_total_rows(timingFN))

        if options.autoStop and dacVthc <127:
            data_size_all.append(csv_len_scan)
            if len(data_size_all) > 5 and Utils.is_all_zero(data_size_all[-6])==False:
                if Utils.is_all_zero(data_size_all[-5]) & Utils.is_all_zero(data_size_all[-4]) & Utils.is_all_zero(data_size_all[-3]) & Utils.is_all_zero(data_size_all[-2]) & Utils.is_all_zero(data_size_all[-1]):
                    print("Stop scan at %d for column %d"%(dacVthc,col))
                    break  
    my_reg_addr=0x1000
    my_reg=alti.rd_asic_reg(my_reg_addr,1)[0]
    print("-----------------------------------------------------ALTIROC3 reg_reading-------------------------------------")
    print(my_reg_addr)
    print(my_reg)
    print ("Module%d, chip%d, Check PS locking: "%(module_nb,chip_nb),reg,bin(reg))

    del alti
