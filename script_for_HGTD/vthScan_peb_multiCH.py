# python3 vthScan_peb_multiCH.py -b 12 --autoStop 1 --dacVthMin 200 --dacVthMax 600 --dacVthStep 1 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 --dacCharge 12 --triggerFre 50 -N 50 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/t1t2_forHV.yelc -o ./Measurements/receptionTest/hvOn_Q12/


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

                    print(alti.rd_asic_reg(0x2011,read_len=1)[0])

                    reg = alti.rd_asic_reg(0x2000,read_len=1)[0]
                    print ("channel %d, Module%d, chip%d, Check PS locking: "%(ch_nb,module_nb,chip_nb),reg,bin(reg))
            # alti.byebye()
            del alti

def scanCfg(channel,col,scanValue):
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
            for modules in ch["Modules"]:
                module_nb = modules["module"]      
                for chips in modules["Chips"]:
                    chip_nb = chips["chip"]
                    alti = altiroc3.Altiroc(devnr = devnr, gbt = ch_nb, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb)

                    if scanValue == options.dacVthMin:
                        options.pixelInj = "col"+str(col)
                        if col != options.startCol:
                            alti.turnOffCol("col"+str(col-1))
                            # alti.disInjCol("col"+str(col-1),options)
                        alti.turnOnCol("col"+str(col))
                        alti.injCol("col"+str(col),options) 

                    alti.setDacVth(scanValue,options.dacVthRange)

            alti.byebye()
            del alti

def dataExtract(channel,col,scanValue,tmpdat):
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
            row_total_ch = 0
            for modules in ch["Modules"]:
                module_nb = modules["module"]
                tick = 0   
                for chips in modules["Chips"]:
                    chip_nb = chips["chip"]
                    alti = altiroc3.Altiroc(devnr = devnr, gbt = ch_nb, addr = timing_addr, use_usb = False, module_id = module_nb, chip_id = chip_nb, use_fice = True, use_serialcomm = False)
                    finaltxt = outputbasedir +"/t"+str(ch_nb)+"M"+str(module_nb + 14*ch_nb)+"/thresScan"+options.suffix+"/"+Utils.getOutName(options)
                    if not os.path.isdir(finaltxt):
                        os.makedirs(finaltxt)
                    prefix = finaltxt            
                    tmptxt = prefix+'txt_data_'+'dacVth_' + str(scanValue) + '.txt'
                    suffix='dacVth_' + str(scanValue) + '_.csv'
                    timingFN = prefix+'timing_data_'+suffix
                    if tick == 0:
                        if os.path.isfile(timingFN):
                            os.system("rm " + timingFN)
                    alti.analyse_data(tmpdat,tmptxt,timingFN,chip_nb)
                    os.system("rm " + tmptxt)
                    tick+=1
                    if Utils.get_total_rows(timingFN) > 0:
                        row_total_ch += 1

            # alti.byebye()  #use_fice == True, no byebye() function
            del alti
            return row_total_ch

def main():
    for channel in [1,2]:
      channelConfig(channel)

    serialcomm.clear()
    os.system("feconf "+elinkConfigFile)
    os.system("flx-config DECODING_HGTD_ALTIROC 1")
    os.system("flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1")
    os.system("flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4")
    for col in range(options.startCol,options.endCol+1,options.stepCol):
        row_nb_allStep = []
        dacVthList = list(range(options.dacVthMin,options.dacVthMax+1,options.dacVthStep))
        for dacVth in dacVthList:
            for channel in [1,2]:
                try:
                    scanCfg(channel,col,dacVth)                    
                except:
                    print('channel %d col %d dacVth %d configuration failed'%(channel,col,dacVth))
                    sys.exit()            
            # serialcomm.clear()
            os.system("fttcemu -f " + str(options.triggerFre))
            os.system("flx-config HGTD_ALTIROC_FASTCMD_GBRST 1")
            os.system("flx-config HGTD_ALTIROC_FASTCMD_GBRST 0")
            tmpdat = outputbasedir+'/Rawdat_vth/col_'+str(col)+'_Vth_'+str(dacVth)
            os.system("fdaq -t 1 "+ tmpdat + " -T")
            os.system("fttcemu -n")
            row_nb_allCH = 0
            for channel in [1,2]:
                row_nb_ch = dataExtract(channel,col,dacVth,tmpdat)
                row_nb_allCH += row_nb_ch
            row_nb_allStep.append(row_nb_allCH)                    
            if options.autoStop and len(row_nb_allStep) > 10:
                if row_nb_allStep[-5:]==[0,0,0,0,0]:
                    print("Stop scan at %d for column %d"%(dacVth,col))
                    break

try:
    main()
except:
    traceback.print_exc()
