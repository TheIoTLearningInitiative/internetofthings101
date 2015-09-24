IoTPy
==

> Internet of Things with Python

## Setup Edison

Install Pip, Python Package Index to install and manage software packages written in Python

    root@edison:~# opkg install python-pip
    
    root@edison:~# pip install psutil paho-mqtt twython
    root@edison:~# pip install --allow-all-external pywapi --allow-unverified pywapi
    root@edison:~# pip install --allow-all-external plotly --allow-unverified plotly
    
    root@edison:~# opkg install python-numpy opencv python-opencv nano alsa-utils mpg123

## Setup Galileo

Install Pip, Python Package Index to install and manage software packages written in Python

    root@galileo:~# curl -O https://bootstrap.pypa.io/get-pip.py
    root@galileo:~# python get-pip.py
    
    root@galileo:~# curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    
    root@galileo:~# pip install psutil paho-mqtt twython
    root@galileo:~# pip install --allow-all-external pywapi --allow-unverified pywapi
    root@galileo:~# pip install --allow-all-external plotly --allow-unverified plotly
    root@galileo:~# opkg install python-numpy opencv python-opencv nano alsa-utils

    root@galileo:~# cd
    root@galileo:~# wget http://downloads.sourceforge.net/project/mpg123/mpg123/1.22.4/mpg123-1.22.4.tar.bz2
    root@galileo:~# tar xvf mpg123-1.22.4.tar.bz2
    root@galileo:~# cd mpg123-1.22.4/
    root@galileo:~# ./configure
    root@galileo:~# make
    root@galileo:~# make install

Not Working!

    opkg update python-pygame

## IoTPy Framework

Clone the IoTPy Workshop Git Repository

    root@platform:~# git clone https://github.com/TheIoTLearningInitiative/InternetOfThings101.git
    
Enable IoTPy Workshop credentials

    root@platform:~# cd InternetOfThings101/iotpy
    root@platform:~/InternetOfThings101/iotpy# mkdir configuration
    root@platform:~/InternetOfThings101/iotpy# nano configuration/credentials
    
    # IoTPy File Configuration
    
    [plotly]
    username = 
    apikey = 
    streamtoken = 
    streamtokentx = 
    streamtokenrx = 
    
    [twitter]
    consumer_key = 
    consumer_secret = 
    access_token = 
    access_token_secret = 
    
    [voicerss]
    mashapekey = 
    apikey = 
    
    # End of File
    
    root@platform:~/InternetOfThings101/iotpy# echo <voicerss mashapekey> > configuration/voicerss.ak
    root@platform:~/InternetOfThings101/iotpy# echo <voicerss apikey> > configuration/voicerss.mk    


Run IoTPy Modules

    root@platform:~/InternetOfThings101/iotpy# python main.py -m aio
    root@platform:~/InternetOfThings101/iotpy# python main.py -m bpta
    root@platform:~/InternetOfThings101/iotpy# python main.py -m gpio    
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mqttpub # IoTPy/Temperature
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mqttsub
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mraa
    root@platform:~/InternetOfThings101/iotpy# time python main.py -m opencv

Run IoTPy Projects

    root@platform:~/InternetOfThings101/iotpy# python main.py -p alive # Audio, Twitter
    root@platform:~/InternetOfThings101/iotpy# python main.py -p climate
    root@platform:~/InternetOfThings101/iotpy# python main.py -p selfie
    root@platform:~/InternetOfThings101/iotpy# python main.py -p system
    root@platform:~/InternetOfThings101/iotpy# python main.py -p weather   

