Protocols
==

## MQTT

> MQTT is a light-weight protocol used for Machine to Machine (M2M) communication. MQTT used a publish/subscribe message forwarding model built on top of TCP/IP protocol.

### Mosquitto

> Mosquitto is an open source (BSD licensed) message broker that implements the MQ Telemetry Transport protocol versions 3.1 and 3.1.1. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model.

[Mosquitto Homepage](http://mosquitto.org/)


#### Mosquitto Intel® Edison Setup

None

#### Mosquitto Intel® Galileo Setup

    root@galileo:~# wget http://mosquitto.org/files/source/mosquitto-1.3.5.tar.gz
    root@galileo:~# tar xvf mosquitto-1.3.5.tar.gz
    root@galileo:~# cd mosquitto-1.3.5
    root@galileo:~# make WITH_SRV=no
    root@galileo:~# adduser mosquitto
    root@galileo:~# cd test/broker
    root@galileo:~# make test
    root@galileo:~# cd ../../
    root@galileo:~# cp client/mosquitto_pub /usr/bin
    root@galileo:~# cp client/mosquitto_sub /usr/bin
    root@galileo:~# cp lib/libmosquitto.so.1 /usr/lib
    root@galileo:~# cp src/mosquitto /usr/bin

#### Mosquitto Applications

    root@platform:~# mosquitto
    root@platform:~# mosquitto_sub
    root@platform:~# mosquitto_pub

#### Mosquitto Demo Temperature Gauge

Go to http://test.mosquitto.org/gauge/ and execute

    root@platform:~# mosquitto_pub -h test.mosquitto.org -t temp/random -m 23.0

####  Mosquitto MQTT Server/Broker

As subscriber

    root@galileo:~# mosquitto_sub -h test.mosquitto.org -p 1883 -t workshop/galileo
    root@edison:~# mosquitto_sub -h test.mosquitto.org -p 1883 -t workshop/edison

As publisher

    root@galileo:~# mosquitto_pub -h test.mosquitto.org -p 1883 -t workshop/galileo -m "Hello Galileo Users!"
    root@edison:~# mosquitto_pub -h test.mosquitto.org -p 1883 -t workshop/edison -m "Hello Edison Users!"

See output for the following command

    root@platform:~# mosquitto_sub -h test.mosquitto.org -t "#" -v

[Building and running Mosquitto MQTT on Intel Edison](https://software.intel.com/en-us/blogs/2015/02/20/building-and-running-mosquitto-mqtt-on-intel-edison)

## Others

- Bluetoth Low Energy
- BT
- ZigBee
- Z-Wave
- Constrained Application Protocol (CoAP)
