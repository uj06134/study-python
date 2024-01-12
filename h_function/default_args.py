# 만약 값을 매개변수로 전다하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value로 작성한다.
# def sub(number1, number2, number3, number4=0):
#     return number1 - number2 - number3 - number4
#
# result = sub(1,2, 3, 4)
# print(result)

# 실습
# 이름이 전달받지 못하면 '익명'으로 대체하고,
# 나이를 전달받지 못하면 0으로 대체한다.
def get_info(name='익명', age=0):
    return {'name':name, 'age':age}

result = get_info(name='khj')
print(result)