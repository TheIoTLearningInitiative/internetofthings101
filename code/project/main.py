#!/usr/bin/python

import psutil
import paho.mqtt.client as paho
import pywapi
import signal
import sys

def dataNetwork():

    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def on_publish(mosq, obj, msg):

    print("MQTT Message Sent!")


def interruptHandler(signal, frame):
	sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, interruptHandler)

    print "Hello Internet of Things 101"
    packets = dataNetwork()
    print "Network Packets: %d " % packets

    mqttclient = paho.Client()
    mqttclient.on_publish = on_publish
    mqttclient.connect("test.mosquitto.org", 1883, 60)
    mqttclient.publish("IoT101/Project", packets)

    weather = pywapi.get_weather_from_yahoo('MXJO0043', 'metric')
    message = "Reporte del Clima en " + weather['location']['city']
    message = message + ", Temperatura " + weather['condition']['temp'] + " grados centigrados"
    message = message + ", Presion Atmosferica " + weather['atmosphere']['pressure'] + " milibares"
    print message

    while True:
        pass

# End of File
