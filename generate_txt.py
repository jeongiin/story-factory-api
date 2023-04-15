import openai
# -*- coding: utf-8 -*-

# 발급받은 API 키 설정
OPENAI_API_KEY = ""

# openai API 키 인증
openai.api_key = OPENAI_API_KEY

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

# 질문 작성하기
query = '다음 글을 5문장으로 줄여줘. \
    옛날 옛날에 모두의 사랑을 받는 작고 귀여운 소녀가 있었습니다. 하지만 그 소녀를 가장 사랑하는 것은 그녀의 할머니였습니다. \
        할머니는 소녀에게 무엇을 줘야 할지 몰랐습니다. 한번은 할머니가 소녀에게 붉은 벨벳으로 만들어진 모자를 선물했습니다. \
            소녀에게 그 모자가 잘 어울렸고, 소녀가 그 모자가 아닌 다른 것은 쓰지 않으려고 했습니다. 그래서 그 소녀는 "빨간 모자"라고 불렸습니다. \
    어느 날, 소녀의 엄마가 그녀에게 말했습니다. "빨간 모자, 여기로 와보렴. 여기 케이크 한 조각과 와인 한 병을 할머니에게 가져다 주렴. \
        할머니가 편찮으시니까 네가 가면 기뻐하실 거야. 더워지기 전에 출발하렴. 그리고 할머니 댁에 갈 때, 조심해서 가고 길에서 벗어나지 마렴. \
            그렇지 않으면 네가 넘어져서 병을 깨뜨릴 거야. 그러면 할머니는 아무것도 받지 못하신단다. \
                그리고 할머니 방에 가면, 먼저 인사하고 방 안 구석구석을 살펴보는 것을 잊지 말아라!"'

# 메시지 설정하기
messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
]

# ChatGPT API 호출하기
response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer = response['choices'][0]['message']['content']
print(answer)