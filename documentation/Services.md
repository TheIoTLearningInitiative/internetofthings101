Services
==

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
