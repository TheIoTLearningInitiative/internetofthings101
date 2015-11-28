#!/usr/bin/python

from libraries.picture import Picture
from libraries.tweet import twythonTimelineSet
from random import randint

class Selfie(object):

    def __init__(self):
        self.picture = Picture()

    def share(self):
        self.picture.capture()
        picturepath = self.picture.path()
        id = str(randint(0,99))
        twythonTimelineSet("0x" + id + " #IoT #IoTLearningInit #IoTLearningInitiative IoTPy Selfie Project!", picturepath)

# End of File
