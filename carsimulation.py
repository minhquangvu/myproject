# automatic car simulation
# Minh Q Vu AUG 5th 2014. See full project at engineeringkool.blogspot.com

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def servo():
	servo=15
	frequency=50
	GPIO.setup(servo,GPIO.OUT)
	
	pwm=GPIO.PWM(servo,frequency) #power width modulation to control servo
	clockwise=0.75  #in second
	anticlockwise=2.5

	input=raw_input('Enter direction right(r)/left(l)/straight(s): ')
	print ('Direction is: '),input
	print ('--------------- ')
	if input=='l': #turn left
		position=0.75
	elif input=='r':
		position=2.50 #turn right
	elif input=='s': #back to initial position
		position=(anticlockwise-clockwise)/2+clockwise
	else:
		print('Invalid command')
		obstacle_check()
	
	msperiod=1000/frequency
	DutyCycle=100*position/msperiod
	pwm.start(DutyCycle)
	time.sleep(1)
	pwm.stop()


def motor():
	led_green=18
	led_red=17
	
	Motor1_Enable = 27
	Motor1_Forward = 23
	Motor1_Reverse = 22

	Motor2_Enable = 4
	Motor2_Forward = 25
	Motor2_Reverse = 24
 
	GPIO.setup(Motor1_Enable,GPIO.OUT)
	GPIO.setup(Motor1_Forward,GPIO.OUT)
	GPIO.setup(Motor1_Reverse,GPIO.OUT)

	GPIO.setup(Motor2_Enable,GPIO.OUT)
	GPIO.setup(Motor2_Forward,GPIO.OUT)
	GPIO.setup(Motor2_Reverse,GPIO.OUT)
	
	GPIO.setup(led_red,GPIO.OUT)
	GPIO.output(led_red,False)
	GPIO.setup(led_green,GPIO.OUT)
	GPIO.output(led_green,True)
	
	print('Car running')
	GPIO.output(Motor1_Enable,GPIO.HIGH)
	GPIO.output(Motor1_Forward,GPIO.LOW)
	GPIO.output(Motor1_Reverse,GPIO.HIGH)

	GPIO.output(Motor2_Enable,GPIO.HIGH)
	GPIO.output(Motor2_Forward,GPIO.LOW)
	GPIO.output(Motor2_Reverse,GPIO.HIGH)
	
	obstacle_check()


def obstacle_check():
	trig=10
	echo=9

	GPIO.setup(trig,GPIO.OUT)
	GPIO.setup(echo,GPIO.IN)
	
	GPIO.output(trig, False)
	time.sleep(0.2)
		
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
	
	#if there is obstacle in 10cm, stop the car
	if distance<10:
		print 'Obstacle ahead ',distance,' cm'
		safety()
	#if path is clear in 10cm, car runs
	if distance >=10:
		motor()


def safety():
	led_green=18
	led_red=17

	Motor1_Enable = 27
	Motor2_Enable = 4

	print "Stopping motor"
	GPIO.setup(led_green,GPIO.OUT)
	GPIO.output(led_green,False)
	GPIO.setup(led_red,GPIO.OUT)
	GPIO.output(led_red,True)
	
	GPIO.setup(Motor1_Enable,GPIO.OUT)
	GPIO.setup(Motor2_Enable,GPIO.OUT)
	GPIO.output(Motor1_Enable,GPIO.LOW)
	GPIO.output(Motor2_Enable,GPIO.LOW)


try:
	command=raw_input('Enter your command (start/stop): ')
	while True:
		if command == 'stop':
			safety()
			time.sleep(0.5)
			GPIO.cleanup()
			break
		elif command == 'start':
			servo()
			obstacle_check()
			time.sleep(0.1)
		else:
			print('Invalid command')
except KeyboardInterrupt:
	print('Program STOP')
	safety()
	GPIO.cleanup()