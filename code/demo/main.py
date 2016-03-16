#!/usr/bin/python

import dweepy
import ConfigParser
import paho.mqtt.client as paho
import psutil
import signal
import sys
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

from random import randint
from threading import Thread
from twython import Twython

import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis

from tendo import singleton

def interruptHandler(signal, frame):
    sys.exit(0)

def mqttClientHandler():
    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    return mqttclient

def on_publish(mosq, obj, msg):
    pass

def dataNetwork():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def dataNetworkHandler(mqttclient):
    idDevice = "ThisDevice"
    while True:
        packets = dataNetwork()
        message = idDevice + " " + str(packets)
        #print "MQTT dataNetworkHandler " + message  
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
    apikey = configuration.get('plotly','apikey')
    streamtokentx = configuration.get('plotly','streamtokentx')
    streamtokenrx = configuration.get('plotly','streamtokenrx')

    py.sign_in(username, apikey)

    trace_network_tx = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=streamtokentx,
        ),
        yaxis='tx'
    )

    trace_network_rx = Scatter(
        x=[],
        y=[],
        stream=Stream(
            token=streamtokenrx,
        ),
        yaxis='rx'
    )

    layout = Layout(
        title='IoT Lab Network Health System',
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

    print py.plot(fig, filename='IoT Lab Network Health System', auto_open=False)

    stream_network_tx = py.Stream(streamtokentx)
    stream_network_tx.open()

    stream_network_rx = py.Stream(streamtokenrx)
    stream_network_rx.open()

    counter = 0

    while True:
        output = psutil.net_io_counters()
        randoma = randint(0,100)
        randomb = randint(0,100)
        stream_network_tx.write({'x': counter, 'y': randoma })
        stream_network_rx.write({'x': counter, 'y': randomb })
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

def dataRotary(mqttclient):
    
    knob = grove.GroveRotary(3)
    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
    twythonid = twitterHandler()

    data = {}
    data['alive'] = "1"
    data['warning'] = "0"
    dweepy.dweet_for('IoTHealthSystem', data)
    
    while True:
        abs = knob.abs_value()
        myLcd.setCursor(0,0)
        myLcd.write('Health System')
        myLcd.setColor(0, 128, 0)
        myLcd.setCursor(1,0)
        myLcd.write('Heart Rate %s' % abs)
        while (abs > 950):
            myLcd.setColor(255, 0, 0)
            id = str(randint(0,99))
            status = "0x" + id + " #IoTLab Health System Heart Rate Warning " + str(abs)
            mqttclient.publish("IoTPy/Buzzer", "None")
            twythonid.update_status(status=status)
            data = {}
            data['alive'] = "1"
            data['warning'] = "1"
            data['message'] = status
            dweepy.dweet_for('IoTHealthSystem', data)
            time.sleep(2)
            data['warning'] = "0"
            dweepy.dweet_for('IoTHealthSystem', data)
            break
        time.sleep(0.25)

if __name__ == '__main__':

    me = singleton.SingleInstance()

    mqttclient = mqttClientHandler()

    signal.signal(signal.SIGINT, interruptHandler)

    threadx = Thread(target=dataNetworkHandler, args=(mqttclient,))
    threadx.start()

    thready = Thread(target=dataMessageHandler)
    thready.start()

    threadz = Thread(target=dataPlotlyHandler)
    threadz.start()

    threada = Thread(target=dataRotary, args=(mqttclient,))
    threada.start()

    print "Internet of Things Lab - Health System"

    button = grove.GroveButton(2)

    while True:
        while button.value():
            print "Help Needed!"
            time.sleep(1)
        time.sleep(0.1)

# End of File
