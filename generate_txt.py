import openai

# 발급받은 API 키 설정
OPENAI_API_KEY = "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"

# openai API 키 인증
openai.api_key = OPENAI_API_KEY

# 모델 - GPT 3.5 Turbo 선택
model = "gpt-3.5-turbo"

# 질문 작성하기
query = "텍스트를 입력받아 이미지를 생성하는 방법을 알려주세요."

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