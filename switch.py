import os
import time
import math
import RPi.GPIO as GPIO

switch = 18
led = 16
led_status = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
    
def swLed(ev = None):
    global led_status
    led_status  = not led_status
    GPIO.output(led, led_status)
    if (led_status == 1):
        print('LED is on')
    else:
        print('LED is off')
    
        
def loop():
    GPIO.add_event_detect(switch, GPIO.FALLING, callback = swLed, bouncetime = 200)
    while True:
        pass

def destroy():
    GPIO.output(led, GPIO.LOW)
    GPIO.cleanup()
    
    
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
    
    
    
    
    