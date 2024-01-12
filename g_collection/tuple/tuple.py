# List
# mutable: 변할 수 있는
data_list = [1, 2, 3, 4]
data_list2 = data_list
data_list2[0] = 10
print(data_list2)
print(data_list)

# Tuple
# immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1
# data_tuple2[0] = 10
data_tuple2 = data_tuple1 + (5, 6)

# 괄호 생략가능
datas = 1, 2
print(type(datas))

# 상수는 대문자
ERROR_CODE = 1,
print(ERROR_CODE[0])