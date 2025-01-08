import ctypes
lib = ctypes.CDLL('./libPebFelix.so')
import numpy as np

array8 = ctypes.c_uint8 * 8

reg_vals = array8(0x11,0x22,0x33,0x44,0x55,0x66,0x77,0x88)

reg_vals_ptr =  ctypes.pointer(reg_vals)

cardnr      = 0
linknr      = 0
i2c_addr    = 0x70
reg_addr    = 0
use_ec      = False
debug       = False
display     = False
nbytes      = 8

read        = False
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("write 0 error")
else:
    print("write 0 successfully")

read        = True
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("read 0 error")
else:
    print("read 0 successfully")

reg_vals = [1,2,3,4,5,6,7,8]
mycbytearray = (ctypes.c_uint8 * nbytes)(*reg_vals)
reg_vals_ptr =  ctypes.pointer(mycbytearray)
debug       = True
display     = True

read        = False
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("write 1 error")
else:
    print("write 1 successfully")

buf = ctypes.create_string_buffer(nbytes) 
reg_vals_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_uint8))

read        = True
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("read 1 error")
else:
    print("read 1 successfully")

for i in range(8):
    print(reg_vals_ptr[i])

list_of_results = np.frombuffer(buf, dtype=np.uint8).tolist()

print(list_of_results)

reg_vals[0] = 0x0F
debug       = True
display     = False

read        = False
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("write 2 error")
else:
    print("write 2 successfully")

read        = True
tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("read 2 error")
else:
    print("read 2 successfully")

debug       = True
display     = True
read        = True

i2c_addr    = 0x71
use_ec      = True

tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("write lumi. error")
else:
    print("write lumi. successfully")

tmp = lib.lpgbt_regs(cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals_ptr, use_ec, debug, display)
if(tmp):
    print("read lumi. error")
else:
    print("read lumi. successfully")