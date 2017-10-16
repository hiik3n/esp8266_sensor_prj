##Lam Do##
import network
import time

try:
	from wifi_config import *
	from my_lm35_lib import *
	from my_thinkspeak_lib import *

	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(WIFI_SSID, WIFI_PWD)
	time.sleep(5)

	while wlan.ifconfig()[0] == '0.0.0.0':
		time.sleep(5)
		print("trying to connect to \"%s\"..." % WIFI_SSID)
	myIp = wlan.ifconfig()[0]
	print('connected to network!')

	import webrepl
	webrepl.start()

	err = 'ok'

	def main():
		print("Hello")
		while 1:
			_temp = howTemp()
			try:
				# make sure data is number
				_temp = eval(str(_temp))
			except Exception as e:
				print("Invalid data from LM35")
				time.sleep(60)
				continue
			print("LM35 data: %f" % _temp)
			update_field_in_channel(fieldname='field1', fieldvalue=_temp)
			print("")
			time.sleep(60)


	main()
except Exception as e:
	while 1:
		err = str(e)
		time.sleep(10)
