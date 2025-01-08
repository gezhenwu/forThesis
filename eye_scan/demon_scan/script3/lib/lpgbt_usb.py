#!/usr/bin/env python
#encoding: utf-8
# Company:  IHEP.CAS
# Engineer:  Jie Zhang
# 2022-07-09 created
import os
import logging
import sys
lpgbtabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + "lpgbt"
sys.path.append(lpgbtabspath)
from lpgbt_control_lib import lpgbt_v1
uplabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + ".."+ os.path.sep +"UPL"+ os.path.sep +"software"+ os.path.sep +"lib"
sys.path.append(uplabspath)
import upl as usb_dongle

class lpgbt(object):
    def __init__(self, usbnr = 0, addr = 0x70):
        usbnr &= 0xFF
        self.addr = addr & 0xFF

        # -------------------------------------------------------------------------
        # UPL sender and receiver
        upl_list = usb_dongle.upl_scan().upl_list
        if usbnr in (upl_list):
            self.upl = usb_dongle.upl(dev = usbnr)
            print(">>> Opened UPL")
        else:
            print(">>> Please connect UPL!")
            return

        # get a logger for lpGBT library logging
        self.lpgbt_logger = logging.getLogger("lpgbt_usb")
        # instantiate lpGBT class
        self.lpgbt = lpgbt_v1.LpgbtV1(logger=self.lpgbt_logger)

        # register communications interface(s)
        self.lpgbt.register_comm_intf(
            name = "I2C",
            write_regs = self.write_regs_i2c,
            read_regs = self.read_regs_i2c,
            default = True
        )

        # register access methods to control pins
        self.lpgbt.register_ctrl_pin_access(
            write_pin=self.write_lpgbt_ctrl_pin,
            read_pin=self.read_lpgbt_ctrl_pin
        )

    def write_byte_i2c(self, reg_addr, reg_val):
        self.upl.write_regs(
            device_addr=self.addr,
            addr_width=2,
            reg_addr=(reg_addr & 0x1FF),
            data=bytes([(reg_val&0xFF)])
        )

    def write_regs_i2c(self, reg_addr, reg_vals):
        reg_vals = [reg_val & 0xFF for reg_val in reg_vals]
        self.upl.write_regs(
            device_addr=self.addr,
            addr_width=2,
            reg_addr=(reg_addr & 0x1FF),
            data=bytes(reg_vals)
        )

    def read_byte_i2c(self, reg_addr):
        return self.upl.read_regs(
            device_addr=self.addr,
            addr_width=2,
            reg_addr=(reg_addr & 0x1FF),
            read_len=1
        )

    def read_regs_i2c(self, reg_addr, read_len):
        return self.upl.read_regs(
            device_addr=self.addr,
            addr_width=2,
            reg_addr=(reg_addr & 0x1FF),
            read_len=read_len
        )

    # do-nothing function
    def write_lpgbt_ctrl_pin(self, pin_name, value):
        pass
    # do-nothing function
    def read_lpgbt_ctrl_pin(self, pin_name):
        return 1
