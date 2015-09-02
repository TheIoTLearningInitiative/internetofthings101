Software Development Advanced
==

## Yocto Edison Advanced

Install Pip, Package Management System to install and manage software packages written in Python

    root@edison:~# opkg install python-pip

## Yocto Galileo Advanced

Install Pip, Package Management System to install and manage software packages written in Python

    https://bootstrap.pypa.io/get-pip.py
    setuptools-12.2.tar.gz
    tar zxf setuptools-12.2.tar.gz
    python setuptools-12.2/ez_setup.py
    ...
    wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py
    python ez_setup.py --insecure
    
    Not Working!
    opkg update python-pygame
    
    Partially Working
    <compile> mpg123 mosquitto
    <python get-pip.py> python-pip
    pip install psutil paho-mqtt
    pip install --allow-all-external pywapi --allow-unverified pywapi
    pip install --allow-all-external plotly --allow-unverified plotly
    
    Working!
    opkg install python-numpy opencv python-opencv nano alsa-utils plotly

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
