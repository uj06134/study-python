# 로또 시뮬레이션 프로그램: 번호뽑기
from random import randint

def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers

# 테스트 코드
# print(generate_numbers(6))


# 로또 시뮬레이션 프로그램: 당첨번호 뽑기(보너스 번호 포함)
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    regular_numbers = sorted(winning_numbers[:6])
    bonus_number = winning_numbers[-1]
    return regular_numbers + [bonus_number]

# 테스트 코드
# print(draw_winning_numbers())


# 로또 시뮬레이션 프로그램: 겹치는 번호 개수
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1
    return count


# 테스트 코드
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))


# 로또 시뮬레이션 프로그램: 당첨금 확인
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 500000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# 테스트 코드
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
