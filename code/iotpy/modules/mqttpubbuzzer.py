
#!/usr/bin/python

import paho.mqtt.client as paho
import time
import pyupm_grove as grove

class MqttPubBuzzer(object):

    def __init__(self):

        self.client = paho.Client()
        self.client.on_publish = self.on_publish
        self.client.connect("test.mosquitto.org", 1883, 60)

        self.button = grove.GroveButton(2)

    def on_publish(self, mosq, obj, msg):
        print("Message sent!")

    def write(self):
        while True:
            while self.button.value():
                self.client.publish("IoTPy/Buzzer", "None")
                time.sleep(1)

# End of File

