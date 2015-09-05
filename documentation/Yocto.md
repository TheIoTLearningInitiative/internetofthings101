Yocto
==

## Yocto Edison

Check your kernel version

    root@edison:~# uname -r
    3.10.17-poky-edison+

Configure your Edison

    root@edison:~# configure_edison
    Configure Edison: Device Name
    Configure Edison: Device Password
    Configure Edison: WiFi Connection

In case only WiFi was configure, configure also password to enable SSH on the wireless interface

    root@edison:~# configure_edison --password
    
    Configure Edison: Device Password
    
    Enter a new password (leave empty to abort)
    This will be used to connect to the access point and login to the device.
    Password:       ********
    Please enter the password again:        ********
    First-time root password setup complete. Enabling SSH on WiFi interface.
    The device password has been changed.

Check IP address assigned

    root@edison:~# ifconfig
    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
    wlan      Link encap:Ethernet  HWaddr 00:1C:C0:AE:B5:E6  
              inet addr:192.168.1.74  Bcast:192.168.0.255  Mask:255.255.255.0


### BlueTooth

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