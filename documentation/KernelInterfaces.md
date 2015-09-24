Kernel Interfaces
==

## Galileo

    root@platform:~# ls /sys/class/gpio/
    root@platform:~# ls /sys/class/gpio/gpio13
    root@platform:~# echo 13 > /sys/class/gpio/export
    root@platform:~# ls /sys/class/gpio/gpio13
    active_low  direction  drive  edge  power  subsystem  uevent  value
    root@platform:~# echo out > /sys/class/gpio/gpio13
    root@platform:~# 
    root@platform:~# 