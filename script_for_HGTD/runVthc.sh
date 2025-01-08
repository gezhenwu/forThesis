#! /bin/bash

# sh runVthc.sh 0 24 0 14 ./config/altiroc/t2_HV.yaml ./config/felix/t2_HV.yelc ./Measurements/coolTest/p10c

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

echo "!!!!!!Make sure the Vth threshold has been set correctly in ./config/altiroc/MixABC.yaml!!!!!"

<<<<<<< HEAD
python3 vthcScan_peb.py -b $board --autoStop 1 --dacVthcMin 0 --dacVthcMax 200 --dacVthcStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --dacCharge $Q -F $moduleFile -d 0 -G 2 --elinkFile $elinkFile --pattern Mix046 --dacVth 380
=======
python3 vthcScan_peb.py -b $board --autoStop 1 --dacVthcMin 0 --dacVthcMax 200 --dacVthcStep 1 -N 50 --triggerFre 50 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir --dacCharge $Q -F $moduleFile -d 0 -G 1 --elinkFile $elinkFile --pattern Mix046 --dacVth 380
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2

#for t2: 0, 255
