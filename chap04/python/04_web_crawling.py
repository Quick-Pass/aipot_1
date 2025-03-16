import requests
from bs4 import BeautifulSoup

url = f"https://license.kpc.or.kr/nasec/qlfint/qlfint/selectAipot.do"

# 페이지 조회 결과 가져오기
response = requests.get(url)

# 응답 확인
if response.status_code == 200: # 200인 경우 정상
    soup = BeautifulSoup(response.text, "html.parser") # 응답 문자열을 HTML 문서로 파싱

    # 페이지 본문 내용 가져오기
    content = soup.find("div", id="content") # 페이지 본문에서 id 값이 content인 부분을 찾음

    # 제목 가져오기
    title = content.find('h2').text # content로부터 h2 요소를 찾고 제목 문자열만 추출
    print(title) # 제목 문자열 추출

else: # 다른 응답 코드는 오류로 판단
    print("웹 페이지를 가져오는 데 실패했습니다.")
