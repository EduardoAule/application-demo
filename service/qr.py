import cv2
import qrcode
import uuid
import os
from service import b64
from service import utils

b64c = b64.B64()
dtu = utils.Utils();

IOT_NO = "#iot00a@"

class QR():
	def __init__(self):
		pass

	def decode(self, pathImg):
		# Lectura de la imagen
		img = cv2.imread(pathImg)
		# Iniciar deteccion de QR Codes de OpenCV
		dtector = cv2.QRCodeDetector()
		#Detectar y Decodificar
		data, bbox, stight_code = dtector.detectAndDecode(img)

		return data

	def generate(self):
		# uuid_data = uuid.uuid4()
		fecha_exp = dtu.set_dt_expiration()
		# print("uuid4:", uuid_data)
		data = b64c.encode(IOT_NO + fecha_exp)
		print("data:", data)
		#Creating an instance of qrcode
		qr = qrcode.QRCode(
				version=1,
				box_size=15,
				border=2)
		qr.add_data(data)
		qr.make(fit=True)

		qr_img = qr.make_image(fill='black', back_color='white')
		print('getcwd:', os.getcwd())
		qr_img.save(os.getcwd() + '/tmp/qrcode001.png')
		return {"qr": "created"}
