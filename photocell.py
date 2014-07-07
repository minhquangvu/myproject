#!/usr/bin/env python
 
import RPi.GPIO as GPIO, time, os
 
DEBUG = 1
GPIO.setmode(GPIO.BCM)
led=22
 
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
 
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
 
while True:
	print RCtime(18) # Read RC timing using pin #18
	GPIO.setup(led,GPIO.OUT)
	if RCtime(18)>20:
		print('LED ON')
		GPIO.output(led,True)
	elif KeyboardInterrupt:
		GPIO.cleanup()
	else:
		print('LED OFF')
		GPIO.output(led,False)

