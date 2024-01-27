import os
from hashlib import sha256
from pyhtml2pdf import converter

from fastapi import FastAPI
from fastapi.responses import Response
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get('/')
async def root():
  return RedirectResponse(url='/docs')

@app.get("/pdf")
async def pdf(url: str):
  fname = sha256(url.encode('utf-8')).hexdigest()
  pdf_path = f'/tmp/{fname}.pdf'
  converter.convert(url, pdf_path, timeout=5)
  pdf = open(pdf_path, 'rb').read()
  os.remove(pdf_path)
  return Response(status_code=200, media_type='application/pdf', content=pdf)
