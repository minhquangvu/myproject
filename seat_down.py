import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

def seat_down():
	
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
	
	GPIO.output(Motor1_Enable,GPIO.HIGH)	//seat down process
	GPIO.output(Motor2_Enable,GPIO.HIGH)
	GPIO.output(Motor2_Forward,GPIO.LOW)
	GPIO.output(Motor1_Forward,GPIO.LOW)
	print('Down')
	GPIO.output(Motor1_Reverse,GPIO.HIGH)
	GPIO.output(Motor2_Reverse,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(Motor1_Reverse,GPIO.LOW)
	GPIO.output(Motor2_Reverse,GPIO.LOW)
	
if __name__=='__main__':
	seat_down()
