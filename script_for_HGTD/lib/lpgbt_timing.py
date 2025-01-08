import os
import logging
import sys
import numpy as np
import time
lpgbtabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + "lpgbt"
sys.path.append(lpgbtabspath)
# from lpgbt_control_lib import lpgbt_v1
from lpgbt_control_lib import lpgbt_calibrated
import ctypes
import os.path
dll_name = "libPebFelix.so"
dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + "libPebFelix" + os.path.sep + dll_name
lib = ctypes.CDLL(dllabspath)

# do-nothing function
def write_lpgbt_ctrl_pin(pin_name, value):
    pass
# do-nothing function
def read_lpgbt_ctrl_pin(pin_name):
    return 1

class lpgbt(object):
    def __init__(self, serialcomm = None, devnr = 0, gbt = 0, addr = 0x70, use_fice = False):
        devnr &= 0xFF
        gbt &= 0xFF
        addr &= 0xFF
        self.devnr = devnr
        self.gbt = gbt
        self.addr = addr
        self.retry_max = 10
        self.retry_delay = 0.1

        self.serialcomm = serialcomm

        # get a logger for lpGBT library logging
        self.lpgbt_logger = logging.getLogger("lpgbt")
        # instantiate lpGBT class
        # self.lpgbt = lpgbt_v1.LpgbtV1(logger=self.lpgbt_logger)        
        self.lpgbt = lpgbt_calibrated.LpgbtCalibrated(logger=self.lpgbt_logger)

        if(use_fice):
            # register communications interface(s)
            self.lpgbt.register_comm_intf(
                name = "IC",
                write_regs = self.write_regs_ic,
                read_regs = self.read_regs_ic,
                default = True
            )
        else:
            # register communications interface(s)
            self.lpgbt.register_comm_intf(
                name = "IC",
                write_regs = self.write_lpgbt_regs,
                read_regs = self.read_lpgbt_regs,
                default = True
            )

        # register access methods to control pins
        self.lpgbt.register_ctrl_pin_access(
            write_pin=write_lpgbt_ctrl_pin,
            read_pin=read_lpgbt_ctrl_pin
        )

    def write_lpgbt_regs(self, reg_addr, reg_vals, retry = True, debug = False):
        devnr = self.devnr
        gbt = self.gbt
        i2c_addr = self.addr
        reg_addr &= 0x1FF
        read = False
        try:
            reg_vals_list = list(reg_vals)
        except TypeError:
            reg_vals_list = list((reg_vals,))
        nbytes = len(reg_vals_list)
        cbytearray = (ctypes.c_uint8 * nbytes)(*reg_vals_list)
        reg_vals_ptr = cbytearray
        # reg_vals_ptr =  ctypes.pointer(cbytearray)
        use_ec = False
        display = debug

        for i in range(self.retry_max):
            if(self.serialcomm):
                reply = self.serialcomm.lpgbt_regs(devnr, gbt, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
            else:
                reply = lib.lpgbt_regs(devnr, gbt, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
            if(reply):
                if retry == False:
                    raise Exception(f"Write failure at address 0x%x"%reg_addr)
                    return
                else:
                    print("Write failure at address 0x%x, and retry..."%reg_addr)
                    time.sleep(self.retry_delay)
            else:
                # Write Successfully
                return
        print("Stop retry")
        raise Exception(f"Write failure at address 0x%x"%reg_addr)
        return

    def read_lpgbt_regs(self, reg_addr, read_len, retry = True, debug = False):
        devnr = self.devnr
        gbt = self.gbt
        i2c_addr = self.addr
        reg_addr &= 0x1FF
        read = True
        nbytes = read_len & 0x1FF
        buf = ctypes.create_string_buffer(nbytes)
        reg_vals_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_uint8))
        use_ec = False
        display = debug
        for i in range(self.retry_max):
            if(self.serialcomm):
                reply = self.serialcomm.lpgbt_regs(devnr, gbt, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
            else:
                reply = lib.lpgbt_regs(devnr, gbt, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
            if(reply):
                if retry == False:
                    raise Exception(f"Read failure at address 0x%x"%reg_addr)
                    return 0
                else:
                    print("Read failure at address 0x%x, and retry..."%reg_addr)
                    time.sleep(self.retry_delay)
            else:
                # Write Successfully
                return np.frombuffer(buf, dtype=np.uint8).tolist()
        print("Stop retry")
        raise Exception(f"Read failure at address 0x%x"%reg_addr)
        return 0

    def write_byte_ic(self, reg_addr, reg_val, retry = True, debug = False):
        reg_addr &= 0x1FF
        reg_val &= 0xFF
        cmd = "fice -1 -d %d -G %d -I 0x%x -a 0x%x 0x%x"%(self.devnr, self.gbt, self.addr, reg_addr, reg_val)
        # print(cmd)
        for i in range(self.retry_max):
            flx = os.popen(cmd)
            reply = flx.read()
            # print("reply:"+reply)
            if reply == "":
                raise Exception(
                    f"Please do \"source ./setup.sh\" first!")
                return
            elif (-1 != reply.find('Nothing received')) or (-1 == reply.find('Reply (size=8): Parity OK  Reg')):
                if retry == False:
                    raise Exception(
                        f"Write failure at address 0x%x"%reg_addr)
                    if debug:
                        print("*************************\n"+reply+"*************************")
                    return
                else:
                    if debug:
                        print("*************************\n"+reply+"*************************")
                    print("Write failure at address 0x%x, and retry..."%reg_addr)
            else:
                # Write Successfully
                return
        print("Stop retry")
        raise Exception(
            f"Write failure at address 0x%x"%reg_addr
        )
        return

    def write_regs_ic(self, reg_addr, reg_vals):
        i = 0
        for val in reg_vals:
            try:
                self.write_byte_ic(reg_addr+i, val)
            except Exception as e:
                print(e)
                return
            i += 1

    def read_byte_ic(self, reg_addr, retry = True, debug = False):
        reg_addr &= 0x1FF
        cmd = "fice -1 -d %d -G %d -I 0x%x -a 0x%x"%(self.devnr, self.gbt, self.addr, reg_addr)
        # print(cmd)
        for i in range(self.retry_max):
            flx = os.popen(cmd)
            reply = flx.read()
            # print("reply:"+reply)
            if reply == "":
                raise Exception(
                    f"Please do \"source ./setup.sh\" first!")
                return 0
            elif (-1 != reply.find('Nothing received')) or (-1 == reply.find('Reply (size=8): Parity OK  Reg')):
                if retry == False:
                    raise Exception(
                        f"Read failure at address 0x%x"%reg_addr)
                    if debug:
                        print("*************************\n"+reply+"*************************")
                    return 0
                else:
                    if debug:
                        print("*************************\n"+reply+"*************************")
                    print("Read failure at address 0x%x, and retry..."%reg_addr)
            else:
                for line in reply.splitlines():
                    # print(line)
                    if (-1 != line.find('Reply')):
                        reg_val = line.split(':')[-1]
                        # print(reg_val)
                        return int(reg_val,base=16)
        print("Stop retry")
        raise Exception(
            f"Read failure at address 0x%x"%reg_addr
        )
        return 0

    def read_regs_ic(self, reg_addr, read_len):
        read_len &= 0x1FF
        reg_vals = [0] * read_len
        for i in range(read_len):
            try:
                temp = self.read_byte_ic(reg_addr+i)
            except Exception as e:
                print(e)
                return reg_vals
            reg_vals[i] = temp
        return reg_vals
