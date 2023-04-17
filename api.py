from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from conti_maker import *

# 

origins = ["*"]

origins = [
    "http://localhost:8000"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/txt2img")
async def make_conti_txt2img(txt2img: Txt2Conti):
    global conti
    conti = generate_conti(txt2img)

    converted_conti = jsonable_encoder(conti)
    return JSONResponse(content=converted_conti)

