IoTPy
==

> Internet of Things Python

## Setup Edison

Install Pip, Package Management System to install and manage software packages written in Python

    root@edison:~# opkg install python-pip

## Setup Galileo

Install Pip, Package Management System to install and manage software packages written in Python

    root@edison:~# curl -O https://bootstrap.pypa.io/get-pip.py
    root@edison:~# python get-pip.py
    
    root@edison:~# setuptools-12.2.tar.gz
    root@edison:~# tar zxf setuptools-12.2.tar.gz
    root@edison:~# python setuptools-12.2/ez_setup.py
    ...
    root@edison:~# wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py
    root@edison:~# python ez_setup.py --insecure
    ...
    root@edison:~# curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    
    Not Working!
    opkg update python-pygame
    
    Partially Working
    <compile> mpg123 mosquitto
    <python get-pip.py> python-pip
    
    root@edison:~# pip install psutil paho-mqtt
    root@edison:~# pip install --allow-all-external pywapi --allow-unverified pywapi
    root@edison:~# pip install --allow-all-external plotly --allow-unverified plotly
    root@edison:~# opkg install python-numpy opencv python-opencv nano alsa-utils plotly

    Steps to follow

    mpg123
    get source code
    ./configure
    make
    make install
    
    pip
    python get-pip.py
    
    curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    
    https://software.intel.com/en-us/blogs/2015/02/20/building-and-running-mosquitto-mqtt-on-intel-edison
    

    root@galileo:~/iot/iotpy# ls configuration/
    credentials.config  voicerss.ak  voicerss.mk

## IoTPy

Install IoTPy Workshop Git Repository

    root@platform:~# git clone https://github.com/xe1gyq/iot.git
    
Run IoTPy Workshop examples

    root@platform:~# cd iot/iotpy
    root@platform:~# python main.py -m <module>
    root@platform:~# python main.py -p <project>
