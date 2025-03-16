import json

# JSON 파일 열기 - 경로 주의하세요
with open("../data/prompt_preset.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # JSON을 Python 딕셔너리로 변환

# 데이터 출력
print(data)