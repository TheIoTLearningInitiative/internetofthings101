#!/usr/bin/python

import ConfigParser
import time
import psutil
import random
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis

class System(object):

    def __init__(self):

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtokentx = self.configuration.get('plotly','streamtokentx')
        self.streamtokenrx = self.configuration.get('plotly','streamtokenrx')

        py.sign_in(self.username, self.apikey)

    def graph(self):

        trace_network_tx = Scatter(
            x=[],
            y=[],
            stream=Stream(
                token=self.streamtokentx,
            ),
            yaxis='tx'
        )

        trace_network_rx = Scatter(
            x=[],
            y=[],
            stream=Stream(
                token=self.streamtokenrx,
            ),
            yaxis='rx'
        )

        layout = Layout(
            title='IoTPy Network Health System',
            yaxis=YAxis(
                title='Bytes'
            ),
            yaxis2=YAxis(
                title='%',
                side='right',
                overlaying="y"
            )
        )

        data = Data([trace_network_tx, trace_network_rx])
        fig = Figure(data=data, layout=layout)

        print py.plot(fig, filename='IoTPy Network Health System', auto_open=False)

        stream_network_tx = py.Stream(self.streamtokentx)
        stream_network_tx.open()

        stream_network_rx = py.Stream(self.streamtokenrx)
        stream_network_rx.open()

        counter = 0

        while True:
            output = psutil.net_io_counters()
            print "Network Bytes Tx %s" % output.bytes_sent
            print "Network Bytes Rx %s" % output.bytes_recv
            stream_network_tx.write({'x': counter, 'y': output.bytes_sent })
            stream_network_rx.write({'x': counter, 'y': output.bytes_recv })
            counter += 1
            time.sleep(0.25)

        stream_network_tx.close()
        stream_network_rx.close()

# End of File
