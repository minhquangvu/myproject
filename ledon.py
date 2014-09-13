import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

led=9

GPIO.setup(led,GPIO.OUT)

def led_on():
	GPIO.output(led,True)
	print('on')
	
if __name__='__main__':
	led_on()
