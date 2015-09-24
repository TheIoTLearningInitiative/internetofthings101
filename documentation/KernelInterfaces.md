Kernel Interfaces
==

## GPIO (General Purpose Input Output)

    root@platform:~# dmesg | grep -i gpio
    root@platform:~# ls /sys/class/gpio/
    root@platform:~# ls /sys/class/gpio/gpio13
    root@platform:~# echo 13 > /sys/class/gpio/export
    root@platform:~# ls /sys/class/gpio/gpio13
    active_low  direction  drive  edge  power  subsystem  uevent  value
    root@platform:~# echo in > /sys/class/gpio/gpio13/direction
    root@platform:~# echo out > /sys/class/gpio/gpio13/direction
    root@platform:~# echo 1 > /sys/class/gpio/gpio13/value
    root@platform:~# cat /sys/class/gpio/gpio13/value    
    root@platform:~# echo 0 > /sys/class/gpio/gpio13/value
    root@platform:~# cat /sys/class/gpio/gpio13/value

## I2C (Inter-IC)

    root@platform:~# dmesg | grep -i i2c
    root@platform:~# ls /sys/class/i2c-dev/
    i2c-0
    root@platform:~# i2cdetect -y -r 0
    root@platform:~# i2cdump -f -y 0 <adress>