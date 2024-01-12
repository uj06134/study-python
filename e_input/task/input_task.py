# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다.
# email = input('이메일을 입력하세요: ')
# id = email.split('@')[0]
# domain = email.split('@')[1]
# print(f'아이디:{id} 도메인:{domain}')

# message = '이메일: '
# id, domain = input(message).split('@')
# formatting = f'아이디: {id}\n도메인: {domain}'
# print(formatting)
'''
    첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''
# yard = int(input("yard 입력: "))
# inch = int(input("inch 입력: "))

# yard_cm = round(yard * 91.44, 2)
# inch_cm = round(inch * 2.54, 2)

# print(f'{yard}야드는 {yard_cm}cm \n{inch}인치는 {inch_cm}cm')

yard_message = 'yard 입력: '
inch_message = 'inch 입력: '

yard = float(input(yard_message))
inch = float(input(inch_message))

yard_to_cm = round(yard * 91.44, 2)
inch_to_cm = round(inch * 2.54, 2)

yard_formatting = f'{yard} yard는 {yard_to_cm}cm'
inch_formatting = f'{inch} yard는 {inch_to_cm}cm'

print(yard_formatting, inch_formatting, sep='\n')
