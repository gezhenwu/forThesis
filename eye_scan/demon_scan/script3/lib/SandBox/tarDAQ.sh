dir=$1
dir2="~/ALTIROC/AllData/"
tar=$dir2$dir".tar.gz" 
echo $dir
echo $dir2
echo $tar

tar -zcf $tar $dir --remove-files

echo "rsync --progress -azr ~/ALTIROC/AllData/ makovec@lx3.lalin2p3.fr:DATA/HGTD/ALTIROC/TarBall/Data3/"

