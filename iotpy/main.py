#!/usr/bin/python

import argparse

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-m', '--modules', help='Modules Mode')
    parser.add_argument('-p', '--projects', help='Projects Mode')
    args = parser.parse_args()

    if args.modules == 'aio':

        from modules.aio import Aio

        aio = Aio()
        aio.read()

    if args.modules == 'bpta':

        from modules.bpta import Bpta

        bpta = Bpta()
        bpta.data()

    if args.modules == 'gpio':

        from modules.gpio import Gpio

        gpio = Gpio()
        gpio.toggle()

    if args.modules == 'mqttpub':

        from modules.mqttpub import MqttPub

        mqttpub = MqttPub()
        mqttpub.write()

    if args.modules == 'mqttsub':

        from modules.mqttsub import MqttSub

        mqttsub = MqttSub()
        mqttsub.listen()

    if args.modules == 'mraa':

        from modules.mraalib import MraaLib

        mraalib = MraaLib()
        mraalib.version()

    if args.projects == 'alive':

        from projects.alive import Alive

        alive = Alive()
        alive.report()

    if args.projects == 'climate':

        from projects.climate import Climate

        climate = Climate()
        climate.graph()

    if args.projects == 'selfie':

        from projects.selfie import Selfie

        selfie = Selfie()
        selfie.share()

    if args.projects == 'system':

        from projects.system import System

        system = System()
        system.graph()

    if args.projects == 'weather':

        from projects.weather import Weather

        weather = Weather()
        weather.report()

# End of File
