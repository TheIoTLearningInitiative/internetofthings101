#!/usr/bin/python

import mraa
import time

class Aio(object):

    def __init__(self):
        self.x = mraa.Aio(0)
        self.x.setBit(10)

    def read(self):
        self.x.read()
        print ("%.5f" % self.x.readFloat())

# End of File
