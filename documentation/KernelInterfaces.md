Kernel Interfaces
==

## Galileo

    root@edison:~# ls /sys/class/gpio/
    root@edison:~# ls /sys/class/gpio/gpio13
    root@edison:~# echo 13 > /sys/class/gpio/export
    root@edison:~# ls /sys/class/gpio/gpio13
    root@edison:~# cd gpio13
    root@edison:~# ls
    active_low  direction  drive  edge  power  subsystem  uevent  value
    root@edison:~# 
    root@edison:~# 
    root@edison:~# 