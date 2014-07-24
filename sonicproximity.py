import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
trig=10
echo=9
buzzer=3

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

enter_number=0

def reading():
		GPIO.output(trig, False)
		time.sleep(0.3)
		
		GPIO.output(trig, True)
		# wait 10 micro seconds (this is 0.00001 seconds) so the pulse
		# length is 10Us as the sensor expects
		time.sleep(0.00001)

		GPIO.output(trig, False)

		while GPIO.input(echo) == 0:
		  signaloff = time.time()
		while GPIO.input(echo) == 1:
		  signalon = time.time()
		
		# work out the difference in the two recorded times above to 
		# calculate the distance of an object in front of the sensor
		timepassed = signalon - signaloff
		
		# we now have our distance but it's not in a useful unit of
		# measurement. So now we convert this distance into centimetres
		distance = 0.5*timepassed * 34029-1.00
		distance=round(distance,2)
                count()
                
def count():
	if distance<115 and distance>90:
		time.sleep(2)
		enter_number+=1
		print'Someone Enters'
		print 'Distance in cm is ',distance
		print 'Number: ',enter_number
			for i in range(0,3):
				GPIO.output(buzzer,True)
				time.sleep(0.2)
				GPIO.output(buzzer,False)
				time.sleep(0.2)

try:
	while True:
		reading()
		time.sleep(0.5)
except KeyboardInterrupt:
	print'Stop'
	GPIO.cleanup()
