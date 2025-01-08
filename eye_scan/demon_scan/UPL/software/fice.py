# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  CAS IHEP
# # Engineer:  zhj_at_ihep.ac.cn
import sys
import pathlib
import traceback
import getopt
import csv
sys.path.append("lib")
import upl as usb_dongle

# Version identifier: year, month, day, release number
VERSION_ID = 0x22031000 # Data value hex must have x or 0x
UPL_LINKS = 24

def arg_range(opt, min, max):
    print("### -%s: argument not in range (%d..%d)"%(opt,min,max))

def arg_error(opt):
    print("### -%s: error in argument"%opt)
    usage()

def usage():
    print("UPL fice version 0x%x tool to read or write lpGBT registers: "%VERSION_ID)
    print("read or write a single byte from or to the given lpGBT register address")
    print("or write to multiple lpGBT registers using the contents of a file")
    print("(i.e. ASCII file: 1 address and 1 (register) byte value per line.")
    print("")
    print("Use option -a with an optional additional byte value to write a single register, ")
    print("without option -a to read all registers.")
    print("or without option -a and file name all registers are read out and displayed")
    print("or without option -a but provide a file name to write multiple lpGBT registers.")
    print("either in one I2C read operation or one-by-one (option -o).")
    print("")
    print("Usage:")
    print("python3 fice.py [-h|V] [-0|1] [-G <gbt>] [-I <i2c>]")
    print("      [-a <addr> [<byte>] | <filename>]")
    print("  -h         : Show this help text.")
    print("  -V         : Show version.")
    print("  -0         : lpGBT v0")
    print("  -1         : lpGBT v1 (default: v1)")
    print("  -a <addr>  : lpGBT register address (decimal or hex, 0x..) to read or write.")
    print("  -G <lpgbt> : lpGBT-link number.")
    print("  -I <i2c>   : lpGBT I2C address.")
    print("  -o         : When reading all registers, do it one-by-one")
    print("               (default: one multi-reg read op).")
    print(" <byte>      : Byte value (decimal or hex, 0x..) to write to lpGBT register (option -a).")
    print(" <filename>  : Name of file with lpGBT register data to write to registers.")
    print("")
    print("=> Examples:")
    print("Read all registers of lpGBTv1 (I2C address 0x70)")
    print("connected to UPL 0:")
    print("  python3 fice.py -1 -G 0 -I 0x70")
    print("Read lpGBT register 32 (0x20):")
    print("  python3 fice.py -1 -G 0 -I 0x70 -a 32 (or: python3 fice.py -1 -G 0 -I 0x70 -a 0x20)")
    print("Write 0xA5 to lpGBT register 32 (0x20):")
    print("  python3 fice.py -1 -G 0 -I 0x70 -a 32 0xA5")
    print("Write contents of GBT-conf.txt to lpGBT registers:")
    print("  python3 fice.py -1 -G 0 -I 0x70 GBT-conf.txt")

def main():
    # cardnr      = 0
    # dma_write   = -1 # Autoselect FromHost DMA controller index
    # dma_read    = 0
    linknr      = -1
    i2c_addr    = -1
    reg_addr    = -1
    databyte    = -1
    write_reg   = False
    one_by_one  = False
    # receive     = True
    # receive_any = False
    # txt_output  = False
    # file_is_xml = False
    # debug       = False
    # use_ec      = False
    lpgbt_v1    = True
    filename    = ""

    # Parse the options
    opts, args = getopt.getopt(sys.argv[1:], "h01a:I:G:oV",["help","version"])
    # print(opts)
    # print(args)

    for (opt_name,opt_value) in opts:
        # print(opt_name, opt_value)
        if opt_name in ('-h','--help'):
            usage()
            return
        if opt_name in ('-0'):
            lpgbt_v1 = False;
            continue
        if opt_name in ('-1'):
            continue
        if opt_name in ('-a'):
            # lpGBT register address
            reg_addr = int(opt_value, 0)
            # print(reg_addr)
            if reg_addr < 0 or reg_addr > 511:
                arg_range('-a', 0, 511)
                return
            else:
                continue
        if opt_name in ('-I'):
            # lpGBT I2C address
            i2c_addr = int(opt_value, 0)
            # print(i2c_addr)
            if i2c_addr < 0 or i2c_addr > 127:
                arg_range('-I', 0, 127)
                return
            else:
                continue
        if opt_name in ('-G'):
            # lpGBT link number
            linknr = int(opt_value, 0)
            # print(linknr)
            if linknr < 0 or linknr > UPL_LINKS-1:
                arg_range('-G', 0, UPL_LINKS-1)
                return
            else:
                continue
        # if opt_name in ('-d'):
        #     cardnr = int(opt_value, 0)
        #     continue;
        # if opt_name in ('-D'):
        #     debug = True
        #     continue;
        # if opt_name in ('-e'):
        #     use_ec = True
        #     continue
        # if opt_name in ('-i'):
        #     # DMA controller to use
        #     dma_read = int(opt_value, 0)
        #     # print(dma_read)
        #     if dma_read < 0 or dma_read > 7:
        #         arg_range('-i', 0, 7)
        #         return
        #     else:
        #         continue;
        if opt_name in ('-o'):
            one_by_one = True
            continue
        # if opt_name in ('-R'):
        #     receive_any = True
        #     continue
        # if opt_name in ('-t'):
        #     txt_output = True
        #     continue
        if opt_name in ('-V', '--version'):
            print("Version 0x%x"%VERSION_ID)
            return
        # if opt_name in ('-X'):
        #     file_is_xml = True
        #     continue
        # if opt_name in ('-Z'):
        #     receive = False
        #     continue
        
        # Unknown parameter
        print("Invalid options, use \"python3 fice.py -h\" for help")
        return

    if linknr < 0 :
        print("### Provide a valid lpGBT link number (-G)")
        return
    if i2c_addr < 0 :
        print("### Provide a valid lpGBT I2C address (-I)")
        return

    # Data byte value to write or name of file with lpGBT register values
    if args != []:
        # There is an additional parameter:
        # it must be a byte value or a file name
        if reg_addr != -1:
            # Expect a byte value to write;
            # accept hex values "x12" and "0x12", as well as decimal "18"
            databyte = int(args[0],0)
            if databyte < 0 or databyte > 255:
                print ("### Data byte value out-of-range 0..0xFF: 0x%x"%databyte)
                return
            write_reg = True
        else:
            filename = args[0]

    # -------------------------------------------------------------------------
    # UPL sender and receiver
    upl_list = usb_dongle.upl_scan().upl_list
    if linknr in (upl_list):
        upl = usb_dongle.upl(dev=linknr)
        print(">>> Opened UPL")
    else:
        print(">>> Please connect UPL!")
        return

    # -------------------------------------------------------------------------
    # Describe the requested operation:
    print(">>> lpGBTv%d #%d I2C-addr=0x%X: "%((1 if lpgbt_v1 else 0),linknr,i2c_addr),end="")
    if filename!="":
        print("apply file %s"%filename)
    elif write_reg:
        print("WRITE 0x%02X (%d) to reg 0x%03X (%d)"%(databyte,databyte,reg_addr,reg_addr))
    elif reg_addr != -1:
        print("READ reg 0x%03X (%d)"%(reg_addr, reg_addr))
    else:
        print("READ all registers")

    if filename=="":
        if write_reg:
            # Write a single register
            upl.write_regs(device_addr=i2c_addr, addr_width=2, reg_addr=reg_addr,data=bytes([databyte & 0xFF]))
        else:
            # Read either a single register or all registers
            if reg_addr != -1:
                dataread=upl.read_regs(device_addr=i2c_addr, addr_width=2, reg_addr=reg_addr, read_len=1)
                print("0x%X"%dataread[0])
            else:
                # lpGBTv0: 463 8-bit registers; first 320 R/W
                # lpGBTv1: 494 8-bit registers; first 336 R/W
                max_regs = 494 if lpgbt_v1 else 463
                print("Addr Value")
                if one_by_one:
                    # Read the registers one-by-one
                    for reg_addr in range(max_regs):
                        dataread=upl.read_regs(device_addr=i2c_addr, addr_width=2, reg_addr=reg_addr, read_len=1)
                        print("0x%X 0x%X"%(reg_addr,dataread[0]))
                else:
                    # Read all registers in one operation
                    reg_addr = 0
                    datareads = upl.read_regs(device_addr=i2c_addr, addr_width=2, reg_addr=reg_addr, read_len=max_regs)
                    for dataread in datareads:
                        print("0x%X 0x%X"%(reg_addr,dataread))
                        reg_addr +=1
    else:
        filename = pathlib.Path(filename)
        if filename.is_file():
            with open(filename, 'r', encoding='utf-8') as f:
                lines = csv.reader(f, delimiter=' ')
                count = 0
                for row in lines:
                    # print(row)
                    if row != []: # skip empty line
                        reg_addr = int(row[0], 0) & 0x1FF
                        databyte = int(row[1], 0) & 0xFF
                        # print("Addr = 0x%x, Data = 0x%x"%(reg_addr, databyte))
                        upl.write_regs(device_addr=i2c_addr, addr_width=2, reg_addr=reg_addr,data=bytes([databyte & 0xFF]))
                        count += 1
            print("Wrote %d regs"%count)
        else:
            print(">>>File does not exist!")

##############################################################################################################
try:
    main()
except:
    traceback.print_exc()
