#!/usr/bin/env python
#encoding: utf-8
# Company:  CAS IHEP
# Engineer:  zhj_at_ihep.ac.cn
# 2021-10-22 created
import ft232h
# import sys

# I2C
I2C_GIVE_ACK            = 1
I2C_GIVE_NACK           = 0
I2C_TIMEOUT             = -1

I2C_ADDRESS_READ_MASK   = 0x01  # LSB 1 = Read
I2C_ADDRESS_WRITE_MASK  = 0xFE  # LSB 0 = Write

class i2c(object):
    """Class for communicating with an I2C device using the adafruit-pureio pure
    python smbus library, or other smbus compatible I2C interface. Allows reading
    and writing 8-bit, 16-bit, and bytes array to registers
    on the device."""
    def __init__(self, dev = None, i2c_freq = 100):
        self.fh232h = ft232h.ft232h(dev = dev, i2c_freq = i2c_freq)

    ##############################################################################################################
    # close device
    def close(self):
        self.fh232h.close()

    ##############################################################################################################
    # write
    def writeChar(self, data, device_addr, internal_addr = 0, internal_addr_length = 1):
        # Write an 8-bit data to the specified register. The internal_addr LSB first
        data &= 0xFF
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(data): # write data byte
            # print("Write data, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write data, return NACK") 
            return
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)

    def writeShort(self, data, device_addr, internal_addr = 0, internal_addr_length = 1, little_endian=1):
        # Write a 16-bit data to the specified register. The internal_addr LSB first
        if little_endian:
            data &= 0xFFFF
        else:
            data = ((data << 8) & 0xFF00) | ((data >> 8) & 0x00FF)
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(data&0xFF): # write data
            # print("Write first data, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write first data, return NACK") 
            return
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK((data>>8)&0xFF): # write data
            # print("Write second data, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write second data, return NACK") 
            return
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)

    def writeBytes(self, data, device_addr, internal_addr = 0, internal_addr_length = 1):
        # Write bytes array to the specified register. The internal_addr LSB first
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        for i in range(len(data)):
            # print(data[i])
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(data[i]): # write data
                # print("Write data, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write data, return NACK") 
                return
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)

    ###########################################################################
    # read
    def readChar(self, device_addr, internal_addr = 0, internal_addr_length = 1):
        # Read an 8-bit value on the bus from register
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        self.fh232h.SetI2CLinesIdle() # the 2 statements used together as start signal
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 | I2C_ADDRESS_READ_MASK): # write device address again
            # print("Write device address for read, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write device address for read, return NACK") 
            return
        DataRead = self.fh232h.ReadByteAndSendACK(ack=I2C_GIVE_NACK)
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)
        return DataRead

    def readShort(self, device_addr, internal_addr = 0, internal_addr_length = 1, little_endian=1):
        # Read an unsigned 16-bit value from the specified register, with the
        # specified endianness (default little endian, or least significant byte first).
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        self.fh232h.SetI2CLinesIdle() # the 2 statements used together as start signal
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 | I2C_ADDRESS_READ_MASK): # write device address again
            # print("Write device address for read, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write device address for read, return NACK") 
            return
        ByteData0 = self.fh232h.ReadByteAndSendACK(ack=I2C_GIVE_ACK)
        # print(ByteData0)
        ByteData1 = self.fh232h.ReadByteAndSendACK(ack=I2C_GIVE_NACK)
        # print(ByteData1)
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)
        DataRead = ByteData1 << 8 | ByteData0
        # print(DataRead)
        # Swap bytes if using big endian because read_word_data assumes little
        # endian on ARM (little endian) systems.
        if little_endian:
            return DataRead
        else:
            DataRead = ((DataRead << 8) & 0xFF00) | ((DataRead >> 8) & 0x00FF)
            return DataRead
        
    def readBytes(self, length, device_addr, internal_addr = 0, internal_addr_length = 1):
        # Read a length number of bytes from the specified register.  
        # Results will be returned as bytes.
        device_addr &= 0xFF 
        self.fh232h.SetLed(1)
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 & I2C_ADDRESS_WRITE_MASK): # write device address
            # print("Device 0x%x is not found"%device_addr)
            self.fh232h.SetI2CStop()
            raise Exception("Device 0x%x is not found"%device_addr) 
            return
        for i in range(internal_addr_length):
            addr = internal_addr & 0xFF
            internal_addr = internal_addr >> 8
            if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(addr): # write internal address
                # print("Write internal address, return NACK")
                self.fh232h.SetI2CStop()
                raise Exception("Write internal address, return NACK") 
                return
        self.fh232h.SetI2CLinesIdle() # the 2 statements used together as start signal
        self.fh232h.SetI2CStart()
        if I2C_GIVE_ACK != self.fh232h.SendByteAndCheckACK(device_addr<<1 | I2C_ADDRESS_READ_MASK): # write device address again
            # print("Write device address for read, return NACK")
            self.fh232h.SetI2CStop()
            raise Exception("Write device address for read, return NACK") 
            return
        ByteData = bytes([0])
        while length>1:
            ByteData += bytes([self.fh232h.ReadByteAndSendACK(ack=I2C_GIVE_ACK)])
            # print(ByteData)
            length -= 1
        ByteData += bytes([self.fh232h.ReadByteAndSendACK(ack=I2C_GIVE_NACK)])
        # print(ByteData)
        self.fh232h.SetI2CStop()
        self.fh232h.SetLed(0)
        return ByteData[1:]
