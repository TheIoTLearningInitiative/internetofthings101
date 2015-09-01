Protocols
==

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