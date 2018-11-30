import RPi.GPIO as GPIO
#import ADC0832
import math
import time
import signal
import sys


switch = 18
led = 16
led_status = 0

pinTrigger = 3
pinEcho = 5


def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
#    GPIO.cleanup() 
    sys.exit(0)


def init():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
    signal.signal(signal.SIGINT, close)
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)
    
    
def swLed(ev = None):
    global led_status
    
    led_status  = not led_status
    GPIO.output(led, led_status)
#    if (led_status == 1):
#        print('Vehicle is in PARKING MODE')
#    else:
#        print('VEHICLE is in FORWARD MODE')
        
        
        
    
    
def loop():
    GPIO.add_event_detect(switch, GPIO.FALLING, callback = swLed, bouncetime = 200)
    while True:
        
        if (led_status == 0):
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)
            startTime1 = time.time()
            stopTime1 = time.time()
            while 0 == GPIO.input(pinEcho):
                startTime1 = time.time()
            while 1 == GPIO.input(pinEcho):
                stopTime1 = time.time()
            TimeElapsed1 = stopTime1 - startTime1
            distance1 = (TimeElapsed1 * 34300) / 2      
    
            time.sleep(0.01)
    
    
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)
            startTime2 = time.time()
            stopTime2 = time.time()
            while 0 == GPIO.input(pinEcho):
                startTime2 = time.time()
            while 1 == GPIO.input(pinEcho):
                stopTime2 = time.time()
            TimeElapsed2 = stopTime2 - startTime2
            distance2 = (TimeElapsed2 * 34300) / 2 

               
    
            time.sleep(0.01)
    
    
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)
            startTime3 = time.time()
            stopTime3 = time.time()
            while 0 == GPIO.input(pinEcho):
                startTime3 = time.time()
            while 1 == GPIO.input(pinEcho):
                stopTime3 = time.time()
            TimeElapsed3 = stopTime3 - startTime3
            distance3 = (TimeElapsed3 * 34300) / 2 
    
            average_distance = (distance1 + distance2 + distance3) / 3
    
            print("Distance: %.1f cm" % average_distance)
        
        else:
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)
            startTime1 = time.time()
            stopTime1 = time.time()
            while 0 == GPIO.input(pinEcho):
                startTime1 = time.time()
            while 1 == GPIO.input(pinEcho):
                stopTime1 = time.time()
            TimeElapsed1 = stopTime1 - startTime1
            distance1 = (TimeElapsed1 * 34300) / 2      
    
            time.sleep(0.05)
    
    
            GPIO.output(pinTrigger, True)
            time.sleep(0.00001)
            GPIO.output(pinTrigger, False)
            startTime2 = time.time()
            stopTime2 = time.time()
            while 0 == GPIO.input(pinEcho):
                startTime2 = time.time()
            while 1 == GPIO.input(pinEcho):
                stopTime2 = time.time()
            TimeElapsed2 = stopTime2 - startTime2
            distance2 = (TimeElapsed2 * 34300) / 2
            
            velocity = (distance2 - distance1) / 0.1
            if (abs(velocity) <= 5):
                velocity = 0
            
            print("Velocity: %.1f cm/s" % (velocity * 10))

            
        
        
        
        
        
        
def destroy():
    GPIO.output(led, GPIO.LOW)
    GPIO.cleanup()

        
        
if __name__ == '__main__':
    init()
    try:
        loop()
            
        
        
    except KeyboardInterrupt:
        close()
        destroy()
        print('The end! ')
        
        
        
        
        
        
