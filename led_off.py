import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

led=9

GPIO.setup(led,GPIO.OUT)

def led_off():
	GPIO.output(led,False)
	print('off')
	
if __name__='__main__':
	led_off()
