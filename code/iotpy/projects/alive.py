#!/usr/bin/python

import subprocess
from libraries.tweet import twythonTimelineSet

class Alive(object):

    def __init__(self):
        pass

    def report(self):
        message = 'Hello Internet of Things Python Learners, Now another test!'
        print message
        twythonTimelineSet(message, None)
        command = ['libraries/voicerss.sh', 'en-us', message]
        proc = subprocess.call(command)

# End of File
