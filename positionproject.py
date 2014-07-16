#positionsensor.
#Minh Vu 07/10/2014

import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BCM)
tilt_switch=17
led=22
frequency=50
servo=9
buzz=10

def position_control():
	GPIO.setup(led,GPIO.OUT)
	GPIO.setup(tilt_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	if GPIO.input(tilt_switch)==False:
		print('Up')
		GPIO.output(led,True)
		GPIO.output(buzz,True)
		time.sleep(0.5)
		GPIO.output(buzz,False)
	else:
		print('Down')
		GPIO.output(led,False)
		GPIO.output(buzz,False)

def dutycycle_calculate():
	clockwise=0.75 #in second
	anticlockwise=2.5
	initial=(anticlockwise-clockwise)/2+clockwise
	msperiod=1000/frequency
	
	input=raw_input('Enter direction (clockwise - c /anticlockwise - a): ')
	if input=='c':
		position=0.75
	elif input=='a':
		position=2.50
	else:
		raise Exception('Invalid Input')
	DutyCycle=100*position/msperiod
	print ('Direction is: '),position
	print ('DutyCycle is: '), DutyCycle
	print (' ')
	
	pwm.start(DutyCycle)
	time.sleep(1.5)

def initial():
	clockwise=0.75 #in second
	anticlockwise=2.5
	initial=(anticlockwise-clockwise)/2+clockwise
	msperiod=1000/frequency
	
	pwm.start(initial*100/msperiod)
	time.sleep(0.5)
	pwm.stop
	GPIO.cleanup()

if __name__=='__main__':
	GPIO.setup(servo,GPIO.OUT)
	GPIO.setup(buzz,GPIO.OUT)
	pwm=GPIO.PWM(servo,frequency)

	dutycycle_calculate()
	position_control()
	pwm.stop()

	initial()
	GPIO.cleanup()