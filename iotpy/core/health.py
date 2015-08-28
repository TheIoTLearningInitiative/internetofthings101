import ConfigParser
import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import psutil
import random

class Health(object):

    def __init__(self):

        self.configuration = ConfigParser.ConfigParser()
        self.configuration.read('configuration/credentials.config')
        self.username = self.configuration.get('plotly','username')
        self.apikey = self.configuration.get('plotly','apikey')
        self.streamtoken = self.configuration.get('plotly','streamtoken')

        py.sign_in(self.username, self.apikey)

    def graph(self):

        trace1 = Scatter(
            x=[],
            y=[],
            stream=dict(
                token=self.streamtoken,
                maxpoints=4
            )
        )

        layout = Layout(
            title="IoTPy Streaming Cpu Data"
        )

        fig = Figure(data=[trace1], layout=layout)
        py.plot(fig, filename='IotPy Streaming Cpu', auto_open=False)
        i = 0
        stream = py.Stream(self.streamtoken)
        stream.open()

        while True:
            cpudata = psutil.cpu_times_percent(interval=1, percpu=False)
            cpudata = random.randint(0,100)
            stream.write({'x': i, 'y': cpudata})
            i += 1
            # delay between stream posts
            time.sleep(0.25)

# End of File
