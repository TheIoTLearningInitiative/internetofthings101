#!/usr/bin/python

import psutil

def dataNetwork():

    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

if __name__ == '__main__':

    print "Hello Internet of Things 101"
    print "Packets: %d " % dataNetwork()

# End of File
