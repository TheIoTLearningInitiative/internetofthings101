#!/usr/bin/python

import ConfigParser
import paho.mqtt.client as paho
import psutil
import signal
import sys
import time
from twython import Twython

from threading import Thread

import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis

from tendo import singleton

def interruptHandler(signal, frame):
    sys.exit(0)

def on_publish(mosq, obj, msg):
    pass

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

    configuration = ConfigParser.ConfigParser()
    configuration.read('credentials.config')
    username = configuration.get('plotly','username')
    api_key = configuration.get('plotly','api_key')
    stream_token_a = configuration.get('plotly','stream_token_a')
    stream_token_b = configuration.get('plotly','stream_token_b')

    py.sign_in(username, api_key)

    trace1 = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=stream_token_a,
        ),
        yaxis='a'
    )

    trace2 = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=stream_token_b,
        ),
        yaxis='b'
    )

    layout = Layout(
        title='Internet of Things Lab Demo',
        yaxis=YAxis(
            title='A'
        ),
        yaxis2=YAxis(
            title='%',
            side='right',
            overlaying="y"
        )
    )

    data = Data([trace1, trace2])
    fig = Figure(data=data, layout=layout)

    print py.plot(fig, filename='IoTPy Network Health System', auto_open=False)

    counter = 0
    stream_a = py.Stream(self.stream_token_a)
    stream_a.open()
    stream_b = py.Stream(self.stream_token_b)
    stream_b.open()
    time.sleep(5)

    while True:
        stream_data = dataPlotly()
        stream_a.write({'x': counter, 'y': stream_data})
        stream_b.write({'x': counter, 'y': stream_data})
        counter += 1
        time.sleep(0.25)

def twitterHandler():
    configuration = ConfigParser.ConfigParser()
    configuration.read('credentials.config')
    consumer_key = configuration.get('twitter','consumer_key')
    consumer_secret = configuration.get('twitter','consumer_secret')
    access_token = configuration.get('twitter','access_token')
    access_token_secret = configuration.get('twitter','access_token_secret')
    twythonid = Twython(consumer_key, \
                        consumer_secret, \
                        access_token, \
                        access_token_secret)
    return twythonid

if __name__ == '__main__':

    me = singleton.SingleInstance()

    signal.signal(signal.SIGINT, interruptHandler)

    threadx = Thread(target=dataNetworkHandler)
    threadx.start()

    thready = Thread(target=dataMessageHandler)
    thready.start()

    threadz = Thread(target=dataPlotlyHandler)
    threadz.start()
    
    twythonid = twitterHandler()

    while True:
        print "Internet of Things Lab Demo"
        time.sleep(5)

# End of File
