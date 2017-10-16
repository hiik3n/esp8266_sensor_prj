##Lam Do##
import socket
from my_info import THINKSPEAK_API_KEY, THINKSPEAK_API_WRITE_KEY

THINKSPEAK_UPDATE_PATH = 'https://api.thingspeak.com/update?api_key='+ THINKSPEAK_API_WRITE_KEY +'&%s=%s'

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def update_field_in_channel(fieldname='', fieldvalue=0):
	_str = THINKSPEAK_UPDATE_PATH % (fieldname, str(fieldvalue))
	http_get(_str)