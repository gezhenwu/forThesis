import os
import sys
import time
import tqdm
import numpy as np
import random
from lib import peb_Mix310
sys.path.append("../")
from ConvertData import ReadBlockData

delay = 0.001

elink = [
    ["000", "004"],["001", "005"],["002", "006"],["003", "007"],["008", "00c"],["009", "00d"],["00A", "00E"],["00b", "00f"],["010", "014"],["011", "015"],["012", "016"],["013", "017"],["018", "01a"],["019", "01b"],
    ["040", "044"],["041", "045"],["042", "046"],["043", "047"],["048", "04c"],["049", "04d"],["04A", "04E"],["04b", "04f"],["050", "054"],["051", "055"],["052", "056"],["053", "057"],["058", "05a"],["059", "05b"],
    ["080", "084"],["081", "085"],["082", "086"],["083", "087"],["088", "08c"],["089", "08d"],["08A", "08E"],["08b", "08f"],["090", "094"],["091", "095"],["092", "096"],["093", "097"],["098", "09a"],["099", "09b"],
    ["0c0", "0c4"],["0c1", "0c5"],["0c2", "0c6"],["0c3", "0c7"],["0c8", "0cc"],["0c9", "0cd"],["0cA", "0cE"],["0cb", "0cf"],["0d0", "0d4"],["0d1", "0d5"],["0d2", "0d6"],["0d3", "0d7"],["0d8", "0da"],["0d9", "0db"],
    ["100", "104"],["101", "105"],["102", "106"],["103", "107"],["108", "10c"],["109", "10d"],["10A", "10E"],["10b", "10f"],["110", "114"],["111", "115"],["112", "116"],["113", "117"],["118", "11a"],["119", "11b"],
    ["140", "144"],["141", "145"],["142", "146"],["143", "147"],["148", "14c"],["149", "14d"],["14A", "14E"],["14b", "14f"],["150", "154"],["151", "155"],["152", "156"],["153", "157"],["158", "15a"],["159", "15b"],
    ["180", "184"],["181", "185"],["182", "186"],["183", "187"],["188", "18c"],["189", "18d"],["18A", "18E"],["18b", "18f"],["190", "194"],["191", "195"],["192", "196"],["193", "197"],["198", "19a"],["199", "19b"],
    ["1C0", "1C4"],["1C1", "1C5"],["1C2", "1C6"],["1C3", "1C7"],["1C8", "1Cc"],["1C9", "1Cd"],["1CA", "1CE"],["1Cb", "1Cf"],["1d0", "1d4"],["1d1", "1d5"],["1d2", "1d6"],["1d3", "1d7"],["1d8", "1da"],["1d9", "1db"],
    ["200", "204"],["201", "205"],["202", "206"],["203", "207"],["208", "20c"],["209", "20d"],["20A", "20E"],["20b", "20f"],["210", "214"],["211", "215"],["212", "216"],["213", "217"],["218", "21a"],["219", "21b"]    
    ]

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

class Altiroc(object):
    def __init__(self, devnr, gbt, addr, use_usb, module_id, chip_id, use_serialcomm=True):
        self.module = peb_Mix310.peb(devnr = devnr, gbt = gbt, addr = addr, use_usb = use_usb, use_serialcomm = use_serialcomm)
        self.module.lumi_add(addr = 0x71, devnr=devnr, gbt=gbt)
        self.module_id = module_id
        self.chip_id = chip_id
        self.elinkN = elink[self.module_id + 14*gbt][self.chip_id]

    def byebye(self):
        self.module.serialcomm.clear()

    def wr_asic_reg(self, reg_address, data):
        self.module.module_i2c_write(module_id = self.module_id, chip_id = self.chip_id, reg_address = reg_address, data = data)

    def rd_asic_reg(self, reg_address, read_len):
        temp = self.module.module_i2c_read(module_id = self.module_id, chip_id = self.chip_id, reg_address = reg_address, read_len = read_len)
        return temp

    def wr_asic_cfg(self, filename):
        filename = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "../"+filename # we need a more clever way to get the path of file
        with open(filename) as file:
            lines = file.readlines()
            for line in tqdm.tqdm(lines):
                line = line.strip(" \t")
                if (len(line) > 2) and (line[0] != '#'):
                    param = line.split(',')
                    addr = param[0].strip(" \t")
                    data = param[1].strip().strip("B'").replace('-', '')   
                                         
                    if 'B' in param[1] or '0b' in param[1]:
                        data = int(data, base=2)
                    elif '0x' in param[1]:
                        data = int(data, base=16)
                    else:
                        data = int(data)
                    if addr == "usleep": # need to use FELIX sleep cmd
                        continue
                    else:
                        if '0x' in param[0]:
                            addr = int(addr, base=16)
                        else:
                            addr = int(addr)
                    self.wr_asic_reg(addr, data)
        # time.sleep(delay)

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

    def cmdtrigger(self, *args):
        if len(args) >= 2:
            cmd = "fttcemu -f %d -L %d"%(args[1], args[0])
        if len(args) == 1:
            if(args[0]== 0):
                cmd = "fttcemu -n"
            else:
                cmd = "fttcemu -f %d"%(args[0])
        os.system(cmd)
        # time.sleep(delay)

    def extract_data(self,tmpdat):
        cmddaq = "fdaq -t 1 {} -T".format(tmpdat)
        os.system(cmddaq)
        # time.sleep(delay)        
        return True

    def analyse_data(self,tmpdat,tmptxt,timingFN,asicID):
        cmdcheck = "fcheck {} -F 100000 -T -e {} > {}".format(tmpdat+'-1.dat',self.elinkN,tmptxt)
        os.system(cmdcheck)
        # time.sleep(delay)
        ReadBlockData(tmptxt,timingFN,asicID)        
        return True

    def set_bit(self, value, position):
        return value | (1 << position)

    def clear_bit(self, value, position):
        return value & ~(1 << position)
    
    ######################################
    #  get pixels in same row
    ######################################
    def getPixelsInSameRow(pixel):
        row = pixel % nbOfLines
        return list(range(row, row + (nbOfLines) * nbOfLines, nbOfLines))

    ######################################
    #  get pixels in same column
    ######################################
    def getPixelsInSameColumn(pixel):
        col = pixel // nbOfLines
        return list(range(col * nbOfLines, (col + 1) * nbOfLines))

    ######################################
    # get list of pixel using a string as input
    ######################################
    def getPixelList(self, pixelStr):
        def errorMessage(pixelStr):
            print("Can't interpret : ", pixelStr)
            print("stop here.....")
            sys.exit()
        # Define the dimensions of the matrix
        rows, cols = 15, 15

        # Create an empty matrix filled with zeros
        matrix = np.zeros((rows, cols))

        # Populate the matrix with the desired values
        for row_position in range(rows):
            for col_position in range(cols):
                res=(row_position) + (col_position * 15)
                #print (col_position, row_position, res)
                matrix[row_position, col_position] = int(res)



        allSquareFive=[]
        # Loop over the starting row indices of each square
        for start_row in range(0, 15, 5):
            # Loop over the starting column indices of each square
            for start_col in range(0, 15, 5):
                # Extract the current square
                squareFive = list(matrix[start_row:start_row+5, start_col:start_col+5].flatten())
                #print(squareFive)
                allSquareFive.append(squareFive)

        
        allSquareThree=[]
        # Loop over the starting row indices of each square
        for start_row in range(0, 15, 3):
            # Loop over the starting column indices of each square
            for start_col in range(0, 15, 3):
                # Extract the current square
                squareThree = list(matrix[start_row:start_row+3, start_col:start_col+3].flatten())
                #print(squareThree)
                allSquareThree.append(squareThree)

        
        allSparseFifteen=[]
        for sparseFifteen_index in range(15):
            sparseFifteen = []
            # Loop over the elements in the current sparseFifteen
            for i in range(15):
                col=(i+10*(i%3))%15
                row=(sparseFifteen_index+i)%15
                value = matrix[col,row]
                sparseFifteen.append(value)
            allSparseFifteen.append(sparseFifteen)

        allRnd=list(range(225))
        random.Random(1).shuffle(allRnd)
        #print("")
        #for i in allRnd: print (i,",", end='')
        #print("")
        allRnd=[159 ,173 ,187 ,67 ,40 ,83 ,192 ,188 ,223 ,43 ,137 ,87 ,90 ,28 ,102 ,14 ,169 ,36 ,172 ,183 ,177 ,37 ,80 ,13 ,35 ,189 ,91 ,176 ,38 ,162 ,149 ,12 ,221 ,207 ,208 ,19 ,63 ,86 ,163 ,31 ,20 ,170 ,160 ,136 ,76 ,146 ,152 ,33 ,185 ,50 ,96 ,79 ,18 ,109 ,89 ,39 ,113 ,92 ,60 ,15 ,17 ,105 ,156 ,121 ,57 ,186 ,10 ,9 ,4 ,32 ,215 ,23 ,174 ,167 ,198 ,3 ,107 ,42 ,118 ,197 ,101 ,111 ,209 ,116 ,147 ,52 ,123 ,119 ,104 ,154 ,46 ,61 ,131 ,54 ,193 ,71 ,66 ,219 ,139 ,180 ,49 ,200 ,143 ,203 ,214 ,84 ,224 ,202 ,45 ,73 ,158 ,144 ,218 ,51 ,148 ,70 ,204 ,171 ,69 ,165 ,98 ,1 ,29 ,64 ,132 ,21 ,82 ,134 ,78 ,11 ,213 ,181 ,125 ,94 ,153 ,133 ,41 ,27 ,130 ,199 ,22 ,95 ,140 ,93 ,44 ,168 ,103 ,62 ,122 ,8 ,100 ,157 ,127 ,150 ,72 ,77 ,48 ,129 ,182 ,128 ,85 ,217 ,75 ,161 ,47 ,25 ,164 ,142 ,106 ,190 ,74 ,117 ,179 ,210 ,88 ,59 ,141 ,222 ,112 ,56 ,135 ,191 ,108 ,55 ,175 ,211 ,2 ,138 ,212 ,6 ,5 ,206 ,81 ,26 ,151 ,58 ,184 ,68 ,114 ,178 ,0 ,196 ,220 ,155 ,110 ,99 ,7 ,124 ,24 ,53 ,201 ,97 ,166 ,120 ,115 ,194 ,126 ,30 ,65 ,16 ,195 ,205 ,216 ,145 ,34]
        allRndThree=[allRnd[i::75] for i in range(75)]
        allRndFive=[allRnd[i::45] for i in range(45)]
        allRndNine=[allRnd[i::25] for i in range(25)]
        allRndFifteen=[allRnd[i::15] for i in range(15)]

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

        elif pixelStr.lower().find("squarefive") >= 0:     
            try:
                squareFiveList = getIntList(pixelStr.replace("squareFive", ""))
                pixelList = []
                for i in squareFiveList:
                    pixelList += [ int(v) for v in allSquareFive[i] ]
            except:
                errorMessage(pixelStr)
                
        elif pixelStr.lower().find("squarethree") >= 0:     
            try:
                squareThreeList = getIntList(pixelStr.replace("squareThree", ""))
                pixelList = []
                for i in squareThreeList:
                    pixelList += [ int(v) for v in allSquareThree[i] ]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("sparsefifteen") >= 0:
            try:
                sparseFifteenList = getIntList(pixelStr.replace("sparseFifteen", ""))
                pixelList = []
                for i in sparseFifteenList:
                    pixelList += [ int(v) for v in allSparseFifteen[i]]
            except:
                errorMessage(pixelStr)
        
        elif pixelStr.lower().find("rndfifteen") >= 0:
            try:
                rndFifteenList = getIntList(pixelStr.replace("rndFifteen", ""))
                pixelList = []
                for i in rndFifteenList:
                    pixelList += [ int(v) for v in allRndFifteen[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndnine") >= 0:
            try:
                rndNineList = getIntList(pixelStr.replace("rndNine", ""))
                pixelList = []
                for i in rndNineList:
                    pixelList += [ int(v) for v in allRndNine[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndfive") >= 0:
            try:
                rndFiveList = getIntList(pixelStr.replace("rndFive", ""))
                pixelList = []
                for i in rndFiveList:
                    pixelList += [ int(v) for v in allRndFive[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndthree") >= 0:
            try:
                rndThreeList = getIntList(pixelStr.replace("rndThree", ""))
                pixelList = []
                for i in rndThreeList:
                    pixelList += [ int(v) for v in allRndThree[i]]
            except:
                errorMessage(pixelStr)
        else:
            try:
                # pixel=int(pixelStr)
                pixelList = getIntList(pixelStr)
            except:
                errorMessage(pixelStr)

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
    def turnOn(self, pixel, onlyTDCOn, ext_discri):
        print("turnOn: ", pixel)
        # In Alti3, non-continuous config address of pixel registers
        # Example: pix0: address x00 to x06; pix1: address x10 to x16; pix2: address x20 to x26;
        # So, the register "n" of pixel number "pixel" has addresses [16*"pixel" + "n"]
        baseaddr = (16*pixel)+(16*(pixel//15))
        self.wr_asic_reg(baseaddr + 3, 0b01111100)     # PA, DISCRI, and TDCs: ON, but NO Ctest NOR ext_disc
        if onlyTDCOn:
            self.wr_asic_reg(baseaddr + 3, 0b01100000)  # Only TDCs ON
        elif ext_discri:
            self.wr_asic_reg(baseaddr + 3, 0b01100001)  # (TDCs,External DISCRI: ON) & (DISCRI: OFF)        
        # reg = self.rd_asic_reg(baseaddr + 3, read_len=1)[0]
        # print("Turn On Pixel-%d -> Reg[0x%04X] = 0x%02X" %(pixel,baseaddr+3,reg))
    def set_trig_latency(self, latency):
        # latency = latency - 2 #added according to ZC706, without this line in origination.
        lsbvalue = latency & 0xFF
        msbvalue = (latency >> 8) & 0x07
        self.wr_asic_reg(0x0FF5, lsbvalue)  # CONF_TRIG_LATENCY_L
        self.wr_asic_reg(0x0FF6, msbvalue)  # CONF_TRIG_LATENCY_H
        # for pixel in range(0,225):
        #    baseaddr = (16*pixel)+(16*(pixel//15))
        #    print("Reg[0x%04X] = 0x%02X" %(baseaddr+5,lsbvalue))
        #    self.wr_asic_reg(baseaddr + 5, lsbvalue)  # CONF_TRIG_LATENCY_L
        #    self.wr_asic_reg(baseaddr + 6, msbvalue)  # CONF_TRIG_LATENCY_H
        ######################################            

    ######################################
    #  Define pixel with injected signal (pulser or external discri)
    ######################################    
    def injection(self, pixel, ext_discri, onlyTDCOn):
        position = 1
        if ext_discri:
            position = 0
        baseaddr = (16*pixel)+(16*(pixel//15))
        # print("Injection: ", pixel,hex(baseaddr),bin(self.rd_asic_reg(baseaddr + 3, read_len = 1)[0]))        
        old=self.rd_asic_reg(baseaddr + 3, read_len=1)[0] #ATT should modif rd_asic_reg() to return the data
        new = self.set_bit(old, position) # set '1' to bit ext_disc or ctest depending of method of injection
        self.wr_asic_reg(baseaddr + 3, new)  # PA, discri, hyst ON and no Ctest nor ext_disc

    def disInjection(self, pixel, ext_discri, onlyTDCOn):
        position = 1
        if ext_discri:
            position = 0
        baseaddr = (16*pixel)+(16*(pixel//15))
        # print("disInjection: ", pixel,hex(baseaddr),bin(self.rd_asic_reg(baseaddr + 3, read_len = 1)[0]))              
        old=self.rd_asic_reg(baseaddr + 3, read_len=1)[0] 
        new = self.clear_bit(old, position) 
        self.wr_asic_reg(baseaddr + 3, new)


    ######################################
    # Print Pixel Registers
    ######################################
    def printPixelRegs(self,pixel):
        baseaddr = (16*pixel)+(16*(pixel//15))
        reg0 = self.rd_asic_reg(baseaddr, read_len=1)[0]
        reg1 = self.rd_asic_reg(baseaddr + 1, read_len=1)[0]
        reg2 = self.rd_asic_reg(baseaddr + 2, read_len=1)[0]
        reg3 = self.rd_asic_reg(baseaddr + 3, read_len=1)[0]
        reg4 = self.rd_asic_reg(baseaddr + 4, read_len=1)[0]
        reg5 = self.rd_asic_reg(baseaddr + 5, read_len=1)[0]
        reg6 = self.rd_asic_reg(baseaddr + 6, read_len=1)[0]
        print("Pixel-%3d : Reg-0x%04X = 0x%02X" %(pixel,baseaddr,reg0))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 1,reg1))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 2,reg2))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 3,reg3))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 4,reg4))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 5,reg5))
        print("          : Reg-0x%04X = 0x%02X" %(baseaddr + 6,reg6))

    def setup(self,startfile,vthcfile,args):
        #save original values
        pixelOn=args.pixelOn
        pixelInj=args.pixelInj 
        pixelPlot=args.pixelPlot
        nMin=0
        nMax=1
        
        if pixelOn in ["col","row","sparseFifteen","rndFifteen"] or pixelInj in ["col","row","sparseFifteen","rndFifteen"]:
            nMin = 0
            nMax = 15
        if pixelOn in ["rndNine"] or pixelInj in ["rndNine"]:
            nMin = 0
            nMax = 25
        if pixelOn in ["rndFive"] or pixelInj in ["rndFive"]:
            nMin = 0
            nMax = 45
        if pixelOn in ["rndThree"] or pixelInj in ["rndThree"]:
            nMin = 0
            nMax = 75
        elif pixelInj == "pix":
            nMin = 0
            nMax =  225
        elif pixelInj == "squareFive":
            nMin = 0
            nMax =  9
        elif pixelInj == "squareThree":
            nMin = 0
            nMax =  25
        for line in range(nMin,nMax):
            if pixelOn == "pix":
                args.pixelOn = str(line) 
            if pixelOn == "col":
                args.pixelOn = "col"+str(line)
            if pixelOn == "row":
                args.pixelOn = "row"+str(line)
            if pixelInj == "pix":
                args.pixelInj = str(line)
            if pixelInj == "col":
                args.pixelInj = "col"+str(line)
            if pixelInj == "row":
                args.pixelInj = "row"+str(line)
            if pixelInj == "rndThree":
                args.pixelInj = "rndThree"+str(line)
            if pixelInj == "rndFive":
                args.pixelInj = "rndFive"+str(line)
            if pixelInj == "rndNine":
                args.pixelInj = "rndNine"+str(line)
            if pixelInj == "rndFifteen":
                args.pixelInj = "rndFifteen"+str(line)
            if pixelInj == "sparseFifteen":
                args.pixelInj = "sparseFifteen"+str(line)
            if pixelInj == "squareFive":
                args.pixelInj = "squareFive"+str(line)
            if pixelInj == "squareThree":
                args.pixelInj = "squareThree"+str(line)

        print ("Load startup_and_periphery.txt")
        self.wr_asic_cfg("config/altiroc/startup_periphery/startup_and_periphery.txt")
        # start-up and periphery
        if startfile is None:
            if args.board is None:
                startfile = "config/altiroc/startup_periphery/startup_and_periphery.txt"
            else:
                startfile = 'config/altiroc/startup_periphery/B{:03d}.txt'.format(args.board)                
        try:
            print ("Loading ",startfile)
            self.wr_asic_cfg(startfile)            
        except:
            print ("Can't load",startfile)

        # turn off TDCs, pa,discris => start from a clean config        
        try:
            print ("Loading disableMatrix.txt: ")
            self.wr_asic_cfg("config/altiroc/startup_periphery/alti3_disableAllMatrix.txt")
        except:
            print ("Can't load disableMatrix.txt")
            

        # turn ON (TDCs, pa and discris) for some or all channels depending on pixelOn
        if args.pixelOn.lower() == "all":
            if args.onlyTDCOn:                
                self.wr_asic_reg(0x0FF3,0b01100000)                
            else:
                self.wr_asic_reg(0x0FF3,0b01111100)
        else:
            pixelOnListist = self.getPixelList(args.pixelOn)
            for pixel in pixelOnListist:
                self.turnOn(pixel, args.onlyTDCOn, args.ext_discri)

        # load vthc
        if args.loadVthc or vthcfile is not None:
            if vthcfile is None:
                vthcfile = "config/altiroc/Vthc/b" + str(args.board) + "_vthc_all_col.txt"      
            try:
                print("loading ", vthcfile)
                self.wr_asic_cfg(vthcfile)                
            except:
                print ("File missing: ",vthcfile)

        # set Ctest or ext_discri to the selected channels
        pixelInjList = self.getPixelList(args.pixelInj)
        for pixel in pixelInjList:
            self.injection(pixel, args.ext_discri, args.onlyTDCOn)
            pass

        if args.smallCtest:#ATT: assume that the config has 0
            #print (bin(self.rd_asic_reg(0x2011, read_len=1)[0]))
            old=self.rd_asic_reg(0x2011, read_len=1)[0]
            new=self.set_bit(old, 7)
            self.wr_asic_reg(0x2011,new)
            #print (bin(self.rd_asic_reg(0x2011, read_len=1)[0]))

        if args.Cp>=0 and args.Cp<2:
            print('... Cp :', args.Cp)
            old=self.rd_asic_reg(0x2011, read_len=1)[0]
            old=self.clear_bit(old, 3)
            new=old+(args.Cp<<3)
            #print (bin(old),bin(new))
            self.wr_asic_reg(0x2011,new)
            print("Cp--0x2011: ",bin(self.rd_asic_reg(0x2011, read_len=1)[0]))

        # # data transmission rate
        # if args.enLumi == 0:
        #     if args.timingRate == 320: self.wr_asic_reg(0x2016,0b01110001)
        #     elif args.timingRate == 640: self.wr_asic_reg(0x2016,0b01110010)
        #     elif args.timingRate == 1280: self.wr_asic_reg(0x2016,0b01110011)
        #     else: self.wr_asic_reg(0x2016,0b01110000)
        # if args.enLumi == 1:
        #     if args.timingRate == 320: self.wr_asic_reg(0x2016,0b11110001)
        #     elif args.timingRate == 640: self.wr_asic_reg(0x2016,0b11110010)
        #     elif args.timingRate == 1280: self.wr_asic_reg(0x2016,0b11110011)
        #     else: self.wr_asic_reg(0x2016,0b11110000)
        # if args.encoding == 0:
        #     old = self.rd_asic_reg(0x2016, read_len=1)[0]
        #     new = self.clear_bit(old,4)
        #     self.wr_asic_reg(0x2016,new)

        #Cd this is Ugly
        if args.Cd in range(8):
            print('... Cd :', args.Cd)
            old=self.rd_asic_reg(0x2011, read_len=1)[0]
            #print (bin(old))
            old=self.clear_bit(old, 4)
            old=self.clear_bit(old, 5)
            #print (bin(old),bin(args.Cd<<4))
            new=old+(args.Cd<<4)
            self.wr_asic_reg(0x2011,new)
            print("Cd--0x2011: ",bin(self.rd_asic_reg(0x2011, read_len=1)[0]))
        
        # fix delay
        print (args.cDelay,args.fDelay)
        clk40delay=int(args.cDelay/2)
        self.wr_asic_reg(0x101B, args.cDelay+(clk40delay<<4))
        self.wr_asic_reg(0x101C, args.fDelay)            
        
        self.wr_asic_reg(0x2004,0b00101101)  # CONF_CMD_CAL_CTRL #  PHASE[3:0]  B'00-1-0-0101, # no impact on ext_discri delay scan

        if args.ext_discri:
            #Latency
            self.wr_asic_reg(0x0FF5, 0b0000100)    # CONF_TRIG_LATENCY_L
        else:
            #Latency
            if args.trigLatency > 0:
                self.set_trig_latency(args.trigLatency)
            else:
                self.wr_asic_reg(0x0FF5, 0b0000010)    # CONF_TRIG_LATENCY_L
                
        
        ###############################################
        # additionnal parameters from command line
        ###############################################
        ## From Alti2; compatibility with alti3 to be checked
        if args.writeReg is not None:      
            vec=args.writeReg.split(",")
            if len(vec)%2 ==0:
                registers=vec[0::2]
                values=vec[1::2]
                for reg,val in zip(registers,values):
                    print (reg,val)
                    self.wr_asic_reg(int(reg),int(val))
            else:
                print ("Can interpret writeReg", args.writeReg )

        # ###############################################
        # #turn off / mask channel X
        # ###############################################
        
        #badPixels=[0,10,21,25,40,53,54,89,107,116,121,136,177,182]#B28
        #badPixels=[0,3,48,92,107,122,137,151,152,167,182,197]#B15
        badPixels=[]#21,40,53,54
        for pix in badPixels:
            print ("TURN OFF pixel",pix)
            #self.wr_asic_reg( (16*pix)+(16*(pix//15))+3, 0b0_0_0_0_0_0_0_0)
            self.wr_asic_reg( (16*pix)+(16*(pix//15))+3, 0b0_1_1_1_1_0_0_0)
            pass
   

    def injCol(self,column,args):
        pixelInjList = self.getPixelList(column)
        for pixel in pixelInjList:
            self.injection(pixel, args.ext_discri, args.onlyTDCOn)

    def disInjCol(self,column,args):
        pixelInjList = self.getPixelList(column)
        for pixel in pixelInjList:
            self.disInjection(pixel, args.ext_discri, args.onlyTDCOn)                
         

    ######################################
    #  probe PA for one pixel
    ######################################
    def turnOnProbePa(self,pixel):
        self.wr_asic_reg(0x2010, 0b1_0_1_0_0000)  # CONF_PROBE_PIX_ADDR
                                                    # Probe PA[5] activated
                                                    # PA_CURRENT_BUFFER[7] activated
        self.wr_asic_reg(0x1014, 0b0_0_0_00000)   # CONF_SEL_PROBE_BIAS
                                                    # Disable bias_probe [5]
        pixelI2CAddress = 16 * pixel
        col = pixel // nbOfLines
        row = pixel % nbOfLines
        print (col,row)
        self.wr_asic_reg(0x200F, int((col << 4) + row))  # CONF_GLOBAL_ENABLE_PROBE
                                                            #  COLUMN[3:0]
                                                            #  ROW[7:4]

    ######################################
    #  Set Vbg (dac)
    ######################################
    def setDacVbg(self, dacvbg):
        self.wr_asic_reg(0x1000, dacvbg)  # Vbg DAC VALUE[3:0]

    # ######################################
    # #  Set bias_ch_dac (dac)
    # ######################################
    # def setdacIDPAConf(self, dacCurrent):
    #    self.wr_asic_reg(0x1004, dacCurrent)  # CONF_DAC_BIAS_ID_PA
    #                                           # VALUE[2:0]
    ######################################
    #  Set Vth (dac)
    ######################################
    def setDacVth(self, dacvth, dacvthrange):
        dac_high = (dacvth >> 8) & 0x03
        self.wr_asic_reg(0x1006, dacvth & 0xFF)
        self.wr_asic_reg(0x1007, dac_high + 4 + (dacvthrange << 3)) # enable_DAC_VTHC[2] and VTHC_RANGE[4:3]

    ######################################
    #  Set Vthc (dac) for a given pixel
    ######################################
    def setDacVthc(self, pixel, dacvthc):
        baseaddr = (16*pixel)+(16*(pixel//15))
        self.wr_asic_reg(baseaddr + 4, dacvthc) #
        #   self.wr_asic_reg(0x1007, rangevthc << 3) # VTHC_RANGE[4:3]

    ######################################
    #  Set Vthc to 0 for channels without injected signal
    ######################################
    def setVthcToZero(self, args):
        # change Vthc
        self.wr_asic_reg(0x0FF4, 0)#set vthc to zero for all channels
        for pix in self.getPixelList(args.pixelInj):
            #print (pix)
            baseaddr = (16*pix)+(16*(pix//15))
            address = baseaddr + 4
            self.wr_asic_reg(address, 0b10000000) #median value for channels with injection

    ######################################
    #
    ######################################
    def setDiscriOff(self, args):#discri off for pixels with no injected signal
        pixelInjList = self.getPixelList(args.pixelInj)
        for pix in range(nbOfPixels):
            if pix in pixelInjList:
                continue
            #print("Discri off for ", pix)
            baseaddr = (16*pix)+(16*(pix//15))
            address = baseaddr + 3
            val=self.rd_asic_reg(address, read_len=1)[0] 
            self.wr_asic_reg(address, val&~(1<<2))

    def setDiscriOffCol(self, column):#discri off for columns with no injected signal
        if column == "all":
            for pix in range(nbOfPixels):
                baseaddr = (16*pix)+(16*(pix//15))
                address = baseaddr + 3
                val=self.rd_asic_reg(address, read_len=1)[0] 
                self.wr_asic_reg(address, val&~(1<<2))
        else:
            pixelInjList = self.getPixelList(column)
            for pix in pixelInjList:
                baseaddr = (16*pix)+(16*(pix//15))
                address = baseaddr + 3
                val=self.rd_asic_reg(address, read_len=1)[0] 
                self.wr_asic_reg(address, val&~(1<<2))                

    def setDiscriOnCol(self, column):#discri off for pixels with no injected signal
        pixelInjList = self.getPixelList(column)
        for pix in pixelInjList:
            baseaddr = (16*pix)+(16*(pix//15))
            address = baseaddr + 3
            old=self.rd_asic_reg(address, read_len=1)[0]
            new=self.set_bit(old,2)
            self.wr_asic_reg(address, new)


    ######################################
    #
    ######################################
    def setPreampOff(self, pixelInj):#discri off for pixels with no injected signal
        tmpFileName = "tmp.txt"
        f = open(tmpFileName, "w")
        pixelInjList = self.getPixelList(pixelInj)
        for pix in range(nbOfPixels):
            if pix in pixelInjList:
                continue
            print("Preamp off for ", pix)
            # TDC
            baseaddr = (16*pix)+(16*(pix//15))
            address = baseaddr + 3
            mystr = "{0}     ,B'0-0-0-0-1-1-0-0 \n".format(address) # Setting of pa, discri, ctest ... ?
                                                                    #  ENABLE_PA[4]
            mystr = mystr.replace("0b", "B'")#????
            f.write(mystr)

        f.close()
        self.wr_asic_cfg(tmpFileName)


    ######################################
    #  Set pulser charger
    ######################################
    def setPulser(self, bias_ch_sel_pulser):
        self.wr_asic_reg(0x1003, bias_ch_sel_pulser) 

    def hard_rst(self, *file):
        self.module.module_reset(self.module_id)
        # time.sleep(delay)

    def por_rst(self):
        self.hard_rst()
        # time.sleep(delay)
        return "POR_RST done"
        
    def cmdgbrst(self):
        os.system('flx-config HGTD_ALTIROC_FASTCMD_GBRST 1')
        # time.sleep(delay)
        os.system('flx-config HGTD_ALTIROC_FASTCMD_GBRST 0')
        # time.sleep(delay)

    def decode8b10b(self,decoder):
        if decoder:
            os.system('flx-config DECODING_HGTD_ALTIROC 1')
        else:
            os.system('flx-config DECODING_HGTD_ALTIROC 0')
        # time.sleep(delay)

    def idle3(self,altiroc):
        if altiroc==3:
            os.system('flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1')
        else:
            os.system('flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 0')
        # time.sleep(delay)

    def nIdle(self, nidle):
        os.system('flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY %d'%nidle)
        # time.sleep(delay)        

    def felixcfg(self, cfgFile):
        cmd = 'feconf ' + str(cfgFile)
        os.system(cmd)
        # time.sleep(delay)  

######################################
# get list of pixel using a string as input
######################################
def getPixelList(pixelStr):
        def errorMessage(pixelStr):
            print("Can't interpret : ", pixelStr)
            print("stop here.....")
            sys.exit()
        # Define the dimensions of the matrix
        rows, cols = 15, 15

        # Create an empty matrix filled with zeros
        matrix = np.zeros((rows, cols))

        # Populate the matrix with the desired values
        for row_position in range(rows):
            for col_position in range(cols):
                res=(row_position) + (col_position * 15)
                #print (col_position, row_position, res)
                matrix[row_position, col_position] = int(res)



        allSquareFive=[]
        # Loop over the starting row indices of each square
        for start_row in range(0, 15, 5):
            # Loop over the starting column indices of each square
            for start_col in range(0, 15, 5):
                # Extract the current square
                squareFive = list(matrix[start_row:start_row+5, start_col:start_col+5].flatten())
                #print(squareFive)
                allSquareFive.append(squareFive)

        
        allSquareThree=[]
        # Loop over the starting row indices of each square
        for start_row in range(0, 15, 3):
            # Loop over the starting column indices of each square
            for start_col in range(0, 15, 3):
                # Extract the current square
                squareThree = list(matrix[start_row:start_row+3, start_col:start_col+3].flatten())
                #print(squareThree)
                allSquareThree.append(squareThree)

        
        allSparseFifteen=[]
        for sparseFifteen_index in range(15):
            sparseFifteen = []
            # Loop over the elements in the current sparseFifteen
            for i in range(15):
                col=(i+10*(i%3))%15
                row=(sparseFifteen_index+i)%15
                value = matrix[col,row]
                sparseFifteen.append(value)
            allSparseFifteen.append(sparseFifteen)

        allRnd=list(range(225))
        random.Random(1).shuffle(allRnd)
        #print("")
        #for i in allRnd: print (i,",", end='')
        #print("")
        allRnd=[159 ,173 ,187 ,67 ,40 ,83 ,192 ,188 ,223 ,43 ,137 ,87 ,90 ,28 ,102 ,14 ,169 ,36 ,172 ,183 ,177 ,37 ,80 ,13 ,35 ,189 ,91 ,176 ,38 ,162 ,149 ,12 ,221 ,207 ,208 ,19 ,63 ,86 ,163 ,31 ,20 ,170 ,160 ,136 ,76 ,146 ,152 ,33 ,185 ,50 ,96 ,79 ,18 ,109 ,89 ,39 ,113 ,92 ,60 ,15 ,17 ,105 ,156 ,121 ,57 ,186 ,10 ,9 ,4 ,32 ,215 ,23 ,174 ,167 ,198 ,3 ,107 ,42 ,118 ,197 ,101 ,111 ,209 ,116 ,147 ,52 ,123 ,119 ,104 ,154 ,46 ,61 ,131 ,54 ,193 ,71 ,66 ,219 ,139 ,180 ,49 ,200 ,143 ,203 ,214 ,84 ,224 ,202 ,45 ,73 ,158 ,144 ,218 ,51 ,148 ,70 ,204 ,171 ,69 ,165 ,98 ,1 ,29 ,64 ,132 ,21 ,82 ,134 ,78 ,11 ,213 ,181 ,125 ,94 ,153 ,133 ,41 ,27 ,130 ,199 ,22 ,95 ,140 ,93 ,44 ,168 ,103 ,62 ,122 ,8 ,100 ,157 ,127 ,150 ,72 ,77 ,48 ,129 ,182 ,128 ,85 ,217 ,75 ,161 ,47 ,25 ,164 ,142 ,106 ,190 ,74 ,117 ,179 ,210 ,88 ,59 ,141 ,222 ,112 ,56 ,135 ,191 ,108 ,55 ,175 ,211 ,2 ,138 ,212 ,6 ,5 ,206 ,81 ,26 ,151 ,58 ,184 ,68 ,114 ,178 ,0 ,196 ,220 ,155 ,110 ,99 ,7 ,124 ,24 ,53 ,201 ,97 ,166 ,120 ,115 ,194 ,126 ,30 ,65 ,16 ,195 ,205 ,216 ,145 ,34]
        allRndThree=[allRnd[i::75] for i in range(75)]
        allRndFive=[allRnd[i::45] for i in range(45)]
        allRndNine=[allRnd[i::25] for i in range(25)]
        allRndFifteen=[allRnd[i::15] for i in range(15)]

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

        elif pixelStr.lower().find("squarefive") >= 0:     
            try:
                squareFiveList = getIntList(pixelStr.replace("squareFive", ""))
                pixelList = []
                for i in squareFiveList:
                    pixelList += [ int(v) for v in allSquareFive[i] ]
            except:
                errorMessage(pixelStr)
                
        elif pixelStr.lower().find("squarethree") >= 0:     
            try:
                squareThreeList = getIntList(pixelStr.replace("squareThree", ""))
                pixelList = []
                for i in squareThreeList:
                    pixelList += [ int(v) for v in allSquareThree[i] ]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("sparsefifteen") >= 0:
            try:
                sparseFifteenList = getIntList(pixelStr.replace("sparseFifteen", ""))
                pixelList = []
                for i in sparseFifteenList:
                    pixelList += [ int(v) for v in allSparseFifteen[i]]
            except:
                errorMessage(pixelStr)
        
        elif pixelStr.lower().find("rndfifteen") >= 0:
            try:
                rndFifteenList = getIntList(pixelStr.replace("rndFifteen", ""))
                pixelList = []
                for i in rndFifteenList:
                    pixelList += [ int(v) for v in allRndFifteen[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndnine") >= 0:
            try:
                rndNineList = getIntList(pixelStr.replace("rndNine", ""))
                pixelList = []
                for i in rndNineList:
                    pixelList += [ int(v) for v in allRndNine[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndfive") >= 0:
            try:
                rndFiveList = getIntList(pixelStr.replace("rndFive", ""))
                pixelList = []
                for i in rndFiveList:
                    pixelList += [ int(v) for v in allRndFive[i]]
            except:
                errorMessage(pixelStr)
        elif pixelStr.lower().find("rndthree") >= 0:
            try:
                rndThreeList = getIntList(pixelStr.replace("rndThree", ""))
                pixelList = []
                for i in rndThreeList:
                    pixelList += [ int(v) for v in allRndThree[i]]
            except:
                errorMessage(pixelStr)
        else:
            try:

                # pixel=int(pixelStr)
                pixelList = getIntList(pixelStr)
            except:
                errorMessage(pixelStr)

        # check
        # pixelList=np.array(pixelList) buggy
        if np.any(np.array(pixelList) > nbOfPixels):
            print(pixelList)
            errorMessage(pixelStr)
        # print (pixelList)
        return pixelList