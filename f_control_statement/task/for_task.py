# # 1~15까지 출력
# for i in range(1, 16):
#     print(i)

# # 30~1까지 출력
# for i in range(30, 0, -1):
#     print(i)

# # 1~100가지 중 홀수만 출력
# for i in range(1, 101, 2):
#     print(i, end=' ')

# # 1~10까지 합 출력
# result = 0
# for i in range(1, 11):
#     result += i
# print(result)

# # 1~n까지 합 출력
# n = int(input())
# result = 0
# for i in range(1, n+1):
#     result += i
# print(result)

## 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(3):
#     for j in range(3, 7):
#         print(i, end=' ')

# for i in range(12):
#     print(i % 4 + 3, end=' ')

# # '1,235,500'을 1235500으로 출력
# str = '1,235,500'
# result = ''
# for i in str:
#     if i != ',':
#         result += i
# result = int(result)
# print(result + 5)

# str = '1,235,500'
# number = str.split(',')
# print(number[0]+number[1]+number[2])

# # 1~10까지 중 3까지만 출력(break)
# for i in range(10):
#     print(i+1)
#     if i == 2:
#         break

# # 1~10까지 중 4를 제외하고 출력(continue)
# for i in range(10):
#     if i == 3:
#         continue
#     print(i+1)