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

with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

temp = ""
for character in content:
    if 'a' <= character <= 'z':
        temp += character
        continue
    temp += " "

content = temp

words = [
    word
    for word in content.split()
    if len(word) > 1
]

result = {}
for word in words:
    if result.get(word) is not None:
        result[word] += 1

    else:
        result[word] = 1

result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}

sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])

#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))
