from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
    camera.capture('/home/kpomroy/Desktop/CS121/finalProject/photos/image.jpg')
    print("Photo taken")

