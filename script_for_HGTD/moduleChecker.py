import pandas as pd
import os

timing_addr = 0x70
tryTimes = 1

moduleStatus = {
    "col1-asic0":{"S1":"ch0 -","S2":"ch0 -","S3":"ch0 -","S4":"ch0 -","S5":"ch0 -","S6":"ch0 -","S7":"ch0 -","S8":"ch0 -","S9":"ch0 -","S10":"ch0 -","S11":"ch3 -","S12":"ch3 -","S13":"ch3 -","S14":"ch6 -","S15":"ch3 -","S16":"ch3 -","S17":"ch6 -","S18":"ch6 -"},
    "col1-asic1":{"S1":"ch0 -","S2":"ch0 -","S3":"ch0 -","S4":"ch0 -","S5":"ch0 -","S6":"ch0 -","S7":"ch0 -","S8":"ch0 -","S9":"ch0 -","S10":"ch0 -","S11":"ch3 -","S12":"ch3 -","S13":"ch3 -","S14":"ch6 -","S15":"ch3 -","S16":"ch3 -","S17":"ch6 -","S18":"ch6 -"},
    "col2-asic0":{"S1":"ch1 -","S2":"ch1 -","S3":"ch1 -","S4":"ch1 -","S5":"ch1 -","S6":"ch1 -","S7":"ch1 -","S8":"ch1 -","S9":"ch1 -","S10":"ch1 -","S11":"ch4 -","S12":"ch4 -","S13":"ch4 -","S14":"ch4 -","S15":"ch4 -","S16":"ch6 -","S17":"ch7 -","S18":"ch7 -"},
    "col2-asic1":{"S1":"ch1 -","S2":"ch1 -","S3":"ch1 -","S4":"ch1 -","S5":"ch1 -","S6":"ch1 -","S7":"ch1 -","S8":"ch1 -","S9":"ch1 -","S10":"ch1 -","S11":"ch4 -","S12":"ch4 -","S13":"ch4 -","S14":"ch4 -","S15":"ch4 -","S16":"ch6 -","S17":"ch7 -","S18":"ch7 -"},
    "col3-asic0":{"S1":"ch2 -","S2":"ch2 -","S3":"ch2 -","S4":"ch2 -","S5":"ch2 -","S6":"ch2 -","S7":"ch2 -","S8":"ch2 -","S9":"ch2 -","S10":"ch2 -","S11":"ch5 -","S12":"ch5 -","S13":"ch5 -","S14":"ch5 -","S15":"ch5 -","S16":"ch7 -","S17":"ch8 -","S18":"ch8 -"},
    "col3-asic1":{"S1":"ch2 -","S2":"ch2 -","S3":"ch2 -","S4":"ch2 -","S5":"ch2 -","S6":"ch2 -","S7":"ch2 -","S8":"ch2 -","S9":"ch2 -","S10":"ch2 -","S11":"ch5 -","S12":"ch5 -","S13":"ch5 -","S14":"ch5 -","S15":"ch5 -","S16":"ch7 -","S17":"ch8 -","S18":"ch8 -"}
    }
df=pd.DataFrame(moduleStatus)

# cmd = "setupFLXcode"
# os.sys(cmd)
# cmd = "flx-init"
# os.system(cmd )
# cmd = "flx-config GBT_TX_RESET -0xfff"
# os.system(cmd )
# cmd = "flx-info link"
# flx = os.popen(cmd)
# reply = flx.read()
# print(reply)

FlxCh = []
alignStatus = ["No","No","No","No","No","No","No","No","No"]

for gbt in range(0,9):
    if gbt in [0,1,2]:
        cmd = "python3 ./initialization.py -p Mix046 -F ./config/lpGBT/Mix046_withLumi.yelc -d 0 -G " + str(gbt)
        print(cmd)
        for j in range(tryTimes):
            initiPEB = os.popen(cmd)
            reply = initiPEB.read()        
            if (-1==reply.find("Successful configuration")):            
                print("Channel %d is NOT succesfully configured"%gbt)
            else:
                alignStatus[gbt] = "Yes"
                print("Channel %d is succesfully configured"%gbt)

        from lib import peb_Mix046
        peb = peb_Mix046.peb(devnr = 0, gbt = gbt, addr = timing_addr)            
        for module in [0,2,4,6,8,9,10,11,12,13]:
            connected = 0
            for chip in range(0,2):
                try:
                    for reg in range(0x1000,0x1001):
                        temp = peb.module_i2c_read(
                            module_id = module,
                            chip_id = chip,
                            reg_address = reg,
                            read_len = 1
                        )
                        connected = 1
                except:
                    connected = 0
                if module == 0 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S10"] = "ch%d *"%gbt
                if module == 2 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S9"] = "ch%d *"%gbt
                if module == 4 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S8"] = "ch%d *"%gbt
                if module == 6 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S7"] = "ch%d *"%gbt
                if module == 8 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S6"] = "ch%d *"%gbt
                if module == 9 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S5"] = "ch%d *"%gbt
                if module == 10 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S4"] = "ch%d *"%gbt
                if module == 11 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S3"] = "ch%d *"%gbt
                if module == 12 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S2"] = "ch%d *"%gbt
                if module == 13 and connected == 1:
                    df["col%d-asic%d"%((gbt+1)%4,chip)]["S1"] = "ch%d *"%gbt
        peb.serialcomm.clear()

    if gbt in [3,4,5]:
        cmd = "python3 ./initialization.py -p Mix230 -F ./config/lpGBT/Mix230.yelc -d 0 -G " + str(gbt)
        print(cmd)
        for j in range(tryTimes):
            initiPEB = os.popen(cmd)
            reply = initiPEB.read()        
            if (-1==reply.find("Successful configuration")):
                print("Channel %d is NOT succesfully configured"%gbt)
            else:
                alignStatus[gbt] = "Yes"
                print("Channel %d is succesfully configured"%gbt)
        from lib import peb_Mix230
        peb = peb_Mix230.peb(devnr = 0, gbt = gbt, addr = timing_addr)
        for module in [0,4,8,10,12]:
            connected = 0
            for chip in range(0,2):
                try:
                    for reg in range(0x1000,0x1001):
                        temp = peb.module_i2c_read(
                            module_id = module,
                            chip_id = chip,
                            reg_address = reg,
                            read_len = 1
                        )
                        connected = 1
                except:
                    connected = 0

                if gbt in [4,5]:
                    if module == 0 and connected == 1:
                        df["col%d-asic%d"%(gbt-2,chip)]["S15"] = "ch%d *"%gbt
                    if module == 4 and connected == 1:
                        df["col%d-asic%d"%(gbt-2,chip)]["S14"] = "ch%d *"%gbt
                else:
                    if module == 0 and connected == 1:
                        df["col%d-asic%d"%(gbt-2,chip)]["S16"] = "ch%d *"%gbt
                    if module == 4 and connected == 1:
                        df["col%d-asic%d"%(gbt-2,chip)]["S15"] = "ch%d *"%gbt             
                if module == 8 and connected == 1:
                    df["col%d-asic%d"%(gbt-2,chip)]["S13"] = "ch%d *"%gbt
                if module == 10 and connected == 1:
                    df["col%d-asic%d"%(gbt-2,chip)]["S12"] = "ch%d *"%gbt
                if module == 12 and connected == 1:
                    df["col%d-asic%d"%(gbt-2,chip)]["S11"] = "ch%d *"%gbt
        peb.serialcomm.clear()

    if gbt in [6,7,8]:
        cmd = "python3 ./initialization.py -p Mix310 -F ./config/lpGBT/Mix310.yelc -d 0 -G " + str(gbt)
        print(cmd)
        for j in range(tryTimes):
            initiPEB = os.popen(cmd)
            reply = initiPEB.read()        
            if (-1==reply.find("Successful configuration")):
                print("Channel %d is NOT succesfully configured"%gbt)
            else:
                alignStatus[gbt] = "Yes"
                print("Channel %d is succesfully configured"%gbt)
        from lib import peb_Mix310
        peb = peb_Mix310.peb(devnr = 0, gbt = gbt, addr = timing_addr)            
        for module in [0,4,8,12]:
            connected = 0
            for chip in range(0,2):
                try:
                    for reg in range(0x1000,0x1001):
                        temp = peb.module_i2c_read(
                            module_id = module,
                            chip_id = chip,
                            reg_address = reg,
                            read_len = 1
                        )
                        connected = 1
                except:
                    connected = 0
                if gbt == 6:
                    if module == 0 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S18"] = "ch%d *"%gbt
                    if module == 4 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S17"] = "ch%d *"%gbt
                    if module == 8 and connected == 1:
                        df["col%d-asic%d"%(gbt-4,chip)]["S16"] = "ch%d *"%gbt
                    if module == 12 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S14"] = "ch%d *"%gbt
                if gbt == 7:
                    if module == 0 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S18"] = "ch%d *"%gbt
                    if module == 4 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S17"] = "ch%d *"%gbt
                    if module == 8 and connected == 1:
                        df["col%d-asic%d"%(gbt-4,chip)]["S16"] = "ch%d *"%gbt
                if gbt == 8:
                    if module == 4 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S18"] = "ch%d *"%gbt
                    if module == 8 and connected == 1:
                        df["col%d-asic%d"%(gbt-5,chip)]["S17"] = "ch%d *"%gbt
        peb.serialcomm.clear()

del peb
FlxCh.append(alignStatus)
alignment = pd.DataFrame(FlxCh)
print("\n lpGBT configuration status: \n")
print(alignment)
print("\n module connection status: \n")
print(df) 