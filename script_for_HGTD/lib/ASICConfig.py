import sys, time
import numpy as np
import random

######################################
# ASIC parameters
######################################
from lib import Utils

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


######################################
# bit manipulation
######################################

def set_bit(value, position):
    return value | (1 << position)


def clear_bit(value, position):
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
   elif pixelStr.lower().find("sparsefifteen") >= 0 :
      try:
         sparseFifteenList = getIntList(pixelStr.replace("sparseFifteen", ""))
         pixelList = []
         for i in sparseFifteenList:
            pixelList += [ int(v) for v in allSparseFifteen[i]]
      except:
         errorMessage(pixelStr)
   elif pixelStr.lower().find("sparse") >= 0 :
      try:
         sparseList = getIntList(pixelStr.replace("sparse", ""))
         pixelList = []
         for i in sparseList:
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

def turnOn(alti, pixel, onlyTDCOn, ext_discri):
    print("turnOn: ", pixel)
    alti.wr_asic_reg(4 * pixel + 1, 0b1_0_1_1_0000)  # Both TDC ON
    # time.sleep(0.001) # really needed?
    if onlyTDCOn:
        alti.wr_asic_reg(4 * pixel + 2, 0)  # PA,discri,hyst OFF !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:

        if ext_discri:
            alti.wr_asic_reg(4 * pixel + 2, 0b000_1_1_0_0_0)  # discri off for external trigger
        else:
            alti.wr_asic_reg(4 * pixel + 2, 0b000_1_1_1_0_0)  # PA, discri, hyst ON and no Ctest nor ext_disc
    # time.sleep(0.001) # really needed?


    
######################################
#  Define pixel with injected signal (pulser or external discri)
######################################    
def injection(alti, pixel, ext_discri, onlyTDCOn):
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

    new = set_bit(old, position)
    # if ext_discri: clear_bit(new, 2) # discri off
    alti.wr_asic_reg(4 * pixel + 2, new)  # PA, discri, hyst ON and no Ctest nor ext_disc
    # alti.rd_asic_reg(4 * pixel + 2)
    # time.sleep(0.001) # really needed?
    #turn-off pixel 79
    #alti.wr_asic_reg(4 * 79 + 2, 0)


    
######################################
# Configuration of the ASIC  
######################################

def setting(alti, board, pixelONStr, pixelSignalStr, ext_discri, onlyTDCOn, loadVthc, cfgFile=None, vthcFile=None,writeReg=None):
    ## start-up and periphery
    if cfgFile is None:
        cfgFile = "config/b" + str(board) + "_startup_and_periphery.txt"
    alti.wr_asic_cfg(cfgFile)

    # alti.wr_asic_cfg("config/b"+str(board)+"_startup_and_periphery.txt")  # initial configuration  ATT should be once ?
    # time.sleep(0.1)

    # turn off TDCs, pa,discris => start from a clean config
    alti.wr_asic_cfg("config/disableAllMatrix.txt")
    # time.sleep(0.1)

    # turn ON (TDCs, pa and discris) for some or all channels depending on pixelONStr
    if pixelONStr.lower() == "all":
        if onlyTDCOn:
            alti.wr_asic_cfg("config/enableTDCAllMatrix.txt")
        else:
            if ext_discri:
                alti.wr_asic_cfg("config/enableAllMatrixButDiscriOff.txt")
            else:
                alti.wr_asic_cfg("config/enableAllMatrix.txt")
    elif pixelONStr.lower() == "allvpa":
        if onlyTDCOn:
            alti.wr_asic_cfg("config/enableTDCAllVpa.txt")
        else:
            if ext_discri:
                alti.wr_asic_cfg("config/enableAllVpaButDiscriOff.txt")
            else:
                alti.wr_asic_cfg("config/enableAllVpa.txt")
    elif pixelONStr.lower() == "alltz":
        if onlyTDCOn:
            alti.wr_asic_cfg("config/enableTDCAllTZ.txt")
        else:
            if ext_discri:
                alti.wr_asic_cfg("config/enableAllTZButDiscriOff.txt")
            else:
                alti.wr_asic_cfg("config/enableAllTZ.txt")
    else:
        pixelONListist = getPixelList(pixelONStr)
        for pixel in pixelONListist:
            turnOn(alti, pixel, onlyTDCOn, ext_discri)

    # load vthc
    if loadVthc or vthcFile is not None:
        if vthcFile is None:
            vthcFile = "config/b" + str(board) + "_vthc_all_col.txt"
        print(vthcFile, "========================")
        try:
            alti.wr_asic_cfg(vthcFile)
        except:
            print ("File missing: ",vthcFile)

        # set Ctest or ext_discri to the selected channels
    pixelSignalList = getPixelList(pixelSignalStr)
    for pixel in pixelSignalList:
        injection(alti, pixel, ext_discri, onlyTDCOn)
        pass

    # turn-on probe
    #alti.wr_asic_reg(979, 0b1011_0000)
    #row, column = Utils.getPixelCoordinates(pixelSignalList[0])
    #alti.wr_asic_reg(967, int((column << 4) + row))
    
    # setting for pulser
    if not ext_discri:
        alti.wr_asic_reg(994, 0b00_010001)  # pllBwConf  ATT to be checked: Sync issue using 100000 in thresSca
       
        alti.wr_asic_reg(999, 0b1000_1001)  # psDelay1 for clk40MHzPS, ck80MHzPS, ck640MHzPS clocks B'1001-0000

        # optimum fund by Maxime
        #alti.wr_asic_reg(999, 0b0010_1101)
        #alti.wr_asic_reg(1000, 0b0000_1010)
        #alti.wr_asic_reg(999, 0b0010_1101)
        #alti.wr_asic_reg(1000, 0b0000_1000)

        # fine_del=0#0b1000_1001
        # coarse_del=8#0b0000_1000
        # alti.wr_asic_reg(999, fine_del << 4)
        #

        alti.wr_asic_reg(962, 0b0_0_001100)  # bias_ch_sel_pulser
        # Bit-7   : not used
        # Bit-6   : dacPulser_large_range
        # Bit-5:0 : dacPulserSetting

        alti.wr_asic_reg(1012, 0b0_1_000011)  # CONF_CMDCALGENCNTR1
        # [5:0]   : Cal Pulse length, 25 ns to 1.575 us, must be at least  50 ns
        # [6]   : calPulseEn
        # [7]   : not used



    if writeReg is not None:
        vec=writeReg.split(",")
        if len(vec)%2 ==0:
            registers=vec[0::2]
            values=vec[1::2]
            for reg,val in zip(registers,values):
                print (reg,val)
                alti.wr_asic_reg(int(reg),int(val)) 
        else:
            print ("Can interpret writeReg", writeReg )
            
    #setPreampOff(alti,pixelSignalStr)

    
    turnOnProbePa(alti,pixelSignalList[0])

######################################
#  probe PA for one pixel
######################################
def turnOnProbePa(alti,pixel):

    #alti.wr_asic_reg(979, 0b1011_0000)
    alti.wr_asic_reg(979, 0b1111_0000)

    
    pixelI2CAddress = 4 * pixel
    
    #turn-on pixel and Ctest
    #alti.wr_asic_reg(pixelI2CAddress + 2, 0b0001_1110)
    # Set dac threshold value
    #alti.wr_asic_reg(pixelI2CAddress + 3, 0b10000000)

    
    col = pixel // nbOfLines

    row = pixel % nbOfLines

    print (col,row)

    alti.wr_asic_reg(967, int((col << 4) + row))

    

######################################
#  Set Vbg (dac)
######################################
def setDacVbg(alti, dacvbg):
    alti.wr_asic_reg(992, (dacvbg << 1) + 1)  # +1 to turn on bandgap


######################################
#  Set bias_ch_dac_p (dac)
######################################
def setdacBiaspaConf(alti, dacCurrent):
    dacCurrent = Utils.truncateToNbits(dacCurrent, 5)
    alti.wr_asic_reg(963, (dacCurrent << 1) + 1)  # (!) alter Bit-0 : Rin_VPA_TZ


######################################
#  Set Vth (dac)
######################################
def setDacVth(alti, dacvth):
    dac_low = dacvth
    dac_high = (dacvth >> 8) + 4  # +0x04 to keep VTH OTA ON
    alti.wr_asic_reg(965, dac_low)
    alti.wr_asic_reg(966, dac_high)


######################################
#  Set Vthc (dac) for a given pixel
######################################
def setDacVthc(alti, pixel, dacvthc):
    alti.wr_asic_reg(4 * pixel + 3, dacvthc)


######################################
#  Set Vthc to 0 for channels without injected signal
######################################
def setVthcToZero(alti, options):
    tmpVthcFileName = "tmpvthc.txt"
    fvthc = open(tmpVthcFileName, "w")
    pixelInjList = getPixelList(options.pixelInj)
    for pix in range(nbOfPixels):
        if pix in pixelInjList: continue
        #print("Vthc=0 for ", pix)
        # vthc
        address = pix * 4 + 3
        val = 0  # highest thres. when no signal injection
        mystr = "{0}     ,{1:#08b}, \n".format(address, val)
        mystr = mystr.replace("0b", "B'")
        fvthc.write(mystr)

    fvthc.close()
    alti.wr_asic_cfg(tmpVthcFileName)


######################################
#  Set TDC off for channels without injected signal
######################################
def setTDCOff(alti, options):
    tmpFileName = "tmp.txt"
    f = open(tmpFileName, "w")
    pixelInjList = getPixelList(options.pixelInj)
    for pix in range(nbOfPixels):
        # if pix in pixelInjList: continue
        #print("TDC off for ", pix)

        # TDC
        address = 4 * pix + 1
        mystr = "{0}     ,B'1-0-0-0-0000 \n".format(address)
        mystr = mystr.replace("0b", "B'")#????
        f.write(mystr)

    f.close()
    alti.wr_asic_cfg(tmpFileName)


def setDiscriOff(alti, options):#discri off for pixels with no injected signal
    tmpFileName = "tmp.txt"
    f = open(tmpFileName, "w")
    pixelInjList = getPixelList(options.pixelInj)
    for pix in range(nbOfPixels):
        if pix in pixelInjList: continue
        #print("Discri off for ", pix)

        # TDC
        address = 4 * pix + 2
        mystr = "{0}     ,B'0-0-0-1-1-0-0-0 \n".format(address)
        mystr = mystr.replace("0b", "B'")#????
        f.write(mystr)

    f.close()
    alti.wr_asic_cfg(tmpFileName)

def setPreampOff(alti, pixelInj):#discri off for pixels with no injected signal
    tmpFileName = "tmp.txt"
    f = open(tmpFileName, "w")
    pixelInjList = getPixelList(pixelInj)
    for pix in range(nbOfPixels):
        if pix in pixelInjList: continue
        #print("Preamp off for ", pix)

        # TDC
        address = 4 * pix + 2
        mystr = "{0}     ,B'0-0-0-0-1-1-0-0 \n".format(address)
        mystr = mystr.replace("0b", "B'")#????
        f.write(mystr)

    f.close()
    alti.wr_asic_cfg(tmpFileName)


######################################
# Set pulser charger
######################################
def setPulser(alti, bias_ch_sel_pulser):  # ATT can do better
    print(bias_ch_sel_pulser)
    alti.wr_asic_reg(962, bias_ch_sel_pulser)
