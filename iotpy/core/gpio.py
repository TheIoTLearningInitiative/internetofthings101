import mraa

class Gpio(object):

    def __init__(self):
        pass

    def toggle(self):
        x = mraa.Gpio(13)
        x.dir(mraa.DIR_OUT)
        value = not x.read()
        x.write(value)

# End of File
