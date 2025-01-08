#!/usr/bin/env python
#encoding: utf-8
# Company:  CAS IHEP
# Engineer:  zhj_at_ihep.ac.cn
# 2021-10-22 created
import i2c
import sys
import ftd2xx as ftd

# device address
GPIO_ADDR   = 0x38

# TCA9554
# The Input Port register (register 0) reflects the incoming logic levels of the pins, regardless of whether the pin is
# defined as an input or an output by the Configuration register.
GPIO_IPR_ADDR = 0x0 # Input Port register, R
# The Output Port register (register 1) shows the outgoing logic levels of the pins defined as outputs by the
# Configuration register.
GPIO_OPR_ADDR = 0x1 # Output Port register, R/W
# The Polarity Inversion register (register 2) allows polarity inversion of pins defined as inputs by the Configuration
# register. If a bit in this register is set (written with 1), the corresponding port pin polarity is inverted.
GPIO_PIR_ADDR = 0x2 # Polarity Inversion register, R/W
# The Configuration register (register 3) configures the directions of the I/O pins. If a bit in this register is set to 1,
# the corresponding port pin is enabled as an input with a high-impedance output driver. If a bit in this register is
# cleared to 0, the corresponding port pin is enabled as an output.
GPIO_CR_ADDR  = 0x3 # Configuration register, R/W

PIN_MODE0     = 0b00000001  # in/out
PIN_MODE1     = 0b00000010  # in/out
PIN_MODE2     = 0b00000100  # in/out
PIN_MODE3     = 0b00001000  # in/out
PIN_RSTB      = 0b00010000  # out
PIN_READY     = 0b00100000  # in
PIN_EFUSEEN   = 0b01000000  # out
PIN_1V2ON     = 0b10000000  # in

PIN_S0        = 0b00000001  # out
PIN_S1        = 0b00000010  # out
PIN_S2        = 0b00000100  # out
PIN_S3        = 0b00001000  # out
PIN_S4        = 0b00010000  # out
PIN_S5        = 0b00100000  # out

class upl_scan(object): 
    def __init__(self):
        # Create the device list.
        num_devices = ftd.createDeviceInfoList()
        if (num_devices == 0):
            print("No device found.")
            sys.exit()
        # print("Found %d devices."%num_devices)

        # Get the device information for the device.
        device_info = None
        self.upl_list = []
        for index in range(num_devices):
            device_info = ftd.getDeviceInfoDetail(devnum = index, update = False)
            # print(device_info)
            if device_info['description'] == 'USB <-> Serial Converter' or device_info['description'] == b'Single RS232-HS':
                self.upl_list.append(index)

        if not self.upl_list:
            print("No device found.")
            sys.exit()
        # print("Found %d devices."%len(self.upl_list))

class upl(object):
    def __init__(self, dev = None, i2c_freq = 100):
        self.i2c = i2c.i2c(dev = dev, i2c_freq = i2c_freq)
        # GPIO Init
        self.i2c.writeChar(data=0, device_addr=GPIO_ADDR, internal_addr=GPIO_PIR_ADDR) # Polarity Inversion register, default: 0
        self.i2c.writeChar(data=PIN_RSTB|0xB, device_addr=GPIO_ADDR, internal_addr=GPIO_OPR_ADDR) # Output Port register, RSTB = 1, MODE = 0xB, others: 0; 
        self.i2c.writeChar(data=PIN_1V2ON|PIN_READY, device_addr=GPIO_ADDR, internal_addr=GPIO_CR_ADDR) # only PIN_EFUSEEN and PIN_RSTB are output    

    ##############################################################################################################
    # close device
    def close(self):
        self.i2c.close()

    ##############################################################################################################
    def write_regs(self, device_addr, addr_width, reg_addr, data): #here reg_addr should be a value while reg_vals should be a list with values
        self.i2c.writeBytes(data=bytes(data), device_addr=device_addr, internal_addr=reg_addr, internal_addr_length=addr_width)

    def read_regs(self, device_addr, addr_width, reg_addr, read_len):
        list = []
        data = self.i2c.readBytes(length=read_len, device_addr=device_addr, internal_addr=reg_addr, internal_addr_length=addr_width)
        for x in data:
            # list.append(int.from_bytes(x, "little"))
            list.append(int(x))
        return list

    ##############################################################################################################
    def gpio_read(self):
        return self.i2c.readChar(GPIO_ADDR, GPIO_IPR_ADDR, 1)

    def gpio_write(self, value):
        value &= 0xFF
        self.i2c.writeChar(value, GPIO_ADDR, GPIO_OPR_ADDR, 1)

    ##############################################################################################################
    # def mode_read(self):
    #     return (0xF & self.gpio_read())

    def mode_write(self, value):
        temp = 0xF0 & self.i2c.readChar(GPIO_ADDR, GPIO_OPR_ADDR, 1)
        temp |= (value & 0xF)
        # print("0x%x"%temp)
        self.gpio_write(temp)

    # def mode_output(self, enable = 1): 
    #     if(enable):
    #         temp = 0xF0 & self.i2c.readChar(GPIO_ADDR, GPIO_CR_ADDR, 1)
    #         # print("0x%x"%temp)
    #         self.i2c.writeChar(temp, GPIO_ADDR, GPIO_CR_ADDR, 1)
    #     else:
    #         temp = 0xF | self.i2c.readChar(GPIO_ADDR, GPIO_CR_ADDR, 1)
    #         print("0x%x"%temp)
    #         self.i2c.writeChar(temp, GPIO_ADDR, GPIO_CR_ADDR, 1)

    ##############################################################################################################
    def rstb_read(self):
        if (PIN_RSTB & self.gpio_read()):
            return 1
        else:
            return 0

    def rstb_high(self): # set to high
        temp = self.i2c.readChar(GPIO_ADDR, GPIO_OPR_ADDR, 1)
        temp |= PIN_RSTB
        self.gpio_write(temp)

    def rstb_low(self): # set to low
        temp = self.i2c.readChar(GPIO_ADDR, GPIO_OPR_ADDR, 1)
        temp &= ~PIN_RSTB & 0xFF
        self.gpio_write(temp)

    ##############################################################################################################
    def efuse_read(self):
        if (PIN_EFUSEEN & self.gpio_read()):
            return 1
        else:
            return 0

    def efuse_high(self): # set to high
        temp = self.i2c.readChar(GPIO_ADDR, GPIO_OPR_ADDR, 1)
        temp |= PIN_EFUSEEN
        self.gpio_write(temp)

    def efuse_low(self): # set to low
        temp = self.i2c.readChar(GPIO_ADDR, GPIO_OPR_ADDR, 1)
        temp &= ~PIN_EFUSEEN & 0xFF
        self.gpio_write(temp)

    ##############################################################################################################
    def ready_read(self):
        if (PIN_READY & self.gpio_read()):
            return 1
        else:
            return 0

    ##############################################################################################################
    def power1v2on_read(self):
        if (PIN_1V2ON & self.gpio_read()):
            return 1
        else:
            return 0