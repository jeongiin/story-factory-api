from .generate_prompt import *
from .generate_reference import *
from .preprcess import *

import matplotlib.pyplot as plt
from pydantic import BaseModel
from typing import Optional
import torch

class Txt2Conti(BaseModel):
    # Conti = story + reference
    contents: Optional[str]
    num_content: Optional[int] = 6 # 몇 문장 요약?
    num_reference: Optional[int] = 1 # 각 몇 장의 이미지 생성?
    style: Optional[str] = "sketch style"
    model_gpt: Optional[str] = "gpt-3.5-turbo"
    model_diff: Optional[str] = "runwayml/stable-diffusion-v1-5"
    height: Optional[int] = 608 # 8의 배수
    width: Optional[int] = 416 # 8의 배수
    num_inference_steps: Optional[int] = 30 # 한 장당 30steps에 2~30초 소요됨
    conti : Optional[dict] = {}


def generate_conti(txt2conti : Txt2Conti) -> Txt2Conti:

    prompt = generate_prompt(txt2conti.contents,txt2conti.num_content) # prompt engineering
    story_str = generate_content(prompt, txt2conti.model_gpt) # return 한국어로 요약된 문장 # 반드시 한글이 들어온다는 전제이므로 추후 개발이 필요할 듯
    contents_ko_with_num = content_to_array(story_str) # return 요약된 한 문장을 \n 기준 분리한 배열

    print(contents_ko_with_num)

    txt2conti.conti = {content : [] for content in contents_ko_with_num}

    for i, content in enumerate(contents_ko_with_num):
        contents_ko = ko_preprocessing(content, i+1) # return 효과적인 이미지 생성을 위한 영어 번역
        prompt_diffusion = txt2conti.style + ", " + ko_to_en(contents_ko)
        print("\n", prompt_diffusion, "\n") # for check
        refers = generate_img(prompt_diffusion, txt2conti)
        for refer in refers:
            refer_bytes = img2bytes(refer)
            txt2conti.conti[content].append(refer_bytes) # 이미지 배열에 담아서 반환
    
    return txt2conti