# USB Programmer for lpGBT (UPL)

## Introduction

The UPL is a dedicated PCB board which is designed to configure the lpGBT on the FMC board and the PEB board through the 14-pin connector. The motivation for the new design is that the existing lpGBT programming tool-kits, piGBT toolkit and CERN USB-I2C dongle, are not suitable for the configuration of the lpGBT on PEB. For example, the piGBT has large size while the CERN USB-I2C dongle is platform-dependent and has no available GPIOs. Moreover, neither of them considered electrical isolation, which is required for PEB configuration.

This UPL design uses the FT232H ASIC chip, which can do the conversion between USB protocol and I2C protocol. Following the FT232H ASIC chip, an I2C isolator is used to electrically isolate the I2C signals from the host side and detector side. Then a GPIO expander and a level shifter can extend more GPIO ports and shift the 3.3 voltage level to lpGBT voltage level respectively. The power supply is also isolated with a power isolator. In this connector, there are 2 I2C pins, 4 MODE pins for lpGBT working mode setting, eFUSE2V5 for lpGBT e-fusing, RSTB Pin and READY pin.

The UPL has the following 2 main features. Firstly, it has the characteristic of electrical isolation for both signal and power supply. The PEB under configuration would not be interfered by the host side since there are no direct electrical connection between the 2 sides. For example, the high surge voltage from the host side doesn't affect the PEB as well as electrical noises. Another feature of the board is good cross-platform compatibility. The FT232H ASIC chip provides multi-platform supported USB driver, which can work on the operating systems such as Mac OS, Linux, Windows 7/8/10, Windows XP, and so on. Moreover, many programming languages such as C++, C#, Python, etc, can be used to control the USB driver.

# Software

This tutorial aims to show you how to install the driver for FT232H-based devices with different operating systems. We have developed python codes to control the FT232H-based device by using one of its MPSSE modes, called USB-TO-I2C, which can implement the data format transfer from USB format(from PC side) to I2C format(to I2C slave side). In short, the data flow is like this: PC-->FT232H-based device-->I2C slave under control. More details can be found in [Jeremy Bentham's blog](https://iosoft.blog/2018/12/02/ftdi-python-part-1/).  

# Driver installation
The following parts will be structured with: operation guide when using windows 10, CentOS7.9, Ubuntu 20 and MAC OS.  

## Windows 10

1. Driver installation

Download [the D2xx driver](https://ftdichip.com/drivers/d2xx-drivers/). On the download page, just scroll down to the windows downloading row, and click the 'setup executable' at the Comment column, where you can download the .exe file. And the following installation will be straightforward, what you need to do is double-click the .exe file and then follow the installation guide GUI.

2. Python installation

You'd better install the python3. You can download it from [the official website](https://www.python.org) 

3. Python package 'ftd2xx' installation and other prerequisite packages installation

Press "Win+R", and type "cmd" to open a terminal. In the terminal, type the following command:
```
  pip3 install ftd2xx
```
After that, you can install some prerequisite packages
```
  pip3 install numpy pytz pyvisa-py pyserial ftd2xx matplotlib seaborn
```  

## CentOS 7.9
1. Update your packages  
In order to make the following steps process smoothly, you'd better install your packages.  
```
  sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel libffi-devel libjpeg-turbo-devel tkinter tcl-devel tk-devel
```
2. Python installation  
```
  sudo yum install -y python3 python3-tkinter python3-devel
```
Type
```
  python3 --version
  pip3 --version
```  
to check the installation, if report following error:   
`ImportError: This package should not be accessible on Python 3. Either you are trying to run from the python-future src folder or your installation of python-future is corrupted.`  
Use
```
  unset PYTHONPATH
```  
to disconnect with order version  
In order to verify if python is successfully installed, you can launch python with the command line: python3. Then inside the launched python, you can execute `import tkinter`, if it is executed without error, the python should be workable for the UPL software. If not, you should install the library.  
After that, you can install some prerequisite packages  
```
  sudo pip3 install numpy pytz pyvisa-py pyserial ftd2xx matplotlib seaborn
```  

3. Driver installation  

3.1 Download [the D2xx driver](https://ftdichip.com/drivers/d2xx-drivers/). On the download page, just scroll down to the Linux downloading row to download a .tgz compressed file.  
```
  tar xfvz libftd2xx-x86_64-1.4.27.tgz
  cd release/build
  su
  cp libftd2xx.* /usr/local/lib
  chmod 0755 /usr/local/lib/libftd2xx.so.1.4.27
  ln -sf /usr/local/lib/libftd2xx.so.1.4.27 /usr/lib/libftd2xx.so
  cd ..
  cp ftd2xx.h  /usr/include
  cp WinTypes.h  /usr/include
  ldconfig -v
  exit
```  
3.2 ftdi_sio clean-up  
  Connect the UPL to your PC.  
  The linux kernel probably will have a built-in module called "ftdi_sio", which will detect a FTDI device and automatically invoke the "usbserial" module and create devices such as "/dev/ttyUSB0"  
  To remove the ftdi_sio module from the running kernel:  
  firstly, list the module with the command line: `sudo lsmod | grep ftdi_sio` (When you try to list the module at the first place, and nothing is listed. You should wait a moment or reconnect the UPL until the module is listed)  
  then, unload the listed items one by one with the command lines:
```
  sudo lsmod | grep ftdi_sio
  sudo rmmod ftdi_sio
  sudo vi /etc/modprobe.d/blacklist.conf
```
  add:
``` 
blacklist ftdi_sio
```
  save  
  Re-connect the UPL to your PC.  
  Re-try: `sudo lsmod | grep ftdi_sio`  
  If there's no output, the driver is successfully installed.  

3.3 Port setting  
  Add the user to obtain the authority for the ft usb device permanently.
```
  sudo vi /etc/udev/rules.d/ft.rules
```
  add the following sentence, modify the "user" as your uesr name.
```
  SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6014", OWNER="user", MODE="0666"
```
  save  
  re-connect the UPL.  
  Use `lsusb` to know the bus id of FT device, and use `ls -al /dev/bus/usb/xxx` to recheck the authority.

Sometimes, when running the scripts on Python 3.10, the terminal reports error "AttributeError: module 'collections' has no attribute 'Mapping'", modify the file ~/.local/lib/python3.10/site-packages/pytz/lazy.py

change "from collections import Mapping" to "from collections.abc import Mapping"

## Ubuntu 20
1. Driver installation  
Download [the D2xx driver](https://ftdichip.com/drivers/d2xx-drivers/). On the download page, just scroll down to the Linux downloading row to download a .tgz compressed file. Then decompress the .tgz file with: tar xfvz XXX.tgz, and you will get a folder called release/.  
In order to install the driver, you just need to follow the instructions in the section "Installing the D2XX shared library and static library" of the file: release/ReadMe.txt. After that, the driver will be successfully installed.  
2. Python installation  
You'd better install the latest python version. You can download the corresponding installation package from the official website: https://www.python.org and install it, or you can directly install it from Terminal with command line like: `sudo apt-get install python3`  
In order to verify if python is successfully installed, you can launch python with the command line: python3. Then inside the launched python, you can execute "import tkinter", if it is executed without error, the python should be workable.  
3. ftdi_sio clean-up  
Connect the UPL to your PC.  
The linux kernel probably will have a built-in module called "ftdi_sio", which will detect a FTDI device and automatically invoke the "usbserial" module and create devices such as "/dev/ttyUSB0"  
To remove the ftdi_sio module from the running kernel:
firstly, list the module with the command line: `sudo lsmod | grep ftdi_sio` (When you try to list the module at the first place, and nothing is listed. You should wait a moment or reconnect the UPL until the module is listed)
then, unload the listed items one by one with the command lines: `sudo rmmod ftdi_sio & sudo rmmod usbserial`  
After that, you can install some prerequisite packages
```
  sudo pip3 install numpy pytz pyvisa-py pyserial ftd2xx matplotlib seaborn
```  
4. Code modification  
If you unfortunately encounter the error saying "...libftd2xx, undefined symbol stime", you need to modify the file: ftd2xx/_ftd2xx_linux.py, that is, just comment out the lines 1508, 1509, 1511, 1512, 1513, 1514 of the file since those lines are related to the undefined symbol stime.  

## Mac OS Mojave 10.14.2
1. Driver installation  
Download [the D2xx driver](https://ftdichip.com/drivers/d2xx-drivers/). On the download page, just scroll down to the mac OS downloading row, click '1.4.27' and 'D2xxHelper' to download the driver and a Helper(for later use). Double-click the driver file and move out the release folder to somewhere, for example the Desktop.  
After downloading, follow the steps below to do the installation:  

  1.1. Open a Terminal window (Finder->Go->Utilities->Terminal).  
  1.2. If the /usr/local/lib directory does not exist, create it:  
```
  sudo mkdir /usr/local/lib
```
  1.3. if the /usr/local/include directory does not exist, create it:  
```
  sudo mkdir /usr/local/include
```
  1.4. Copy the dylib file to /usr/local/lib:  
```
  sudo cp Desktop/release/build/libftd2xx.1.4.27.dylib /usr/local/lib/libftd2xx.1.4.27.dylib
```
  1.5. Make a symbolic link:  
```
  sudo ln -sf /usr/local/lib/libftd2xx.1.4.27.dylib /usr/local/lib/libftd2xx.dylib
```
  1.6. Copy the D2XX include file:  
```
  sudo cp Desktop/release/ftd2xx.h /usr/local/include/ftd2xx.h
```
  1.7. Copy the WinTypes include file:  
```
  sudo cp Desktop/release/WinTypes.h /usr/local/include/WinTypes.h
```
  1.8. You have now successfully installed the D2XX library.  

2. Python installation
You'd better install the latest python version. You can download the corresponding .dmg installation package from [the official website](https://www.python.org)

3. Python package 'ftd2xx' installation and other prerequisite packages installation  
Open a Terminal window. Type the following command:
```
  python3 -m pip install ftd2xx
```
After that, you can install some prerequisite packages  
```
  sudo pip3 install numpy pytz pyvisa-py pyserial ftd2xx matplotlib seaborn
```  
4. Troubleshooting  
If you encounter the error: 'can not open device'. Probably your mac OS version is higher than 10.9, in which case another driver claims the device for use as a virtual COM port.  
To solve the issue, you just need to install the Helper that you download in step 1, then reboot you computer. Then, the error should disappear and read operation will be well fulfilled.
