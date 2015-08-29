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

        stream_temperature = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
            )
        )

        layout = Layout(
            title="IoTPy Climate"
        )

        this = Figure(data=[stream_temperature], layout=layout)
        py.plot(this, filename='IotPy Climate', auto_open=False)

        stream = py.Stream(self.streamtoken)
        stream.open()

        counter = 0

        while True:
            temperaturedata = self.bpta.getTemperature()
            stream.write({'x': counter, 'y': temperaturedata})
            counter += 1
            time.sleep(0.25)

# End of File
