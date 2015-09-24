Kernel Interfaces
==

## Galileo

    root@edison:~# ls /sys/class/gpio/
    root@edison:~# cd /sys/class/gpio/gpio13
    root@edison:~# echo 13 > /sys/class/gpio/export
    root@edison:~# cd /sys/class/gpio/gpio13
    root@edison:~# ls /sys/class/gpio/gpio13
    active_low  direction  drive  edge  power  subsystem  uevent  value
    root@edison:~# 
    root@edison:~# 
    root@edison:~# 