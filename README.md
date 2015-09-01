

# IoTPy

Install IoTPy Workshop Git Repository

    root@platform:~# git clone https://github.com/xe1gyq/iot.git
    
Run IoTPy Workshop examples

    root@platform:~# cd iot/iotpy
    root@platform:~# python main.py -m <module>
    root@platform:~# python main.py -p <project>

# Software Development Advanced

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
    
    wget http://mosquitto.org/files/source/mosquitto-1.3.5.tar.gz
    tar xvf mosquitto-1.3.5.tar.gz
    cd mosquitto-1.3.5
    make
    adduser mosquitto
    cd test/broker
    make test
    cd ../../
    cp client/mosquitto_pub /usr/bin
    cp client/mosquitto_sub /usr/bin
    cp lib/libmosquitto.so.1 /usr/lib
    cp src/mosquitto /usr/bin

    root@galileo:~/iot/iotpy# ls configuration/
    credentials.config  voicerss.ak  voicerss.mk

## Common

Freeing up space

    root@platform:~# mv /var/cache /home
    root@platform:~# cd /var
    root@platform:~# ln -sf /home/cache cache
    root@platform:~# mv /usr/share /home
    root@platform:~# cd /usr
    root@platform:~# ln -sf /home/share share

# Services

## Intel® IoT Developer Kit Cloud-based Analytics

> Intel provides a cloud-based analytics system for the Internet-of-Things (IoT) that includes resources for the collection and analysis of sensor data that the Intel® IoT Developer Kit provides. Using this service, Intel Galileo/Edison device developers can jump-start data acquisition and analysis without having to invest in large-scale storage and processing capacity.

    # Create an account
      https://dashboard.us.enableiot.com/
    # In Edison / Galileo
    root@galileo:~# iotkit-admin initialize  
    root@galileo:~# iotkit-admin reset-components  
    root@galileo:~# iotkit-admin test
    root@galileo:~# iotkit-admin device-id
    # From https://dashboard.us.enableiot.com/ui/dashboard#/devices, add a New Device
    # From https://dashboard.us.enableiot.com/ui/dashboard#/account, get Activation Code
    root@galileo:~# iotkit-admin activate <Activation Code from Webpage>
    root@galileo:~# iotkit-admin catalog
    root@galileo:~# iotkit-admin register temp temperature.v1.0
    root@galileo:~# iotkit-admin observation temp 35
    root@galileo:~# iotkit-admin observation temp 30

* [Intel® IoT Developer Kit Cloud-based Analytics Homepage](www.enableiot.com)
* [Intel® IoT Developer Kit Cloud-based Analytics User Guide](https://software.intel.com/en-us/intel-iot-developer-kit-cloud-based-analytics-user-guide)

## Plot.Ly

> Plotly is an online analytics and data visualization tool, headquartered in Montreal, Quebec. Plotly provides online graphing, analytics, and stats tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.

    Get an account @ plot.ly
    root@galileo:~# pip install plotly
    root@galileo:~# python -c "import plotly; plotly.tools.set_credentials_file(username='yourusername', api_key='youapikey', stream_ids=['yourstreamid', 'yourotherstreamid'])"

[Plot.ly Homepage](https://plot.ly)

[Plot.ly Getting Started](https://plot.ly/python/getting-started/)

## Temboo

> Create, make, code the Internet of everything. Another API arbiter is called Temboo. This platform acts as a layer on top of third-party APIs, using code snippets to trigger complex processes that run through their cloud platform. Code snippets are added to your device code, perhaps on an Arduino Yun, and present a common methodology of function calls across a broad range of APIs. Code snippets are same format between different APIs. Temboo also tries to shield developers from having to maintain APIs on each device. If you know how to use Temboo for one application, you know how to use it for all.

## Project EON

* [An open-source chart and map framework for realtime data](http://www.pubnub.com/developers/eon/)

# Image Customization

[Intel® Edison Boards Board Support Package (BSP) User Guide](http://www.intel.com/support/edison/sb/CS-035278.htm)

# Links

* [Robot Wpi Edu Galileo Images](http://robot.wpi.edu/wiki/index.php/Galileo_Images)
* [Coding in your browser: Using the Codebox* IDE with your Intel® Edison](https://software.intel.com/en-us/blogs/2015/05/04/coding-in-your-browser-using-the-codebox-ide-with-your-intel-edison)
* [Microsoft Power BI](https://powerbi.microsoft.com/)
* [Google BigQuery](https://cloud.google.com/bigquery/)
* [IBM BlueMix The Digital Innovation Platform](http://www.ibm.com/cloud-computing/bluemix/)
* [microBUS](http://www.mikroe.com/mikrobus/)
* [Soletta Project](https://github.com/solettaproject)
* [Mashery](http://www.mashery.com/)
* [Internet of Things @ Intel®](http://www.intel.com/iot)
* [Developer IBM IoT](https://developer.ibm.com/recipes/?)
* [Wyliodrin](https://www.wyliodrin.com/)
* [non-official blog devoted to Intel® Galileo & Edison development boards
](http://alextgalileo.altervista.org/blog/)

# Key Phrases

Temporal section :)

- Industry Standard Protocols
- Open Environments

# End of File
