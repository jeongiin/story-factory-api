import openai
from translate import Translator
# -*- coding: utf-8 -*-

def ko_to_en(text : str):
    translator = Translator(from_lang="ko", to_lang="en")
    
    return translator.translate(text)


def generate_prompt(query, n):
    
    return query + "\n === \n" + "위 내용을 문장 "+str(n)+"개로 넘버링해서 묘사해줘." 


def ko_preprocessing(content_array, n):
    result_array = []
    for content in content_array:
        result_array.append(content.replace(str(n)+'. ',""))
    return result_array


def content_to_array(content):
    array = content.split('\n')
    return array


def generate_content(prompt, model="gpt-3.5-turbo"):

    # model(default) - GPT 3.5 Turbo 

    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    
    return answer