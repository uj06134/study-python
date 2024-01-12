# 두 정수의 연산을 수행하는 계산기 모듈 및 로그 기록 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록한다.
# 로그를 기록하는 모듈은 데코레이터로 제작한다.
# 아래와 같은 형식으로 현재 시간을 기록한다
# now = datetime.datetime.now()
# now.strftime('%Y-%m-%dT%H:%M:%S')

# 입력 예
# 두 정수를 입력하세요.
# 예)3 4
# 1 3

# 연산자를 입력하세요.(+, -, *, / 중 1 택)
# +

# 출력 예
# 1 + 3 = 4  KST2024-01-11T00:00:00
# ZeroDivisionError KST2024-01-11T00:00:00

from advanced.calc import Calculator

menu = "1. 계산하기\n2. 로그보기\n3. 종료하기\n"
number_message = "두 정수를 입력하세요.\n예)3 4\n"
oper_message = "연산자를 입력하세요.(+, -, *, / 중 1 택)\n"
error_message = "다시 시도하세요."
error_code = None

while True:
    choice = int(input(menu))
    # 계산하기
    if choice == 1:
        error_code = ""
        number1, number2, oper = "", "", ""
        try:
            number1, number2 = map(int, input(number_message).split())
            oper = input(oper_message)

        except ValueError:
            error_code = "ValueError"

        finally:
            if oper == "/":
                if number2 == 0:
                    error_code = "ZeroDivisionError"
            result = Calculator(number1).calc(number2, oper, error_code=error_code)
            if result:
                print(result)
            else:
                print("다시 시도해주세요.")
    elif choice == 2:
        with open('log.txt', 'r', encoding='utf-8') as file:
            print(file.read())

    elif choice == 3:
        break

    else:
        print(error_message)











