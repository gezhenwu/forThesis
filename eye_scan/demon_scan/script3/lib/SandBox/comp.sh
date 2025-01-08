ls Plots/*vthScan*Q_12*thres.npy|awk -FQ_12 '{print "python comp.py --ylabel Vth -i "$0" "$1"Q_24"$2" --doDiff 1 -n Q_12_thres_"$1" &"}' |zsh
ls Plots/*vthScan*Q_87*thres.npy|awk -FQ_87 '{print "python comp.py --reversed 1 --ylabel Vth -i "$0" "$1"Q_110"$2" --doDiff 1 -n Q_87_thres_"$1" &"}' |zsh

python comp.py -i Plots/comp_Q_87_thres_*npy -n vthScan_DeltaVth_87_110_thres  --ylabel "#Delta Vth(87,110)" --ymin 0 --ymax 100&
python comp.py -i Plots/comp_Q_12_thres_*npy -n vthScan_DeltaVth_12_24_thres  --ylabel "#DeltaVth(12,24)"&
python comp.py -i Plots/*width*lsb.npy --ylabel "TOT LSB (ext. discri) [ps]" -n widthScan_TOTLSB_extDiscri      --ymin 100 --ymax 220 &
python comp.py -i Plots/*delay*True*lsb.npy --ylabel "TOA LSB (ext. discri) [ps]" -n delayScan_TOALSB_extDiscri --ymin 0   --ymax  50 &
#python comp.py -i Plots/*delay*False*lsb.npy --ylabel "TOA LSB (pulser) [ps]" -n delayScan_TOALSB_pulser   --ymin 0   --ymax  50 &

python comp.py -i Plots/*vthScan*Q_12*thres.npy --ylabel "Vth [DACU]" -n vthScan_VTH_Q12   --ymin 0   --ymax  600 &
python comp.py -i Plots/*vthScan*Q_24*thres.npy --ylabel "Vth [DACU]" -n vthScan_VTH_Q24   --ymin 0   --ymax  600 &
python comp.py -i Plots/*vthScan*Q_87*thres.npy --ylabel "Vth [DACU]" -n vthScan_VTH_Q87   --ymin 0   --ymax  600 &
python comp.py -i Plots/*vthScan*Q_110*thres.npy --ylabel "Vth [DACU]" -n vthScan_VTH_Q110   --ymin 0   --ymax  600 &
python comp.py -i Plots/*vthScan*Q_12*noise.npy --ylabel "noise [DACU]" -n vthScan_NOISE_Q12   --ymin 0   --ymax  5 &
python comp.py -i Plots/*vthScan*Q_24*noise.npy --ylabel "noise [DACU]" -n vthScan_NOISE_Q24   --ymin 0   --ymax  5 &
python comp.py -i Plots/*vthScan*Q_87*noise.npy --ylabel "noise [DACU]" -n vthScan_NOISE_Q87   --ymin 0   --ymax  5 &
python comp.py -i Plots/*vthScan*Q_110*noise.npy --ylabel "noise [DACU]" -n vthScan_NOISE_Q110   --ymin 0   --ymax  5 &
python comp.py -i Plots/*vthScan*Q_87*slope.npy --ylabel "slope [DACU]" -n vthScan_SLOPE_Q87   --ymin 0   --ymax  0.2 &
python comp.py -i Plots/*vthScan*Q_110*slope.npy --ylabel "slope [DACU]" -n vthScan_SLOPE_Q110   --ymin 0   --ymax  0.2 &
python comp.py -i Plots/*vthcScan*Vth_380*thres.npy --ylabel "Vthc [DACU]" -n vthcScan_Vth_380   --ymin 0   --ymax  400 &
python comp.py -i Plots/*vthcScan*Vth_380*noise.npy --ylabel "Noise [DACU]" -n vthcScan_Noise_380   --ymin  0  --ymax  3 &

#list=( 380 384 
list=( 374 376 378 380 384)
for vth in "${list[@]}";
do
    echo $vth
    python comp.py -i Plots/*chargeScan*Vth_$vth*noise.npy --ylabel "Noise [fC]" -n chargeScan_NOISE_Vth_$vth   --ymin  0  --ymax  0.6 &
    python comp.py -i Plots/*chargeScan*Vth_$vth*thres.npy --ylabel "Thres. [fC]" -n chargeScan_THRES_Vth_$vth   --ymin  0  --ymax  7 &
    python comp.py -i Plots/*chargeScan*Vth_$vth*effQ0.996.npy --ylabel "eff Qinj=1fC" -n chargeScan_eff_1_fC_Vth_$vth   --ymin  0  --ymax  1.1 &
done



#charge scan 10fC
python comp.py -i Plots/*chargeScan*Vth_384*toaMean9.927200000000001.npy --ylabel "TOA [ps]" -n chargeScan_TOA_10fC_Vth_384   --ymin  0  --ymax  3600 &
python comp.py -i Plots/*chargeScan*Vth_384*toaRMS9.927200000000001.npy --ylabel "TOA RMS [ps]" -n chargeScan_TOARMS_10fC_Vth_384   --ymin  0  --ymax  160 &
python comp.py -i Plots/*chargeScan*Vth_384*totMean9.927200000000001.npy --ylabel "TOT [ps]" -n chargeScan_TOT_10fC_Vth_384   --ymin  0  --ymax  10000 &
python comp.py -i Plots/*chargeScan*Vth_384*totRMS9.927200000000001.npy --ylabel "TOT RMS [ps]" -n chargeScan_TOTRMS_10fC_Vth_384   --ymin  0  --ymax  650 &

# #charge scan 6fC
# python comp.py -i Plots/*chargeScan*Vth_374*toaMean6.024.npy --ylabel "TOA [ps]" -n chargeScan_TOA_6fC_Vth_374   --ymin  0  --ymax  3600 &
# python comp.py -i Plots/*chargeScan*Vth_374*toaRMS6.024.npy --ylabel "TOA RMS [ps]" -n chargeScan_TOARMS_6fC_Vth_374   --ymin  0  --ymax 160 &
# python comp.py -i Plots/*chargeScan*Vth_374*totMean6.024.npy --ylabel "TOT [ps]" -n chargeScan_TOT_6fC_Vth_374   --ymin  0  --ymax  10000 &
# python comp.py -i Plots/*chargeScan*Vth_374*totRMS6.024.npy --ylabel "TOT RMS [ps]" -n chargeScan_TOTRMS_6fC_Vth_374   --ymin  0  --ymax  650 &

# python comp.py -i Plots/*chargeScan*Vth_384*toaMean6.024.npy --ylabel "TOA [ps]" -n chargeScan_TOA_6fC_Vth_384   --ymin  0  --ymax  3600 &
# python comp.py -i Plots/*chargeScan*Vth_384*toaRMS6.024.npy --ylabel "TOA RMS [ps]" -n chargeScan_TOARMS_6fC_Vth_384   --ymin  0  --ymax 160 &
# python comp.py -i Plots/*chargeScan*Vth_384*totMean6.024.npy --ylabel "TOT [ps]" -n chargeScan_TOT_6fC_Vth_384   --ymin  0  --ymax  10000 &
# python comp.py -i Plots/*chargeScan*Vth_384*totRMS6.024.npy --ylabel "TOT RMS [ps]" -n chargeScan_TOTRMS_6fC_Vth_384    --ymin  0  --ymax  650 &


# #charge scan 4fC
# python comp.py -i Plots/*chargeScan*Vth_374*toaMean3.9848000000000003.npy --ylabel "TOA [ps]" -n chargeScan_TOA_4fC_Vth_374   --ymin  0  --ymax  3600 &
# python comp.py -i Plots/*chargeScan*Vth_374*toaRMS3.9848000000000003.npy --ylabel "TOA RMS [ps]" -n chargeScan_TOARMS_4fC_Vth_374   --ymin  0  --ymax 160 &
# python comp.py -i Plots/*chargeScan*Vth_374*totMean3.9848000000000003.npy --ylabel "TOT [ps]" -n chargeScan_TOT_4fC_Vth_374   --ymin  0  --ymax  10000 &
# python comp.py -i Plots/*chargeScan*Vth_374*totRMS3.9848000000000003.npy --ylabel "TOT RMS [ps]" -n chargeScan_TOTRMS_4fC_Vth_374   --ymin  0  --ymax  650 &

