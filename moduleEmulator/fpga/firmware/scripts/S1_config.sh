fttcemu -n

#config digital module or emulator
for((i=5;i<14;i=i+1)) 
do
    python3 configure.py /home/user/zhenwu/altiroc/m$i.yaml --pixelInj 0 --dacCharge 12 --dacVth 0
done

flx-config DECODING_HGTD_ALTIROC 1

sh scan.sh