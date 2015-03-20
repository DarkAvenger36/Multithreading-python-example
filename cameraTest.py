__author__ = 'lmillucci'
import cameraThread
import cameraFrame
import threading
import cv2
import time

#oggetto condiviso per l'acquisizione dei frame
cameraFeed = cameraFrame.Frame()
fps_time = 200

thread1 = cameraThread.CameraImport(1, "Thread camera capture", cameraFeed)
#impostando il thread come demone quando termina il main termina anche il thread
thread1.setDaemon(True)
thread1.start()

#Aspetto che il thread abbia iniziato a catturare frame
time.sleep(1)

try:
    while True:

        cameraFeed.lockT()
        print "Lock acquisito - main"

        try:
            cv2.imshow("Finestra",cameraFeed.getFrame())
        except:
            print 'Risorsa occupata - main'
        finally:
            cameraFeed.unlockT()
            print "Lock rilasciato - main"

        cv2.waitKey(fps_time)

except KeyboardInterrupt:
    cv2.destroyAllWindows()

print 'Exiting main thread'


