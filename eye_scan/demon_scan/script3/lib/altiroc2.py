#!/usr/bin/env python
#encoding: utf-8
# Company:
# Engineer:
# 2021-10-22 created
import os
import sys
import time
import tqdm
import numpy as np
# parentabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".."
# sys.path.append(parentabspath)
from lib import modular_peb
sys.path.append("../")
from ConvertData import ReadBlockData

elink = [["000", "004"],
         ["001", "005"],
         ["002", "006"],
         ["003", "007"],
         ["008", "00c"],
         ["009", "00d"],
         ["00A", "00E"],
         ["00b", "00f"],
         ["010", "014"],
         ["011", "015"],
         ["012", "016"],
         ["013", "017"],
         ["018", "01a"],
         ["019", "01b"]]

nbOfLines = 15
nbOfPixels = nbOfLines * nbOfLines

firstVpaPixel = 0
lastVpaPixel = 119
firstVpaColumn = 0
lastVpaColumn = 7

firstTZPixel = 120
lastTZPixel = 224
firstTZColumn = 8
lastTZColumn = 14

widthDacToPs = 781.25
coarseDelayDacToPs = 1562
fineDelayDacToPs = 97

class Altiroc2(object):
    def __init__(self, card, dev, addr, use_usb, module_id, chip_id, use_serialcomm=True):
        self.module = modular_peb.modular_peb(card = card, dev = dev, addr = addr, use_usb = use_usb, use_serialcomm = use_serialcomm)
        self.module_id = module_id
        self.chip_id = chip_id
        self.elinkN = elink[self.module_id][self.chip_id]

    def byebye(self):
        self.module.serialcomm.clear()

    def wr_asic_reg(self, reg_address, data):
        self.module.module_i2c_write(module_id = self.module_id, chip_id = self.chip_id, reg_address = reg_address, data = data)

    def rd_asic_reg(self, reg_address, read_len):
        temp = self.module.module_i2c_read(module_id = self.module_id, chip_id = self.chip_id, reg_address = reg_address, read_len = read_len)
        return temp

    def wr_asic_cfg(self, filename):
        filename = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "../FADA/software/"+filename # we need a more clever way to get the path of file
        with open(filename) as file:
            lines = file.readlines()
            for line in tqdm.tqdm(lines):
                line = line.strip(" \t")
                if (len(line) > 2) and (line[0] != '#'):
                    param = line.split(',')
                    addr = param[0].strip(" \t")
                    data = param[1].strip("B'").replace('-', '')
                    if 'B' in param[1] or '0b' in param[1]:
                        data = int(data, base=2)
                    elif '0x' in param[1]:
                        data = int(data, base=16)
                    else:
                        data = int(data)
                    if addr == "usleep": # need to use FELIX sleep cmd
                        continue
                    else:
                        addr = int(addr)
                        self.wr_asic_reg(addr, data)
        time.sleep(1)

    def rd_asic_cfg(self, filename):
        regs = []
        data = []
        with open(filename) as file:
            for line in file:
                line = line.strip(" \t")
                if (len(line) > 2) and (line[0] != '#') and ('usleep' not in line):
                    param = line.split(',')
                    addr = int(param[0].strip(" \t"))
                    temp = self.rd_asic_reg(addr, read_len=1)
                    regs.append(addr)
                    data.append(temp[0])
        return regs, data

    def set_bit(self, value, position):
        return value | (1 << position)


    def clear_bit(self, value, position):
        return value & ~(1 << position)
    
    def cmdtrigger(self, *args):
        if len(args) >= 2:
            cmd = "fttcemu -f %d -L %d"%(args[1], args[0])
        if len(args) == 1:
            if(args[0]== 0):
                cmd = "fttcemu -n"
            else:
                cmd = "fttcemu -f %d"%(args[0])
        os.system(cmd)
        time.sleep(0.5)
        # print(cmd)
        # s = os.popen(cmd)
        # print(s.read())

    def extract_data(self,tmpdat):
        cmddaq = "fdaq -t 1 {} -T".format(tmpdat)
        # answerdaq = os.popen(cmddaq)
        # print(answerdaq.read())
        os.system(cmddaq)
        time.sleep(0.5)
        
        return True

    def analyse_data(self,tmpdat,tmptxt,timingFN):
        cmdcheck = "fcheck {} -F 100000 -T -e {} > {}".format(tmpdat+'-1.dat',self.elinkN,tmptxt)
        # answercheck = os.popen(cmdcheck)
        # print(answercheck.read())
        os.system(cmdcheck)
        time.sleep(0.5)
        ReadBlockData(tmptxt,timingFN)
        
        return True

    ######################################
    # get list of pixel using a string as input  
    ######################################
    def getPixelList(self, pixelStr):
        def errorMessage(pixelStr):
            print("Can't interpret : ", pixelStr)
            print("stop here.....")
            sys.exit()

        def getIntList(mystr):
            return [int(pix) for pix in mystr.split("-")]
            # return np.array([int(pix) for pix in mystr.split("-")])

        if pixelStr.lower() == "all":
            return list(range(nbOfLines * nbOfLines))
        elif pixelStr.lower() == "allvpa":
            return list(range(firstVpaPixel, lastVpaPixel + 1))
        elif pixelStr.lower() == "alltz":
            return list(range(firstTZPixel, lastTZPixel + 1))
        # elif pixelStr.lower()=="allpreamps":
        #     return list(range(nbOfLines*nbOfLines))
        elif pixelStr.lower().find("row") >= 0:
            try:
                # row=int(pixelStr.replace("row",""))
                rowList = getIntList(pixelStr.replace("row", ""))
                pixelList = []
                for row in rowList:
                    pixelList += list(range(row, row + (nbOfLines) * nbOfLines, nbOfLines))
            except:
                errorMessage(pixelStr)
                pass

        elif pixelStr.lower().find("col") >= 0:
            try:
                # col=int(pixelStr.replace("col",""))
                colList = getIntList(pixelStr.replace("col", ""))
                pixelList = []
                for col in colList:
                    pixelList += list(range(col * nbOfLines, (col + 1) * nbOfLines))
            except:
                errorMessage(pixelStr)
            # pixelList=list(range(col,col+(nbOfLines)*nbOfLines,nbOfLines))
        else:
            try:
                # pixel=int(pixelStr)
                pixelList = getIntList(pixelStr)
            except:
                errorMessage(pixelStr)
            # pixelList=[pixel]

        # check
        # pixelList=np.array(pixelList) buggy
        if np.any(np.array(pixelList) > nbOfPixels):
            print(pixelList)
            errorMessage(pixelStr)
        # print (pixelList)
        return pixelList


    ######################################
    # Turn on one channel  ( PA, discri, TDC or only TDC)
    ######################################

    def turnOn(alti, pixel):
        print("turnOn: ", pixel)
        alti.wr_asic_reg(4 * pixel + 1, 0b1_0_1_1_0000)  # Both TDC ON

        alti.wr_asic_reg(4 * pixel + 2, 0b000_1_1_1_0_0)  # PA, discri, hyst ON and no Ctest nor ext_disc

    ######################################
    #  Define pixel with injected signal (pulser or external discri)
    ######################################    
    def injection(self, pixel, ext_discri, onlyTDCOn):
        position = 1
        if ext_discri: position = 0
        print("Injection: ", pixel)
        # old=alti.rd_asic_reg(4 * pixel + 2) ATT should modif rd_asic_reg() to return the data
        if onlyTDCOn:
            old = 0
        else:
            if ext_discri:
                old = 0b000_1_1_0_0_0  # discri off for external trigger
            else:
                old = 0b000_1_1_1_0_0  # PA, hyst, discri ON

        new = self.set_bit(old, position)
        # if ext_discri: clear_bit(new, 2) # discri off
        self.wr_asic_reg(4 * pixel + 2, new)  # PA, discri, hyst ON and no Ctest nor ext_disc
        # alti.rd_asic_reg(4 * pixel + 2)
        # time.sleep(0.001) # really needed?

        #turn-off pixel 79
        #alti.wr_asic_reg(4 * 79 + 2, 0)
    
    def setDacVth(self, dacvth):
        dac_low = dacvth
        dac_high = (dacvth >> 8) + 4  # +0x04 to keep VTH OTA ON
        self.wr_asic_reg(965, dac_low)
        self.wr_asic_reg(966, dac_high)
				
        print("I'm in altiroc2.py, setDacVth = ", dacvth)
        print("rd_asic_reg_965 = ", self.rd_asic_reg(965, 1))
        print("rd_asic_reg_966 = ", self.rd_asic_reg(966, 1))
        #print("rd_asic_reg_962 = ", self.rd_asic_reg(962, 1))

    def setPulser(self, bias_ch_sel_pulser):
        self.wr_asic_reg(962, bias_ch_sel_pulser)
        print("I'm in altiroc2.py, setPulser = ", bias_ch_sel_pulser)
        print("rd_asic_reg_962 = ", self.rd_asic_reg(962, 1))

    def setup(self,startfile,vthcfile,args):
        print(startfile, "========================")
        self.wr_asic_cfg(startfile) # startup_and_periphery file

        if args.pixelOn.lower() == "all":
            pixel_file = "config/enableAllMatrix.txt"
            print(pixel_file, "========================")
            self.wr_asic_cfg(pixel_file) # default open all pixel
        elif args.pixelOn.lower() == "allvpa":
            pixel_file = "config/enableAllVpa.txt"
            print(pixel_file, "========================")
            self.wr_asic_cfg(pixel_file) # default open all pixel
        elif args.pixelOn.lower() == "alltz":
            pixel_file = "config/enableAllTZ.txt"
            print(pixel_file, "========================")
            self.wr_asic_cfg(pixel_file) # default open all pixel
        else:
            pixelONListist = self.getPixelList(args.pixelOn)
            for pixel in pixelONListist:
                self.turnOn(pixel)

        print(vthcfile, "========================")
        self.wr_asic_cfg(vthcfile) # vthc file

        pixelSignalList = self.getPixelList(args.pixelInj)
        for pixel in pixelSignalList:
            self.injection(pixel, ext_discri=False, onlyTDCOn=False) # default false two parameters
            pass

        # setting for pulser
        self.wr_asic_reg(994, 0b00_010001)  # pllBwConf  ATT to be checked: Sync issue using 100000 in thresSca
        self.wr_asic_reg(999, 0b1000_1001)  # psDelay1 for clk40MHzPS, ck80MHzPS, ck640MHzPS clocks B'1001-0000
        #self.wr_asic_reg(962, 0b0_0_001100)  # bias_ch_sel_pulser
        # Bit-7   : not used
        # Bit-6   : dacPulser_large_range
        # Bit-5:0 : dacPulserSetting
        self.wr_asic_reg(1012, 0b0_1_000011)  # CONF_CMDCALGENCNTR1
        # [5:0]   : Cal Pulse length, 25 ns to 1.575 us, must be at least  50 ns
        # [6]   : calPulseEn
        # [7]   : not used
    def hard_rst(self, *file):
        # self.client.write(constants.OP_HARD_RESET)
        # if file:
        #     self.wr_asic_cfg(file)
        # time.sleep(0.1)
        self.module.module_reset(self.module_id)

    def por_rst(self):
        # self.client.write(constants.OP_POR_RESET)
        # time.sleep(0.1)
        self.hard_rst()
        return "POR_RST done"
        
    def cmdgbrst(self):
        # self.client.write(constants.OP_CMDGBRST)
        os.system('flx-config HGTD_ALTIROC_FASTCMD_GBRST 1')
        time.sleep(0.1)
        os.system('flx-config HGTD_ALTIROC_FASTCMD_GBRST 0')








