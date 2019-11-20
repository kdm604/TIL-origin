import webbrowser

#webbrowser.open('https://google.com')
#webbrowser.open_new('https://www.naver.com')
#webbrowser.open_new_tab('https://www.naver.com')
lists = ['짱구','짱구 훈이']
for i in lists:
    print(type(i))
    webbrowser.open('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%s'%i)

