# python3 delayScan_peb_multiCH.py -b 1 --autoStop 1 --cDelayMin 0 --cDelayMax 15 --cDelayStep 1 --fDelayMin 0 --fDelayMax 15 --fDelayStep 1 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 --dacCharge 76 --smallCtest --triggerFre 50 -N 50 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/1F_timing_320M.yelc -o ./Measurements/peb1f/

#!/usr/bin/env python3
#sudo python3 scripts/test0.py  -o ~/Measures

#=======================================================
# import
#=======================================================
import sys,os
from lib import Utils
import traceback
from lib import serial_comm

# get parameters
(options, args) = Utils.getParser()
devnr = options.devnr

serialcomm = serial_comm.SerialComm(card = devnr)

timing_addr = options.timingAddr
lumi_addr = options.LumiAddr
moduleConfigFile = options.ConfigFile
if moduleConfigFile is None:
    print("\n***No module is configured beacause no file is input.***\n")
alti_dict = Utils.read_yaml_to_dict(moduleConfigFile)

elinkConfigFile = options.elinkFile
if elinkConfigFile is None:
    print("\n***Please input the file to configure FELIX elinks for data taking.***\n")
    sys.exit()

# output dir -----------------------------------------
outputbasedir = options.outputDir
if not os.path.isdir(outputbasedir):
    os.makedirs(outputbasedir)

def channelConfig(channel):
    if channel in range(0,3):
        from lib import altiroc3_Mix046
        altiroc3 = altiroc3_Mix046
        use_lumi = True
    elif channel in range(3,6):
        from lib import altiroc3_Mix230
        altiroc3 = altiroc3_Mix230
        use_lumi = False
    elif channel in range(6,9):
        from lib import altiroc3_Mix310
        altiroc3 = altiroc3_Mix310
        use_lumi =  False
    else:
        print("Please input the elink Pattern you want to configure.")
        sys.exit()   

    for ch in alti_dict["Channels"]:
        ch_nb = ch["channel"]
        if ch_nb == channel:
            print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,ch_nb))
            for modules in ch["Modules"]:
                module_nb = modules["module"]      
                for chips in modules["Chips"]:
                    chip_nb = chips["chip"]
                    chip_startfile = chips["startfile"]
                    vth_thre = chips["vth_thre"]
                    chip_vthcfile = chips["vthcfile"]
                    print("Configure: module: "+str(module_nb)+", chip: "+str(chip_nb)+"\n")
                    alti = altiroc3.Altiroc(devnr = devnr, gbt = ch_nb, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

                    alti.setup(chip_startfile,chip_vthcfile,options)
                    alti.setDacVth(vth_thre, options.dacVthRange)
                    alti.setPulser(options.dacCharge)

                    reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
                    print ("channel %d, Module%d, chip%d, Check PS locking: "%(ch_nb,module_nb,chip_nb),reg,bin(reg))

                    cdelay=3
                    clk40delay=int(cdelay/2)
                    alti.wr_asic_reg(0x101B, cdelay+(clk40delay<<4))

            # alti.byebye()
            del alti

def scanCfg(channel,col,cdelay,fdelay):
    if channel in range(0,3):
        from lib import altiroc3_Mix046
        altiroc3 = altiroc3_Mix046
        use_lumi = True
    elif channel in range(3,6):
        from lib import altiroc3_Mix230
        altiroc3 = altiroc3_Mix230
        use_lumi = False
    elif channel in range(6,9):
        from lib import altiroc3_Mix310
        altiroc3 = altiroc3_Mix310
        use_lumi =  False
    else:
        print("Please input the elink Pattern you want to configure.")
        sys.exit()

    for ch in alti_dict["Channels"]:
        ch_nb = ch["channel"]
        if ch_nb == channel:
            print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,ch_nb))
            for modules in ch["Modules"]:
                module_nb = modules["module"]      
                for chips in modules["Chips"]:
                    chip_nb = chips["chip"]
                    alti = altiroc3.Altiroc(devnr = devnr, gbt = ch_nb, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

                    print("Configuring channel %d module %d asic %d column %d cDelay %d fDelay"%(ch_nb,module_nb,chip_nb,col,cdelay,fdelay))

                    if cdelay == options.cDelayMin and fdelay == options.fDelayMin:
                        options.pixelInj = "col"+str(col)
                        if col != options.startCol:
                            alti.turnOffCol("col"+str(col-1))
                            # alti.disInjCol("col"+str(col-1),options)
                        alti.turnOnCol("col"+str(col))
                        # alti.injCol("col"+str(col),options) 
                
                    clk40delay=int(cdelay/2)            
                    alti.wr_asic_reg(0x101B, cdelay+(clk40delay<<4))
                    alti.wr_asic_reg(0x101C, fdelay)

            # alti.byebye()
            del alti

def dataExtract(channel,col,cdelay,fdelay,tmpdat):
    if channel in range(0,3):
        from lib import altiroc3_Mix046
        altiroc3 = altiroc3_Mix046
        use_lumi = True
    elif channel in range(3,6):
        from lib import altiroc3_Mix230
        altiroc3 = altiroc3_Mix230
        use_lumi = False
    elif channel in range(6,9):
        from lib import altiroc3_Mix310
        altiroc3 = altiroc3_Mix310
        use_lumi =  False
    else:
        print("Please input the elink Pattern you want to configure.")
        sys.exit()

    for ch in alti_dict["Channels"]:
        ch_nb = ch["channel"]
        if ch_nb == channel:
            print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,ch_nb))
            row_total_ch = 0
            for modules in ch["Modules"]:
                module_nb = modules["module"]
                tick = 0   
                for chips in modules["Chips"]:
                    chip_nb = chips["chip"]
                    alti = altiroc3.Altiroc(devnr = devnr, gbt = ch_nb, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb, use_fice = True, use_serialcomm = False)
                    print("options.suffix: ",options.suffix)
                    print("Utils.getOutName(options): ",Utils.getOutName(options))
                    finaltxt = outputbasedir +"/t"+str(ch_nb)+"/M"+str(module_nb + 14*ch_nb)+"C"+str(chip_nb)+"/delayScan"+options.suffix+"/"+Utils.getOutName(options)
                    print("finaltxt: ",finaltxt)
                    if not os.path.isdir(finaltxt):
                        os.makedirs(finaltxt)
                    prefix = finaltxt            
                    tmptxt = prefix+'txt_data_'+'cdelay_' + str(cdelay) +'_fdelay_'+ str(fdelay)+ '.txt'
                    print("tmptxt: ",tmptxt)                
                    suffix='cdelay_' + str(cdelay) +'_fdelay_'+ str(fdelay)+ '.csv'
                    print("suffix: ",suffix)
                    timingFN = prefix+'timing_data_'+suffix
                    print("timingFN: ",timingFN)
                    if tick == 0:
                        if os.path.isfile(timingFN):
                            os.system("rm " + timingFN)
                    alti.analyse_data(tmpdat,tmptxt,timingFN,chip_nb)
                    tick+=1

                    if Utils.get_total_rows(timingFN) > 0:
                        row_total_ch += 1

            # alti.byebye()  #use_fice == True, no byebye() function
            del alti
            return row_total_ch

def main():
    for channel in range(0,9):
        if channel < 4 or channel > 7:
            continue
        channelConfig(channel)

    serialcomm.clear()
    os.system("feconf "+elinkConfigFile)
    os.system("flx-config DECODING_HGTD_ALTIROC 1")
    os.system("flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1")
    os.system("flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4")

    for col in range(options.startCol,options.endCol+1,options.stepCol):        
        cdelayList = list((range(options.cDelayMin,options.cDelayMax+1,options.cDelayStep)))
        fdelayList = list((range(options.fDelayMin,options.fDelayMax+1,options.fDelayStep)))
        for cdelay in cdelayList:
            for fdelay in fdelayList:
                for channel in range(0,9):
                    if channel < 4 or channel > 7:
                        continue
                    try:
                        scanCfg(channel,col,cdelay,fdelay)
                    except:
                        print('channel %d col %d cdelay %d fdelay %d configuration failed'%(channel,col,cdelay,fdelay))
                
                serialcomm.clear()
                os.system("fttcemu -f " + str(options.triggerFre))
                os.system("flx-config HGTD_ALTIROC_FASTCMD_GBRST 1")
                os.system("flx-config HGTD_ALTIROC_FASTCMD_GBRST 0")
                tmpdat = outputbasedir+'/Rawdat_delay/col_'+str(col)+'_cdelay_' + str(cdelay) +'_fdelay_'+ str(fdelay)
                os.system("fdaq -t 1 "+ tmpdat + " -T")
                os.system("fttcemu -n")

                for channel in range(0,9):
                    if channel < 4 or channel > 7:
                        continue                
                    row_nb_allCH = 0
                    row_nb = dataExtract(channel,col,cdelay,fdelay,tmpdat)
                    row_nb_allCH += row_nb
                
                # row_nb_allStep = []
                # row_nb_allStep.append(row_nb_allCH)                    
                # if options.autoStop and dacVth >400:
                #     if row_nb_allStep[-5]==0 and row_nb_allStep[-4]==0 and row_nb_allStep[-3]==0 and row_nb_allStep[-2]==0 and row_nb_allStep[-1]==0:
                #         print("Stop scan at %d for column %d"%(dacVth,col))
                #         break

try:
    main()
except:
    traceback.print_exc()
