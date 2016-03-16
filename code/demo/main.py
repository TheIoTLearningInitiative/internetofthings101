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
    configuration.read('configuration/credentials.config')
    username = self.configuration.get('plotly','username')
    apikey = self.configuration.get('plotly','apikey')
    streamtokentx = self.configuration.get('plotly','streamtokentx')
    streamtokenrx = self.configuration.get('plotly','streamtokenrx')

    py.sign_in(username, apikey)

    trace_network_tx = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=self.streamtokentx,
        ),
        yaxis='tx'
    )

    trace_network_rx = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=self.streamtokenrx,
        ),
        yaxis='rx'
    )

    layout = Layout(
        title='IoTPy Network Health System',
        yaxis=YAxis(
            title='Bytes'
        ),
        yaxis2=YAxis(
            title='%',
            side='right',
            overlaying="y"
        )
    )

    data = Data([trace_network_tx, trace_network_rx])
    fig = Figure(data=data, layout=layout)

    print py.plot(fig, filename='IoTPy Network Health System', auto_open=False)

    stream_network_tx = py.Stream(self.streamtokentx)
    stream_network_tx.open()

    stream_network_rx = py.Stream(self.streamtokenrx)
    stream_network_rx.open()
    time.sleep(5)

    counter = 0

    while True:
        output = psutil.net_io_counters()
        print "Network Bytes Tx %s" % output.bytes_sent
        print "Network Bytes Rx %s" % output.bytes_recv
        stream_network_tx.write({'x': counter, 'y': output.bytes_sent })
        stream_network_rx.write({'x': counter, 'y': output.bytes_recv })
        counter += 1
        time.sleep(0.25)

    stream_network_tx.close()
    stream_network_rx.close()

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
