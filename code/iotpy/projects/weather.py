#!/usr/bin/python

import pywapi
import string
import subprocess

class Weather(object):

    def __init__(self):

        pass

    def report(self):

        result = pywapi.get_weather_from_yahoo('MXJO0043', 'metric')

        message = "Reporte del Clima en " + result['location']['city']
        message = message + ", Temperatura " + result['condition']['temp'] + " grados centigrados"
        message = message + ", Presion Atmosferica " + result['atmosphere']['pressure'] + " milibares"
        message = message + ", Visibilidad " + result['atmosphere']['visibility'] + " kilometros"
        message = message + ", Humedad " + result['atmosphere']['humidity'] + " por ciento"
        message = message + ", El Sol se oculta a las " + result['astronomy']['sunset']
        print message

        command = ['libraries/voicerss.sh', 'es-mx', message]
        proc = subprocess.call(command)

# End of File
