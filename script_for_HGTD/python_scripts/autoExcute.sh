
#python3 vthScan_peb_multiCH.py -b 12 --autoStop 1 --dacVthMin 225 --dacVthMax 575 --dacVthStep 1 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 --dacCharge 36 --triggerFre 50 -N 50 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/t1t2_forHV.yelc -o ./Measurements/receptionTest/hvOn_Q36/

#python3 vthcScan_peb_multiCH.py -b 12 --autoStop 1 --dacVthcMin 50 --dacVthcMax 200 --dacVthcStep 1 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 --dacCharge 24 --triggerFre 50 -N 50 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/t1t2_forHV.yelc -o ./Measurements/receptionTest/hvOn_Q24/ --dacVth 380

#change altiroc configuration file: VTHC file


#for((m=24;m<28;m=m+1))
#do
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/t1M${m}/vthcScan/B_12_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/hvOn_Q24/t1M${m}/
#done

#for((m=28;m<37;m=m+2))
#do
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/t2M${m}/vthcScan/B_12_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/hvOn_Q24/t2M${m}/
#done

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/t2M37/vthcScan/B_12_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/hvOn_Q24/t2M37/

#python3 chargeScan_peb_multiCH.py -b 12 --autoStop 1 --dacChargeMin 0 --dacChargeMax 63 --dacChargeStep 1 -N 100 --triggerFre 100 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/t1t2_forHV.yelc -o ./Measurements/receptionTest/hvOn_Q24/ --dacVth 380

#power off HV

#python3 vthScan_peb_multiCH.py -b 12 --autoStop 1 --dacVthMin 200 --dacVthMax 600 --dacVthStep 1 --pixelOn col0 --pixelInj col0 --startCol 0 --endCol 14 --dacCharge 36 --triggerFre 50 -N 50 -F ./config/altiroc/module_peb_1f.yaml --elinkFile ./config/felix/t1t2_forHV.yelc -o ./Measurements/receptionTest/hvOff_Q36/






# for((m=9;m<=13;m=m+1))
# do
#  python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/M$m/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/hvOn_Q24/M$m/
# done

# sh runCharge.sh 0 0 14 ./config/altiroc/t0_forHV.yaml ./config/felix/t0_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/



#for diffCharge_hvOn#######################################################
#for((m=9;m<14;m=m+1))
#do
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/M${m}/thresScan/B_0_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/M${m}

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q12/M${m}/thresScan/B_0_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_12/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/M${m}   #in fact here is HV_On_Q_12

#python3 bump_connection.py --input-folder ./Plots/receptionTest/diffCharge_hvOn/M${m}/ --output-dir ./Plots/receptionTest/diffCharge_hvOn/M${m} --upper-thresh 65 --conn-thresh 40
#done

#for((m=24;m<28;m=m+1))
#do
#for diffCharge_hvOn
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t1M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t1M${m}

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q12/t1M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_12/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t1M${m}   #in fact here is HV_On_Q_12

#python3 bump_connection.py --input-folder ./Plots/receptionTest/diffCharge_hvOn/t1M${m}/ --output-dir ./Plots/receptionTest/diffCharge_hvOn/t1M${m} --upper-thresh 65 --conn-thresh 40
#done

#for((m=28;m<37;m=m+2))
#do
#for diffCharge_hvOn
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t2M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M${m}

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q12/t2M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_12/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M${m}   #in fact here is HV_On_Q_12

#python3 bump_connection.py --input-folder ./Plots/receptionTest/diffCharge_hvOn/t2M${m}/ --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M${m} --upper-thresh 65 --conn-thresh 40
#done

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t2M37/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M37

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q12/t2M37/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_12/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M37   #in fact here is HV_On_Q_12

#python3 bump_connection.py --input-folder ./Plots/receptionTest/diffCharge_hvOn/t2M37/ --output-dir ./Plots/receptionTest/diffCharge_hvOn/t2M37 --upper-thresh 65 --conn-thresh 40
##################################################

#for ON - OFF#####################################
#for(m=9;m<14;m=m+1))
#do
#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/M${m}/thresScan/B_0_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/M${m}

#python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOff_Q36/M${m}/thresScan/B_0_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/M${m}

#python3 bump_connection.py --input-folder ./Plots/receptionTest/hvOn-Off/M${m}/ --output-dir ./Plots/receptionTest/hvOn-Off/M${m} --upper-thresh 35
#done

# for((m=24;m<28;m=m+1))
# do
# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t1M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t1M${m}

# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOff_Q36/t1M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t1M${m}

# python3 bump_connection.py --input-folder ./Plots/receptionTest/hvOn-Off/t1M${m}/ --output-dir ./Plots/receptionTest/hvOn-Off/t1M${m} --upper-thresh 35
# done

# for((m=28;m<37;m=m+2))
# do
# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t2M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t2M${m}

# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOff_Q36/t2M${m}/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t2M${m}

# python3 bump_connection.py --input-folder ./Plots/receptionTest/hvOn-Off/t2M${m}/ --output-dir ./Plots/receptionTest/hvOn-Off/t2M${m} --upper-thresh 35
# done

# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q36/t2M37/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_On_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t2M37

# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOff_Q36/t2M37/thresScan/B_12_On_col_Inj_col_N_50_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_36/ --prefix HV_Off_Q_36 --output-dir ./Plots/receptionTest/hvOn-Off/t2M37

# python3 bump_connection.py --input-folder ./Plots/receptionTest/hvOn-Off/t2M37/ --output-dir ./Plots/receptionTest/hvOn-Off/t2M37 --upper-thresh 35



##############################################################


#for tot tuning
#for((a=0;a<2;a=a+1))
#do
# python3 makeEffCurve_ALTIROC3.py --module --input /Measurements/receptionTest/hvOn_Q24/M${m}C${a}/chargeScan/B_0_On_col_Inj_col_N_100_Vth_0_Cd_-1_cDel_8_fDel_9_Ctest_26_/  --output-dir ./Plots/receptionTest/tot_tune/t0M${m}/

#python3 anaCharge.py -i Measurements/receptionTest/hvOn_Q24/M${m}C${a}/chargeScan/B_0_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_/ -o Plots/receptionTest/tot_tune/t0M${m}/ --debug 1 --noLSBCor 1
#done


#done


#sh runVth.sh  0 36 0 14 ./config/altiroc/t0_forHV.yaml ./config/felix/t0_forHV.yelc ./Measurements/receptionTest/hvOff_Q36/





#ZC706 analysis scripts########################
for((i=9;i<=13;i=i+1))
do
python3 bump_connection_Q.py --input ../Plots/receptionTest/diffCharge_hvOn/M$i/ --output-dir ../Plots/receptionTest/diffCharge_hvOn/M$i/ --meas QdiffHvOn
done

for((i=24;i<28;i=i+1))
do
python3 bump_connection_Q.py --input ../Plots/receptionTest/diffCharge_hvOn/t1M$i/ --output-dir ../Plots/receptionTest/diffCharge_hvOn/t1M$i/ --meas QdiffHvOn
done

for((i=28;i<37;i=i+2))
do
python3 bump_connection_Q.py --input ../Plots/receptionTest/diffCharge_hvOn/t2M$i/ --output-dir ../Plots/receptionTest/diffCharge_hvOn/t2M$i/ --meas QdiffHvOn
done

python3 bump_connection_Q.py --input ../Plots/receptionTest/diffCharge_hvOn/t2M37/ --output-dir ../Plots/receptionTest/diffCharge_hvOn/t2M37/ --meas QdiffHvOn 

















# #!/usr/bin/bash
# echo "$1"

# mkdir $1
# mkdir $1/threscan
# mkdir $1/threscan/HVOn
# mkdir $1/threscan/HVOff
# mkdir $1/threscan/bumpConnection
# mkdir $1/threscan_charge36_12
# mkdir $1/threscan_charge36_12/charge_12
# mkdir $1/threscan_charge36_12/bumpConnection
# mkdir $1/TOT_TOA
# mkdir $1/vthc

# #threscan plots

# python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_36  --module --output-dir $1/threscan/HVOn

# python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_Off/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_36  --module --output-dir $1/threscan/HVOff

# cp $1/threscan/HVOff/thresScan_threshold_list.csv $1/threscan/bumpConnection/thresScan_HV_Off_Q_36_threshold_list.csv
# cp $1/threscan/HVOn/thresScan_threshold_list.csv $1/threscan/bumpConnection/thresScan_HV_On_Q_36_threshold_list.csv
# python3 bump_connection.py --input $1/threscan/bumpConnection --output-dir $1/threscan/

# #threscan_charge plots
# python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/thresScan/B_None_On_col_Inj_col_N_100_Vth_380_Q_12  --module --output-dir $1/threscan_charge36_12/charge_12/

# cp $1/threscan/HVOn/thresScan_threshold_list.csv $1/threscan_charge36_12/bumpConnection/thresScan_HV_On_Q_36_threshold_list.csv
# cp $1/threscan_charge36_12/charge_12/thresScan_threshold_list.csv $1/threscan_charge36_12/bumpConnection/thresScan_HV_On_Q_12_threshold_list.csv
# python3 bump_connection_Q.py --input $1/threscan_charge36_12/bumpConnection --output-dir $1/threscan_charge36_12/ --meas QdiffHvOn

# #vthc plots

# python3 makeEffCurve_ALTIROC3_FADAPro.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/vthcScan/B_None_On_all_Inj_col_N_100_Vth_380_Q_24  --module --output-dir $1/vthc

# mkdir /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1

# cp $1/vthc/asic1_vthc.txt /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1
# cp $1/vthc/asic0_vthc.txt /home/module-qa/Documents/ModuleTest/FADAPro/fadapro/config/vthc/$1

# #TOT_TOA plots
# #    python3 analyse_file.py --input /home/module-qa/Documents/ModuleTest/Measurements/FastFadaMeasurements/Measurements2ASIC/$1_Hv_On_90/chargeScan/B_None_On_all_Inj_col_N_100_Vth_380_Q_12/pixelOn_col*_pixelInj_col*/timing_data_dacCharge_127.csv --output $1/TOT_TOA/
