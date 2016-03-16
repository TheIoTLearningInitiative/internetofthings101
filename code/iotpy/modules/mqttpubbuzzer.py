
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
        self.temp = grove.GroveTemp(0)

    def on_publish(self, mosq, obj, msg):
        print("Message sent!")

    def write(self):
        while True:
            while self.button.value():
                self.client.publish("IoTPy/Buzzer", "None")
                time.sleep(1)

            for i in range(0, 1):
                celsius = self.temp.value()
                fahrenheit = celsius * 9.0/5.0 + 32.0;
                print "%d degrees Celsius, or %d degrees Fahrenheit" \
                    % (celsius, fahrenheit)
                time.sleep(0.1)

# End of File

