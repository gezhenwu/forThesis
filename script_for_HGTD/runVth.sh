#! /bin/bash

# sh runVth.sh  1 12 0 14 ./config/altiroc/t1_forHV.yaml ./config/felix/t1_forHV.yelc ./Measurements/receptionTest/hvOn_Q12/


if [ $# = 7 ]; then
  board=$1
  Q=$2
  startCol=$3
  endCol=$4
  moduleFile=$5
  elinkFile=$6
  outDir=$7

else 
   echo '7 Arguments should be:   boardNumber, dacChrge, starCol, endCol, module cfg file, elink cfg file, output dir'
   exit 0
fi


echo "===================+> Board: "$board
echo "===================+> dacChrge: "$Q
echo "===================+> start column: "$startCol
echo "===================+> end Column: "$endCol
echo "===================+> moduleFile: "$moduleFile
echo "===================+> elinkFile: "$elinkFile
echo "===================+> outDir: "$outDir

python3 vthScan_peb.py -b $board --autoStop 1 --dacVthMin 200 --dacVthMax 600 --dacVthStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --dacCharge $Q -F $moduleFile -d 0 -G 1 --elinkFile $elinkFile --pattern Mix046 


