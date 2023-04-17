import openai
from generate_txt import *
from generate_img import *
import matplotlib.pyplot as plt


# -*- coding: utf-8 -*-
# for generate_txt
# 발급받은 API 키 설정
OPENAI_API_KEY = open("/Users/timdalxx/PROJECT/story-factory-api/token.txt", 'r').readline()
# openai API 키 인증
openai.api_key = OPENAI_API_KEY

# 사용자로부터 받아야 함, 임시 쿼리
query = '아주 옛날에 모두의 사랑을 받는 작고 귀여운 소녀가 있었습니다. 하지만 그 소녀를 가장 사랑하는 것은 그녀의 할머니였습니다. \
            할머니는 소녀에게 무엇을 줘야 할지 몰랐습니다. 한번은 할머니가 소녀에게 붉은 벨벳으로 만들어진 모자를 선물했습니다. \
                소녀에게 그 모자가 잘 어울렸고, 소녀가 그 모자가 아닌 다른 것은 쓰지 않으려고 했습니다. 그래서 그 소녀는 "빨간 모자"라고 불렸습니다. \
        어느 날, 소녀의 엄마가 그녀에게 말했습니다. "빨간 모자, 여기로 와보렴. 여기 케이크 한 조각과 와인 한 병을 할머니에게 가져다 주렴. \
            할머니가 편찮으시니까 네가 가면 기뻐하실 거야. 더워지기 전에 출발하렴. 그리고 할머니 댁에 갈 때, 조심해서 가고 길에서 벗어나지 마렴. \
                그렇지 않으면 네가 넘어져서 병을 깨뜨릴 거야. 그러면 할머니는 아무것도 받지 못하신단다. \
                    그리고 할머니 방에 가면, 먼저 인사하고 방 안 구석구석을 살펴보는 것을 잊지 말아라!"'
num_content = 3
num_reference = 1

prompt = generate_prompt(query,num_content) # num_content 만큼 abstract
print(prompt)
content_str = generate_content(prompt) # 한국어로 요약된 문장 # 반드시 한글이 들어온다는 전제이므로 추후 개발이 필요할 듯
print(content_str)
content_arr = content_to_array(content_str)
print(content_arr)
content_res = ko_preprocessing(content_arr, num_content)
print(content_res)
for content in content_res:
    prompt_diffusion = ko_to_en(content)
    print(prompt_diffusion)
    image = generate_img(prompt_diffusion, num_reference)
    plt.imshow(image)
    plt.show()
# en_content = ko_to_en(query) # 요약된 문장 각각을 영어로 변환
# print(query)
# 문장 수만큼 for 문 돌며 generate_img
# 만든 이미지를 img array 형태로 전송
