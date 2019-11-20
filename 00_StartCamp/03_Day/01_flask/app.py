from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route('/')

def hello():
    return 'Hello world!김도훈'

@app.route('/ssafy')
def ssfay():
    return '싸피싸피 얍얍'
#FLASK_APP=hello.py flask run

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return '''
    <h1> 여러줄로 작성하자~! </h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다. {name}님!'

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'

# 점심메뉴 리스트(5개)에서 2개(person)ㅔ를 뽑아 출력하기

@app.route('/menu/<int:person>')
def menu(person):
    menus = ['우동','소고기','갈치','카레','저염김치']
    menus2  = str(menus)
    rame = random.sample(menus,person)
    rame2 = str(rame)
    return f'오늘의 전체 메뉴는 {menus2}이며 그 중 {person}개를 뽑아 고른 메뉴는 {rame2}입니다.'