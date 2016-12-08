import dropbox
import picamera
import threading
import datetime
from time import sleep
 

cuenta = 'qVXHQSId0KAAAAAAAAAAEXsY6ZxDN6_f71o15SFhUyH-9Uhn90coKwR9JAhejwEZ'
cliente = dropbox.client.DropboxClient(cuenta)
	
camara_1 = picamera.PiCamera()

capturando = False

def captura():
	#camara_1.hflip = True
	#camara_1.vflip = True
	t = datetime.datetime.now()
	fecha = t.strftime('%Y-%m-%d_%H:%M:%S')
	print('Grabando...')
	capturando = True
	camara_1.start_recording('sala_pasillo.h264')
	sleep(30)
	camara_1.stop_recording()
	print('Video Capturado')
	capturando = False
	
	print('Subiento video...')
	video = open('sala_pasillo.h264', 'rb')
	subir = cliente.put_file('/sala_pasillo_'+fecha+'.h264', video)
	print('Video guardado')


def get_thread():
	if capturando:
		return None
	cap_thread = threading.Thread(target=captura)
	return cap_thread
