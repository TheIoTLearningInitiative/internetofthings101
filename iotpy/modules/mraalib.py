#!/usr/bin/python

import mraa

class MraaLib(object):

    def __init__(self):
        pass

    def version(self):
        print (mraa.getVersion())
        print (mraa.getPlatformName())
        print (mraa.getPlatformType())

# End of File
