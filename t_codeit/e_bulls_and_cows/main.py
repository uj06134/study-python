# 먼저 정답 숫자 3개를 뽑아 주는 generate_numbers() 함수를 작성할 것입니다.
# 이 함수는 무작위로 0과 9 사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴합니다.
from random import randint

def generate_numbers():
    numbers = []
    for i in range(3):
        numbers.append(randint(0,9))
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
print(generate_numbers())


# 이번에는 유저에게 숫자 3개를 입력 받는 take_guess() 함수를 작성하겠습니다.
# 이 함수는 유저에게 숫자 3개를 반복적으로 입력 받은 후, 유저가 입력한 숫자들을 리스트에 정리해서 리턴합니다.
# 유저가 범위에서 벗어나는 숫자를 입력하면, 범위를 벗어나는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다
# 마찬가지로 유저가 이미 입력한 숫자를 다시 입력하면, 중복되는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다.
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 여기에 코드를 작성하세요

    return new_guess


# 테스트 코드
print(take_guess())