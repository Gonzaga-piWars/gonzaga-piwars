import time
import RPi.GPIO as GPIO
import pygame
from subprocess import call

class Controller(object):

    #Set up constants
    RIGHT = 25
    LEFT = 24
    FORWARD = 18
    BACKWARD = 23
    EMERGENT = 14

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(RIGHT,GPIO.OUT)
        GPIO.setup(LEFT,GPIO.OUT)
        GPIO.setup(FORWARD,GPIO.OUT)
        GPIO.setup(BACKWARD,GPIO.OUT)
        GPIO.setup(EMERGENT,GPIO.OUT)

        stop()
        goStraight()
        GPIO.output(EMERGENT,False)

    def turnRight():
        GPIO.output(RIGHT,True)
        GPIO.output(LEFT,False)

    def turnLeft():
        GPIO.output(LEFT,True)
        GPIO.output(RIGHT,False)

    def moveForward():
        GPIO.output(FORWARD,True)
        GPIO.output(BACKWARD,False)

    def moveBackward():
        GPIO.output(BACKWARD,True)
        GPIO.output(FORWARD,False)

    def stop():
        GPIO.output(FORWARD,False)
        GPIO.output(BACKWARD,False)

    def goStraight():
        GPIO.output(RIGHT,False)
        GPIO.output(LEFT,False)

    def emergent():
        keys = pygame.key.get_pressed()
        stop()
        goStraight()
        GPIO.output(EMERGENT,True)
        while keys[pygame.K_RETURN]:
            time.sleep(1)
            keys = pygame.key.get_pressed()
        GPIO.output(EMERGENT,False)
            
