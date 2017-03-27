import time
import RPI.GPIO as GPIO
from subprocess import call

#Set up constants
RIGHT = 25
LEFT = 24
FORWARD = 18
BACKWARD = 23

run = True

GPIO.setup(RIGHT,GPIO.OUT)
GPIO.setup(LEFT,GPIO.OUT)
GPIO.setup(FORWARD,GPIO.OUT)

GPIO.output(FORWARD,True)
time.sleep(5)
GPIO.output(RIGHT,True)
time.sleep(.005)
GPIO.output(RIGHT,False)
time.sleep(5)
GPIO.output(LEFT,True)
time.sleep(.005)
time.sleep(2)
GPIO.output(FORWARD,False)

def turnRight():

def turnLeft():

def moveForward():

def moveBackward():
