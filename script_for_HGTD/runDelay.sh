#! /bin/bash

# sh runDelay.sh 0 0 14 ./config/altiroc/t0_forHV.yaml ./config/felix/t0_forHV.yelc ./Measurements/t0_320M/

if [ $# = 6 ]; then
  board=$1
  startCol=$2
  endCol=$3
  moduleFile=$4
  elinkFile=$5
  outDir=$6

else 
   echo '6 Arguments should be:   boardNumber, dacChargeStep, starCol, endCol, module cfg file, elink cfg file, output dir'
   exit 0
fi


echo "===================+> Board: "$board
echo "===================+> start column: "$startCol
echo "===================+> end Column: "$endCol
echo "===================+> moduleFile: "$moduleFile
echo "===================+> elinkFile: "$elinkFile
echo "===================+> outDir: "$outDir

echo "!!!!!!Make sure the Vth and Vthc threshold has been set correctly in ./config/altiroc/MixABC.yaml!!!!!"

python3 delayScan_peb.py -b $board --cDelayMin 0 --cDelayMax 15 --cDelayStep 1 --fDelayMin 0 --fDelayMax 15 --fDelayStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --ext_discri 1 --cDelay 0 -F $moduleFile -d 0 -G 1 --elinkFile $elinkFile --pattern Mix046 
