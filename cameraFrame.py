__author__ = 'lmillucci'
import  cv2
import threading

class Frame:

    def __init__(self):
        self.cameraFeed = None
        self.threadLock = threading.RLock()

    def setFrame(self, frame):
        self.cameraFeed = frame

    def getFrame(self):
        return self.cameraFeed

    def lockT(self):
        self.threadLock.acquire()


    def unlockT(self):
        self.threadLock.release()