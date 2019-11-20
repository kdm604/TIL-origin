from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.

# 1. 기본로직
def index(request):
    return render(request, 'pages/index.html')
    #템플릿의 이름공간을 나눠서 사용하기!
def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')

# 2. Template Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'pages/dinner.html', context)


# 3. variable Routing(동적 라우팅)
def hello(request, name, age):
    # names = ['justin', 'john', 'jason', 'juan', 'zzulu']
    # name = random.choice(names)
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name':name, 
        'age':age,
        'pick':pick,
        }
    return render(request, 'pages/hello.html', context)


# 4. 실습
# 4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기소개파일
def introduce2(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'pages/introduce2.html', context)

# 4-2 . 두개의 숫자를 인자로 받아 (num1, num2) 곱셈결과를 출력
def mul(request, num1, num2):
    my_mul = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'my_mul': my_mul
    }
    return render(request, 'pages/mul.html', context)

# 4-3 . 반지름을 인자로 받아 원의 넓이를 구하시오

def area(request, r):
    area = 3.14 * r * r
    context = {
        'r': r,
        'area': area
    } 
    return render(request, 'pages/area.html', context)

# 5 DTL (django template language)
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'pages/template_language.html', context)



    # 13 워크샵
def info(request):
    return render(request, 'pages/info.html')

def student(request, name):
    context = {
        'name': name
    }
    return render(request, 'pages/student.html', context)



# 6. 실습
# 6 - 1 isbirth

def isbirth(request):
    today = datetime.now()
    day2 = today.day
    month2 = today.month
    if day2 == 29 and month2 == 1:
        result = True
    else: 
        result = False
      
    context = {
        # 'today': today,
        # 'day2': day2,
        # 'month2': month2,
        'result': result
    }
    return render(request, 'pages/isbirth.html', context)
    
# 6-2 회문판별
# 회문이면(반대로 돌려도 같은 글자 -ex. racecar) '회문입니다'
# 회문이 아니면 '회문이 아닙니다'

def ispal(request, name):
    if name == name[::-1]:
        result = True
    else:
        result = False
    context = {
        'name': name,
        'result': result
    }
    return render(request, 'pages/ispal.html', context)

# 6-3 로또번호 추첨
# lottos -> 1~45 번호중 6개 픽한 리스트
# real_lotto - > [21,24,30,32,40,42]
# 1. lotto 번호를 하나씩 출력 for문

def lotto(request):
    real_lotto2=[21,24,30,32,40,42]
    lottos = list(range(1,46))
    real_lotto = random.sample(lottos,6)
    context = {
        'real_lotto':sorted(real_lotto),
        'real_looto2': real_lotto2,
    }
    return render(request, 'pages/lotto.html', context)



# 7. Form - GET  default가 get 요청
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)



def ping(request):
    return render(request, 'ping.html')

def pong(request):
    pingping = request.GET.get('pingping')
    pingping2 = request.GET.get('pingping2')
    context = {
        'pingping': pingping,
        'pingping2': pingping2
    }
    return render(request, 'pages/pong.html', context)

# 8. Form - GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다.(GET.get())
    word = request.GET.get('word')

    #2. ARTII api로 요청을 보내 응답결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text    

    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어 있는 요소 중 하나를 선택해
    # font 라는 변수에 저장(str)
    font =  random.choice(fonts)

    #5. 위에서 사용자에게 받은 word와 font를 가지고 다시
    # 요청을 보낸다. 그리고 응답 결과를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result': result,
    }
    
    return render(request, 'pages/result.html', context)


    # 글을 쓰거나, 수정, 삭제할 때 post방식?
    # 특정한 csrf 토큰을 넣지않으면 오류가난데.

#9. Form - Post
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context ={
        'name': name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html',context)


#10. 정적파일
def static_example(request):
    return render(request, 'pages/static_example.html')