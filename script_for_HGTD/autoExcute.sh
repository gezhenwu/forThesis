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




# for tot tuning###################################

# python3 initialization.py -p Mix046 -d 0 -G 0 -F ./config/lpGBT/Mix046_withLumi.yelc

# sh runVthc.sh 0 24 0 14 ./config/altiroc/t0_forHV.yaml ./config/felix/t0_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/

# for((m=9;m<14;m=m+1))
# do
# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/M$m/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/tot_tune/t0M$m/
# done

# sh runCharge.sh 0 0 14 ./config/altiroc/t0_forHV.yaml ./config/felix/t0_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/

# feconf ./config/felix/ic_ec_only.yelc

# python3 initialization.py -p Mix046 -d 0 -G 0

# python3 initialization.py -p Mix046 -d 0 -G 1 -F ./config/lpGBT/Mix046_withLumi.yelc

# sh runVthc.sh 1 24 0 14 ./config/altiroc/t1_forHV.yaml ./config/felix/t1_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/

# for((m=23;m<28;m=m+1))
# do
# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/M$m/vthcScan/B_1_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/tot_tune/t1M$m/
# done

# sh runCharge.sh 1 0 14 ./config/altiroc/t1_forHV.yaml ./config/felix/t1_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/

# feconf ./config/felix/ic_ec_only.yelc

# python3 initialization.py -p Mix046 -d 0 -G 1

# python3 initialization.py -p Mix046 -d 0 -G 2 -F ./config/lpGBT/Mix046_withLumi.yelc

# sh runVthc.sh 2 24 0 14 ./config/altiroc/t2_forHV.yaml ./config/felix/t2_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/

# for((m=37;m<42;m=m+1))
# do
# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/M$m/vthcScan/B_2_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/tot_tune/t2M$m/
# done

# sh runCharge.sh 2 0 14 ./config/altiroc/t2_forHV.yaml ./config/felix/t2_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/


# Plot charge #########################################
# for((c=0;c<2;c=c+1))
# do
#     #T0
#     for((m=9;m<14;m=m+1))
#     do
#         python3 anaCharge.py -i Measurements/receptionTest/hvOn_Q24/M${m}C${c}/chargeScan/B_0_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/receptionTest/tot_tune/t0M${m}/ --debug 1 --noLSBCor 1
#     done
#     #T1
#     for((m=23;m<28;m=m+1))
#     do
#         python3 anaCharge.py -i Measurements/receptionTest/hvOn_Q24/M${m}C${c}/chargeScan/B_1_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/receptionTest/tot_tune/t1M${m}/ --debug 1 --noLSBCor 1    
#     done
#     #T2
#     for((m=37;m<42;m=m+1))
#     do
#         python3 anaCharge.py -i Measurements/receptionTest/hvOn_Q24/M${m}C${c}/chargeScan/B_2_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/receptionTest/tot_tune/t2M${m}/ --debug 1 --noLSBCor 1    
#     done

# done


# sh runVth.sh  0 12 0 14 ./config/altiroc/t0_forHV_temp.yaml ./config/felix/t0_forHV.yelc ./Measurements/receptionTest/hvOn_Q12/



# sh runVthc.sh 0 24 0 14 ./config/altiroc/t0_forHV_temp.yaml ./config/felix/t0M9_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/oneModule/

# python3 makeEffCurve_ALTIROC3.py --module --input ./Measurements/receptionTest/hvOn_Q24/oneModule/M9/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir ./Plots/receptionTest/tot_tune/oneModule/t0M9/

# sh runCharge.sh 0 0 14 ./config/altiroc/t0_forHV_temp.yaml ./config/felix/t0M9_forHV.yelc ./Measurements/receptionTest/hvOn_Q24/oneModule/


<<<<<<< HEAD
sh runVthc.sh 0 24 0 14 ./config/altiroc/t2_HV.yaml ./config/felix/t2_HV.yelc ./Measurements/coolTest/m35c_col2

for((m=37;m<42;m=m+1))
do
   python3 makeEffCurve_ALTIROC3.py --module --input Measurements/coolTest/m35c_col2/M$m/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir Plots/coolTest/m35c_col2/M$m/
done

sh runCharge.sh 0 0 14 ./config/altiroc/t2_HV.yaml ./config/felix/t2_HV.yelc ./Measurements/coolTest/m35c_col2

for((c=0;c<2;c=c+1))
do
    for((m=37;m<42;m=m+1))
    do
        python3 anaCharge.py -i Measurements/coolTest/m35c_col2/M${m}C$c/chargeScan/B_0_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/coolTest/m35c_col2/M$m/ --debug 1 --noLSBCor 1
=======
# sh runVthc.sh 0 24 0 14 ./config/altiroc/t0_HV.yaml ./config/felix/t0_HV.yelc ./Measurements/coolTest/m35c_plate

# for((m=9;m<14;m=m+1))
# do
#    python3 makeEffCurve_ALTIROC3.py --module --input Measurements/coolTest/m35c_plate/M$m/vthcScan/B_0_On_col_Inj_col_N_50_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ --output-dir Plots/coolTest/m35c_plate/M$m/
# done

# sh runCharge.sh 0 0 14 ./config/altiroc/t0_HV.yaml ./config/felix/t0_HV.yelc ./Measurements/coolTest/m35c_plate

for((c=0;c<2;c=c+1))
do
    for((m=9;m<14;m=m+1))
    do
        python3 anaCharge.py -i Measurements/coolTest/m35c_plate/M${m}C$c/chargeScan/B_0_On_col_Inj_col_N_100_Vth_380_Cd_-1_cDel_8_fDel_9_Ctest_208_Q_24/ -o Plots/coolTest/m35c_plate/M$m/ --debug 1 --noLSBCor 1
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
    done
done
