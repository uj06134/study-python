from module import *
# 여기서부터 게임 시작!
if __name__ == "__main__":
    ANSWER = generate_numbers()
    tries = 0
    print(ANSWER)
    while True:
        GUESS = take_guess()
        tries += 1
        str, ball = get_score(GUESS, ANSWER)
        print(f"{str}S {ball}B")
        if GUESS == ANSWER:
            print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
            break