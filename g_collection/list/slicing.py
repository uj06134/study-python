# 인덱스 슬라이싱
# animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0 : exclusive_end=len(list)] -> list
# print(animals[0])
# print(animals[0:3])
# print(animals[1:4])
# print(animals[:2])
# print(animals[2:])

# list[inclusive_start=0 : exclusive_end=len(list) : step=1] -> list
# food = ['noodle', 'meat', 'bread', 'chicken']
# print(food[:3:2])
# print(food[2::2])

# 역순 출력
# print(food[::-1])

# 실습
# number_list = list(range(1, 11))
#
# # [1, 3, 5, 7, 9]
# print(number_list[::2])
#
# # [6, 5, 4, 3, 2]
# print(number_list[5:0:-1])
#
# # [2, 4, 6]
# print(number_list[1:6:2])
#
# # [2, 3, 4, 5, 6, 7]
# print(number_list[1:7])

# animals = ['dog', 'dog', 'cat', 'bird']
# zoo = ['panda', 'giragge']
#
# animals[1:2] = zoo
# print(animals)
#
# animals.insert(animals.index('dog') + 1, 'elephant')
# print(animals)

# 슬라이싱, insert, del를 사용하여 아래의 list만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
# animals = ['dog', 'dog', 'cat', 'bird']
# add = ['hamster', 'fish']
# animals.insert(animals.index('dog') + 1, add[0])
# animals.insert(animals.index('dog') + 2, add[1])
# animals[4] = 'whale'
# print(animals)