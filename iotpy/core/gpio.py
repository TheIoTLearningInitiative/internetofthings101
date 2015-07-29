import mraa
import time

class Gpio(object):

    def __init__(self):
        self.x = 0
        if mraa.getPlatformType() == 1:
            self.x = mraa.Gpio(12)

    def toggle(self):
        self.x.dir(mraa.DIR_OUT)
        value = not self.x.read()
        self.x.write(value)
        time.sleep(1)
        self.x.write(not value)

# End of File
