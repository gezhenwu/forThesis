# Examples  

Read all registers of lpGBTv1 (I2C address 0x70) connected to UPL 0:  
```
python3 fice.py -1 -G 0 -I 0x70
```
Read lpGBT register 0x20 (32):  
```
python3 fice.py -1 -G 0 -I 0x70 -a 0x20 (or: fice -1 -G 0 -I 0x70 -a 32)
```
Write 0xA5 to lpGBT register 32 (0x20):  
```
python3 fice.py -1 -G 0 -I 0x70 -a 32 0xA5
```
Write contents of config_min_timing.txt to lpGBT registers:
```
python3 fice.py -1 -G 0 -I 0x70 ./configFiles/v1/config_min_timing.txt
```

# Debug  
if the terminal reports "NACK"(shown below), the reason is the lpGBT I2C slave has timeout feature (1.6ms), which is explained at here(https://lpgbt-support.web.cern.ch/t/lpgbt-i2c-slave-timeout/695). The server CPU may be too busy to write the adjacent bytes within 1.6ms, which makes timeout. You may re-run the script, it will be possible to return to normal.

![](./figure/error.png)
