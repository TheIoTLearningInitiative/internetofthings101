#!/usr/bin/python

import numpy as np
import subprocess
import sys
import cv2

from libraries.picture import Picture
from libraries.tweet import twythonTimelineSet

class Faces(object):

    def __init__(self):
        self.picture = Picture()
        self.imageinput = None
        self.cascPath = "libraries/haarcascade_frontalface_alt.xml"
        self.imageoutput = "output/out.jpeg"

    def execute(self):
        faceCascade = cv2.CascadeClassifier(self.cascPath)
        image = cv2.imread(self.imageinput)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        print "Found {0} faces!".format(len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(0)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,'IoT Lab!',(10,100), font, 4,(255,255,255),2)

        cv2.imwrite(self.imageoutput, image)
        return len(faces)

    def share(self):
        command = ['libraries/voicerss.sh', 'es-mx', "Hola! Buscare identificar el numero de personas en la foto! Listos? Comenzamos!"]
        proc = subprocess.call(command)
        self.picture.capture()
        self.imageinput = self.picture.path()
        faces = self.execute()
        messagefaces = "Segun mi algoritmo, hay {0} personas en la foto".format(faces)
        command = ['libraries/voicerss.sh', 'es-mx', messagefaces]
        proc = subprocess.call(command)

# End of File
