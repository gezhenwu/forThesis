import os
import sys

lpgbtabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + "lpgbt"
sys.path.append(lpgbtabspath)
from lpgbt_control_lib import lpgbt_v1
import ctypes
import os.path
dll_name = "libPebFelix.so"
dllabspath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + ".." + os.path.sep + "libPebFelix" + os.path.sep + dll_name
lib = ctypes.CDLL(dllabspath)

class SerialComm(object):
    __instance = None

    def __init__(self, output_filenname = "", card = 0):
        # Declare input and output types for each method you intend to use

        charptr = ctypes.POINTER(ctypes.c_char)

        lib.init.argtypes = [ctypes.c_char_p]
        lib.init.restype = ctypes.c_void_p

        lib.deleteInstance.argtypes = []
        lib.deleteInstance.restype = ctypes.c_void_p

        pointer_type = ctypes.POINTER(ctypes.c_ubyte)

        lib.lpgbt_regs_serialcomm.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool, ctypes.c_int, pointer_type, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool]

        lib.lpgbt_regs_serialcomm.restype = ctypes.c_int

        ba = bytearray()
    
        self.obj = lib.init(ctypes.create_string_buffer(output_filenname.encode("UTF-8")), card)

    def lpgbt_regs(self, cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals, use_ec, debug, display):
        return lib.lpgbt_regs_serialcomm(self.obj, cardnr, linknr, i2c_addr, reg_addr, read, nbytes, reg_vals, use_ec, debug, display)
    
    def clear(self):
        lib.deleteInstance(self.obj)
