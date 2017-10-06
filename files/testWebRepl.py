import network
from wifi_config import *

import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PWD)
time.sleep(5)

while wlan.ifconfig()[0] == '0.0.0.0':
	time.sleep(5)
	print("trying to connect to network...")
myIp = wlan.ifconfig()[0]
print('connected to network!')

import webrepl
webrepl.start()

i = 0
while 1:
	i = i + 1
	print(i)
	print(myIp)
	time.sleep(1)

