# esp8266_sensor_prj

Use esp8266 to read data from sensor, then push data to server

Use MicroPython to develop firmware

Use webrepl to remote monitoring and modify the code

Python version is 2.7.10


## User Stories

* [x] Setup environment
	* [x] Usb2Uart driver
	* [x] Flashing tool (esptool)
	* [x] Download firmware for micropython
	* [x] Play with micropython cmd

* [ ] Data Acquisition
	* [x] LED indicator
	* [x] Flash start-up fw
	* [x] Play with WEBREPL
	* [ ] Analog read

* [ ] Publish data to cloud
	* [ ] Prepare database
	* [ ] Visualize data

## Notes
http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/index.html

https://cdn-learn.adafruit.com/downloads/pdf/micropython-basics-load-files-and-run-code.pdf

https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl

Paste multiple line in terminal: Crtl + E,  Ctrl-C to cancel, Ctrl-D to finish

## Logs
	* Check if driver for usb2uart available by

		`ls /dev/tty.*`

	* If not, download from: https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

		`pip install esptool`	(https://github.com/espressif/esptool/)

	* Clear current fw

		`esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash`

	* Download firmware for micropython http://micropython.org/download#esp8266

	* Flash micropython fw

		`esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 esp8266-20170823-v1.9.2.bin`

	* REPL python

		`screen /dev/tty.SLAB_USBtoUART 115200`

		[Errno 16] Resource busy: '/dev/tty.SLAB_USBtoUART'

		```lsof | grep UART
		screen -x 27127
		use ctr-A ctr-\ to close it properly```

		```>>> print("hello")
		hello
		>>> 1+1
		2```

		```>>> import os
		>>> os.listdir()
		['boot.py']
		>>> os.getcwd()
		'/'```

		`help()`

	* Adafruit MicroPython tool to modify main.py for start-up firmware

		`pip install adafruit-ampy`

		`ampy --port /dev/tty.SLAB_USBtoUART run test.py`

		`ampy --port /dev/tty.SLAB_USBtoUART run --no-output  testv2.py 	(do not display any thing to console, used= REPL for moniotring)`

		`ampy --port /dev/tty.SLAB_USBtoUART put testfol`

		`ampy --port /dev/tty.SLAB_USBtoUART get boot.py`

		`ampy --port /dev/tty.SLAB_USBtoUART get testfol/test`

		`ampy --port /dev/tty.SLAB_USBtoUART get boot.py board_boot.py`

		`ampy --port /dev/tty.SLAB_USBtoUART mkdir foo`

		`ampy --port /dev/tty.SLAB_USBtoUART ls`

		`ampy --port /dev/tty.SLAB_USBtoUART rm test.py`

		`ampy --port /dev/tty.SLAB_USBtoUART put blink_led.py /main.py`

		* use ctr-A ctr-\ to close it properly (in order to process more ampy cmd)

			`ampy.pyboard.PyboardError: failed to access dev/tty.SLAB_USBtoUART`

	* WEBREPL
		* station mode
			import webrepl_setup

			access http://micropython.org/webrepl/

			ws://192.168.4.1:8266/

			micropython - micropythoN

		* ap mode

			import network
			wlan = network.WLAN(network.STA_IF)
			wlan.active(True)
			wlan.connect('ssid', 'password')

			wlan.ifconfig()

			import webrepl_setup

					import webrepl
					webrepl.start()

			~~replace webrepl_setup to overide user confirmation~~

				~~ampy --port /dev/tty.SLAB_USBtoUART put webrepl_setup.py~~

			add testWebRepl.py to main.py

				ampy --port /dev/tty.SLAB_USBtoUART put testWebRepl.py /main.py


