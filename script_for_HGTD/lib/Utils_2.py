import yaml
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
import time



def getParser():
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-d","--devnr", help="FLX-device to use", default=0,type=int)
    parser.add_option("-G","--gbt", help="GBT-link number", default=0,type=int)
    parser.add_option("-T","--timingAddr", help="Timing lpGBT I2C address", default=112,type=int)
    parser.add_option("-L","--LumiAddr", help="Lumi lpGBT I2C address", default=113,type=int)
    parser.add_option("-V","--vtrxAddr", help="VTRX+ lpGBT I2C address", default=80,type=int)

    parser.add_option("--writeReg", help="write in register: register,value or register1,value1,register2,value2", default=None,type=str)
    parser.add_option("-F","--ConfigFile", help="PEB and module configuration file", default=None,type=str)    
    parser.add_option("--suffix", help="suffix", default="",type=str)
    parser.add_option("-o","--outputDir", help="Output directory", default=None,type=str)
    parser.add_option("--pixelOn", help="Activated pixel (TDC,preamp,discri)", default="all",type=str)
    parser.add_option("--pixelInj", help="Pixel with injected signal (ext_discri or pulser)", default="0",type=str)
    parser.add_option("--onlyTDCOn", help="Only TDC On (PA and discri off)", default=False,action="store_true")
    parser.add_option("--autoStop", help="Stop automatically threshold scan", default=False,action="store_true")
    parser.add_option("-b","--board", help="Board number", default=None,type=int)
    parser.add_option("-N","--Nevents", help="Number of events", default=100,type=int)
    parser.add_option("--Cd", help="Cd", default=-1,type=int)
    parser.add_option("--ext_discri", help="Use of the external discriminator (if False pulser if used)", default=False,action="store_true")
    parser.add_option("--pixelPlot", help="Pixel used for plotting", default=0,type=int)
    parser.add_option("--asicPlot", help="Asic used for plotting", default=None,type=int)    
    # parser.add_option("-d","--debug", help="For debugging", default=False,action="store_true")
    parser.add_option("--loadVthc", help="Load Vthc file", default=False,action="store_true")
    parser.add_option("--setVthcToZero", help="Set Vthc to 0 for channels without injected signal", default=False,action="store_true")
    parser.add_option("--setTDCOff", help="Set TDC Off for channels without injected signal", default=False,action="store_true")
    parser.add_option("--vthcFile", help="File containing Vthc", default=None,type=str)
    parser.add_option("--elinkFile", help="File configuring FELIX elink", default=None,type=str)
    #parser.add_option("--hostIP", help="host IP address", default="129.104.89.216",type=str)
    parser.add_option("--hostIP", help="host IP address", default="10.10.0.98",type=str)
    parser.add_option("--localIP", help="local IP address", default="10.10.0.100",type=str)
    parser.add_option("--port", help="port", default=7,type=int)
    parser.add_option("--periodtrigger", help="trigger period in microsecond", default=250,type=int)
    parser.add_option("--triggerFre", help="trigger frequency in Hz", default=100,type=int)
    parser.add_option("--nIdle", help="latency between CAl and L0/L1", default=5,type=int)
    parser.add_option("--smallCtest", help="Ctest=26pF", default=False,action="store_true")
    parser.add_option("--Cp", help="Cp if different from 0 or 1, take value from config file", default=-1,type=int)
    parser.add_option("-q","--quick", help="", default=False,action="store_true")

    #trig_latency
    parser.add_option("--trigLatency", help="Trig Latency", default=-1,type=int)
    parser.add_option("--nbCalCMD", help="Nb CalCMD", default=1,type=int)
    parser.add_option("--nbTrigCMD", help="Nb TrigCMD", default=1,type=int)    

    parser.add_option("--dacVth", help="DAC Vth", default=0,type=int)
    parser.add_option("--dacVth0", help="DAC Vth0", default=0,type=int)
    parser.add_option("--dacVth1", help="DAC Vth1", default=0,type=int)
    parser.add_option("--dacCharge", help="DAC charge", default=-1,type=int)
    parser.add_option("--cDelay", help="CoarseDelay", default=8,type=int)
    parser.add_option("--fDelay", help="FineDelay", default=9,type=int)

    #vth scan
    parser.add_option("--dacVthMin", help="DAC Vth min", default=300,type=int)
    parser.add_option("--dacVthMax", help="DAC Vth max ", default=600,type=int)
    parser.add_option("--dacVthStep", help="DAC Vth step", default=1,type=int)
    parser.add_option("--dacVthRange", help="DAC Vth range", default=3,type=int)

    #vthc scan
    parser.add_option("--dacVthcMin", help="DAC Vthc min", default=0,type=int)
    parser.add_option("--dacVthcMax", help="DAC Vthc max ", default=220,type=int)
    parser.add_option("--dacVthcStep", help="DAC Vthc step", default=1,type=int)

    #charge scan
    parser.add_option("--dacChargeMin", help="DAC charge min", default=-1,type=int)
    parser.add_option("--dacChargeMax", help="DAC charge max ", default=-1,type=int)
    parser.add_option("--dacChargeStep", help="DAC charge step", default=1,type=int)

    #width scan
    parser.add_option("--widthMin", help="Width min", default=0,type=int)
    parser.add_option("--widthMax", help="Width max", default=31,type=int)
    parser.add_option("--widthStep", help="Width step", default=1,type=int)

    #delay scan
    parser.add_option("--cDelayMin", help="CoarseDelay min", default=0,type=int)
    parser.add_option("--cDelayMax", help="CoarseDelay max", default=15,type=int)
    parser.add_option("--cDelayStep", help="CoarseDelay step", default=1,type=int)
    parser.add_option("--fDelayMin", help="FineDelay min", default=0,type=int)
    parser.add_option("--fDelayMax", help="FineDelay max (cant be larger than 15)", default=15,type=int)
    parser.add_option("--fDelayStep", help="FineDelay step", default=1,type=int)

    #prologix
    parser.add_option("--prologixIP", help="prologix IP address", default="10.10.0.130", type=str)
    # equipements GPIB port
    parser.add_option("--multimeter1Port", help="Keithley GPIB port defined", default=16, type=int)

    parser.add_option("--ps_CoarseDelay", help="psDelay1 coarse delay (1.560ns)", default=-1,type=int)
    parser.add_option("--ps_FineDelay", help="psDelay1 fine delay (97 ps)", default=-1,type=int)
    parser.add_option("--ps_CoarseTDCDelay", help="psDelay2 CoarseDelayTDC (1.562ns)", default=-1,type=int)

    parser.add_option("--timingRate", help="Timing Data Rate 320,640,1280", default=320, type=int)
    parser.add_option("--encoding", help="1:8b10b encoding, 0:Raw", default=1, type=int)
    parser.add_option("--enAsic", help="Enable/Disable ASIC, bit0=ASIC-0x42, ...", default=3, type=int)
    parser.add_option("--enTiming", help="Enable(1)/Disable(0) Timing Line", default=1, type=int)
    parser.add_option("--enLumi", help="Enable(1)/Disable(0) Lumi Line", default=0, type=int)

    parser.add_option("--loop", help="Run loop number", default=1, type=int)
    parser.add_option("--fmc", help="FMC Board version", default=1,type=int)

    parser.add_option("--startCol", help="column start to scan", default=0, type=int)
    parser.add_option("--endCol", help="column start to end", default=14,type=int)
    parser.add_option("--stepCol", help="step fro column scan", default=1,type=int)    
    #parser.add_option("--dacVthDataZero", help="DAC Vth Max Data = 0", default=780,type=int)
    parser.add_option("-p","--pattern", help="lpGBT elink pattern", default=None, type=str)    
    return parser.parse_args()


def read_yaml_to_dict(yaml_path: str, ):
    with open(yaml_path) as file:
        dict_value = yaml.load(file.read(), Loader=yaml.FullLoader)
    return dict_value

#############################################
# function for output prefix
#############################################
def getOutName(options):
   pixelOn = options.pixelOn
   pixelInj = options.pixelInj

   outName= "B_"+str(options.board)#.zfill(3)
   def getName(mystr):
      if "col" in mystr.lower():
         if mystr.find("-")<0:
            return "col"
         else: return "multicol"
      elif "row" in mystr.lower():
         if mystr.find("-")<0:
            return "row"
         else: return "multirow"
      elif "squarefive" in mystr.lower():
         if mystr.find("-")<0:
            return "squareFive"
         else: return "multisquareFive"
      elif "squarethree" in mystr.lower():
         if mystr.find("-")<0:
            return "squareThree"
         else: return "multisquareThree"
         
      elif "sparsefifteen" in mystr.lower():
         if mystr.find("-")<0:
            return "sparseFifteen"
         else: return "multisparseFifteen"
      elif "rndfifteen" in mystr.lower():
         if mystr.find("-")<0:
            return "rndFifteen"
         else: return "multirndFifteen"
         
      elif "rndnine" in mystr.lower():
         if mystr.find("-")<0:
            return "rndNine"
         else: return "multirndNine"
         
      elif "rndfive" in mystr.lower():
         if mystr.find("-")<0:
            return "rndFive"
         else: return "multirndFive"
         
      elif "rndthree" in mystr.lower():
         if mystr.find("-")<0:
            return "rndThree"
         else: return "multirndThree"
         
      elif mystr.lower() == "all":
         return "all"
      elif "alltz" in mystr.lower():
         return "allTZ"
      elif "allvpa" in mystr.lower():
         return "allVpa"
      else:
         return "pix"

   outName+="_On_"+getName(pixelOn)
   outName+="_Inj_"+getName(pixelInj)

   #add N
   try:
      outName +="_N_"+str(options.Nevents)
   except:
      pass

   #add Vth
   try:
      outName +="_Vth_"+str(options.dacVth)
   except:
      pass

   #if options.Cd>=0:
   outName +="_Cd_"+str(options.Cd)
         #add charge

   if options.Cp>=0:
      outName +="_Cp_"+str(options.Cp)
         #add charge
   outName +="_cDel_"+str(options.cDelay)
   outName +="_fDel_"+str(options.fDelay)
         
   #add charge
   if not options.ext_discri:
      outName +="_Ctest_"
      if options.smallCtest:
         outName +="26_"
      else:
         outName +="208_"
      if options.dacCharge>=0:
         outName +="Q_"+str(options.dacCharge)

   #if int(options.setVthcToZero):
   #   outName +="_Vthc0_"

   outName+="/pixelOn_"+options.pixelOn+"_pixelInj_"+options.pixelInj +"/"
   # print (outName)
   return outName+"/"

#############################################
# get pixel list from string
#############################################
def getPixelList(channels):
   vec=channels.split(",")
   if len(vec) == 1:
      pixels=[int(vec[0])]
   elif len(vec) == 3:
      pixels = range(int(vec[0]),int(vec[1])+1,int(vec[2]))
   else:
      print("I am not able to interpret --channels :", channels)
      sys.exit()
   return pixels
#############################################
# linear fit
#############################################
def linear_fit(x,y):

   par=[9999,9999]
   if len(x) < 2:
      return par
   else:
      try:
         #print ("Fit data:",x,y)
         par=np.polyfit(np.array(x), np.array(y), 1)
      except:
         print ('Failed')
         #print (x,y)
         return par
   #print (par)
   return par

#############################################
# make some plots and compute also LSB
#############################################
def plot(df,ymax,xVarName,yVarName,outname,xList=None,showBidim=False,savePlots=True,displayPlots=False,xUnit="[ps]",doLSB=True):

   if len(df.index) ==0:
      print ("No data to be plotted....")
      return 0

   if xList==None:
      xList=np.sort(np.unique(df[xVarName].values))
   xMin=np.min(xList)
   xMax=np.max(xList)
   xStep=np.min(np.diff(xList))

   #compute average
   yMean=[]
   yRMS=[]
   xOK=[]
   nEvents=[]
   for x in xList:
      y=df.loc[df[xVarName] == x][yVarName]
      nEvents.append(len(y))
      okY=y<ymax
      if sum(okY)>0:
         yMean.append(np.mean(y[okY]))
         yRMS.append(np.std(y[okY]))
         xOK.append(x)

   #fit ans LSB
   slope,intercept=linear_fit(xOK[:],yMean[:])
   lsb=0
   if slope!=0:
      lsb=1/slope

   #plot
   fig, ((ax1, ax2, ax3)) = plt.subplots(nrows = 1, ncols = 3, figsize=(18,6))

   #ax1
   ax1.scatter(xList, nEvents   , facecolors='none', edgecolors='g')
   ax1.plot(xList, nEvents)
   ax1.grid(True)
   ax1.set_xlabel(xVarName+ " "+xUnit, fontsize = 10)
   ax1.set_ylabel(' Nb of events', fontsize = 10)
   ax1.set_xlim(left = np.min(xList), right = np.max(xList))

   #ax2
   if showBidim:
      xedges = np.arange(      xMin-xStep/2.,xMax,xStep)
      yedges = np.arange(-1/2,ymax+1,1.)
      HY, xedges, yedges = np.histogram2d(df[xVarName], df[yVarName], bins=(xedges, yedges))
      HY = HY.T  # Let each row list bins with common y range.
      X, Y = np.meshgrid(xedges, yedges)
      HY[HY==0]=np.nan
      current_cmap = matplotlib.cm.get_cmap().copy()
      current_cmap.set_bad(color='white')
      ax2.pcolormesh(X, Y, HY,cmap=plt.cm.rainbow)
   ax2.scatter(xOK, yMean      , facecolors='none', edgecolors='g')
   ax2.grid(True)
   ax2.set_xlabel(xVarName + " "+xUnit, fontsize = 10)
   ax2.set_ylabel(yVarName +' [dac]', fontsize = 10)
   ax2.set_ylim(bottom = 0, top = ymax)
   print (xOK)
   if len(xOK)>0:
      ax2.set_xlim(left = np.min(xOK), right = np.max(xOK))
   if doLSB:
      ax2.plot(xOK,      slope*np.array(xOK)+      intercept, color='r')
      ax2.legend(['LSB: %.1f ' % lsb],loc = 'upper right', fontsize = 9, markerfirst = False, markerscale = 0, handlelength = 0)

   #ax3
   yrms=np.array(yRMS)
   if doLSB:yrms*=lsb
   ax3.scatter(xOK, yrms     , facecolors='none', edgecolors='g')
   ax3.grid(True)
   ax3.set_xlabel(xVarName+ " "+xUnit, fontsize = 10)
   ytitle="RMS"
   if doLSB:ytitle+="[ps]"
   ax3.set_ylabel(yVarName+' '+ytitle, fontsize = 10)
   ax3.set_ylim(bottom = 0)
   if len(xOK)>0:
      ax3.set_xlim(left = np.min(xOK), right = np.max(xOK))

   #plt.subplots_adjust(hspace = 0.35, wspace = 0.2)
   if savePlots:
      plt.savefig(outname+".pdf")
   if displayPlots:
      plt.show()

   return lsb
############################################
#
############################################
def truncateToNbits(x, nbBitsToKeep):
   binary = '0000000'+bin(x)[2:]
   end = len(binary)
   start = end - nbBitsToKeep
   newX = int(binary[start:end + 1], 2)
   if newX != x:
      print("WARNING : you are probably overwriting other config bits\n"
           "  {0} within {1} bits = {2} (overflow) ".format(x, nbBitsToKeep, newX))
   return newX

############################################
#
############################################
def create_output_dir(outputDir):
   if outputDir != None:
      binoutdir = outputDir
   else:
      binoutdir = "output"

   isExist = os.path.exists(binoutdir)
   if not isExist:
      os.makedirs(binoutdir)
   return binoutdir

def get_total_rows(file_path):
    df = pd.read_csv(file_path)
    total_rows = df.shape[0]
    return total_rows

def is_all_zero(lst):
   for element in lst:
      if element != 0:
         return False
   return True