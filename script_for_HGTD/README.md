# Overview

The increase of the particle flux (pile-up) at the HL-LHC with instantaneous luminosities up to ~ 7.5 × 10^34 cm^-2 s^-1 will have a severe impact on the ATLAS detector reconstruction and trigger performance. The High Granularity Timing Detector (HGTD) is an ATLAS Phase II upgrade project, the goal of which is to provide an accurate measurement of the time of the tracks (< 50 ps) in order to mitigate the effect of the pile-up in the object reconstruction such as the jets, the electrons or the b-jets. In addition, the number of collected hits being proportional to the luminosity, it will provide an instantaneous measurement of the luminosity, which will be read out at 40 MHz.

HGTD is composed of 8032 front-end modules. Each module consists of two Low Gain Avalanche Sensors (LGADs) of approximately 2 × 2 cm^2 bump-bonded to two [ATLAS LGAD Timing Integrated Read-Out Chips (ALTIROC)](https://twiki.cern.ch/twiki/bin/view/Atlas/HGTDElectronics) and held together by a module flex (flexible PCB). These modules are arranged with overlap on the two sides on each disk. In order to facilitate the detector assembly, the modules will be mounted on support units forming detector units (a detector unit is a support unit with modules mounted on it). Each module will be connected to the Peripheral Electronic Boards (PEB) through a flex tail (another flexible PCB). The detector units and PEBs will be mounted on the HGTD cooling plates. The connections between on-detector and off-detector electronics are performed via optical fibers, high/low voltage cables, interlock cables and monitoring signal cables. The PEB acts as a bridge between the front-end modules and the off-detector systems. The optical fibers provide shared data streams for Timing, Trigger and Control (TTC), Detector Control System (DCS) and [Data Acquisition System (DAQ)](https://atlas-project-FELIX.web.cern.ch/atlas-project-FELIX/), and dedicated data streams for the luminosity system.

For error-free data transmission at the bandwidths (320 Mbps, 640 Mbps, or 1.28 Gbps) required by the expected HGTD data volume, the PEB uses the [low-power GigaBit Transmission chip (lpGBT)](https://lpgbt.web.cern.ch/lpgbt/v1/) and the [Versatile Link + Transceiver (VTRx+)](https://espace.cern.ch/project-Versatile-Link-Plus/SitePages/Home.aspx). The PEB also includes the 12 V to 1.2 V [DC-DC converters (bPOL12v)](https://espace.cern.ch/project-DCDC-new/_layouts/15/start.aspx#/index/Home.aspx) for the digital and analogue voltages supplied to the front-end modules. The supply voltages are monitored using the internal multiplexed ADC on the lpGBTs. Since the input channel number of this ADC is limited to 8, a multiplexing chip is required to handle all the signals connected to PEB. A full custom [64-to-1 multiplexing ASIC (MUX64)](
https://doi.org/10.1088/1748-0221/18/03/C03012) has been developed with a radiation tolerance suitable for its implementation on the PEB.

According to the optimization of mirror structure for the layout of the modules, 6 types of PEBs need to be designed for HGTD.

# Pre-condition

If your server is using this repository for the first time, follow the [clone and update instructions](manual/clone_update.md) to get the latest design and script files, and if you plan to operate the hardware and software, you also need to [build the software environment](manual/software_environment.md) which is required by [FELIX (FrontEnd LInk eXchange)](https://atlas-project-felix.web.cern.ch/atlas-project-felix/user/dist/) and PEB.

# Demonstrator introduction
The following picture shows the demonstrator in the clean room (Building 180, CERN).

<img src="./script3/config/demonstrator.jpg"  width="500">

The PEB 1F can be used to connect the column 1\~3 (21\~19) of the front (back) side. For the demonstrator, it is the front side. It contains 9 timing data channels (T0\~T8) and 3 lumi data channels (L0\~L2).

<img src="./script3/config/map_PEB1F.png"  width="500">

From the detector units point of view, for each column, we name the modules as 1 to 18 from the out to the inner, as the following plot shows.

<img src="./script3/config/module.png"  width="500">

From the data rate (or the eLink of lpGBT) point of view, for the modules connected with each lpGBT, we also name them as "M#". The following tables show how the mdules are connected with the PEB 1F and how the eLinks are allocated in each timing/lumi lpGBT. For each timing lpGBT, according to the data rates of the modules the lpGBT connects, we give a pattern name to it, "MixABC". Here A means the number of modules working at 1280 Mbps, B means the number of modules working at 640 Mbps, and C means the number of modules working at 320 Mbps. For PEB 1F, T0\~T2 are pattern Mix046, T3\~T5 are pattern Mix230, T6 is Mix310 and T7\~T8 are Mix300. 

<img src="./script3/config/connection.png"  width="500">

<img src="./script3/config/pattern.png"  width="500">

You can find more information from [here](https://gitlab.cern.ch/atlas-hgtd/hgtd-peb/-/blob/script_altiroc3/script3/config/PEB_1F_info.xlsx?ref_type=heads)

To operate the Demonstrator smoothly, one needs to know some knowledge from [FELIX user manual](https://atlas-project-felix.web.cern.ch/atlas-project-felix/), [lpGBT](https://lpgbt.web.cern.ch/lpgbt/v1/), [PEB PDR](https://edms.cern.ch/document/2644367/1
), [PEB 1F schematic](https://gitlab.cern.ch/atlas-hgtd/hgtd-peb/-/blob/master/peb/1F/v1/peb_1f.pdf?ref_type=heads), [ALTRIC3 datasheet](https://cernbox.cern.ch/s/GoUJyGwHSVlJmNM), [high voltage](https://cernbox.cern.ch/s/3UyIqcQJv5KaKFR) and [FADA](https://gitlab.cern.ch/atlas-hgtd/Electronics/FADA)

# Login the Demonstrator DAQ server (you need password) and setup FELIX environment
```
ssh hgtd-daq@pc-hgtd-daq-flx-01 -XY
```
```
setupFLXcode 
```
or
```
source <your FELIX software path>/setup.sh
```
Go to folder "path/hgtd-peb/script3" if you are testing altiroc3, or go to folder "path/hgtd-peb/script2" if you are testing altiroc2

# Low voltage (LV) power supplies controlling

Script: path/hgtd-peb/script3/powerControl_LV.py
```
python3 powerControl_LV.py <--ON/--OFF/-s>
```
--ON: turn on the low voltage supplies for PEB and high voltage (HV) module  
--OFF: turn off the low voltage supplies for PEB and HV module  
-s: check the output of the low voltage supplies for PEB and HV module  

# Align the GBT channels between PEB and FELIX
9 full GBT channels (TX+RX) of FELIX card are used for the 9 timing lpGBT. The 3 lumi lpGBTs are configured by 3 timing lpGBT through EC channel. So, to establish the communication between FELIX and PEB 1F (lPGBT), the frist step is to align these 9 channels. Each channel is independent and does not affect the others. It is ok to only align the channel(s) you want to test. The following screenshot shows the 9 timing channels.

<img src="./script3/config/GBT.png"  width="500">

Run the following command for several times until the channel(s) alignment shows "YES"
```
flx-init
```
or if you want to align all the 9 channels at the same time, you can run the following script:
```
cd path/hgtd-peb/script3
python3 alignCh.py
```
The script keeps trying until aligning all the 9 channels at the same time.
If you cannot align the channels after several times, you can try re-power off/on the LV power supplies or reboot the DAQ server.

# Turn on the high voltage
From the PEB 1F schematic to learn how to do the connections to power on the HV for the modules you want to test.

There are two HV connector on PEB 1F (J112 and J333). As the following picture shows, the HV cables have been coded from 1/G1 to 28/G28 according to the connectors. Mark "#" means the channel number and mark "G#" means the GND.

<img src="./script3/config/HVpin.jpg"  width="500">

Each HV module only has 14 output channels. The HV cables connect the output of the HV filter. The distribution of the filter output channels is shown as the following plots.

<img src="./script3/config/filter.jpg"  width="500">

<img src="./script3/config/filterOUT.png"  width="500">

The correct HV connector(J112 or J333) should be connected with the HV cables, and then select the correct HV cables to connect with the filter output according to the moudules you want to test. The relationship between HV pins (same with the HV cable code number) and the correspond modules is shown as the following table.

<img src="./script3/config/connection.png"  width="500">

From the HV User manual, you can learn how to connect the HV module output channels to the filter input channels, and also, you can learn how to install the HV software and how to contorl the HV module.

# Demonstrator configuration
For the current scripts, we can only configure the Demonstrator channel by channel.

ALTIROC2 configuration (channels 3~8): 
```
path/hgtd-peb/script2
```
ALTIROC3 configuration (channels 0~2): 
```
path/hgtd-peb/script3
```

1. PEB

PEB configuration includes lpGBT configuration and VTRX+ configuration.

For lpGBT configuratin, it enables the bpol12vs to power on the front-end modules, sends primary clocks to the front-end modules, sets the data rate of the eLinks and also sets the pre-empahsis for signal transmission.

For VTRX+ configuration, it sets the pre-empahsis for signal transmission and enable the lumi channels for T0~T2.

Channels 0\~2. Pattern: Mix046
```
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 0
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 1
python3 initialization.py -F ./config/lpGBT/mix046.yelc -d 0 -G 2
```
Channels 3\~5. Pattern: Mix230
```
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 3
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 4
python3 initialization.py -F ./config/lpGBT/mix230.yelc -G 5
```
Channels 6\~8. Pattern: Mix310
```
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 6
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 7
python3 initialization.py -F ./config/lpGBT/mix310.yelc -G 8
```
The configurations above are for the final detector according to the different data rates for different modules. If you only do the scanning test, for convenience, you can configure the data rate of all lpGBT eLinks to 320 Mbps by running the following command:
```
python3 initialization.py -F ./config/lpGBT/all_320M.yelc -d 0 -G <0/1//2/3/4/5/6/7/8>
```
Note: All above commands may not succeed at once, so if it fails, you need to run it again.

After above configuration, the front-end modules are powered on, now you can communicate with them through I2C bus.

You need too have a first time monitoring now, to find if there's anything wrong in temperature, GND, VDDA and VDDD:
```
python3 monitor_interested.py -G <0/1//2/3/4/5/6/7/8> > monitor_before_configure.txt
```
You need to pay attention to PEB-related monitor results -- if temperature makes sense, if GND almost equals 0, if VDDA and VDDD are not too low. At this stage, don't be so nervous if any ERROR found in altiroc monitoring results, they may fix after configuration.

Next step is to check the I2C bus is ok or not, you can try the following commands:
```
python3 i2c_check.py -d 0 -G <0/1//2/3/4/5/6/7/8>
```
The script i2c_check.py tries to read out some register values of the front-end modules, if any abnormal found, you will find a message looks like `!!!!!!!!!!!!!I2C wrong number, may need configuration!!!!!!!!!!`

2. Front-end module

Now need to configure modules for further tests:
```
python3 configure.py --pixelOn col7 --pixelInj col7 --dacCharge 24 -F ./config/altiroc/mix046.yelc -d 0 -G 0 <0/1//2/3/4/5/6/7/8>
```
--pixelOn: turn on the pixels, including PA, discriminator, TDC  
--pixelInj: pixels with internal charge injection  
--dacCharge: DAC value for the charge injection, here using large Ctest.  
-F: front-end module configuration file.  

A further I2C test should be done now:
```
python3 i2c_vth_address_check.py -G <0/1//2/3/4/5/6/7/8>
```
This script will first set vth to 0 for all chips and read the corresponding I2C adress value and ADC value, then configure vth to 800 chip by chip, in the meantime will read the corresponding I2C adress value and ADC value each time one chip is configured. Thus one can find each time one chip's value is changing, and in the end all chips' value are changed.

As the end of all the tests before scanning, you should make a second time of monitoring:
```
python3 monitor_interested.py -G <0/1//2/3/4/5/6/7/8> > monitor_after_configure.txt
```
You should pay attention to altiroc's monitor results this time, all important monitoring channel will automatically have a check on the output voltage, make sure you find `xxx is OK` all te time.

If you find any abnormal value, please write it down in your elog as a reference.

3. FELIX card

Enable 8b10b decoding mode:  
```
flx-config DECODING_HGTD_ALTIROC 1
```
Setting the IDLE fast command character. The default is for ALTIROC2. If you are running ALTIROC3, run the following command:
```
flx-config HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1
```
Set the latency between CAL trigger and L0/L1 trigger:
```
flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4
```
You can check all the configurable registers in FELIX card by running:
```
flx-config list |grep HGTD
```
# Scanning test
The scripts for scanning test are almost same with FADA scripts, the main difference is the way of front-end module configuration. For Demonstrator, we use FELIX, but for FADA, they use ZC706 FPGA.

In fact, the scan test is a process of repeatedly configuring the module and taking data. There are some .py scripts for scanning test in the folder path/hgtd-peb/script3 or path/hgtd-peb/script2, inlcuding vthScan_peb.py, vthcScan_peb.py, chargeScan_peb.py, delayScan_peb.py and widthScan_peb.py. Usually, you don not need to modify these scripts. When doing scanning test, we do modifications in the corresponding sh scripts and run them, including runVth.sh, runVthc.sh, runCharge.sh, runDelay.sh and runWidth.sh. For example:
1. Vthc scanning 
```
sh runVthc.sh 0 24 0 14 ./config/altiroc/t0_HV.yaml ./config/felix/t0_HV.yelc ./Measurements/coolTest/m10c
```
Before running this script, some modifications are needed in this line according to your test:
```
python3 vthcScan_peb.py -b $board --autoStop 1 --dacVthcMin 0 --dacVthcMax 175 --dacVthcStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --dacCharge $Q -F $moduleFile -d 0 -G 0 --elinkFile $elinkFile --dacVth 380
```
--autoStop: If true, the scanning will be stopped automatically when receiving nothing.  
--dacVthcMin: the minimum vthc DAC value for the scanning  
--dacVthcMax: the maximum vthc DAC value for the scanning  
--dacVthcStep: scanning step for vthc DAC  
--N: number of trigger, the setting should be keep same with triggerFre, because only taking data for 1 second for each vthc DAC  
--triggerFre: the frequency of trigger  
--startCol: the start coulumn to scan  
--endCol: the end column to scan  
-o: where you save the scanning data  
--dacVth: the Vth DAC value in your vthc scanning. It should be keep same with the front-end module configuration file.  
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

NOTE: if you want to scan nulti-channles at the same time, you can try the scripts whose name with "multiCH.py".

# Monitoring test
Downloading "lpgbt_calibration.csv" from [here](https://lpgbt.web.cern.ch/lpgbt/calibration/lpgbt_calibration_latest.zip) and moving it two "path/hgtd-peb/script3" and "path/hgtd-peb/script2".

Runing the following command accroding to the channel you want to test and all monitoring signals will be read out.
```
python3 monitor_all.py -G <0/1//2/3/4/5/6/7/8>
```
# Up-link eye-diagram scanning
1. Connecting the UPL with the Test pins (T0/L0-J11, T1/L1-J12, T2/J2-J287, T3-J10, T4-J284, T5-J286, T6-J9, T7-J285, T8-J283) on PEB 1F according the lpGBT you want to test.

<img src="./script3/config/UPL.jpg"  width="500">

2. Connecting the UPL with computer via USB and install the software according to [UPL reference](https://gitlab.cern.ch/atlas-hgtd/hgtd-peb/-/blob/script_altiroc3/script3/eye_scan/demon_scan/UPL/README.md?ref_type=heads).

3. Connecting the coresponding uplink optical fiber with oscilloscope.

<img src="./script3/config/uplink.jpg"  width="500">

<img src="./script3/config/scopeConnection.jpg"  width="500">


4. Runing the scanning script in folder "path/hgtd-peb/script3/eye_scan/demon_scan/script3/eye_scan"
```
python3 demon_eye_scan.py <your file name for saving results>
```
NOTE:  
You need to change the I2C address of lpGBT in line 310 according to the lpGBT you are testing, addr = 0x70 for timing lpGBT and addr = 0x71 for lumi lpGBT.  
You need to use the correct scope IP adress in line 328.  
You need to change the scanning parameter according to what you want to test in lines 376\~386.  
Besides, This script is used for the scope "Infiniium DSOV164A". If you are using other scope, you need to develop your own script to control the scope. 

# Scanning by steps

The scanning scripts above will do everything in one script, if you want to learn step by step, try the following examples:
```
python3 configure_bystep.py --triggerFre 50 --pixelOn col0 --pixelInj col0 --dacCharge 24 -F ./config/altiroc/mix046.yelc --elinkFile ./config/felix/peb_1f.yelc -d 0 -G 0
```
--triggerFre: L0/L1 trigger frequency, Hz  
--pixelOn: turn on the pixels, including PA, discriminator, TDC  
--pixelInj: pixels with internal charge injection  
--dacCharge: DAC value for the charge injection, here using large Ctest.  
-F: front-end module configuration file.  
--elinkFile: configuration file for FELIX card  

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
-T: determining the file name style for the received data. 

Disable the fast command
```
fttcemu -n
```
NOTE: you need to disable the fast command before next PEB/module configuration, otherwise the communication may be blocked.

Check the received data
```
fcheck <your file name> -F 100 -e 010
```
-F: the block number you want to check  
-e: the elink you want to check

# Troubleshooting

1. if report "OSError: libftd2xx.so: cannot open shared object file: No such file or directory", follow the instruction to install the usb driver for the UPL, https://gitlab.cern.ch/atlas-hgtd/hgtd-peb/-/tree/master/UPL

2. if too many ‘Write failure at address xxxx, and retry...’ occurs and finally end up with failure, try the followling methods one by one:

- Reduce noise
```
feconf config/FELIX/ic_ec_only.yelc
```
This command will close most of FELIX links except ic and ec to ensure basic communication, thus will have few noise in configuration.

- Initialize again
```
flx-init
```
Try this command several times to make environment clean enough

- Soft reboot FELIX
```
flx-reset ALL
```

- Reboot PEB power supply

reboot will save everything, right?

- Reboot FELIX

The last resort.

3. if ‘### Receiver@FLX0: FlxCard open: Some requested resources locked’ occurs, try the following steps one by one:
- Check if some jobs are working, if so, use `kill`
- Change a new terminal
- Check if using ‘use_serialcomm’ but not using ‘alti.byebye()’ before using FELIX command
- Reboot FELIX

# For developer
If you want to participate in developing this script template, just read [this](manual/developer.md).