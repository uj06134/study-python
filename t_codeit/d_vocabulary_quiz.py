# 프로그램은 터미널에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
# 사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 정답은 OOO입니다.가 출력되어야 합니다.
# 문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.

with open('data/vocabulary.txt', 'r', encoding='utf-8') as file_data:
    for line in file_data:
        # print(line)
        strip_data = line.strip()  # 문자열 공백 제거
        split_data = strip_data.split(": ")  # 문자열 나누기
        english_word = split_data[0]
        korean_word = split_data[1]
        quiz = input(f'{korean_word}: ')
        if quiz == english_word:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {english_word}입니다")

# 실행 결과
# 고양이: cat
# 맞았습니다!
# 말: horse
# 맞았습니다!
# 개: dog
# 맞았습니다!
# 물: a
# 아쉽습니다. 정답은 water입니다
# 책: b
# 아쉽습니다. 정답은 book입니다
# 수학: c
# 아쉽습니다. 정답은 math입니다
