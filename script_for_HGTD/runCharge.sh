#! /bin/bash

# sh runCharge.sh 0 0 14 ./config/altiroc/t2_HV.yaml ./config/felix/t2_HV.yelc ./Measurements/coolTest/p10c


if [ $# = 6 ]; then
  board=$1
  startCol=$2
  endCol=$3
  moduleFile=$4
  elinkFile=$5
  outDir=$6

else 
   echo '6 Arguments should be:   boardNumber, starCol, endCol, module cfg file, elink cfg file, output dir'
   exit 0
fi


echo "===================+> Board: "$board
echo "===================+> start column: "$startCol
echo "===================+> end Column: "$endCol
echo "===================+> moduleFile: "$moduleFile
echo "===================+> elinkFile: "$elinkFile
echo "===================+> outDir: "$outDir

echo "!!!!!!Make sure the Vth and Vthc threshold has been set correctly in ./config/altiroc/MixABC.yaml!!!!!"

<<<<<<< HEAD
python3 chargeScan_peb.py -b $board --autoStop 1 --dacChargeMin 0 --dacChargeMax 63 --dacChargeStep 1 -N 100 --triggerFre 100 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir -F $moduleFile -d 0 -G 2 --elinkFile $elinkFile --pattern Mix046 --dacVth 380 --dacCharge 24
=======
python3 chargeScan_peb.py -b $board --autoStop 1 --dacChargeMin 0 --dacChargeMax 63 --dacChargeStep 1 -N 100 --triggerFre 100 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir -F $moduleFile -d 0 -G 1 --elinkFile $elinkFile --pattern Mix046 --dacVth 380 --dacCharge 24

# python3 convert.py -b $board --autoStop 1 --dacChargeMin 0 --dacChargeMax 63 --dacChargeStep 1 -N 100 --triggerFre 100 --pixelOn col$startCol --pixelInj col$startCol --startCol $startCol --endCol $endCol -o $outDir -F $moduleFile -d 0 -G 1 --elinkFile $elinkFile --pattern Mix046 --dacVth 380 --dacCharge 24
>>>>>>> 4cf58c88179a9dbfdf086443337f5e5358a75ba2
