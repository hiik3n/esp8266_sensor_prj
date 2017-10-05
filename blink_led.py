import time as t
from machine import Pin

def initLedPin():
	p2 = Pin(2, Pin.OUT)
	return p2

def flashLed2Times(iport):
	iport.on()
	t.sleep(2)
	iport.off()
	t.sleep(2)

def setPinHigh(pinNo):
	_pin = Pin(pinNo, Pin.OUT)
	_pin.on()

def setPinLow(pinNo):
	_pin = Pin(pinNo, Pin.OUT)
	_pin.off()

print("Hi")

myport = initLedPin()
i = 0

while 1:
	
	flashLed2Times(myport)
	i = 1 + i
	print(i)
	t.sleep(2)
