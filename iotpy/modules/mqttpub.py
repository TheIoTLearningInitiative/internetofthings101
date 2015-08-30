
#!/usr/bin/python

import paho.mqtt.client as paho

class MqttPub(object):

    def __init__(self):

        self.client = paho.Client()
        self.client.on_publish = self.on_publish
        self.client.connect("test.mosquitto.org", 1883, 60)

    def on_publish(self, mosq, obj, msg):
        print("Message sent!")

    def write(self):
        self.client.publish("IoTPy/Temperature", "None")

# End of File
