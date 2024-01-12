# # print(list("ABC"))
#
# # for i in "ABC":
# #     print(i)
#
# # upper(), lower()
# print("Apple123!@#".upper())
# print("Apple123!@#".lower())
#
# # split()
# data = "사과, 바나나, 파인애플, 포도, 복숭아"
# print(data.split(",", maxsplit=2))
# print("A B C D E F".split())
# print("A    \n      B".split())
# print("A   B".split(" "))
#
# # join()
# print(":".join(['a', 'b', 'c']))
# print("".join(['a', 'b', 'c']))
#
# # replace('기존 값', '새로운 값')
# print("A b C d".replace(" ", ""))
# print("안녕! 반가워~!".replace("!", "?"))
#
# # strip(), lstrip(), rstrip(): 앞 뒤 공백을 제거할 때 보통 사용한다.
# print("a    b    c         ".strip())
# print("a    b    c         ".strip(" "))
# print("apple".strip("a"))
#
# # index(): 찾고자 하는 값이 없으면 오류가 발생한다.
# print("ABC".index("A"))
# # print("ABC".index("Z")) # 오류
#
# # find(): 찾고자 하는 값이 없으면 -1을 가져온다.
# print("ABC".find("A"))
# print("ABC".find("Z"))
#
# # in: 값의 유무 검사
# print("A" in "ABC")
# print("Z" in "ABC")
#
# # count(): 전달한 값이 몇 개 있는지 검사
# print("fmdsklfmldksmfoiejwonfodsnjkfnoieqnofnip".count("o"))

# s = "189,000 원"
# print("".join(i for i in s if '0' <= i <= '9'))
