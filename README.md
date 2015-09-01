

# Software Development Basics

## HowTo

- Arduino
- Intel XDK
- Eclipse
- Linux 

| | Arduino | Visual Programming | Node.JS | C / C++ |  C / C++ / Python / NodeJS
|-----------------|---------|------------------|--------|-------|----------------|
| Target Audience | Maker | Beginner | Intermediate | Advanced | Advanced |
| IDE | Arduino IDE | Wyliodrin | Intel XDK | Eclipse IDE | None |
| Platform | Win / Mac / Linux | Browser | Win / Mac / Linux | Win / Mac /Linux | Edison |

## Flashing Edison

At the Edison

    U-Boot 2014.04 (Aug 20 2014 - 16:08:32)
       Watchdog enabled
    DRAM:  980.6 MiB
    MMC:   tangier_sdhci: 0
    In:    serial
    Out:   serial
    Err:   serial
    Hit any key to stop autoboot:  0
    boot > run do_ota
    reading ota_update.scr
    14747 bytes read in 31 ms (463.9 KiB/s)
    ## Executing script at 00100000
    ...
 
At the host

    C:\Users\aarcemor\Downloads\edison-image-ww25.5-15>flashall.bat

[All your Intel® Edison Board Downloads in One Spot!](https://software.intel.com/en-us/iot/hardware/edison/downloads)

# Flashing Galileo

[All the Intel® Galileo Board Downloads in One Spot!](https://software.intel.com/en-us/iot/hardware/galileo/downloads)

## Yocto Edison Basic

Check your kernel version

    root@edison:~# uname -r
    3.10.17-poky-edison+

Configure your Edison

    root@edison:~# configure_edison
    Configure Edison: Device Name
    Configure Edison: Device Password
    Configure Edison: WiFi Connection

Check IP address assigned

    root@edison:~# ifconfig
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
    wlan      Link encap:Ethernet  HWaddr 00:1C:C0:AE:B5:E6  
              inet addr:192.168.1.74  Bcast:192.168.0.255  Mask:255.255.255.0

Update Opkg Repositories

    root@edison:~# opkg update
    Downloading http://iotdk.intel.com/repos/1.5/intelgalactic/Packages.
    Updated list of available packages in /var/lib/opkg/iotkit.
    root@edison:~#

Enable a Opkg feed and update package list, we will not upgrade to avoid consuming disk space

    root@edison:~# vi /etc/opkg/base-feeds.conf # Add the below lines to the opened file
    src/gz all http://repo.opkg.net/edison/repo/all
    src/gz edison http://repo.opkg.net/edison/repo/edison
    src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
    root@edison:~# opkg update
    Downloading http://repo.opkg.net/edison/repo/all/Packages.gz.
    Inflating http://repo.opkg.net/edison/repo/all/Packages.gz.
    Updated list of available packages in /var/lib/opkg/all.
    Downloading http://repo.opkg.net/edison/repo/edison/Packages.gz.
    Inflating http://repo.opkg.net/edison/repo/edison/Packages.gz.
    Updated list of available packages in /var/lib/opkg/edison.
    Downloading http://repo.opkg.net/edison/repo/core2-32/Packages.gz.
    Inflating http://repo.opkg.net/edison/repo/core2-32/Packages.gz.
    Updated list of available packages in /var/lib/opkg/core2-32.
    Downloading http://iotdk.intel.com/repos/1.5/intelgalactic/Packages.
    Updated list of available packages in /var/lib/opkg/iotkit.
    root@edison:~# 

Install Git, Version Control System

    root@edison:~# opkg install git

Install RMAA and UPM Libraries

    root@edison:~# opkg install libmraa0
    root@edison:~# opkg install upm

In case only WiFi was configure, configure also password to enable SSH on the wireless interface

    root@edison:~# configure_edison --password
    
    Configure Edison: Device Password
    
    Enter a new password (leave empty to abort)
    This will be used to connect to the access point and login to the device.
    Password:       ********
    Please enter the password again:        ********
    First-time root password setup complete. Enabling SSH on WiFi interface.
    The device password has been changed.

## Yocto Galileo Basic

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

# Protocols

## MQTT

> MQTT is a light-weight protocol used for Machine to Machine (M2M) communication. MQTT used a publish/subscribe message forwarding model built on top of TCP/IP protocol.

### Mosquitto Applications

    root@edison:~# mosquitto
    root@edison:~# mosquitto_sub
    root@edison:~# mosquitto_pub

### Mosquitto Demo Temperature Gauge

Go to http://test.mosquitto.org/gauge/ and execute

    root@edison:~# mosquitto_pub -h test.mosquitto.org -t temp/random -m 23.0

###  Mosquitto MQTT Server/Broker

As subscriber

    root@galileo:~# mosquitto_sub -h test.mosquitto.org -p 1883 -t workshop/galileo
    root@edison:~# mosquitto_sub -h test.mosquitto.org -p 1883 -t workshop/edison

As publisher

    root@galileo:~# mosquitto_pub -h test.mosquitto.org -p 1883 -t workshop/galileo -m "Hello Galileo Users!"
    root@edison:~# mosquitto_pub -h test.mosquitto.org -p 1883 -t workshop/edison -m "Hello Edison Users!"

See output for the following command

    root@edison:~# mosquitto_sub -h test.mosquitto.org -t "#" -v

[Building and running Mosquitto MQTT on Intel Edison](https://software.intel.com/en-us/blogs/2015/02/20/building-and-running-mosquitto-mqtt-on-intel-edison)

## Others

- Bluetoth Low Energy
- BT
- ZigBee
- Z-Wave
- CoAP

# IoTPy

Install IoTPy Workshop Git Repository

    root@platform:~# git clone https://github.com/xe1gyq/iot.git
    
Run IoTPy Workshop examples

    root@platform:~# cd iot/iotpy
    root@platform:~# python main.py -m <module>
    root@platform:~# python main.py -p <project>

# Software Development Advanced

## Yocto Edison Advanced

Install Pip, Package Management System to install and manage software packages written in Python

    root@edison:~# opkg install python-pip

## Yocto Galileo Advanced

Install Pip, Package Management System to install and manage software packages written in Python

    https://bootstrap.pypa.io/get-pip.py
    setuptools-12.2.tar.gz
    tar zxf setuptools-12.2.tar.gz
    python setuptools-12.2/ez_setup.py
    ...
    wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py
    python ez_setup.py --insecure
    
    Not Working!
    opkg update python-pygame
    
    Partially Working
    <compile> mpg123 mosquitto
    <python get-pip.py> python-pip
    pip install psutil paho-mqtt
    pip install --allow-all-external pywapi --allow-unverified pywapi
    pip install --allow-all-external plotly --allow-unverified plotly
    
    Working!
    opkg install python-numpy opencv python-opencv nano alsa-utils plotly

    Steps to follow

    mpg123
    get source code
    ./configure
    make
    make install
    
    pip
    python get-pip.py
    
    curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    
    https://software.intel.com/en-us/blogs/2015/02/20/building-and-running-mosquitto-mqtt-on-intel-edison
    
    wget http://mosquitto.org/files/source/mosquitto-1.3.5.tar.gz
    tar xvf mosquitto-1.3.5.tar.gz
    cd mosquitto-1.3.5
    make
    adduser mosquitto
    cd test/broker
    make test
    cd ../../
    cp client/mosquitto_pub /usr/bin
    cp client/mosquitto_sub /usr/bin
    cp lib/libmosquitto.so.1 /usr/lib
    cp src/mosquitto /usr/bin

    root@galileo:~/iot/iotpy# ls configuration/
    credentials.config  voicerss.ak  voicerss.mk

## Common

Freeing up space

    root@platform:~# mv /var/cache /home
    root@platform:~# cd /var
    root@platform:~# ln -sf /home/cache cache
    root@platform:~# mv /usr/share /home
    root@platform:~# cd /usr
    root@platform:~# ln -sf /home/share share

# Services

## Intel® IoT Developer Kit Cloud-based Analytics

> Intel provides a cloud-based analytics system for the Internet-of-Things (IoT) that includes resources for the collection and analysis of sensor data that the Intel® IoT Developer Kit provides. Using this service, Intel Galileo/Edison device developers can jump-start data acquisition and analysis without having to invest in large-scale storage and processing capacity.

    # Create an account
      https://dashboard.us.enableiot.com/
    # In Edison / Galileo
    root@galileo:~# iotkit-admin initialize  
    root@galileo:~# iotkit-admin reset-components  
    root@galileo:~# iotkit-admin test
    root@galileo:~# iotkit-admin device-id
    # From https://dashboard.us.enableiot.com/ui/dashboard#/devices, add a New Device
    # From https://dashboard.us.enableiot.com/ui/dashboard#/account, get Activation Code
    root@galileo:~# iotkit-admin activate <Activation Code from Webpage>
    root@galileo:~# iotkit-admin catalog
    root@galileo:~# iotkit-admin register temp temperature.v1.0
    root@galileo:~# iotkit-admin observation temp 35
    root@galileo:~# iotkit-admin observation temp 30

* [Intel® IoT Developer Kit Cloud-based Analytics Homepage](www.enableiot.com)
* [Intel® IoT Developer Kit Cloud-based Analytics User Guide](https://software.intel.com/en-us/intel-iot-developer-kit-cloud-based-analytics-user-guide)

## Plot.Ly

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.

    Get an account @ plot.ly
    root@galileo:~# pip install plotly
    root@galileo:~# python -c "import plotly; plotly.tools.set_credentials_file(username='yourusername', api_key='youapikey', stream_ids=['yourstreamid', 'yourotherstreamid'])"

[Plot.ly Homepage](https://plot.ly)

[Plot.ly Getting Started](https://plot.ly/python/getting-started/)

## Temboo

> Create, make, code the Internet of everything. Another API arbiter is called Temboo. This platform acts as a layer on top of third-party APIs, using code snippets to trigger complex processes that run through their cloud platform. Code snippets are added to your device code, perhaps on an Arduino Yun, and present a common methodology of function calls across a broad range of APIs. Code snippets are same format between different APIs. Temboo also tries to shield developers from having to maintain APIs on each device. If you know how to use Temboo for one application, you know how to use it for all.

## Project EON

* [An open-source chart and map framework for realtime data](http://www.pubnub.com/developers/eon/)

# Image Customization

[Intel® Edison Boards Board Support Package (BSP) User Guide](http://www.intel.com/support/edison/sb/CS-035278.htm)

# Links

* [Robot Wpi Edu Galileo Images](http://robot.wpi.edu/wiki/index.php/Galileo_Images)
* [Coding in your browser: Using the Codebox* IDE with your Intel® Edison](https://software.intel.com/en-us/blogs/2015/05/04/coding-in-your-browser-using-the-codebox-ide-with-your-intel-edison)
* [Microsoft Power BI](https://powerbi.microsoft.com/)
* [Google BigQuery](https://cloud.google.com/bigquery/)
* [IBM BlueMix The Digital Innovation Platform](http://www.ibm.com/cloud-computing/bluemix/)
* [microBUS](http://www.mikroe.com/mikrobus/)
* [Soletta Project](https://github.com/solettaproject)
* [Mashery](http://www.mashery.com/)
* [Internet of Things @ Intel®](http://www.intel.com/iot)
* [Developer IBM IoT](https://developer.ibm.com/recipes/?)
* [Wyliodrin](https://www.wyliodrin.com/)
* [non-official blog devoted to Intel® Galileo & Edison development boards
](http://alextgalileo.altervista.org/blog/)

# Key Phrases

Temporal section :)

- Industry Standard Protocols
- Open Environments

# End of File
