import cv2
# frece varias operaciones de alto nivel en archivos y colecciones de archivos
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import UploadFile

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

	def save_upload_file_tmp(upload_file: UploadFile) -> Path:
		try:
			suffix = Path(upload_file.filename).suffix
			with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
				shutil.copyfileobj(upload_file.file, tmp)
				tmp_path = Path(tmp.name)
		finally:
			upload_file.file.close()
		return tmp_path