# random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 문제를 내도록 프로그램을 바꿔 보세요.
# 같은 단어를 여러 번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random

vocab = {}
with open('data/vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word
    keys = list(vocab.keys())
    # print(vocab)
    # print(len(keys))
while True:
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    quiz = input(f'{korean_word}: ')
    if quiz == english_word:
        print("맞았습니다!")
    elif quiz == "q":
        break
    else:
        print(f"아쉽습니다. 정답은 {english_word}입니다")

# 실행 결과
# 말: horse
# 맞았습니다!
# 개: dog
# 맞았습니다!
# 물: water
# 맞았습니다!
# 말: q