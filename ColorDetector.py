from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

class ColorDetector():
    def __init__(self):
        self.camera = PiCamera()
        self.RESOLUTION= (640,480) #(1024,768)#(640,480)
        self.camera.resolution=RESOLUTION
        self.rawCapture = PiRGBArray(camera,size=RESOLUTION)
        time.sleep(0.2)

    def getImage(self):
        self.camera.capture(self.rawCapture, format="bgr")
        self.image = rawCapture.array
        return self.image









if __name__ == "__main__":
    colorDetector=ColorDetector()
    image=colorDetector.getImage()

    cv2.imshow("Image", image)
    cv2.waitKey(0)

