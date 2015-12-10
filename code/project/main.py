#!/usr/bin/python

import psutil
import paho.mqtt.client as paho

def dataNetwork():

    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def on_publish(mosq, obj, msg):

    print("MQTT Message Sent!")

if __name__ == '__main__':

    print "Hello Internet of Things 101"
    packets = dataNetwork()
    print "Packets: %d " % packets
    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    mqttclient.publish("IoT101/Project", packets)

# End of File
