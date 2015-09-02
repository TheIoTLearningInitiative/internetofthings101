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
