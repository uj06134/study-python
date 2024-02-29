# 먼저 정답 숫자 3개를 뽑아 주는 generate_numbers() 함수를 작성할 것입니다.
# 이 함수는 무작위로 0과 9 사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴합니다.
from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 테스트 코드
# print(generate_numbers())


# 이번에는 유저에게 숫자 3개를 입력 받는 take_guess() 함수를 작성하겠습니다.
# 이 함수는 유저에게 숫자 3개를 반복적으로 입력 받은 후, 유저가 입력한 숫자들을 리스트에 정리해서 리턴합니다.
# 유저가 범위에서 벗어나는 숫자를 입력하면, 범위를 벗어나는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다
# 마찬가지로 유저가 이미 입력한 숫자를 다시 입력하면, 중복되는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 다시 입력을 받습니다.
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        guess_number = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))
        if 0 <= guess_number <= 9:
            if guess_number not in new_guess:
                new_guess.append(guess_number)
            else:
                print("중복되는 숫자입니다. 다시 입력하세요.")

        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

    return new_guess


# 테스트 코드
# print(take_guess())

# 이제 스트라이크 수와 볼 수를 알려 주는 get_score() 함수를 작성할 것입니다. 이 함수는 두 개의 파라미터를 받는데요.
# guesses: 유저가 뽑은 번호 3개가 담긴 리스트
# solution: 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
# 두 리스트를 비교해서 스트라이크와 볼의 개수를 계산하고 리턴합니다.

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        else:
            if guesses[i] in solution:
                ball_count += 1

    return strike_count, ball_count


# 테스트 코드
# s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
# print(s_1, b_1)
#
# s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
# print(s_2, b_2)
#
# s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
# print(s_3, b_3)
#
# s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
# print(s_4, b_4)

