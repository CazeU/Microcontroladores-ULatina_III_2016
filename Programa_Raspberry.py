import serial
import time
import dropbox
import picamera
import threading
from time import sleep
import alertas
import capturando
#from capturando import captura

#cap = threading.Thread(target=captura)
#cap = threading.Thread(target=capturando.captura)
ser = serial.Serial('/dev/ttyACM0', 9600)
b = 0
i = 0
f = 0
v = 0
while True:
	arduino = int(ser.readline())
	if arduino == 0:
		i = 0
		f = 0
		v = 0
		if b == 0: 
			b = 1
			print("Todo Bien")
	elif arduino == 1:
		b = 0
		f = 0
		v = 0
		if i == 0:
			i = 1
			print("Hay un Intruso")
			alertas.intr_alert(alertas.eliaddr)
			alertas.intr_alert(alertas.uriaddr)
	elif arduino == 2:
		b = 0
		i = 0
		v = 0
		if f == 0:
			f = 1
			print ("Hay un Incendio")
			alertas.fire_alert(alertas.eliaddr)
			alertas.fire_alert(alertas.uriaddr)
	elif arduino == 3 or arduino == 4:
		b = 0
		i = 0
		f = 0
		if v == 0:
			v = 1
			cap = capturando.get_thread()
                	if cap:
                		cap.start()
                	else:
				print("no obtuvo thread")


