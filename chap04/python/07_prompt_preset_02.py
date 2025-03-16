import json

# JSON 파일 열기 - 경로 주의하세요
with open("../data/prompt_preset.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # JSON을 Python 딕셔너리로 변환

list_keyword = []
prompt = ''

for category in data:
    for key in data[category]:
        list = (data[category][key])
        list_keyword.append(random.choice(list))

prompt = (", ").join(list_keyword)
print(prompt)