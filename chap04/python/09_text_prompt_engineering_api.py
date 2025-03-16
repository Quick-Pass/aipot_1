from openai import OpenAI
client = OpenAI(api_key="API 키 입력")

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 유능한 비즈니스 컨설턴트입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=250
    )
    return response.choices[0].message.content

result = ask_gpt("새로운 사업 아이디어를 제안해주세요.")
print(result)
