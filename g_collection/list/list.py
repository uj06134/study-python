# animals = ["dog", "cat", "bird", "fish"]
# print(animals)
# print(type(animals))
#
# # 인덱스로 접근
# print(animals[1])
# print(animals[2])
#
# # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
# print(animals[-1])
# print(animals[-2])
#
# # len()
# print(len(animals))
#
# # append()
# animals.append("hamster")
# print(len(animals))
# print(animals)
#
# animals.append("cat")
# print(animals)
#
# # insert()
# animals.insert(1, "dog")
# print(animals)
#
# # remove()
# animals.remove('fish')
# print(animals)
#
# # del()
# # del(animals[1])
# del animals[1]
# print(animals)
#
# # clear()
# # animals.clear()
# # print(animals)
#
# # index()
# print(animals.index('bird'))
# # print(animals.index('tiger'))
#
# # 수정
# index = animals.index('bird')
# animals[index] = 'lion'
# print(animals)
#
# # 그 외
# animals = ["dog", "cat", "bird", "fish"]
# print(animals * 2)
#
# print("dog" in animals)
# print("tiger" in animals)
#
# for animal in animals:
#     print(animal)

# # 실습
# 1~90까지 list에 담고 출력
# list1 = []
# for i in range(1, 91):
#     list1.append(i)
# print(list1)

# 플이
# number_list = list(range(90))
# for i in range(len(number_list)):
#     number_list[i] = i + 1
# print(number_list)


# # 1~100까지 중 짝수만 list에 담고 출력
# list2 = []
# for i in range(2, 101, 2):
#     list2.append(i)
# print(list2)

# 플이
# number_list = list(range(100))
# for i in range(number_list):
#     number_list[i] = (i+1) * 2
# print(number_list)

# # 1~10까지 list에 담은 후 짝수만 출력
#1~10까지 list에 담은 후  짝수만 출력
# number_list3 = [0] * 10
# for i in range(len(number_list3)):
#     number_list3[i] = i + 1
#     if i % 2 == 0:
#         print(i, end ='')

# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# member = ['사람1', '사람2', '사람3', '사람4']
#
# member[1] = '바꾼 사람2'
# print(member)
#
# member.remove(member[-1])
# print(member)

# list안에 list
number_list = [[1, 3, 5],[2, 4, 6]]
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j] )
