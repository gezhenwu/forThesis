import pyvisa
import traceback
import sys
import argparse
import time

#Power supply for fans: PL303, 192.168.1.201
FAN_NAME = 'TCPIP::192.168.1.201::9221::SOCKET' 
fan_1_ch = 1 
fan_1_vlt = 24.0
fan_1_amp = 1

fan_2_ch = 2 
fan_2_vlt = 24.0
fan_2_amp = 1

#Power supply for HV module: PL303, 192.168.1.200
#HV_NAME = 'TCPIP::172.17.1.62::9221::SOCKET' 
HV_NAME = 'TCPIP::LVforHV::9221::SOCKET' 
HV_1_ch = 1 
HV_1_vlt = 24.0
HV_1_amp = 3

HV_2_ch = 2 
HV_2_vlt = 24.0
HV_2_amp = 3

#Power supply for PEB LV0: tsx1820, 192.168.1.100
#LV0_NAME = 'TCPIP::172.17.1.60::9221::SOCKET'
LV0_NAME = 'TCPIP::LV0forPEB::9221::SOCKET'
LV0_1_ch = 1 
LV0_1_vlt = 11.0
LV0_1_amp = 10.0

#Power supply for PEB LV1: tsx1820, 192.168.1.101
#LV1_NAME = 'TCPIP::172.17.1.61::9221::SOCKET'
LV1_NAME = 'TCPIP::LV1forPEB::9221::SOCKET'
LV1_1_ch = 1 
LV1_1_vlt = 11.0
LV1_1_amp = 10.0

# time (s) to delay
delay = 0.1

def powerUp(device, channel, voltage, current):
    rm = pyvisa.ResourceManager()
    PowerSupply = rm.open_resource(device, read_termination='\r') # use your dedicated device name

    setVoltageCmd = 'V{ch} {vtg}'
    PowerSupply.write(setVoltageCmd[:].format(ch=channel, vtg=voltage))
    print("Setting channel {ch} to {volt}V".format(ch=channel, volt=voltage))
    time.sleep(delay)

    setCCCmd = 'I{ch} {amp}'
    PowerSupply.write(setCCCmd[:].format(ch=channel, amp=current))
    print("Setting channel {ch} to {amp}A current limit".format(ch=channel, amp=current))
    time.sleep(delay)

    setOffCmd = 'OP{ch} 1'
    PowerSupply.write(setOffCmd[:].format(ch=channel))
    print("Turning channel{ch} ON".format(ch=channel))

    PowerSupply.close()

def powerDown(device, channel):
    rm = pyvisa.ResourceManager()
    PowerSupply = rm.open_resource(device, read_termination='\r') # use your dedicated device name

    setOffCmd = 'OP{ch} 0'
    PowerSupply.write(setOffCmd[:].format(ch=channel))

    print("Turning channel{ch} OFF".format(ch=channel))

    PowerSupply.close()

def getPowerStatus(device, channel):
    rm = pyvisa.ResourceManager()
    PowerSupply = rm.open_resource(device, read_termination='\r') # use your dedicated device name

    queryStatusCmd = 'OP{ch}?'
    queryVoltageCmd = 'V{ch}O?'
    queryCurrentCmd = 'I{ch}O?'

    status = PowerSupply.query(queryStatusCmd[:].format(ch=channel))
    voltage = PowerSupply.query(queryVoltageCmd[:].format(ch=channel))
    current = PowerSupply.query(queryCurrentCmd[:].format(ch=channel))

    if int(status) == 0:
        status = "OFF"
    else:
        status = "ON:\t" + current.strip('\n') + "\t@ " + voltage.strip('\n')

    print("Channel{ch}:".format(ch=channel), status)
    PowerSupply.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Choose if you want to power on or off the PSU")
    parser.add_argument('--ON', default=False, action="store_true",
                      help="Turn PSU on")
    parser.add_argument('--OFF', default=False, action="store_true",
                      help="Turn PSU off")
    parser.add_argument('--Status', '-s', default=False, action="store_true",
                      help="Read PSU status")

    # parse args
    args = parser.parse_args()

    if (args.ON and not args.OFF and not args.Status):
        #step 1: turn on the fans
        #print("Turn on fan 1: ")
        #powerUp(FAN_NAME, fan_1_ch, fan_1_vlt, fan_1_amp)
        #print("Turn on fan 2: ")
        #powerUp(FAN_NAME, fan_2_ch, fan_2_vlt, fan_2_amp)
        #step 2: power on the PEB
        print("Power on PEB LV0: ")
        powerUp(LV0_NAME, LV0_1_ch, LV0_1_vlt, LV0_1_amp) 
        print("Power on PEB LV1: ")    
        powerUp(LV1_NAME, LV1_1_ch, LV1_1_vlt, LV1_1_amp)
        #step 3: turn on the HV
<<<<<<< HEAD
        # print("Turn on HV 1: ")
        # powerUp(HV_NAME, HV_1_ch, HV_1_vlt, HV_1_amp)
        # print("Turn on HV 2: ")
        # powerUp(HV_NAME, HV_2_ch, HV_2_vlt, HV_2_amp)
    elif(args.OFF and not args.ON and not args.Status):
        #step 1: turn off the HV
        # print("Turn off HV 1: ")
        # powerDown(HV_NAME, HV_1_ch)
        # print("Turn off HV 2: ")
        # powerDown(HV_NAME, HV_2_ch)
=======
        print("Turn on HV 1: ")
        powerUp(HV_NAME, HV_1_ch, HV_1_vlt, HV_1_amp)
        print("Turn on HV 2: ")
        powerUp(HV_NAME, HV_2_ch, HV_2_vlt, HV_2_amp)
    elif(args.OFF and not args.ON and not args.Status):
        #step 1: turn off the HV
        print("Turn off HV 1: ")
        powerDown(HV_NAME, HV_1_ch)
        print("Turn off HV 2: ")
        powerDown(HV_NAME, HV_2_ch)
>>>>>>> c43e174cfb626d13d64e2993367c0412d654a4f1
        #step 2: turn off the PEB 
        print("Power off PEB LV0: ")       
        powerDown(LV0_NAME, LV0_1_ch)
        print("Power off PEB LV1: ")
        powerDown(LV1_NAME, LV1_1_ch)
        #step 2: turn off the fans
        #print("Turn off fan 1: ")
        #powerDown(FAN_NAME, fan_1_ch)
        #print("Turn off fan 2: ")
        #powerDown(FAN_NAME, fan_2_ch)
        time.sleep(delay)
    elif(args.Status and not args.ON and not args.OFF):
        print("PEB LV0: ")
        getPowerStatus(LV0_NAME, LV0_1_ch)
        print("PEB LV1: ")
        getPowerStatus(LV1_NAME, LV1_1_ch) 
        print("HV1: ")
<<<<<<< HEAD
        # getPowerStatus(HV_NAME, HV_1_ch)
        # getPowerStatus(HV_NAME, HV_2_ch) 
=======
        getPowerStatus(HV_NAME, HV_1_ch)
        getPowerStatus(HV_NAME, HV_2_ch) 
>>>>>>> c43e174cfb626d13d64e2993367c0412d654a4f1
        #print("Fan 1: ")
        #getPowerStatus(FAN_NAME, fan_1_ch)
        #getPowerStatus(FAN_NAME, fan_2_ch)
        time.sleep(delay)
    else:
        print("ERROR, decide if you want to turn the PSU ON or OFF")
