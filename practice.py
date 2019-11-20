# 02 workshop 3번문제

# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# blood_dict = {}

# for b in blood_types:
#     if blood_dict.get(b):
#         blood_dict[b] += 1
#     else:
#         blood_dict[b] = 1
# print(blood_dict)

# 02 homework 2번

# a = list(range(1, 51))
# b = a[0:-1:2]
# print(b)
#------------------------------------------------------------------------
# 03  workshop
# sol = input()
# def palindrome_sol1(x):    
# 	if x == x[::-1]:
#     	    return True
# 	else:
#     	    return False

# sol1 = palindrome_sol1(sol)
# print(sol1)


# 1-2 

# def is_palindrome(word):
#     list_word = list(word)
#     for i in range(len(list_word) // 2):
#         if list_word[i] != list_word[-i-1]:
#             return False
#     return True

# print(is_palindrome('level'))
# print(is_palindrome('asdf'))


# # 4444444444444 workshop 4444444444444444444444444

# def my_sqrt(n):
#     x, y = 1, n # 양의 정수 -> 1 ~ n
#     result = 1 # 우리가 추측하는 제곱근의 근사값

#     # while not math.isclose(result ** 2, n):
#     while abs(result**2 - n) > 0.0000000001:
#         # 제곱근의 제곱과 입력 값의 차이가 적어도 0.000000001보다
#         # 작아지면 그 차이가 거의 없다고 봄.
#         result = (x + y) / 2
#         # 양쪽 끝 값의 절반을 다시 제곱근의 근사치로 둠
#         if result ** 2 < n :
#             x = result
#         else :
#             y = result

#     return result

# print(my_sqrt(2))

# import math
# print(math.sqrt(2))

#44444444444444444 Home Work 44444444444444444444444444444

