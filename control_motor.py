#Control Motor with tilt_switch and NPN
import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(motor,FALSE)

tilt_switch=18
motor=3

def wheel():
	GPIO.setup(motor,GPIO.OUT)
	GPIO.setup(tilt_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	if (GPIO.input(tilt_switch)==False):
		print('Up-OFF')
		GPIO.output(motor,False)
		time.sleep(0.2)
	elif((GPIO.input(tilt_switch)==True) or (temp>=27)):
		print('Down-ON')
		GPIO.output(motor,True)
		time.sleep(0.2)

if __name__=='__main__':
    wheel()