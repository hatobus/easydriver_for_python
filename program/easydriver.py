import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT)
#23 is DIR pin
GPIO.setup(24,GPIO.OUT)
#24 is STEP pin

class stpmotor():
    def __init__(self):
        pass 

    def Drive(self, rpm):
        one_rot = 200
        l = rpm * one_rot
        delay = 30/(2*float(l))
        steps = l/6 #rotato to 5 sec
        for x in range(1,steps):
            GPIO.output(24,GPIO.HIGH)
            time.sleep(delay)
            GPIO.output(24,GPIO.LOW)
            time.sleep(delay)

    def inv_Direction(self):
        GPIO.output(23, not GPIO.input(23))

if __name__ == '__main__':
    Motor = stpmotor()
    Motor.Drive(YOUR_VALUE)
    GPIO.cleanup()
