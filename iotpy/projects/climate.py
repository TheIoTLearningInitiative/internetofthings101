#!/usr/bin/python

import ConfigParser
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import pyupm_bmpx8x as upmBmpx8x

class Climate(object):

    def __init__(self):

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

        self.bpta = upmBmpx8x.BMPX8X(1, upmBmpx8x.ADDR);

    def graph(self):

        trace1 = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
                maxpoints=200
            )
        )

        layout = Layout(
            title="IoTPy Streaming Temperature Data"
        )

        fig = Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='IotPy Streaming Temperature', auto_open=False)
        i = 0
        stream = py.Stream(self.streamtoken)
        stream.open()

        while True:
            temperaturedata = self.bpta.getTemperature()
            stream.write({'x': i, 'y': temperaturedata})
            i += 1
            # delay between stream posts
            time.sleep(0.25)

# End of File
