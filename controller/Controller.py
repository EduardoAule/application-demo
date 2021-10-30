import cv2

class Controller():
	def __init__(self):
		print("Controller QR!")

	def decodeImageQR(pathImg):
		# Lectura de la imagen
		img = cv2.imread(pathImg)
		# Iniciar deteccion de QR Codes de OpenCV
		dtector = cv2.QRCodeDetector()
		# Detectar y Decodificar
		data, bbox, stight_code = dtector.detectAndDecode(img)
		print("data:", data)
		return data

