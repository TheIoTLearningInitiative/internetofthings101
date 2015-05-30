#!/usr/bin/python

import argparse

from core.system import System

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='MinnowBoard Bot')
    parser.add_argument('-m', '--modules', help='Module Mode')
    args = parser.parse_args()

    if args.modules == 'system':
        system = System()
        print system.cpuUser()
        print system.cpuSystem()

# End of File
