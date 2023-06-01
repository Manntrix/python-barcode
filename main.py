from typing import Union
from glob import glob
from fastapi import FastAPI, File, UploadFile
from pyzbar import pyzbar
import cv2

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcode_info = barcode.data.decode("utf-8")
    return barcode_info


@app.get("/get-barcode")
async def get_barcode():
    try:
        decoded_barcodes = glob("barcode1.png")
        for barcode in decoded_barcodes:
            img = cv2.imread(barcode)
            barcodeData = read_barcodes(img)
        return {"barcode": barcodeData}
    except Exception:
        return {"message": "There was error"}
