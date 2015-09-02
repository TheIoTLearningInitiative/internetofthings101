Yocto Edison
==

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

