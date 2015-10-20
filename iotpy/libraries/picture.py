import commands
import logging
import pygame
import pygame.camera

class Picture(object):

    def __init__(self):

        self.picturepygame = 'output/camerapygame.jpg'
        self.picturefswebcam = 'output/camerafswebcam.jpg'

    def __del__(self):
        pass

    def setup(self):

        try:
            logging.info('Camera Setup')
            pygame.camera.init()
            self.mypicture = pygame.camera.Camera("/dev/video0",(1280,720))
            self.mypicture.start()

            self.fswebcam = 'fswebcam'
            self.fswebcamarguments = ' -r 1280x720 -s brightness=65% -s Contrast=50% -s Gamma=100% --jpeg 100 --no-banner '
            self.fswebcamcommand = self.fswebcam + self.fswebcamarguments + self.picturefswebcam
        except:
            print 'Picture Error'

    def capture(self):
        self.setup()

        image = self.mypicture.get_image()
        pygame.image.save(image, self.picturepygame)
        self.mypicture.stop()

        status, output = commands.getstatusoutput(self.fswebcamcommand)

    def path(self):
        return self.picturefswebcam
