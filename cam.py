import picamera
import time



camera = picamera.PiCamera()
#camera.capture('a.jpg')

camera.start_preview()
camera.start_recording('a.h264')
time.sleep(2)
camera.stop_recording()
camera.stop_preview()