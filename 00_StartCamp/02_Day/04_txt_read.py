# #1-1. 파일 읽기(옛날방식) - read()
# # f = open('ssafy.txt','r')
# # all_text = f.read() # read는 문자열로 리턴해주는 친구~
# # print(all_text)
# # f.close()

# #1-2. 파일 읽기 (최에에에신 방식) - read()
# with open('with_ssafy.txt','r') as f:
#     all_text = f.read()
#     print(all_text)


# 2-1. 파일읽기 (옛날 방식 )  - readlines()
# f = open('ssafy.txt','r')
# lines = f.readlines()
# print(lines)
# for line in lines:
#   # print(lines)
#     print(line)
# f.close()

# 2-2. 파일읽기 (최에에에에에ㅔ시시시ㅣ잉인 방식) - readlines

with open('with_ssafy.txt','r') as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip()) # 개행문자를 제거한다? strip??

