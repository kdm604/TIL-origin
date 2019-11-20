import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names=soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
'''
#print(f'실시간 {names}')
print(type(names))

for name in names:
    print(name.text)'''

for idx, name in enumerate(names):
    print(f'{idx+1}위: {name.text}')