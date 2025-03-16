# RunwayML API를 사용하기 위해서 아래의 파이썬 코드를 실행하기 전에 먼저 라이브러리를 설치해주세요
# pip install runwayml

import time
from runwayml import RunwayML

client = RunwayML(api_key='API 키 입력')

task = client.image_to_video.create(
    model='gen3a_turbo',
    prompt_image='이미지 주소 입력',
    prompt_text='string',
)
task_id = task.id

# Poll the task until it's complete
time.sleep(10)  # Wait for a second before polling
task = client.tasks.retrieve(task_id)
while task.status not in ['SUCCEEDED', 'FAILED']:
    time.sleep(10)  # Wait for ten seconds before polling
    task = client.tasks.retrieve(task_id)

print('Task complete:', task)