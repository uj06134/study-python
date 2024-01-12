# 문자열끼리만 연결(+)이 가능하다
# data = 3
# print('안' + str(data))

# name = input("이름: ")
# print(f'{name}님 환영합니다')

# 제 이름은 ???, 키는 ???cm입니다.
# name = input("이름: ")
# height = input("키: ")
# print(f'제 이름은 {name}, 키는 {height}cm입니다.')

# 두 정수를 입력받은 후 곱셈 결과 출력
# x = int(input('정수 1 입력: '))
# y = int(input('정수 2 입력: '))
# print(f'두 정수의 곱: {x * y}')

# map(각각 어떻게 바꿀 것인가, [])
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2z
# formatting = f'{number1} * {number2} =
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# message = '현재 시간: '
# time = input(message)
# hours, minutes = time.split(':')
# formatting = f'{hours}시 {minutes}분'

# print(formatting)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
# message = '핸드폰 번호: '
# number1, number2, number3 = input(message).split('-')
# formatting = f'통신사: {number1}\n앞번호: {number2}\n뒷번호: {number3}\n'

# print(formatting)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
# message = '이름과 나이를 입력하세요'
# example_message = '예)홍길동 20'
#
# name,age = input(message + '\n' + example_message + '\n').split()
# formatting = f'{name}님의 나이는 {age}살'

# print(formatting)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
# message = '3개의 정수를 입력해주세요.'
# example_message = '예)1/2/3'

# number1, number2, number3 = map(int, input(message + '\n' + example_message + '\n').split('/'))
# result = number1 + number2 + number3
# formatting = f'{number1} + {number2} + {number3} = {result}'

# print(formatting)