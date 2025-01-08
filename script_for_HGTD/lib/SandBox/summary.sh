
board=-1
if [ $# = 1 ]; then
  board=$1
fi

echo $board

#rm -rf Plots/*Inj_col*

python SandBox/catData.py |sh

python SandBox/chargeSummaryVsCharge.py -b $board &
python SandBox/chargeSummaryVsThres.py -b $board &




list=( 374 376 378 380 384)
for vth in "${list[@]}";
do
python comp.py -i Plots/*chargeScan*$vth*thres.npy --doDiff 1 --ylabel thres -n thres_$vth
python SandBox/compNPZ.py -i Plots/TOTO_B_*toaps_vs_Q*$vth* -n toaps_vs_Q_$vth  --xlabel "Charge [fC]" --ylabel "TOA [ps]" --xmin 3.5 --xmax 20  --ymin 0 --ymax 2000&
python SandBox/compNPZ.py -i Plots/TOTO_B_*jitter*$vth* -n jitter_$vth  --xlabel "Charge [fC]" --ylabel "Jitter [ps]"  --xmin 3.5 --xmax 20 --ymin 0 --ymax 100&
python SandBox/compNPZ.py -i Plots/TOTO_B_*totps_vs_QfC*$vth* -n totps_$vth --xlabel "Charge [fC]" --ylabel "TOT  [ps]"   --xmin 3.5 --xmax 20 --ymin 0 --ymax 5000&
python SandBox/compNPZ.py -i Plots/TOTO_B_*totRMSps*$vth* -n totRMSps_$vth --xlabel "Charge [fC]" --ylabel "TOT RMS [ps]" --xmin 3.5 --xmax 20  --ymin 0 --ymax 250&
done
