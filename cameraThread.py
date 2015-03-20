__author__ = 'lmillucci'
import threading
import time
import cv2


class CameraImport(threading.Thread):
    def __init__(self, threadID, name, cameraFeed):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.capture = cv2.VideoCapture(0)
        self.cameraFeed = cameraFeed

    def run(self):
        print "Starting " + self.name
        while True:
            self.cameraFeed.lockT()
            print "lock acquisito da cameraThread"
            _, tmp = self.capture.read()

            try:
                self.cameraFeed.setFrame(tmp)
                cv2.imshow("Acquisito", self.cameraFeed.getFrame())
            except:
                print "Risorsa occupata - camera"
            finally:
                self.cameraFeed.unlockT()
                print "lock rilasciato da cameraThread"

            cv2.waitKey(33)

        print "Exiting " + self.name