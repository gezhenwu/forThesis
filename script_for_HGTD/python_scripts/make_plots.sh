#!/usr/bin/bash
echo "$1"

mkdir $1
mkdir $1/threscan
mkdir $1/threscan/HVOn
mkdir $1/threscan/HVOff
mkdir $1/threscan/bumpConnection
mkdir $1/threscan_charge36_12
mkdir $1/threscan_charge36_12/charge_12
mkdir $1/threscan_charge36_12/bumpConnection
mkdir $1/TOT_TOA
mkdir $1/vthc

#threscan plots

python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_36  --module --output-dir $1/threscan/HVOn

python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_Off/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_36  --module --output-dir $1/threscan/HVOff

cp $1/threscan/HVOff/thresScan_threshold_list.csv $1/threscan/bumpConnection/thresScan_HV_Off_Q_36_threshold_list.csv
cp $1/threscan/HVOn/thresScan_threshold_list.csv $1/threscan/bumpConnection/thresScan_HV_On_Q_36_threshold_list.csv
python3 bump_connection.py --input $1/threscan/bumpConnection --output-dir $1/threscan/

#threscan_charge plots

python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_12  --module --output-dir $1/threscan_charge36_12/charge_12/

cp $1/threscan/HVOn/thresScan_threshold_list.csv $1/threscan_charge36_12/bumpConnection/thresScan_HV_On_Q_36_threshold_list.csv
cp $1/threscan_charge36_12/charge_12/thresScan_threshold_list.csv $1/threscan_charge36_12/bumpConnection/thresScan_HV_On_Q_12_threshold_list.csv
python3 bump_connection_Q.py --input $1/threscan_charge36_12/bumpConnection --output-dir $1/threscan_charge36_12/ --meas QdiffHvOn

#vthc plots

python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/vthcScan/B_None_On_all_Inj_col_N_100_Vth_380_Q_24  --module --output-dir $1/vthc

mkdir /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1

cp $1/vthc/asic1_vthc.txt /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1
cp $1/vthc/asic0_vthc.txt /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1

#TOT_TOA plots
#    python3 analyse_file.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/chargeScan/B_None_On_all_Inj_col_N_100_Vth_380_Q_12/pixelOn_col*_pixelInj_col*/timing_data_dacCharge_127.csv --output $1/TOT_TOA/


