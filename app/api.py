from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from app.conti_maker import *



origins = [
    "http://0.0.0.0:80",
    "http://localhost",
    "http://localhost:3000",
    "https://story-factory-frontend.vercel.app/"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/txt2img")
async def make_conti_txt2img(txt2img: Txt2Conti):
    global g_conti
    g_conti = generate_conti(txt2img)
    converted_conti = jsonable_encoder(g_conti)
    return JSONResponse(content=converted_conti)

