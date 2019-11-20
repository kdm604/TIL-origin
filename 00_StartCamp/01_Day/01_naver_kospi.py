import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser') # 파씽 유의미한 정보를 가져오기위한 2번쨰인자?
kospi = soup.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')
print(type(soup))
print(type(html))