import time
import RPi.GPIO as GPIO
import pygame
from subprocess import call

class Controller(object):

    #Set up constants
    TURN = 25
    FORWARD = 18
    BACKWARD = 23
    EMERGENT = 14

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TURN,GPIO.OUT)
        servo = GPIO.PWM(TURN,1000)
        servo.start(50)
            
        GPIO.setup(FORWARD,GPIO.OUT)
        GPIO.setup(BACKWARD,GPIO.OUT)
        GPIO.setup(EMERGENT,GPIO.OUT)

        stop()
        goStraight()
        GPIO.output(EMERGENT,False)

    def turn(percent):
        servo.ChangeDutyCycle(percent)

    def moveForward():
        GPIO.output(FORWARD,True)
        GPIO.output(BACKWARD,False)

    def moveBackward():
        GPIO.output(BACKWARD,True)
        GPIO.output(FORWARD,False)

    def stop():
        GPIO.output(FORWARD,False)
        GPIO.output(BACKWARD,False)


    def emergent():
        keys = pygame.key.get_pressed()
        stop()
        turn(50)
        GPIO.output(EMERGENT,True)
        while keys[pygame.K_RETURN]:
            time.sleep(1)
            keys = pygame.key.get_pressed()
        GPIO.output(EMERGENT,False)
                
