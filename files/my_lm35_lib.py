##Lam Do##
from machine import ADC

def readAdc0():
	return ADC(0).read()

def readAdc(i_port):
	return ADC(i_port).read()

def howTemp():
	return (readAdc0()*3.3)/1024*100