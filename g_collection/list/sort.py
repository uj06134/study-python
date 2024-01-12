# 정렬
number_list = [5, 4, 6, 1, 3]
# 1. sort(): 원본이 그대로 변경됨
# number_list.sort(reverse=True)
# print(number_list)

# 2. sorted(): 원본은 유지되고 새로운 list가 만들어짐
sorted_list = sorted(number_list, reverse=True)
print(sorted_list)


