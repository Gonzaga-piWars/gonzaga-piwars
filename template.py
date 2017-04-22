import time
import RPi.GPIO as GPIO
import pygame
from subprocess import call

class Controller(object):

    #Set up constants
    TURN = 25
    MOVE = 25
    EMERGENT = 14

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TURN,GPIO.OUT)
        servo = GPIO.PWM(TURN,1000)
        servo.start(50)
            
        GPIO.setup(MOVE,GPIO.OUT)
        motor = GPIO.PWM(TURN,1000)
        motor.start(50)
        
        GPIO.setup(EMERGENT,GPIO.OUT)

        stop()
        goStraight()
        GPIO.output(EMERGENT,False)

    def turn(percent):
        servo.ChangeDutyCycle(percent)

    def move(percent):
        motor.ChangeDutyCycle(percent)

    def emergent():
        keys = pygame.key.get_pressed()
        move(50)
        turn(50)
        GPIO.output(EMERGENT,True)
        while keys[pygame.K_RETURN]:
            time.sleep(1)
            keys = pygame.key.get_pressed()
        GPIO.output(EMERGENT,False)
                
