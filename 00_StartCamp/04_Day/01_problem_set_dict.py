"""
python dictionary 문제
"""

#1. 평균을 구하세요
# score = {
#     '수학':80, '국어':90, '음악': 100
# }
#
# sum = 0
# for i in score.values():
#     sum = (sum + i)
    
# print(sum/len(score))

#2. 반 평균을 구하세요 -> 전체 평균
# scores = {
# 'a' : {
#     '수학':80, '국어':90, '음악': 100
#     }
# ,
# 'b' : {
#     '수학':80, '국어':90, '음악': 100
#     }
# }

# total_score = 0
# length = 0
# for person_score in scores.values():
#     for sub_score in person_score.values():
#         total_score += sub_score
#         length += 1
# print(total_score/length)

#3. 도시별 최근 3일 온도입니다.

city = { 
    '서울':[-6, -10, 5],
    '대전':[-3, -5, 2],
    '광주':[0, -2, 10],
    '부산':[2, -2, 9]
}
# 3-1 도시별 최근 3일 평균 온도는?
# 3-2 도시 중 최근 3일 중에 가장 추웠던, 가장 더웠던 곳은?
# 3-3 서울 은 영상 2도였던 적이 있나요? -> ex. 네 있어요! or 없어요

#3-1 

for name, temp in city.items():
   average_temp = sum(temp)/len(temp)
   print(f'{name}: {average_temp}')

#3-2 (숙제)

#3-3 
if 2 in city['서울']:
    print('네 있어요!')
else : 
    print('없어요~')

