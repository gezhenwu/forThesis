import os
import time

alginment = False
i = 0
while alginment is False:    
    i = i+1
    if i%10 == 0:
        print(i)
        os.system('python3 ../../t0_powerControl_LV.py --OFF')
        time.sleep(1)
        os.system('python3 ../../t0_powerControl_LV.py --ON')
    cmd = "flx-info link"
    flx = os.popen(cmd)
    reply = flx.read()
    print(reply)
    if (-1==reply.find("Aligned | YES  YES  YES  YES  YES  YES  YES  YES  YES")):
        os.system('flx-init')
        time.sleep(1)
    else:
        alginment = True
        print("9 channels are aligned")
        
