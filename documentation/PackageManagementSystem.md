## OPKG Edison

Update Opkg Repositories

    root@edison:~# opkg update
    Downloading http://iotdk.intel.com/repos/1.5/intelgalactic/Packages.
    Updated list of available packages in /var/lib/opkg/iotkit.
    root@edison:~#

Try to install nano command line editor

    root@edison:~# opkg install nano

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

Install nano command line editor

    root@edison:~# opkg install nano

Install Git, Version Control System

    root@edison:~# opkg install git

Check if RMAA and UPM Libraries are installed

    root@galileo:~# opkg list-installed | grep mraa
    root@galileo:~# opkg list-installed | grep upm

## OPKG Galileo

Update Opkg sources, we will not upgrade to avoid consuming disk space

    root@galileo:~# opkg update
    ...
    root@galileo:~# 

Install Git, Version Control System

    root@galileo:~# opkg install git

Check if RMAA and UPM Libraries are installed

    root@galileo:~# opkg list-installed | grep mraa
    root@galileo:~# opkg list-installed | grep upm
