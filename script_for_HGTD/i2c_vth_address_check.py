# #!/usr/bin/env python
# #encoding: utf-8
# # Company:  IHEP.CAS
# # Engineer:  Jie Zhang
import time
import sys
import traceback
from lib import Utils

(options, args) = Utils.getParser()

if options.gbt in range(0,3):
    from lib import altiroc3_Mix046
    from lib import peb_Mix046
    peb_1f = peb_Mix046
    altiroc3 = altiroc3_Mix046
    use_lumi = True
elif options.gbt in range(3,6):
    from lib import altiroc3_Mix230
    from lib import peb_Mix230
    peb_1f = peb_Mix230
    altiroc3 = altiroc3_Mix230
    use_lumi = False
elif options.gbt in range(6,9):
    from lib import altiroc3_Mix310
    from lib import peb_Mix310
    peb_1f = peb_Mix310
    altiroc3 = altiroc3_Mix310
    use_lumi =  False
else:
    print("Please input the elink Pattern you want to configure.")
    sys.exit()

# Config parameter
devnr = options.devnr
gbt = options.gbt
print("\n***FLX-device number is %d. GBT-link number is %d.***\n"%(devnr,gbt))
timing_addr = options.timingAddr
lumi_addr = options.LumiAddr

def write_and_read_adc(peb,options):
    for module in [0, 2, 4, 6, 8, 9, 10, 11, 12, 13]:
        for chip in range(2):
            try:
                # Write 0b1111111 to register 0x1006 for each chip
                print("start with module %d, chip %d"%(module,chip))
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module, chip_id = chip)
                alti.setDacVth(800, options.dacVthRange)
                read_back = peb.module_i2c_read(
                        module_id = module,
                        chip_id = chip,
                        reg_address = 0x1006,
                        read_len = 2
                    )
                print(read_back)
                # Read adc_get_vin for all chips immediately after writing
                i=0
                for module_read in [0,2,4,6,8,9,10,11,12,13]:
                # for module in [9]:
                    j=0
                    for chip_read in range(0,2):
                        try:  
                            for reg in [0x1015]:
                                peb.module_i2c_write(
                                    module_id = module_read,
                                    chip_id = chip_read,
                                    reg_address = reg,
                                    data = 124
                                )
                            mux_ch = 3+i*6+j
                            peb.mux_select(channel=mux_ch)
                            peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
                            adc_value= peb.timing.lpgbt.adc_convert(1)
                            calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
                            print("chanel %d module %d chip %d monitor_sig 10: ADC: %d, voltage: %d"%(options.gbt,module_read,chip_read,adc_value,calibrated_v*1000))
                            time.sleep(0.1)
                        except:
                            continue
                        j+=1
                    i+=1
            except Exception as e:
                continue


def main():
    # instantiate lpGBT class
    peb = peb_1f.peb(devnr = devnr,gbt = gbt, addr = timing_addr)
    peb.lumi_add(devnr = devnr, gbt = gbt, addr = lumi_addr)

    peb.timing.lpgbt.auto_tune_vref()
                    
    i=0
    for module in [0,2,4,6,8,9,10,11,12,13]:
    # for module in [9]:
        j=0
        for chip in range(0,2):
            try:  
                alti = altiroc3.Altiroc(devnr = devnr, gbt = gbt, addr = timing_addr, use_usb = False, module_id = module, chip_id = chip)
                alti.setDacVth(0, options.dacVthRange)
                read_back = peb.module_i2c_read(
                        module_id = module,
                        chip_id = chip,
                        reg_address = 0x1006,
                        read_len = 2
                    )
                print(read_back)
                for reg in [0x1015]:
                    peb.module_i2c_write(
                        module_id = module,
                        chip_id = chip,
                        reg_address = reg,
                        data = 124
                    )
                mux_ch = 3+i*6+j
                peb.mux_select(channel=mux_ch)
                peb.timing.lpgbt.adc_config(inp=0, inn=15, gain=0)
                adc_value= peb.timing.lpgbt.adc_convert(1)
                calibrated_v= peb.timing.lpgbt.adc_get_vin(1)
                print("chanel %d module %d chip %d monitor_sig 10: ADC: %d, voltage: %d"%(options.gbt,module,chip,adc_value,calibrated_v*1000))
                time.sleep(0.1)
            except:
                continue
            j+=1
        i+=1

    write_and_read_adc(peb, options)

    del peb

try:
    main()
except:
    traceback.print_exc()
