sleep 3600

# fttcemu -n

# python3 configure_Mix046.py --dacCharge 20 --pixelOn all --pixelInj col0-8 -F ./config/altiroc/Mix046.yaml --elinkFile ./config/felix/threeModule.yelc -d 0 -G 2

# p3 i2c_check.py -d 0 -G 0 > reg_cfg.txt

# flx-config list |grep HGTD
(python_env) [user@localhost script]$ flx-config list |grep HGTD
0x2f90 [RW    00]                          DECODING_HGTD_ALTIROC                0x0  Set to 1 to use HGTD Altiroc K characters in the 8b10b decoders 
0x3ac0 [RW    14]             HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE                0x0  0 for ALTIROC2 10101100, 1 for ALTIROC3 11110000
0x3ac0 [RW    13]                   HGTD_ALTIROC_FASTCMD_USE_CAL                0x1  When set to 1, CAL will be sent on L1A, then after TRIG_DELAY 
0x3ac0 [RW    12]                  HGTD_ALTIROC_FASTCMD_SYNCLUMI                0x0  Set to 1 to trigger a SYNCLUMI command, rising edge of this bit. 
0x3ac0 [RW    11]                     HGTD_ALTIROC_FASTCMD_GBRST                0x0  Set to 1 to trigger a GBRST command, rising edge of this bit. 
0x3ac0 [RW 10:00]                HGTD_ALTIROC_FASTCMD_TRIG_DELAY              0x005  Number of BC clocks between CAL and TRIGGER command if USE_CAL 

#flx-config get DECODING_HGTD_ALTIROC HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE HGTD_ALTIROC_FASTCMD_USE_CAL HGTD_ALTIROC_FASTCMD_SYNCLUMI HGTD_ALTIROC_FASTCMD_GBRST HGTD_ALTIROC_FASTCMD_TRIG_DELAY

# flx-config DECODING_HGTD_ALTIROC 1
# flx-config  HGTD_ALTIROC_FASTCMD_ALTIROC3_IDLE 1
# flx-config  HGTD_ALTIROC_FASTCMD_USE_CAL 1
# flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4
# sleep 3
# flx-config HGTD_ALTIROC_FASTCMD_TRIG_DELAY 4

# flx-config HGTD_ALTIROC_FASTCMD_GBRST 1
# flx-config HGTD_ALTIROC_FASTCMD_GBRST 0


# upload elinkconfig
fttcemu -f 1000
fdaq -t 3 B2T1 -T
# fttcemu -f n
# feconf ./config/felix/ic_ec_only.yelc


# python3 configure_Mix046.py -d 0 -G 0 -F ./config/altiroc/Mix046.yaml --pixelOn col0 --dacVth 300 --dacCharge 100 --smallCtest 1 --timingRate 320 --enLumi 1 --pixelInj col0

