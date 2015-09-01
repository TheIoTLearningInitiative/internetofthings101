Software
==

## Operating Systems

### Yocto

> It's not an embedded Linux distribution – it creates a custom one for you. The Yocto Project is an open source collaboration project that provides templates, tools and methods to help you create custom Linux-based systems for embedded products regardless of the hardware architecture. It was founded in 2010 as a collaboration among many hardware manufacturers, open-source operating systems vendors, and electronics companies to bring some order to the chaos of embedded Linux development.

[Yocto Project](http://www.yoctoproject.org/)

### Ubilinux

> ubilinux™ is an embedded Linux distribution from Emutex and is based on Debian "Wheezy". It is targeted at embedded devices that have limited memory and storage capabilities.

* [Emutexlabs ubilinux™](http://www.emutexlabs.com/ubilinu)
* [µCast #21: Installing Ubilinux on the Edison (Windows)](https://www.youtube.com/watch?v=BSnXjuttSgY)
* [Sparkfun Loading Debian (Ubilinux) on the Edison](https://learn.sparkfun.com/tutorials/loading-debian-ubilinux-on-the-edison)

## Libraries

### Mraa

> C/C++ library with bindings to JavaScript and Python to interface with the I/O on the Intel® Galileo board, Intel® Edison board, and other platforms. With board detection done at runtime, you can create portable code that works across multiple platforms.

* AIO Sensors requiring an ADC value to be read
* I2C Modules using the i2c bus
* SPI Modules using the SPI bus
* GPIO Modules using GPIOs directly
* PWM Modules using a PWM capable GPIO pin
* UART Modules using a serial connection (RX/TX)

[Github](https://github.com/intel-iot-devkit/mraa)

### Upm

> High-level repository for sensors and actuators that use libmraa. In other words, UPM gives you easy function calls to use your sensors, such as reading temperature values or writing data to an LCD screen. With over a hundred sensors and more being added, this library speeds up your development time.

[Github](https://github.com/intel-iot-devkit/upm)

### The IoT Kit Communications (IoTkitcomm) Library

> The IoTkitcomm library allows network-connected devices to easily discover and communicate with each other and the cloud. 

## Integrated Development Environment

> Which programming environment do you prefer? Choose between Arduino*, JavaScript (Intel® XDK IoT Edition), or C/C++ (Eclipse*)

### Arduino IDE

> Run sketches on your Intel® IoT board using the Arduino IDE

### Intel® XDK IoT Edition

> Create, Test, and Deliver Internet of Things Solutions. Software tool for JavaScript on-board app and HTML5 companion app development, create and test applications on Intel®-based IoT platforms. It helps you write applications in C and C++ languages and provides two libraries (mraa and upm), specially designed for the Intel IoT Developer Kit

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

### Intel® IoT Developer Kit Eclipse

> Intel® IoT Developer Kit version of the Eclipse IDE

### Wyliodrin

> Wyliodrin is an online service that allows you to visually create applications for Linux development boards and control them from your browser. You can use their service to program a Raspberry Pi and they've recently partnered with Intel to allow you to program second generation Galileo boards...

## Linux Development

> Tbd

