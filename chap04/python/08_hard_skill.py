import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일 로드
file_path = "/content/bench.csv"
df = pd.read_csv(file_path)
labels = ["code", "crm", "docs", "integrate", "marketing", "reason", "final"]
num_vars = len(labels)

# 상위 10개 모델만 선택
top_10_models = df.nlargest(10, "final")

# 각 모델의 데이터 정규화
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # 마지막에 첫 번째 각도를 추가하여 차트 닫기

# 레이더 차트 생성
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, row in top_10_models.iterrows():
    values = row[labels].tolist()
    values += values[:1]  # 마지막에 첫 번째 값을 추가하여 차트 닫기
    ax.plot(angles, values, label=row["model"], marker="o", linestyle="-")
    ax.fill(angles, values, alpha=0.1)  # 투명한 채우기

# 축 설정
ax.set_xticks(angles[:-1])  # 마지막 각도는 라벨에서 제외
ax.set_xticklabels(labels)
ax.set_yticklabels([])
ax.set_title("Top 10 LLM Performance Comparison", pad=20)

plt.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
plt.show()