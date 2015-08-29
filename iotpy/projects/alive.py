#!/usr/bin/python

import subprocess

class Alive(object):

    def __init__(self):
        pass

    def report(self):
        message = 'Hello Internet of Things Python Learners, What will you make?'
        print message
        command = ['libraries/voicerss.sh', 'en-us', message]
        proc = subprocess.call(command)

# End of File
