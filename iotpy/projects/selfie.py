#!/usr/bin/python

from libraries.picture import Picture

class Selfie(object):

    def __init__(self):
        self.picture = Picture()        

    def share(self):
        self.picture.capture()

# End of File
