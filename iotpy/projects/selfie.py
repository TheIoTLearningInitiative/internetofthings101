#!/usr/bin/python

from libraries.picture import Picture
from libraries.tweet import twythonTimelineSet

class Selfie(object):

    def __init__(self):
        self.picture = Picture()

    def share(self):
        self.picture.capture()
        picturepath = self.picture.path()
        twythonTimelineSet("#NuupXe IoTPy Selfie Project!", picturepath)

# End of File
