# 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요.
# 사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다.
# 사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다.

# w: 쓰기 모드
# a: 추가 모드(기존 내용을 유지한 채로 내용을 추가)
while True:
    with open('vocabulary.txt', 'a', encoding='utf-8') as file_data:
        english_word = input('영어 단어를 입력하세요: ')
        if english_word == "q":
            break
        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == "q":
            break
        file_data.write(english_word + ': ' + korean_word + '\n')

# 실행 결과
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: horse
# 한국어 뜻을 입력하세요: 말
# 영어 단어를 입력하세요: dog
# 한국어 뜻을 입력하세요: 개
# 영어 단어를 입력하세요: q