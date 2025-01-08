To operate the Demonstrator smoothly, one needs to know some knowledge from [FELIX user manual](https://atlas-project-felix.web.cern.ch/atlas-project-felix/user/felix-doc/felix-user-manual/5.x/felix-user-manual.html), [lpGBT](https://lpgbt.web.cern.ch/lpgbt/v1/), [PEB PDR](https://edms.cern.ch/document/2644367/1
), [PEB 1F schematic](https://gitlab.cern.ch/atlas-hgtd/hgtd-peb/-/blob/master/peb/1F/v1/peb_1f.pdf?ref_type=heads), [ALTRIC3 datasheet](https://cernbox.cern.ch/s/GoUJyGwHSVlJmNM), [high voltage](https://cernbox.cern.ch/s/3UyIqcQJv5KaKFR) and [FADA](https://gitlab.cern.ch/atlas-hgtd/Electronics/FADA)

# Demonstrator introduction
The following picture shows the demonstrator in the clean room (Building 180, CERN).
The PEB 1F can be used to connect the column 1~3 (21~19) of the front (back) side. For the demonstrator, it is the front side. It contains 9 timing data channels (T0~T8) and 3 lumi data channels (L0~L2).
From the detector units point of view, for each column, we name the modules as 1 to 18 from the out to the inner, as the following plot shows.
From the data rate (or the eLink of lpGBT) point of view, For each lpGBT, we also name the modules connected with the lpGBT as "M#".
The following picture and tables show how the mdules are connected with the PEB 1F and how the eLinks are allocated in each timing/lumi lpGBT.

# Login Demonstrator server (you need password) and setup Felix environment

```
ssh hgtd-daq@pc-hgtd-daq-flx-01 -XY
setupFLXcode
```
# Low voltage (LV) power suplies controlling

Script: powerControl_LV.py
Location: /home/hgtd-daq/hgtd-peb
```
python3 ../powerControl_LV.py <--ON/--OFF/-s>
```
--ON: turn on the low voltage suplies for PEB and high voltage (HV) module
--OFF: turn off the low voltage suplies for PEB and HV module
-s: check the output of the low voltage suplies for PEB and HV module

# Align the GBT channels between PEB and FELIX
Each channel is independent and does not affect the others. It is ok to only align the channel(s) you want to test

Run the following command for several times until the channel(s) alignment shows "YES"
```
flx-init
```
or if you want to align all the 9 channels, you can run the following script:
```
cd /home/hgtd-daq/hgtd-peb/hgtd-peb/script3
python3 alignCh.py
```
The script keeps trying until aligning all the 9 channels at the same time.
If you cannot align the channels after several times, you can try re-power off/on the LV power suplies and reboot the server.

# Turn on the high voltage
From the PEB 1F scematic to learn how do the connections to power on the HV for the modules you want to test.
There are two HV connector on PEB 1F (J112 and J333). The HV cables have been coded from 1/G1 to 28/G28 according to the connectors. Mark "#" means the channel number and mark "G#" means the GND.
Each HV module only has 14 output channels. The HV cables connect the output of the HV filter. The distribution of the filter output channels is shown as the following plot.
The correct HV connector should be connected with the HV cables, and then select the correct HV cables to connect with the filter output according to the moudles you want to test. The relationship between HV pins and the correspond modules is shown as the following table.

From the HV User manual, you can learn how to connect the HV module output channels to the filter input channels, and also, you can learn how to install the HV software and how to contorl the HV module.

# Demonstrator configuration
For the current scripts, we can only configure the Demonstrator channel by channel.

ALTIROC2 configuration (channels 3~8): 
```
/home/hgtd-daq/hgtd-peb/hgtd-peb/script2
```
ALTIROC3 configuration (channels 0~2): 
```
/home/hgtd-daq/hgtd-peb/hgtd-peb/script3
```

1. PEB
PEB configuration includes lpGBT configuration and VTRX+ configuration.
For lpGBT configuratin, it eables the bpol12vs to power on the front-end modules, sends primary clocks to the front-end modules, sets the data rate of the eLinks and also sets the pre-empahsis for signal transmission.
For VTRX+ configuration, it sets the pre-empahsis for signal transmission and enable the lumi channels for T0~T2.

Channels 0~2. Patter: Mix046
```
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 0
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 1
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 2
```
Channels 3~5. Patter: Mix230
```
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 3
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 4
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 5
```
Channels 3~5. Patter: Mix310
```
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 6
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 7
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 8
```
The configurations above are for the final detector seetings according to the different data rates for different modules. If you only do the scanning test, for convenience, you can configure all the all the data rate of lpGBT eLinks to 320 Mbps by running the following command:
```
python3 initialization.py -F ./config/lpGBT/all_320M.yelc -d 0 -G <0/1//2/3/4/5/6/7/8>
```
Note: All the above commands may not succeed at once, so if failed, you need to run it again.

After above configuration, the front-end modules are powered on, now we can comunicate with them through I2C bus. So if you want to check the I2C bus is ok or not, you can try the following commands:
```
python3 i2c_check.py -d 0 -G <0/1//2/3/4/5/6/7/8>
```
The script i2c_check.py tries to read out some register values of the front-end modules.

2. Front-end module
Here is an example:
```
python3 configure.py -b 0 --triggerFre 50 --pixelOn col0 --pixelInj col0 --dacCharge 24 -F ./config/altiroc/mix046.yelc --elinkFile ./config/felix/peb_1f.yelc -d 0 -G 0
```
-b: board number, for naming the folder's name
--triggerFre: L0/L1 trigger frequency, Hz
--pixelOn: turn on the pixels, including PA, discriminator, TDC
--pixelInj: pixels with internal charge injection
--dacCharge: DAC value for the charge injection, here using large Ctest.
-F: front-end module configuration file.
--elinkFile: configuration file for FELIX card

3. FElIX card
Enable 8b10b decoding mode:  
```
flx-config DECODING_HGTD_ALTIROC 1
```
Setting the IDLE fast command character. The default is for ALTIROC2. If you are running ALTIROC3, run the following command:
```
flx-config HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1
```
Set the latency between CAL tirgger and L0/L1 trigger:
```
flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4
```
# Data taking
Send fast command:
```
fttcemu -f 100
```
-f: the frequency of the fast command, Hz

Take data:
```
fdaq -t 3 <your file name> -T
```
-t: time of taking data, second
-T: determing the file name style for the received data. 

Disable the fast command
```
fttcemu -n
```
NOTE: you need to disable the fast command before next PEB/module configuration, otherwise the communication may be blocked.

check the received data
```
fcheck <your file name> -F 100 -e 010
```
-F: the block number you want to check
-e: the elink you want to check

# Scanning test
The scripts for Scanning test are almost same with FADA scripts, the main difference is the way of front-end module configuration. For Demonstrator, we use FELIX, but for FADA, they use ZC706 FPGA.

In fact, the scan test is a process of repeatedly configuring the module and taking data. There are some .py scripts for scanning test in the folder /home/hgtd-daq/hgtd-peb/hgtd-peb/script3 or /home/hgtd-daq/hgtd-peb/hgtd-peb/script2, inlcuding vthScan_peb.py, vthcScan_peb.py, chargeScan_peb.py, delayScan_peb.py and widthScan_peb.py. Usually, you don not need to modify these scripts. When doing scanning test, we do modifications in the corresponding sh scripts and run them, including runVth.sh, runVthc.sh, runCharge.sh, runDelay.sh and runWidth.sh. For example:
1. Vthc scanning 
```
sh runVthc.sh 0 24 0 14 ./config/altiroc/t0_HV.yaml ./config/felix/t0_HV.yelc ./Measurements/coolTest/m10c
```
Before running this script, some modifications are needed in this line according to your test:
```
python3 vthcScan_peb.py -b $board --autoStop 1 --dacVthcMin 0 --dacVthcMax 175 --dacVthcStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --dacCharge $Q -F $moduleFile -d 0 -G 0 --elinkFile $elinkFile --dacVth 380
```
autoStop: If true, the scanning will be stopped automatically when receiving nothing.
dacVthcMin: the minimum vthc DAC value for the scanning
dacVthcMax: the maximum vthc DAC value for the scanning
dacVthcStep: scanning step for vthc DAC
N: number of trigger, the setting should be keep same with triggerFre, because only taking data for 1 second for each vthc DAC
triggerFre: the frequency of trigger
startCol: the start coulumn to scan
endCol: the end column to scan
o: where you save the scanning data
dacVth: the Vth DAC value in your vthc scanning. It should be keep same with the front-end module configuration file.
NOTE:When doing vthc scan, the vthcfile in the front-end module configuration file should be set as "config/altiroc/Vthc/empty.txt"

This scanning will take about few hours according the module number in the scanning, after that, you will have the raw data in your output folder. Then you should run the following script to analyse the data.
```
python3 makeEffCurve_ALTIROC3.py --module --input Measurements/coolTest/m10c/M9/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir Plots/coolTest/m10c/M9/
```
You will find the new vthc configuration files in the folder ./Plots/coolTest/m10c/M9/: asic0_vthc.txt and asic1_vthc.txt.
With these two files, you can go on to do the charge scanning.

2. Charge scanning

First, you need to replace the vthcfile with "./Plots/coolTest/m10c/M9/asic0_vthc.txt" and "./Plots/coolTest/m10c/M9/asic1_vthc.txt" in the front-end module configuration file. Then simmilarly, we run the following commands:
```
sh runCharge.sh 0 0 14 ./config/altiroc/t2_HV.yaml ./config/felix/t2_HV.yelc ./Measurements/coolTest/m10c
```
Before running this script, some modifications are also needed in this line according to your test:
```
python3 chargeScan_peb.py -b $board --autoStop 1 --dacChargeMin 0 --dacChargeMax 63 --dacChargeStep 1 -N 100 --triggerFre 100 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir -F $moduleFile -d 0 -G 2 --elinkFile $elinkFile --pattern Mix046 --dacVth 380 --dacCharge 24
```
This scanning will take about 1~2 hours according the module number in the scanning, after that, you will have the raw data in your output folder. Then you should run the following script to analyse the data.
```
python3 anaCharge.py -i Measurements/coolTest/m10c/M9C0/chargeScan/B_0_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/coolTest/m10c/M9/ --debug 1 --noLSBCor 1
```
Then you will have the result in the folder "./Plots/coolTest/m10c/M9/"


# Up-link diagram scanning
1. Connecting the UPL with the Test pins (T0/L0-J11, T1/L1-J12, T2/J2-J287, T3-J10, T4-J284, T5-J286, T6-J9, T7-J285, T8-J283) on PEB 1F according the lpGBT you want to test.
2. Connecting the UPL with computer via USB and install the software according to [UPL reference]().
3. Connecting the coresponding uplink optical fiber with oscilloscope.
4. 





```
cd hgtd-peb/hgtd-peb/
python3 ../powerControl_LV.py --ON




# Power on the low voltage suplies for PEB and high voltage (HV) module

```
cd hgtd-peb/hgtd-peb/
python3 ../powerControl_LV.py --ON
```











# PEB 1F  
<img src="./config/map_PEB1F.png"  width="500">  

# Parameters in PEB 1F test scripts  
See "parameter.py" in directory "hgtd-peb/script/lib/"

# How to use PEB 1F test scripts

1. Initialize FELIX to align the timing data channel
```
flx-init
```
2. lpGBT and VTRX+ configuration  

For T0, T1 and T2:  
```
python3 initialization_Mix046.py -F ./config/felix/Mix046_withLumi.yelc -d <FLX-device number> -G <GBT-link number>
```
For T3, T4 and T5:  
``` 
python3 initialization_Mix230.py -F ./config/felix/Mix230.yelc -d <FLX-device number> -G <GBT-link number>
```
For T6, T7 and T8:  
```
python3 initialization_Mix310.py -F ./config/felix/Mix310.yelc -d <FLX-device number> -G <GBT-link number>
```
3. MUX and ADC readout  

For T0, T1 and T2:  
```
python3 i2c_Mix046.py -d <FLX-device number> -G <GBT-link number>
```
For T3, T4 and T5: 
```
python3 i2c_Mix230.py -d <FLX-device number> -G <GBT-link number>
```
For T6, T7 and T8:  
```
python3 i2c_Mix310.py -d <FLX-device number> -G <GBT-link number>
```
4. Module configuration (ALTIROC2)  

For T0, T1 and T2:  
```
python3 configure_Mix046.py -F ./config/altiroc/Mix046.yaml -d <FLX-device number> -G <GBT-link number>
```
For T3, T4 and T5:  
```
python3 configure_Mix046.py -F ./config/altiroc/Mix230.yaml -d <FLX-device number> -G <GBT-link number>
```
For T6:  
```
python3 configure_Mix046.py -F ./config/altiroc/Mix310.yaml  -d <FLX-device number> -G <GBT-link number>
```
For T7 and T8:  
```
python3 configure_Mix046.py -F ./config/altiroc/Mix300.yaml  -d <FLX-device number> -G <GBT-link number>
```
5. Data taking (ALTIROC2)  
```
elinkconfig
```
open the configuration file in 'elinkconfig' window (./config/felix/Mix046_withLumi.yelc or ./config/felix/Mix230.yelc or ./config/felix/Mix310.yelc).  

Generate/Upload Config and Emulator Data  

Enable ALTIROC2 8b10b decoding mode:  
```
flx-config DECODING_HGTD_ALTIROC 1
```
Set L0/L1 frequncy:  
```
fttcemu -f <frequency in Hz>
```
Data taking: 
```
fdaq -t <time in second> <your file name> -T
```
Data checking  
```
fcheck <your file name-1.dat> -F <numbers of block> -e <eLink number>
```
# Note
## It is better to disable TTC emualtor (run "fttcemu -n") and configure the 'elinkconfig' with "./config/felix/ic_ec_only.yelc" after finishing data taking or before next PEB/Module configuration. Otherwise the communication may be blocked.  

## If the optical link is not stable, try to change the parameters for pre-emphasis in "initialization_MixABC.py". Some combinations of the parameters can be found in file "hgtd-peb/script/eye_scan/pre-emphasis_parameters_for_PEB_1F.xlsx" which are obtained base on IHEP setup. If the combiantions are not fit to your setup, you can get your combinations from optical eye-diagram scaning. The script for eye-diagram scaning can be found in ""hgtd-peb/script/eye_scan/".  

## The frequency of the e-port clock from lpGBT to front-end module can be changed to 40MHz/320MHz/640MHz by uncommenting lines 100~102 in the scripts "hgtd-peb/script/lib/peb_MixABC.py".
