#!/usr/bin/python

import sys

import pyupm_bmpx8x as upmBmpx8x

class Bpta(object):

    def __init__(self):

        try:
            self.bpta = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);
        except:
            print 'Error! BMP180 Barometric Pressure / Temperature / Altitude Sensor'
            sys.exit(1)

    def data(self):

        bptadata = ("Pressure {0} | "
                    "Temperature {1} | "
                    "Altitude {2} | "
                    "Sealevel {3}".format(
                     self.bpta.getPressure(),
                     self.bpta.getTemperature(),
                     self.bpta.getAltitude(),
                     self.bpta.getSealevelPressure()))
        print bptadata

# End of File
