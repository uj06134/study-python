# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
# with 문을 사용하면 with 문에 속해 있는 문장을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.
with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()
# temp = 임시 저장공간
temp = ""

# 내용을 반복문을 돌려 한글자씩 추출
for character in content:
    # 알파벳이라면
    if 'a' <= character <= 'z':
        # temp에 하나씩 추가
        temp += character
    # 알파벳이 아니라면
    else:
        # temp에 빈 문자열을 추가 (서로 떨어져 있는 단어들끼리 구분을 위해 사용)
        temp += " "

content = temp


# 내용을 공백으로 분리하고 글자수가 두개이상이면 word에 담는다.
# word를 반환하면서 리스트 형태가 풀렸기 떄문에 다시 리스트 형태로 바꿔준다.
words = [word for word in content.split() if len(word) >= 2]


# 컴프리헨션을 푼 식
# content = content.split()
# if len(content) >= 2:
#     words = content
# print(words)

# 키-값으로 찾기위해 딕셔너리 변수 생성
result = {}

# words에서 하나씩 단어를 뽑아
for word in words:
    # 딕셔너리에 단어가 존재하면
    if result.get(word) is not None:
        # 그 단어(key)의 value에 1을 더함
        result[word] += 1
    # 단어가 존재하지 않는다면 value에 1을 저장
    else:
        result[word] = 1

# 단어의 value, 즉 빈도수가 100이상이라면 word를 result의 key:value에 나눠 저장한다.
result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}

# value로 내림차순 정렬을 하기 위해 key에 result.get을 사용해 정렬
sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])

