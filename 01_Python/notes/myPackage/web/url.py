def my_url(itemPerPage=10, **api):
    print(api)
    print(type(api))
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    if 1<=itemPerPage<=10:
        
        base_url += f'itemPerPage={itemPerPage}&'
        
        for key, value in api.items():
            if api['key'] != '' and api['targetDt'] != '':
                
                base_url += f'{key}={value}&'
            else: 
                base_url = '필수 요청변수가 누락되었습니다'
                
        
    else: 
        base_url = '1~10까지의 값을 넣어주세요.'
    
    return base_url
