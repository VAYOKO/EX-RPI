from picamera import PiCamera , Color
from time import sleep
while True:
    camera = PiCamera()
    camera.brightness = 45
    camera.rotation = 90
    camera.resolution = (1280,720)
    camera.framerate = 24
    camera.annotate_background = Color('orange')
    camera.annotate_foreground = Color('yellow')
    camera.annotate_text = "Hello world"
    camera.annotate_text_size = 50
    camera.start_preview()
    camera.start_recording("/home/pi/Desktop/py.h264")
     
    sleep(200)
    camera.stop_recording()
    #camera.capture("/home/pi/Desktop/pic.jpg")
    #camera.stop_preview()


