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

    if args.modules == 'mraa':

        from modules.mraalib import MraaLib

        mraalib = MraaLib()
        mraalib.version()

    if args.projects == 'alive':

        from projects.alive import Alive

        alive = Alive()
        alive.report()

    if args.projects == 'system':

        from projects.system import System

        system = System()
        print system.cpuUser()
        print system.cpuSystem()

    if args.projects == 'climate':

        from projects.climate import Climate

        climate = Climate()
        climate.graph()

    if args.projects == 'health':

        from projects.health import Health

        health = Health()
        health.graph()

# End of File
