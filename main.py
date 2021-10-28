import os
import uvicorn
from fastapi import FastAPI, Response
# from models import ModelName
from controller import Controller as con

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

