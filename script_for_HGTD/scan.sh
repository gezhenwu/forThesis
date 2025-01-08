flx-config DECODING_HGTD_ALTIROC 1
sleep 0.1
flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1
sleep 0.1
flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 5
sleep 0.1

for((j=200;j<700;j=j+2))
do
    fttcemu -n
    sleep 0.5

    python3 scan_gzw_1.py $j -d 0 -G 1

    fttcemu -f 100
    sleep 0.5

    flx-config HGTD_ALTIROC_FASTCMD_GBRST 1
    sleep 0.1
    flx-config HGTD_ALTIROC_FASTCMD_GBRST 0
    sleep 0.1

    fdaq -t 1  ./rawData/vth${j} -T
    sleep 0.5

    for((i=0;i<14;i=i+1))
    do
        if [ $i -eq 6 ]; then
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 04a >> ./rawData/module${i}_vth${j}_04a.txt
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 04e >> ./rawData/module${i}_vth${j}_04e.txt
        fi
        if [ $i -eq 8 ]; then
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 050 >> ./rawData/module${i}_vth${j}_050.txt
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 054 >> ./rawData/module${i}_vth${j}_054.txt
        fi
        if [ $i -eq 9 ]; then
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 051 >> ./rawData/module${i}_vth${j}_051.txt
            fcheck ./rawData/vth${j}-1.dat -F 1000 -e 055 >> ./rawData/module${i}_vth${j}_055.txt
        fi
    done
    # rm ./rawData/*.dat
done
