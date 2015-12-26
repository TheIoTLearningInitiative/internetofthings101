#!/usr/bin/python

import paho.mqtt.client as paho
import psutil
import signal
import sys
import time

from threading import Thread

def interruptHandler(signal, frame):
    sys.exit(0)

def dataNetwork():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def dataNetworkHandler():
    idDevice = "IoT101Device"
    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    while True:
        packets = dataNetwork()
        message = idDevice + " " + str(packets)
        print "dataNetworkHandler " + message  
        mqttclient.publish("IoT101/Project", message)
        time.sleep(1)

def on_publish(mosq, obj, msg):
    pass

if __name__ == '__main__':

    signal.signal(signal.SIGINT, interruptHandler)

    threadx = Thread(target=dataNetworkHandler)
    threadx.start()

    while True:
        print "Hello Internet of Things 101"
        time.sleep(1)
        

# End of File


