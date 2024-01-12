# 중복이 없고, 순서가 없다.
# 중괄호로 값이 하나씩 연결되어 있으면 set (키-값이 있으면 딕셔너리)
world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
# print(world_set[0]) set은 값을 가져올 수 없음

# 중복을 제거할 때 효과적이다.
datas = [1, 1, 3, 2, 3, 4, 1, 4, 4]
print(list(set(datas)))

# add
world_set.add('korea')
print(world_set)

