Software Development
==

## Yocto Galileo

Check your kernel version

    root@galileo:~# uname -r
    3.8.7-yocto-standard

Check IP address assigned

    root@edison:~# ifconfig
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
    eth0      Link encap:Ethernet  HWaddr 00:1C:C0:AE:B5:E6  
              inet addr:192.168.1.74  Bcast:192.168.0.255  Mask:255.255.255.0

Update Opkg sources, we will not upgrade to avoid consuming disk space

    root@galileo:~# opkg update
    ...
    root@galileo:~# 

Install Git, Version Control System

    root@galileo:~# opkg install git

Install RMAA and UPM Libraries

    root@galileo:~# opkg install libmraa0
    root@galileo:~# opkg install upm

## BlueTooth Edison

More information at [Intel Edison Bluetooth Guide](http://download.intel.com/support/edison/sb/edisonbluetooth_331704004.pdf)

    root@galileo:~# rfkill unblock bluetooth
    root@galileo:~# bluetoothctl
    [bluetooth]# scan on
    [bluetooth]# scan off
    [bluetooth]# pair 40:78:6A:26:4A:C2
    [bluetooth]# connect 40:78:6A:26:4A:C2
    [bluetooth]# paired-devices
    [bluetooth]# info 40:78:6A:26:4A:C2
    [bluetooth]# exit
    root@edison:~# rfcomm bind - 40:78:6A:26:4A:C2 1
    root@edison:~# ls /dev/rfcomm0

## Python

### Python Installation

Check Python is installed

    root@platform:~# python --version

### Python Mraa Hello Internet of Things

Create your first Python script, the common "Hello Internet of Things" example

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Hello Internet of Things
print 'Hello Internet of Things @ Python'

# End of Python Script
```
    root@platform:~# python iot.py

### Python Mraa Version

Let's get the version of mraa library we installed

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Libraries
import mraa

# Mraa Version
print (mraa.getVersion())
print (mraa.getPlatformName())
print (mraa.getPlatformType())

# End of Python Script
```
    root@platform:~# python iot.py

### Python Mraa Analog Input Output (AIO)

Let's work with Analog Input Output

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Libraries
import mraa

# Mraa Aio
aioline = mraa.Aio(0)
aioline.setBit(10)
aioline.read()
print ("%.5f" % aioline.readFloat())
# End of Python Script
```
    root@platform:~# python iot.py

### Python Mraa Inter-Integrated Circuit (I2C)

Let's work with Inter-Integrated Circuit protocol

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Libraries
import mraa

# Mraa I2C
if mraa.getPlatformType() == 1:
    i2cline = mraa.I2c(0)
if mraa.getPlatformType() == 2:
    i2cline = mraa.I2c(1)
i2cline.address(0x6b)
print i2cline.readReg(0x6b, 0x80)

# End of Python Script
```
    root@platform:~# python iot.py

### Python Mraa General Purpose Input Output (GPIO) Direction Output

Let's work with General Purpose Input Output, Direction Output

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Libraries
import mraa

# Mraa GPIO Direction Output
if mraa.getPlatformType() == 1:
    gpioline = mraa.Gpio(12)
if mraa.getPlatformType() == 2:
    gpioline = mraa.Gpio(44)
gpioline.dir(mraa.DIR_OUT)
gpionextvalue = not gpioline.read()
gpioline.write(gpionextvalue)
time.sleep(1)
gpioline.write(not gpionextvalue)

# End of Python Script
```
    root@platform:~# python iot.py

### Python Mraa Universal Asynchronous Receiver/Transmitter (UART)

Let's work with Universal Asynchronous Receiver/Transmitter

    root@platform:~# vi iot.py

```python
#!/usr/bin/python

# Libraries
import mraa

# Mraa UART
uartdevice = mraa.Uart(0)
print uartdevice.getDevicePath()

# End of Python Script
```
    root@platform:~# python iot.py
