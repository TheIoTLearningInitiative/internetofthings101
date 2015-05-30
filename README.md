# Background

## Intel Developer Zone
> Get going on your Internet of Things project. Find guides, docs, downloads, support, and more.
* Intel® Edison Board
* Intel® Galileo Board
* Sensors
* Intel® IoT Developer Kit

[Intel® Developer Zone Internet of Things](https://software.intel.com/en-us/iot/home)

## Intel® IoT Devkit
> The Intel Development Kit for IoT (IoTDK) is a complete solution to create and test applications for Intel IoT platforms like the Intel® Galileo and Edison maker boards.
* Intel® XDK IoT Edition
* Yocto Project
* Libraries (RMAA & UPM)

[Getting Started with the Intel® IoT Devkit and Intel® XDK IoT Edition](https://software.intel.com/en-us/xdk/docs/getting-started-with-intel-xdk-iot-edition)

## Intel® System Studio
> The explosion of connected smart devices – expected to reach 50 billion by 2020 – is driving unprecedented need for efficient tools to meet shorter development cycles for system software and embedded c applications.
Intel® System Studio 2015 does exactly that, enabling developers to get the most out of Intel® architecture-based systems and embedded applications.I
Intel® System Studio 2015 is a comprehensive and integrated tool suite that provides developers with advanced system tools and technologies to help accelerate the delivery of the next-generation, energy-efficient, high-performance, and reliable embedded and mobile devices.
Intel® System Studio is a fully validated and Intel-supported product optimized for Intel® architecture, while being compatible with open source technologies.
* Host Operating Systems
* Integrated Development Environment
* Intel® C++ Compiler
* Intel® Integrated Performance Primitives Library
* Intel® Math Kernel Library
* Intel® Threading Building Blocks
* Intel-enhanced GDB* Application Debugger
* More ...

**Windows, Android, Linux*, Embedded Linux, Wind River* Linux*, Yocto Project*, Tizen***

[Intel® System Studio](https://software.intel.com/en-us/intel-system-studio)

# Hardware

## Edison

[IoT Intel® Edison Board](https://software.intel.com/en-us/iot/hardware/edison)

[Sparkfun Intel® Edison](https://www.sparkfun.com/categories/272)

[SeedStudio Xadow Wearable Kit For Intel® Edison](http://www.seeedstudio.com/depot/Xadow-Wearable-Kit-For-Intel-Edison-p-2428.html?cPath=84_120)

## Galileo

[IoT Intel® Galileo Board](https://software.intel.com/en-us/iot/hardware/galileo)

[SeedStudio Grove - Starter Kit for Arduino](http://www.seeedstudio.com/depot/Grove-Starter-Kit-for-Arduino-p-1855.html)

## Sensors

### Intel & Seeed Studio
> Grove starter kit plus – Intel IoT Edition for Intel Galileo Gen 2 and Edison

[IoT Intel® Sensors Bring IoT Projects to Life](https://software.intel.com/en-us/iot/hardware/sensors)

[Grove starter kit plus – Intel IoT Edition for Intel Galileo Gen 2 and Edison](http://www.seeedstudio.com/depot/Grove-starter-kit-plus-Intel-IoT-Edition-for-Intel-Galileo-Gen-2-and-Edison-p-1978.html)

### Sparkfun
> SparkFun Electronics (sometimes known by its abbreviation, SFE) is an electronics retailer in Niwot, Colorado, United States. It manufactures and sells microcontroller development boards and breakout boards.

[Sparkfun](https://www.sparkfun.com/)

### Adafruit
> Adafruit Industries is an open-source hardware company founded by Limor Fried in 2005.[1][2] The company designs and manufactures a number of electronics products, sells a wide variety of electronics components, tools, and accessories via its online storefront, and produces a number of learning resources, including written tutorials, introductory videos for children, and the longest running live video electronics show on the Internet.

[Adafruit Industries](https://www.adafruit.com/)

### Others
[Top DIY Electronics Stores Suppliers](http://www.instructables.com/id/Top-DIY-Electronics-Stores-Suppliers/)

# Operating Systems

## Yocto
> It's not an embedded Linux distribution – it creates a custom one for you. The Yocto Project is an open source collaboration project that provides templates, tools and methods to help you create custom Linux-based systems for embedded products regardless of the hardware architecture. It was founded in 2010 as a collaboration among many hardware manufacturers, open-source operating systems vendors, and electronics companies to bring some order to the chaos of embedded Linux development.

[Yocto Project](http://www.yoctoproject.org/)

## Ubilinux
> ubilinux™ is an embedded Linux distribution from Emutex and is based on Debian "Wheezy". It is targeted at embedded devices that have limited memory and storage capabilities.

[Emutexlabs ubilinux™](http://www.emutexlabs.com/ubilinu)

[µCast #21: Installing Ubilinux on the Edison (Windows)](https://www.youtube.com/watch?v=BSnXjuttSgY)

[Sparkfun Loading Debian (Ubilinux) on the Edison](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison)

# Libraries

## Mraa
> Low Level Skeleton Library for IO Communication on GNU/Linux platforms

[Github](https://github.com/intel-iot-devkit/mraa)

## Upm
> UPM is a high level repository for sensors that use mraa

[Github](https://github.com/intel-iot-devkit/upm)

# Getting Started

## Edison

[Intel® Edison Board Get Started Guide](https://software.intel.com/en-us/iot/library/edison-getting-started)

*Windows Device Manager Serial Ports
**Intel Edison Virtual Com Port (COM16)
**USB Serial Port (COM14) < PuTTY

### Others 

[Sparkfun Edison Getting Started](https://learn.sparkfun.com/tutorials/edison-getting-started-guide)

[Instructables A Comprehensive Intel Edison Getting Started Guide](http://www.instructables.com/id/A-Comprehensive-Intel-Edison-Getting-Started-Guide/)

[Codefoster Setting up an Intel Edison](http://www.codefoster.com/edison-setup/)

## Galileo

[Intel® Galileo Board Get Started Guide](https://software.intel.com/en-us/iot/library/galileo-getting-started)

# Workshop

## Edison Yocto

Check your kernel version

    root@edison:~# uname -r
    3.10.17-poky-edison+

Configure your Edison

    root@edison:~# configure_edison
    Configure Edison: Device Name
    Configure Edison: Device Password
    Configure Edison: WiFi Connectio
    
Enable a Opkg feed, update and upgrade existing packages

    root@edison:~# vi /etc/opkg/base-feeds.conf
    src all     http://iotdk.intel.com/repos/1.1/iotdk/all
    src x86 http://iotdk.intel.com/repos/1.1/iotdk/x86
    src i586    http://iotdk.intel.com/repos/1.1/iotdk/i586
    root@edison:~# opkg update
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/all/Packages.
    Updated list of available packages in /var/lib/opkg/all.
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/x86/Packages.
    Updated list of available packages in /var/lib/opkg/x86.
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/i586/Packages.
    Updated list of available packages in /var/lib/opkg/i586.
    root@edison:~# opkg upgrade
    ...
    root@edison:~# 

Install Git, Version Control System, using Opkg

    root@edison:~# opkg install git

Install RMAA and UPM Libraries

    root@edison:~# echo "src mraa-upm http://iotdk.intel.com/repos/1.1/intelgalactic" > /etc/opkg/mraa-upm.conf
    root@edison:~# opkg update
    root@edison:~# opkg install libmraa0
    root@edison:~# opkg install upm

Install IoT Workshop Git Repository

    root@edison:~# git clone https://github.com/xe1gyq/iot.git
    
Run IoT Workshop examples

    root@edison:~# cd iot/iotpy
    root@edison:~# python main.py -m alive
    root@edison:~# python main.py -m system
    root@edison:~# python main.py -m mraa
    root@edison:~# python main.py -m bpta

## Galileo Yocto

Check your kernel version

    root@galileo:~# uname -r
    3.8.7-yocto-standard

Update Opkg sources and upgrade existing packages

    root@galileo:~# opkg update
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/all/Packages.
    Updated list of available packages in /var/lib/opkg/iotdk-all.
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/i586/Packages.
    Updated list of available packages in /var/lib/opkg/iotdk-i586.
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/quark/Packages.
    Updated list of available packages in /var/lib/opkg/iotdk-quark.
    Downloading http://iotdk.intel.com/repos/1.1/iotdk/x86/Packages.
    Updated list of available packages in /var/lib/opkg/iotdk-x86.
    Downloading http://iotdk.intel.com/repos/1.1/intelgalactic/Packages.
    Updated list of available packages in /var/lib/opkg/mraa-upm.
    root@galileo:~# opkg upgrade
    ...
    root@galileo:~# 

Install Python Pip

    https://bootstrap.pypa.io/get-pip.py

Install IoT Workshop Git Repository

    root@galileo:~# git clone https://github.com/xe1gyq/iot.git
    
Run IoT Workshop examples

    root@galileo:~# cd iot/iotpy
    root@galileo:~# python main.py -m alive
    root@galileo:~# python main.py -m system
    root@galileo:~# python main.py -m mraa
    root@galileo:~# python main.py -m bpta

## Intel® XDK IoT Edition
> Create, Test, and Deliver Internet of Things Solutions. Software tool for JavaScript on-board app and HTML5 companion app development

1. Download and Install
2. Sign Up / Log In
3. Create a New Project
4. Optional Install Multicast DNS Service Discovery
   @ Windows
   https://support.apple.com/downloads/DL999/en_US/BonjourPSSetup.exe
   https://developer.apple.com/bonjour/index.html
   @ Linux
   sudo apt-get install libavahi-compat-libdnssd1 avahi-utils
5. Create Manual Connection via IoT Device Manual Connection through the IP Address assigned to your board
6. Yes when asked to update your Board IoT Daemon

## Plot.Ly

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.

[Plot.ly Homepage](https://plot.ly)

# Resources

[Robot Wpi Edu Galileo Images](http://robot.wpi.edu/wiki/index.php/Galileo_Images)

[Coding in your browser: Using the Codebox* IDE with your Intel® Edison](https://software.intel.com/en-us/blogs/2015/05/04/coding-in-your-browser-using-the-codebox-ide-with-your-intel-edison)

# End of File
