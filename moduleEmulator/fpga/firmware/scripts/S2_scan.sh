
for((j=0;j<1024;j=j+1))
do
    fttcemu -n

    python3 scan_gzw_1.py $j

    fttcemu -f 100
    fdaq -t 1  vth${j} -T

    for((i=5;i<14;i=i+1))
    do
        if [ $i -eq 5 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 009 >> module${i}_vth${j}_009.txt
            fcheck vth${j}-1.dat -F 1000 -e 00d >> module${i}_vth${j}_00d.txt
        fi
        if [ $i -eq 6 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 00a >> module${i}_vth${j}_00a.txt
            fcheck vth${j}-1.dat -F 1000 -e 00e >> module${i}_vth${j}_00e.txt
        fi
        if [ $i -eq 7 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 00b >> module${i}_vth${j}_00b.txt
            fcheck vth${j}-1.dat -F 1000 -e 00f >> module${i}_vth${j}_00f.txt
        fi
        if [ $i -eq 8 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 010 >> module${i}_vth${j}_010.txt
            fcheck vth${j}-1.dat -F 1000 -e 014 >> module${i}_vth${j}_014.txt
        fi
        if [ $i -eq 9 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 011 >> module${i}_vth${j}_011.txt
            fcheck vth${j}-1.dat -F 1000 -e 015 >> module${i}_vth${j}_015.txt
        fi
        if [ $i -eq 10 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 012 >> module${i}_vth${j}_012.txt
            fcheck vth${j}-1.dat -F 1000 -e 016 >> module${i}_vth${j}_016.txt
        fi
        if [ $i -eq 11 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 013 >> module${i}_vth${j}_013.txt
            fcheck vth${j}-1.dat -F 1000 -e 017 >> module${i}_vth${j}_017.txt
        fi
        if [ $i -eq 12 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 018 >> module${i}_vth${j}_018.txt
            fcheck vth${j}-1.dat -F 1000 -e 01a >> module${i}_vth${j}_01a.txt
        fi
        if [ $i -eq 13 ]; then
            fcheck vth${j}-1.dat -F 1000 -e 019 >> module${i}_vth${j}_019.txt
            fcheck vth${j}-1.dat -F 1000 -e 01b >> module${i}_vth${j}_01b.txt
        fi
    done
    #rm *.dat
    #mv module*.txt $your_path/rawData_txt
done
