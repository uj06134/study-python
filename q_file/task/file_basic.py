# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면, fish.txt의 전체 내용을 삭제한다.
# 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.

# with open('./fish.txt', 'w', encoding='utf-8') as file:
#     pass

# with open('./fish.txt', 'a', encoding='utf-8') as file:
#     fish = input('물고기: ') + '\n'
#     file.write(fish)

# with open('./fish.txt', 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         print(line, end='')

# title = 'q: 삭제, r: 읽기'
# message = '물고기: '
#
# while True:
#     path = input('경로: ')
#     fish = input(title + '\n' + message)
#
#     if fish == 'q':
#         with open(path, 'w', encoding='utf-8') as file:
#             pass
#
#     elif fish == 'r':
#         try:
#             with open(path, 'r', encoding='utf-8') as file:
#                 for line in file.readlines():
#                     print(line, end='')
#             break
#         except FileNotFoundError:
#             print('경로를 다시 확인해주세요.')
#
#     else:
#         with open(path, 'a', encoding='utf-8') as file:
#             file.write(fish + '\n')

# 고등어를 참치로 수정하기
content = ""
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    # 전체 내용을 한 줄씩 읽어오기
    while line != '':
        # 한 줄을 line에 담기
        line = file.readline()
        # 담은 내용이 찾고 있는 햄버거일 경우
        if line == '고등어\n':
            # content에 치킨으로 변경해서 담기
            content += '참치\n'
            continue

        # 수정 대상이 아닌 줄은 그대로 content에 담기
        content += line

    # 수정 완료된 문자열 값 확인
    print(content)

# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(content)

# 원본 파일의 내용 확인
with open('fish.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))