import cv2
from service import qr_service as qr
from service import b64
from service import utils
qrc = qr.QR_Service()
b64c = b64.B64()
dtu = utils.Utils();

class Controller():
	def __init__(self):
		print("Controller QR!")

	def decodeImageQR(self, pathImg):
		# obtiene la data de la imagen QR
		data = qrc.decode(pathImg)
		print("decode:", b64c.decode(data))
		# convierte la data(base64) a data legible
		# y valida contra la fecha de expiracion
		flag_door = dtu.validate(b64c.decode(data))
		return {flag_door, data}
	
	def generateImageQR(self):

		return qrc.generate()


