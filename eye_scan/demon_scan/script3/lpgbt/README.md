# Common lpGBT control library
This library unifies configuration and control of the lpGBT ASIC. It aims to implement
usage of all the lpGBT components. All configuration interfaces (I2C, EC, IC) of the
chip are conceptually supported. The implementation of these low-level protocols
is to be performed by the library user.

## Installation
This library is packaged using setuptools. It can be installed after checking out the repository using

```
pip install lpgbt_control_lib
```

Utilize the following command to install it as a symlink to your git repository, which makes it easier to update
the library. Even though the package bundles matplotlib as a dependency, you may want to install a specific
backend for it, for example:

```
pip install pycairo ptqt5
```

## Usage
To use this library in your project, the following steps are required:
  * Import the library into your Python application
  * Implement the required low level interface(s) for your system
    * Read/write a number of registers via I2C/EC/IC
    * Read/write a configuration pin
  * Instantiate a Lpgbt instance
  * Register at least one (a default) communication interface
  * Register the methods for reading/writing a configuration pin

The library exposes only a few main symbols:
  * `LpgbtV0` - driver for chip version 0
  * `LpgbtV1` - (in the future) driver for chip version 1
  * `LpgbtException` - run time errors raised from the drivers
  * `u32_to_bytes` - conversion of a single uint32 to bytes used for setting constant patterns etc.

## Example
Below you can find a small outline of how to use the library.

```python
import logging

from lpgbt_control_lib import LpgbtV0

# low level access to control pins
GPIO_MAP = [
    LpgbtV0.CTRL_RSTB: 0,
    LpgbtV0.CTRL_ADDR: 1,
    # ... add a mapping to your hardware GPIOs for all control pins
]

def write_lpgbt_ctrl_pin(pin_name, value):
    gpio_id = GPIO_MAP[pin_name]
    # TODO: write 'value' to your hardware GPIO

def read_lpgbt_ctrl_pin(pin_name):
    gpio_id = GPIO_MAP[pin_name]
    gpio_val = # TODO read value of hardware GPIO
    return gpio_val

# low level access to I2C interface
def write_lpgbt_regs_i2c(reg_addr, reg_vals):
    some_i2c_master.write_regs(
        device_addr=0x70
        addr_width=2,
        reg_addr=reg_addr,
        data=reg_vals
    )

def read_lpgbt_regs_i2c(reg_addr, read_len):
    values = some_i2c_master.read_regs(
        device_addr=0x70,
        addr_width=2,
        reg_addr=reg_addr,
        read_len=read_len
    )
    return values

def main():
    # get a logger for lpGBT library logging
    lpgbt_logger = logging.getLogger("lpgbt")

    # instantiate lpGBT class
    lpgbt = LpgbtV0(logger=lpgbt_logger)

    # register communications interface(s)
    lpgbt.register_comm_intf(
        name="I2C",
        write_regs=write_lpgbt_regs_i2c,
        read_regs=read_lpgbt_regs_i2c,
        default=True
    )

    # register access methods to control pins
    lpgbt.register_ctrl_pin_access(
        write_pin=write_lpgbt_ctrl_pin,
        read_pin=read_lpgbt_ctrl_pin
    )

    # communicate with your chip
    lpgbt.generate_reset_pulse()
    lpgbt.clock_generator_setup()
    # etc

    # in order to use a different communication interface
    lpgbt.adc_convert(..., comm_intf="I2C")
    lpgbt.adc_convert(..., comm_intf="EC")
    lpgbt.adc_convert(..., comm_intf="IC")
```
