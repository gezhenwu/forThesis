#!/usr/bin/env python
#encoding: utf-8
# Company:  CAS IHEP
# Engineer:  zhj_at_ihep.ac.cn
# 2021-10-22 created
import sys
import ftd2xx as ftd
import time

# MPSSE Control Commands
MPSSE_CMD_SET_DATA_BITS_LOWBYTE         = 0x80
MPSSE_CMD_SET_DATA_BITS_HIGHBYTE        = 0x82
MPSSE_CMD_GET_DATA_BITS_LOWBYTE         = 0x81
MPSSE_CMD_GET_DATA_BITS_HIGHBYTE        = 0x83

MPSSE_CMD_SEND_IMMEDIATE                = 0x87
MPSSE_CMD_ENABLE_3PHASE_CLOCKING        = 0x8C
MPSSE_CMD_DISABLE_3PHASE_CLOCKING       = 0x8D
MPSSE_CMD_ENABLE_DRIVE_ONLY_ZERO        = 0x9E

# MPSSE Data Command - LSB First 
MPSSE_CMD_DATA_LSB_FIRST                = 0x08

# MPSSE Data Commands - bit mode - MSB first 
MPSSE_CMD_DATA_OUT_BITS_POS_EDGE        = 0x12
MPSSE_CMD_DATA_OUT_BITS_NEG_EDGE        = 0x13
MPSSE_CMD_DATA_IN_BITS_POS_EDGE         = 0x22
MPSSE_CMD_DATA_IN_BITS_NEG_EDGE         = 0x26
MPSSE_CMD_DATA_BITS_IN_POS_OUT_NEG_EDGE = 0x33
MPSSE_CMD_DATA_BITS_IN_NEG_OUT_POS_EDGE = 0x36

# MPSSE Data Commands - byte mode - MSB first 
MPSSE_CMD_DATA_OUT_BYTES_POS_EDGE       = 0x10
MPSSE_CMD_DATA_OUT_BYTES_NEG_EDGE       = 0x11
MPSSE_CMD_DATA_IN_BYTES_POS_EDGE        = 0x20
MPSSE_CMD_DATA_IN_BYTES_NEG_EDGE        = 0x24
MPSSE_CMD_DATA_BYTES_IN_POS_OUT_NEG_EDGE = 0x31
MPSSE_CMD_DATA_BYTES_IN_NEG_OUT_POS_EDGE = 0x34

# Data size in bits
DATA_SIZE_8BITS         = 0x07
DATA_SIZE_1BIT          = 0x00

SEND_ACK                = 0x00
SEND_NACK               = 0x80

# ADBUS
PIN_SCL                 = 0b00000001
PIN_SDA_O               = 0b00000010
PIN_SDA_I               = 0b00000100

# ACBUS
PIN_LED                 = 0b00010000

# SCL & SDA directions
# 1 in the direction byte will make that bit an output.
DIRECTION_SCLIN_SDAIN   = 0x00
DIRECTION_SCLOUT_SDAIN  = PIN_SCL
DIRECTION_SCLIN_SDAOUT  = PIN_SDA_O
DIRECTION_SCLOUT_SDAOUT = PIN_SCL | PIN_SDA_O

DIRECTION_LEDOUT        = PIN_LED

# SCL & SDA values
VALUE_SCLLOW_SDALOW     = 0x00
VALUE_SCLHIGH_SDALOW    = PIN_SCL
VALUE_SCLLOW_SDAHIGH    = PIN_SDA_O
VALUE_SCLHIGH_SDAHIGH   = PIN_SCL | PIN_SDA_O

VALUE_LEDHIGH           = PIN_LED
VALUE_LEDLOW            = 0x00

# I2C
I2C_GIVE_ACK            = 1
I2C_GIVE_NACK           = 0
I2C_TIMEOUT             = -1

class ft232h(object): 
    def __init__(self, dev = 0, i2c_freq = 100): # kHz
        self.ft232h = ftd.open(dev = dev)
        # print(self.ft232h.getDeviceInfo())

        # Reset the FT232H
        self.ft232h.resetDevice()

        # Purge USB receive buffer 
        # Get the number of bytes in the FT232H receive buffer and then read them
        # By purge, it means after reading the receive buffer, it will becomes empty
        # Get number of bytes in the input buffer
        NumBytesInBuffer = self.ft232h.getQueueStatus() 
        if NumBytesInBuffer > 0:
            self.ft232h.read(NumBytesInBuffer) 

        # Set USB request transfer sizes
        self.ft232h.setUSBParameters(65536, 65535) 
        # Disable event and error characters
        self.ft232h.setChars(False, 0, False, 0) 
        # Set the read and write timeouts to 5 seconds
        self.ft232h.setTimeouts(5000, 5000) 
        # Keep the latency timer at default of 16ms
        self.ft232h.setLatencyTimer(16) 
        # Reset the mode to whatever is set in EEPROM
        self.ft232h.setBitMode(0x0, 0x00) 
        # Enable MPSSE mode
        self.ft232h.setBitMode(0x0, 0x02) 

        # Synchronise the MPSSE by sending bad command AA to it
        if 1 != self.ft232h.write(b'\xAA'): # Send off the invalid command 0xAA
            print("Write timed out!")
            sys.exit()
        # Now read the response from the FT232H. It should return error code 0xFA followed by the actual bad command 0xAA
        # Wait for the two bytes to come back
        NumBytesInBuffer = 0
        Counter = 0
        # Sit in this loop until
        # (1) we receive the two bytes expected
        # or (2) a hardware error occurs causing the GetQueueStatus to return an error code
        # or (3) we have checked 500 times and the expected byte is not coming
        while NumBytesInBuffer < 2 and Counter < 500:
            # Get number of bytes in the input buffer
            NumBytesInBuffer = self.ft232h.getQueueStatus() 
            Counter = Counter + 1
            time.sleep(0.001) # short delay 0.001s(1ms)
        # If the loop above exited due to the byte coming back (not an error code and not a timeout)
        # then read the bytes available and check for the error code followed by the invalid character
        if Counter == 500 or b'\xfa\xaa'!= self.ft232h.read(NumBytesInBuffer):
            print(("Fail to synchronize MPSSE with command 0xAA\n"))
            sys.exit()

        # Synchronise the MPSSE by sending bad command AA to it
        if 1 != self.ft232h.write(b'\xab'): # Send off the invalid command 0xAA
            print("Write timed out!")
            sys.exit()
        # Now read the response from the FT232H. It should return error code 0xFA followed by the actual bad command 0xAA
        # Wait for the two bytes to come back
        NumBytesInBuffer = 0
        Counter = 0
        # Sit in this loop until
        # (1) we receive the two bytes expected
        # or (2) a hardware error occurs causing the GetQueueStatus to return an error code
        # or (3) we have checked 500 times and the expected byte is not coming
        while NumBytesInBuffer < 2 and Counter < 500:
            # Get number of bytes in the input buffer
            NumBytesInBuffer = self.ft232h.getQueueStatus() 
            Counter = Counter + 1
            time.sleep(0.001) # short delay 0.001s(1ms)

        # If the loop above exited due to the byte coming back (not an error code and not a timeout)
        # then read the bytes available and check for the error code followed by the invalid character
        if Counter == 500 or b'\xfa\xab'!= self.ft232h.read(NumBytesInBuffer):
            print(("Fail to synchronize MPSSE with command 0xAB\n"))
            sys.exit()

        # Configure the MPSSE settings
        OutputBuffer  = b'\x8A' # Disable clock divide-by-5 to allow 60Mhz as master clock
        OutputBuffer += b'\x97' # Ensure adaptive clocking is off
        OutputBuffer += b'\x8C' # Enable 3 phase data clocking, data valid on both clock edges for I2C
        OutputBuffer += b'\x9E' # Enable the FT232H's drive-zero mode on the lines used for I2C ...
        # This will make the I/Os only drive when the data is '0' and tristate on the data being '1' when
        # the appropriate bit is set. This op-code/command is only used when configuring the MPSSE for I2C use,
        # since the I2C lines are pulled up and not needed to be drived when data being '1'.
        OutputBuffer += b'\x07' # ...on the bits 0, 1 and 2 of the lower port (AD0, AD1, AD2)...
        OutputBuffer += b'\x00' # ...not required on the upper port AC 0-7
        OutputBuffer += b'\x85' # Ensure internal loopback is off
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer) # Send off the commands
        # Now configure the dividers to set the SCLK frequency which we will use
        # The SCLK clock frequency can be worked out by the algorithm (when divide-by-5 is off)
        # SCLK frequency  = 60MHz /((1 +  [(1 +0xValueH*256) OR 0xValueL])*2)
        factor = 1.5
        ClockDivisor = int(60000/2/factor/i2c_freq-1)
        ClockDivisor_H = (ClockDivisor>>8) & 0xFF
        ClockDivisor_L = ClockDivisor & 0xFF
        OutputBuffer  = b'\x86' # Command to set clock divisor
        # OutputBuffer += b'\xc8'
        # OutputBuffer += b'\x00'
        OutputBuffer += ClockDivisor_L.to_bytes(1, 'big') # Set 0xValueL of clock divisor
        OutputBuffer += ClockDivisor_H.to_bytes(1, 'big') # Set 0xValueH of clock divisor
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer) # Send off the commands

        # Init ADBUS and ACBUS
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_HIGHBYTE])  # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([PIN_LED])    # Set ADBUS0,1,2 to high level (only affects pins which are output)
        OutputBuffer += bytes([DIRECTION_LEDOUT])     # Set input/output
        # Tristate the SCL & SDA pins
        OutputBuffer += bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([VALUE_SCLHIGH_SDAHIGH])  # Set the value of the pins (only affects pins which are output)
        OutputBuffer += bytes([DIRECTION_SCLIN_SDAIN])  # Set input
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer)

    ##############################################################################################################
    # close device
    def close(self):
        self.ft232h.close()

    ##############################################################################################################
    # Function to set all lines to idle states
    # For I2C lines, it releases the I2C clock and data lines to be pulled high externally
    def SetI2CLinesIdle(self):
        # Set the idle states for the AD lines
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([VALUE_SCLHIGH_SDAHIGH]) # Bring data out low (bit 1)
        OutputBuffer += bytes([DIRECTION_SCLIN_SDAIN]) # Set input, tristate the SCL & SDA pins
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer)

    ##############################################################################################################
    # Function to set the I2C Start state on the I2C clock and data lines
    # It generates an negedge on the data line when the clock line is high
    def SetI2CStart(self):
        # SCL high, SDA high
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([VALUE_SCLHIGH_SDAHIGH]) 
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAOUT]) # Set output
        # SCL high, SDA low
        OutputBuffer += bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([VALUE_SCLHIGH_SDALOW])
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAOUT]) # Set output
        self.ft232h.write(OutputBuffer)

    ##############################################################################################################
    # Function to set the I2C Stop state on the I2C clock and data lines
    # It generates an posedge on the data line when the clock line is high 
    def SetI2CStop(self):
        # SCL high, SDA low
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set directions of ADbus and data values for pins set as o/p
        OutputBuffer += bytes([VALUE_SCLHIGH_SDALOW])
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAOUT]) # Set output
        # SCL high, SDA high
        OutputBuffer += bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) 
        OutputBuffer += bytes([VALUE_SCLHIGH_SDAHIGH]) 
        OutputBuffer += bytes([DIRECTION_SCLIN_SDAIN]) # Tristate the SCL & SDA pins
        self.ft232h.write(OutputBuffer)

    ##############################################################################################################
    # Function to write 1 byte, and check if it returns an ACK or NACK by clocking in one bit
    # This function combines the data and the Read/Write bit to make a single 8-bit value
    #    We clock one byte out to the I2C Slave
    #    We then clock in one bit from the Slave which is the ACK/NAK bit
    # Returns 1 if the write was ACKed by the slave
    def SendByteAndCheckACK(self, data): #the data here can be any radix
        data &= 0xFF
        # Set direction
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) 
        OutputBuffer += bytes([VALUE_SCLLOW_SDALOW])
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAOUT]) 
        # Command to write 8 bits
        OutputBuffer += bytes([MPSSE_CMD_DATA_OUT_BITS_NEG_EDGE]) # command to clock data bytes out MSB first on clock falling edge
        OutputBuffer += bytes([DATA_SIZE_8BITS]) # Data length of 0x0000 means 1 byte data to clock out
        OutputBuffer += bytes([data]) # Actual byte to clock out
        # Put I2C line back to idle (during transfer) state... Clock line driven low, Data line high (open drain)
        OutputBuffer += bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE]) # Command to set lower 8 bits of port (ADbus 0-7 on the FT232H)
        OutputBuffer += bytes([VALUE_SCLLOW_SDALOW]) # Set the value of the pins (only affects those set as output)
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAIN]) # Set the directions
        # Command to get ACK bit
        OutputBuffer += bytes([MPSSE_CMD_DATA_IN_BITS_POS_EDGE]) # Command to clock in bits MSB first on clock rising edge
        OutputBuffer += bytes([DATA_SIZE_1BIT]) # Length of 0x00 means to scan in 1 bit
        # This command then tells the MPSSE to send any results gathered back immediately
        OutputBuffer += bytes([MPSSE_CMD_SEND_IMMEDIATE]) # Send answer back immediate command
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer)

        # Wait for the one byte to come back
        NumBytesInBuffer = 0
        Counter = 0
        # Sit in this loop until
        # (1) we receive the one byte expected
        # or (2) a hardware error occurs causing the GetQueueStatus to return an error code
        # or (3) we have checked 500 times and the expected byte is not coming
        while NumBytesInBuffer < 1 and Counter < 50:
            # Get number of bytes in the input buffer
            NumBytesInBuffer = self.ft232h.getQueueStatus() 
            Counter = Counter + 1
            # time.sleep(0.001) # short delay 0.001s(1ms)
        # If the loop above exited due to the byte coming back (not an error code and not a timeout)
        # then read the bytes available and check for the error code followed by the invalid character
        if Counter < 500:
            # Check if ACK bit received by reading the byte sent back from the FT232H containing the ACK bit
            BytesRead = self.ft232h.read(1)[0]
            # print(BytesRead)
            if BytesRead & 0x1 : # Check ACK bit(low active), which is the LSB of the received byte
                return I2C_GIVE_NACK # Error, can't get the ACK bit
            else:
                return I2C_GIVE_ACK # Return True if the ACK was received
        else:
            return I2C_TIMEOUT

    ##############################################################################################################
    # Function to read 1 byte from the I2C slave (e.g. FT-X chip)
    #    Clock in one byte from the I2C Slave which is the actual data to be read
    #    Clock out one bit to the I2C Slave which is the ACK/NAK bit
    # This function reads only one byte from the I2C Slave. It sends a '0' as the ACK/NAK bit. 
    # return one byte of data read from the I2C Slave
    def ReadByteAndSendACK(self, ack = I2C_GIVE_ACK):
        # Set pin directions - SCL is output driven low, SDA is input (set high but does not matter)
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE])
        OutputBuffer += bytes([VALUE_SCLLOW_SDALOW])
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAIN])
        # Clock one byte of data in
        OutputBuffer += bytes([MPSSE_CMD_DATA_IN_BITS_POS_EDGE]) # Command to clock data byte in on the clock rising edge
        OutputBuffer += bytes([DATA_SIZE_8BITS]) # Length
        # Now clock out one bit (the ACK/NAK bit). This bit has value '1' to send a NAK to the I2C Slave
        OutputBuffer += bytes([MPSSE_CMD_SET_DATA_BITS_LOWBYTE])
        OutputBuffer += bytes([VALUE_SCLLOW_SDALOW])
        OutputBuffer += bytes([DIRECTION_SCLOUT_SDAOUT])
        # send ACK/NACK
        OutputBuffer += bytes([MPSSE_CMD_DATA_OUT_BITS_NEG_EDGE]) # Command to clock data bits out on clock falling edge
        OutputBuffer += bytes([DATA_SIZE_1BIT]) # Length of 0x00 means clock out ONE bit
        if ack == I2C_GIVE_ACK:
            # Clock out the ack bit as a '0' on negative edge
            OutputBuffer += bytes([SEND_ACK]) # Command will send bit 7 of this byte, we send a '1' here
        else:
            # Clock out the ack bit as a '1' on negative edge
            OutputBuffer += bytes([SEND_NACK]) # Command will send bit 7 of this byte, we send a '1' here
        # This command then tells the MPSSE to send any results gathered back immediately
        OutputBuffer += bytes([MPSSE_CMD_SEND_IMMEDIATE]) # Send answer back immediate command
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer)

        # Now wait for the byte which we read to come back to the host PC
        # Wait for the one byte to come back
        NumBytesInBuffer = 0
        Counter = 0
        # Sit in this loop until
        # (1) we receive the one byte expected
        # or (2) a hardware error occurs causing the GetQueueStatus to return an error code
        # or (3) we have checked 500 times and the expected byte is not coming
        while NumBytesInBuffer < 1 and Counter < 500:
            # Get number of bytes in the input buffer
            NumBytesInBuffer = self.ft232h.getQueueStatus() 
            Counter = Counter + 1
            # time.sleep(0.001) # short delay 0.001s(1ms)
        # If the loop above exited due to the byte coming back (not an error code and not a timeout)
        # then read the bytes available and check for the error code followed by the invalid character
        if Counter < 500:
            return self.ft232h.read(1)[0]
        else:
            return I2C_TIMEOUT # Timeout and Failed to get any data back

    ##############################################################################################################
    def SetLed(self, value = 1):
        if value:
            status = VALUE_LEDLOW
        else:
            status = VALUE_LEDHIGH
        OutputBuffer  = bytes([MPSSE_CMD_SET_DATA_BITS_HIGHBYTE]) # Command to set lower 8 bits of port (ACbus 0-7 on the FT232H)
        OutputBuffer += bytes([status]) # Set the value of the pins (only affects those set as output)
        OutputBuffer += bytes([DIRECTION_LEDOUT]) # Set the directions
        # print(OutputBuffer)
        self.ft232h.write(OutputBuffer)
