#!/usr/bin/python

import paho.mqtt.client as paho
import time
import pyupm_buzzer as upmBuzzer

class MqttSubBuzzer(object):

    def __init__(self):

        self.client = paho.Client()
        self.client.on_message = self.on_message
        self.client.connect("test.mosquitto.org", 1883, 60)
        self.buzzer = upmBuzzer.Buzzer(5)

        self.chords = [upmBuzzer.SI, upmBuzzer.SI]

    def on_message(self, mosq, obj, msg):
        print "%s %s" % (msg.topic, msg.payload)
        print self.buzzer.name()
        for chord_ind in range (0,1):
            print self.buzzer.playSound(self.chords[chord_ind], 
1000000)
            time.sleep(0.01)

    def listen(self):
        self.client.subscribe("IoTPy/Buzzer", 0)

        while self.client.loop() == 0:
            pass

# End of File
