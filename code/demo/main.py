#!/usr/bin/python

import paho.mqtt.client as paho
import psutil
import signal
import sys
import time

from threading import Thread

import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure

from tendo import singleton

username = 'your_plotly_username'
api_key = 'your_api_key'
stream_token = 'your_stream_token'

def interruptHandler(signal, frame):
    sys.exit(0)

def on_publish(mosq, obj, msg):
    pass

def credentialsConfig():
    configuration = ConfigParser.ConfigParser()
    return configuration

def dataNetwork():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def dataNetworkHandler():
    idDevice = "ThisDevice"
    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    while True:
        packets = dataNetwork()
        message = idDevice + " " + str(packets)
        print "MQTT dataNetworkHandler " + message  
        mqttclient.publish("IoT101/Demo", message)
        time.sleep(1)

def on_message(mosq, obj, msg):
    print "MQTT dataMessageHandler %s %s" % (msg.topic, msg.payload)

def dataMessageHandler():
    mqttclient = paho.Client()
    mqttclient.on_message = on_message
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    mqttclient.subscribe("IoT101/Message", 0)
    while mqttclient.loop() == 0:
        pass

def dataPlotly():
    return dataNetwork()

def dataPlotlyHandler():

    py.sign_in(username, api_key)

    trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(
            token=stream_token,
            maxpoints=200
        )
    )

    layout = Layout(
        title='Hello Internet of Things 101 Data'
    )

    fig = Figure(data=[trace1], layout=layout)

    print py.plot(fig, filename='Hello Internet of Things 101 Plotly')

    i = 0
    stream = py.Stream(stream_token)
    stream.open()

    while True:
        stream_data = dataPlotly()
        stream.write({'x': i, 'y': stream_data})
        i += 1
        time.sleep(0.25)

def twitterHandler(configuration):
    configuration.read('credentials.config')
    consumer_key = self.configuration.get('twitter','consumer_key')
    consumer_secret = self.configuration.get('twitter','consumer_secret')
    access_token = self.configuration.get('twitter','access_token')
    access_token_secret = self.configuration.get('twitter','access_token_secret')
    twythonid = Twython(self.consumer_key, \
                         self.consumer_secret, \
                         self.access_token, \
                         self.access_token_secret)
    return twythonid

if __name__ == '__main__':

    me = singleton.SingleInstance()

    signal.signal(signal.SIGINT, interruptHandler)

    credentials = credentialsConfig()

    threadx = Thread(target=dataNetworkHandler)
    threadx.start()

    thready = Thread(target=dataMessageHandler)
    thready.start()

    threadz = Thread(target=dataPlotlyHandler)
    threadz.start()
    
    twythonid = twitterHandler(credentials)

    while True:
        print "Hello Internet of Things 101"
        time.sleep(5)

# End of File
