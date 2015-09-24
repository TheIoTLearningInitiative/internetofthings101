Radio Frequency
==

## WiFi

## Bluetoth Low Energy

> Bluetooth low energy (Bluetooth LE, BLE, marketed as Bluetooth Smart[1]) is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group aimed at novel applications in the healthcare, fitness, beacons,[2] security, and home entertainment industries.[3] Compared to Classic Bluetooth, Bluetooth Smart is intended to provide considerably reduced power consumption and cost while maintaining a similar communication range ... *From Wikipedia, the free encyclopedia*

## BlueTooth @ Edison

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

## ZigBee

> ZigBee is a specification for a suite of high-level communication protocols used to create personal area networks built from small, low-power digital radios. ZigBee is based on an IEEE 802.15.4 standard. Its low power consumption limits transmission distances to 10–100 meters line-of-sight, depending on power output and environmental characteristics ... *From Wikipedia, the free encyclopedia*

## Z-Wave

> Z-Wave is a wireless communications specification designed to allow devices in the home (lighting, access controls, entertainment systems and household appliances, for example) to communicate with one another for the purposes of home automation ... *From Wikipedia, the free encyclopedia*
