import face_recognition
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT) # servo motor
GPIO.setwarnings(False)

IR_PIN = 3
GPIO.setup(IR_PIN, GPIO.IN)  #ir sensor


p = GPIO.PWM(2, 50) # GPIO 2 for PWM with 50Hz
p.start(8.8) 

video_capture = cv2.VideoCapture(0)
a=1
if a:
    print("Door open")
    p.ChangeDutyCycle(6)
    time.sleep(0.5)
else:
    print("door close")
    p.start(8.8)

time.sleep(10)
# Release handle to the webcam
p.start(5.8)
GPIO.cleanup()
video_capture.release()
cv2.destroyAllWindows()