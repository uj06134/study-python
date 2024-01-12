# f(x) = 2x+1
# def f(x):
#     return 2 * x + 1
#
# result = f(2)
# print(result)
#
# 두 정수의 곱셈 함수
# def multiply(x, y):
#     result = x * y
#     return print(result)
# multiply(2,4)
#
# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def division(x, y):
#     if y != 0:
#         quotient = x // y
#         remainder = x % y
#     return quotient, remainder
# print(division(5, 3))
#
# 1~10까지 print()로 출력하는 함수
# def num_print():
#     for i in range(1, 11):
#         print(i, end='')
# num_print()
#
# 이름을 n번 print()로 출력하는 함수
# def name_print(name, n):
#     for i in range(n):
#         print(name)
# name_print('khj', 6 )
#
# 1~n까지의 합을 구해주는 함수
# def sum_n(n):
#     result = 0
#     for i in range(1, n):
#         result = result + i
#     return result
#
# print(sum_n(5))
#
# 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def multiples_n(n):
#     for i in range(1, 101):
#         if i % n == 0:
#             print(i)
#
# multiples_n(5)
#
# 세 정수의 뺄셈 함수
# def subtraction(x, y, z):
#     return x - y - z
#
# print(subtraction(1, 2, 3))
#
# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
# def str_len(string, keyword):
#     count=0
#     for i in string:
#         if i == keyword:
#             count= count + 1
#     print(count)
# str_len('aaaabbbccd','b')
#
# '''
#     문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
#     만약 해당 문자가 없으면 -1을 리턴하는 함수
# '''
# def find(string, keyword):
#     for i in range(len(string)):
#         if string[i] == keyword:
#             return i
#
#     return -1
#
# print(find('apple', 'l'))
