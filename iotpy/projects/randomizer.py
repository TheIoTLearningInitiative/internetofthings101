#!/usr/bin/python

import ConfigParser
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
from random import randint

class Randomizer(object):

    def __init__(self):

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

    def graph(self):

        stream_randomizer = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
            )
        )

        layout = Layout(
            title="IoTPy Randomizer"
        )

        this = Figure(data=[stream_randomizer], layout=layout)
        py.plot(this, filename='IotPy Randomizer', auto_open=False)

        stream = py.Stream(self.streamtoken)
        stream.open()
        time.sleep(5)

        counter = 0

        while True:
            randomizerdata = randint(0,100)
            stream.write({'x': counter, 'y': randomizerdata})
            counter += 1
            time.sleep(0.25)

# End of File
