from django.shortcuts import render,redirect
from .models import Job
from faker import Faker
from decouple import config
import requests
from pprint import pprint
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')
    person = Job.objects.filter(name=name).first()

    # DB에 이름이 있을경우
    if person:
        past_job = person.past_job

        # context = {
        #     'person':person
        #     # 'past_job' : past_job,
        #     # 'name' : name,
        # }
        
    # DB에 이름이 없을 경우
    else:
        fake = Faker()
        # name = fake.name()
        #랜덤 직업생성
        past_job = fake.job()
        # 새로운 이름, 직업 추가후 DB저장
        person = Job(name=name, past_job=past_job)
        person.save()

    # GIPHY
    #1. API key 가져오기
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    #2. 요청 URL 셋팅~
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1&lang=ko'

    #3. 실제 요청을 보내자~(json -> dict로 바꾸자))
    data = requests.get(url).json()

    #4. 이미지 추출
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None

    NAVER_ID = config('NAVER_ID')
    NAVER_SECRET = config('NAVER_SECRET')

    # NAVER_IMAGE
    # 1. 요청 헤더 정보 준비
    headers = {
        'X-Naver-Client-Id': NAVER_ID,
        'X-Naver-Client-Secret': NAVER_SECRET
        }    

    # 2. 요청 URL 준비
    naver_url = f'https://openapi.naver.com/v1/search/image?query={past_job}&filter=medium&display=1'

    # 3. 실제 요청 보내기
    naver_data = requests.get(naver_url, headers=headers).json()
    pprint(naver_data)

    # 4. 이미지 링크 추출하기
    naver_image = naver_data.get('items')[0].get('link')


    context = {
        'person' : person,
        'image' : image,
        'naver_image' : naver_image,
    }

        
        # return redirect('jobs:index')
    return render(request, 'jobs/past_life.html',context)



