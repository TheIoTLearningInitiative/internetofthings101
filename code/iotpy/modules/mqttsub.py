#!/usr/bin/python

import paho.mqtt.client as paho

class MqttSub(object):

    def __init__(self):

        self.client = paho.Client()
        self.client.on_message = self.on_message
        self.client.connect("test.mosquitto.org", 1883, 60)

    def on_message(self, mosq, obj, msg):
        print "%s %s" % (msg.topic, msg.payload)

    def listen(self):
        self.client.subscribe("IoTPy/#", 0)

        while self.client.loop() == 0:
            pass

# End of File
