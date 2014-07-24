import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

enable=17
motor_a=18
motor_b=22


GPIO.setup(enable,GPIO.OUT)
GPIO.setup(motor_a,GPIO.OUT)
GPIO.setup(motor_b,GPIO.OUT)

if __name__=='__main__':
	print 'Running'
	GPIO.output(enable,True)
	GPIO.output(motor_a,True)
	GPIO.output(motor_b,False)
	time.sleep(5)

	GPIO.output(enable,False)
	time.sleep(0.1)

	GPIO.output(enable,True)
	GPIO.output(motor_a,False)
	GPIO.output(motor_b,True)
	time.sleep(5)
	
	GPIO.output(enable,False)
	print'Done'

