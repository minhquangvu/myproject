import RPi.GPIO as GPIO,time
import operator

GPIO.setmode(GPIO.BCM)

Red=17
Green=18
Blue=22
sleeptime=0.5

LED=[Red,Green,Blue]

for port in LED:
	GPIO.setup(port,GPIO.OUT)

for port in LED:
	GPIO.output(port,False)


colorcode={
	'rb':'1',
	'rg':'2',
	'bg':'3',
	'al':'4',
}

def rb():
	GPIO.output(Red,True)
	GPIO.output(Blue,True)
	GPIO.output(Green,False)

def rg():
	GPIO.output(Red,True)
	GPIO.output(Green,True)
	GPIO.output(Blue,False)

def bg():
	GPIO.output(Blue,True)
	GPIO.output(Green,True)
	GPIO.output(Red,False)

def al():
	GPIO.output(Red,True)
	GPIO.output(Green,True)
	GPIO.output(Blue,True)

def resolve_colorcode(char):
	"code light"
	sequence=colorcode[char]
	for light in sequence:
		if light is '1':
			rb()
		elif light is '2':
			rg()
		elif light is '3':
			bg()
		elif light is '4':
			al()
		else:
			raise Exception('Invalid input')

def resolve_lightup(string):
	for one in map(operator.add,string[::2],string[1::2]):
		resolve_colorcode(one)

if __name__=="__main__":
	print 'running LED'
	string=raw_input('Enter your string: ')
	resolve_lightup(string)