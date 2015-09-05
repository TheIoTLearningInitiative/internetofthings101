IoTPy
==

> Internet of Things Python

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
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mqttpub
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mqttsub
    root@platform:~/InternetOfThings101/iotpy# python main.py -m mraa
    root@platform:~/InternetOfThings101/iotpy# time python main.py -m opencv    

Run IoTPy Projects

    root@platform:~/InternetOfThings101/iotpy# python main.py -p alive
    root@platform:~/InternetOfThings101/iotpy# python main.py -p climate
    root@platform:~/InternetOfThings101/iotpy# python main.py -p selfie
    root@platform:~/InternetOfThings101/iotpy# python main.py -p system
    root@platform:~/InternetOfThings101/iotpy# python main.py -p weather   

## Setup Edison

Install Pip, Python Package Index to install and manage software packages written in Python

    root@edison:~# opkg install python-pip
    
    root@edison:~# pip install psutil paho-mqtt twython
    root@edison:~# pip install --allow-all-external pywapi --allow-unverified pywapi
    root@edison:~# pip install --allow-all-external plotly --allow-unverified plotly
    
    root@edison:~# opkg install python-numpy opencv python-opencv nano alsa-utils mpg123

## Setup Galileo

Install Pip, Python Package Index to install and manage software packages written in Python

    root@edison:~# curl -O https://bootstrap.pypa.io/get-pip.py
    root@edison:~# python get-pip.py
    
    root@edison:~# curl https://bootstrap.pypa.io/ez_setup.py -o - | python
    
    root@edison:~# pip install psutil paho-mqtt twython
    root@edison:~# pip install --allow-all-external pywapi --allow-unverified pywapi
    root@edison:~# pip install --allow-all-external plotly --allow-unverified plotly
    root@edison:~# opkg install python-numpy opencv python-opencv nano alsa-utils

    root@edison:~# wget http://downloads.sourceforge.net/project/mpg123/mpg123/1.22.4/mpg123-1.22.4.tar.bz2
    root@edison:~# tar xvf mpg123-1.22.4.tar.bz2
    root@edison:~# cd mpg123-1.22.4/
    root@edison:~# ./configure
    root@edison:~# make
    root@edison:~# make install

    Pending To Process

    Not Working!
    opkg update python-pygame

    root@edison:~# setuptools-12.2.tar.gz
    root@edison:~# tar zxf setuptools-12.2.tar.gz
    root@edison:~# python setuptools-12.2/ez_setup.py
    ...
    root@edison:~# wget --no-check-certificate https://bootstrap.pypa.io/ez_setup.py
    root@edison:~# python ez_setup.py --insecure
    ...
