import os
import uvicorn
from fastapi import FastAPI, Response, File, UploadFile, File
# from models import ModelName
from controller import Controller as con
# frece varias operaciones de alto nivel en archivos y colecciones de archivos
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "QR API Ready!"}

# Recibe un int
@app.get("/qr/decode")
async def decode_QR_Image():
	pathImg = os.path.abspath("qrtest.png")
	res = con.Controller.decodeImageQR(pathImg)
	return {"data": res }
	#return {"sensor": "404 - not sensor found!"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
	return {"filename": file.filename}


@app.post("/qr/deco")
async def create_upload_file(file: UploadFile = File(...)):
	# return {"filename": file.filename}
	# contents = await file.read()
	res = con.Controller.decodeImageQR("C:\\Users\\Edu\\AppData\\Local\\Temp\\tmphimqifml.png")
	return {"data": res }

@app.post("/qr/decode")
def save_upload_file_tmp_and_decode(upload_file: UploadFile = File(...)) :
	try:
		suffix = Path(upload_file.filename).suffix
		with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
			shutil.copyfileobj(upload_file.file, tmp)
			tmp_path = Path(tmp.name)
			print("path:", tmp_path)
			print("path str:", tmp_path.__str__())
			print("path pox:", tmp_path.as_posix())
			
	finally:
		upload_file.file.close()
		res = con.Controller.decodeImageQR(tmp_path.__str__())
	return {"decode": res, "path": tmp_path}

