import plotly.plotly as py
from plotly.graph_objs import *

class PlotLyLib(object):

    def __init__(self):
        pass

    def graph(self):

        trace0 = Scatter(
            x=[1, 2, 3, 4],
            y=[10, 15, 13, 7]
        )

        trace1 = Scatter(
            x=[1, 2, 3, 4],
            y=[5, 12, 17, 2]
        )

        trace2 = Scatter(
            x=[1, 2, 3, 4],
            y=[2, 9, 3, 17]
        )

        data = Data([trace0, trace1, trace2])

        unique_url = py.plot(data, filename='IoTPy PlotLy')

# End of File
