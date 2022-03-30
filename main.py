import os
import uvicorn
from fastapi import FastAPI, Response, File, UploadFile, File
# from models import ModelName
from controller import Controller as con
# frece varias operaciones de alto nivel en archivos y colecciones de archivos
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi.responses import FileResponse

conn = con.Controller()
app = FastAPI(root_path="/api/v1")

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Bienvenidos al Workshop-Steren!"}

@app.post("/qr/validate")
async def save_upload_file_tmp_and_decode( upload_file: UploadFile = File(...)) :
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
		flag_door, res = conn.decodeImageQR(tmp_path.__str__())
	return {"status": flag_door, "decode": res, "path": tmp_path}

@app.get("/qr/generate")
async def generate_qr():
	res_img = conn.generateImageQR()
	# return StreamingResponse(res_img, media_type="image/png")
	return FileResponse(os.getcwd() + '/tmp/qrcode001.png', media_type="image/png")
