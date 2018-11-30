import RPi.GPIO as GPIO
import time
import signal
import sys

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set GPIO Pins
pinTrigger = 3
pinEcho = 5

def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup() 
    sys.exit(0)

signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
    
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
#    print("Velocity: %.1f cm/s" % (velocity * 10))
#    time.sleep(0.1)
    
    
    
    
    
    
    
    