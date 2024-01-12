# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # 추가(초보자용)
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     user_info.append({'number': number, 'name': name})
#
#
# # 추가
# # 회원 번호는 자동 증가한다.
# number = 5
# def insert(name):
#     global number
#     number += 1
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     return user_info
#
#
# # 조회(번호로 조회)
# def select(number):
#     for user in user_info:
#         if user['number'] == number:
#             return user
#     return {}
#
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#     '''
#     select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     del user_info[user_info.index(select(number))]
#

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
number_list = 5
def insert(number, title, content, file, read_count=0):
    global number_list
    number_list += 1
    post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})

insert(number= 6, title='테스트 제목6', content= '테스트 내용6', file= '/usr/post/file/img005.png')

# 목록(최신순으로 조회)
def list():
    return post_info[::-1]
print(list())

# 조회(번호로 조회, 조회수 1 증가)
def select(number):
    for user in post_info:
        if user['number'] == number:
            user['read_count'] += 1
            return user

# 수정(번호로 정보 수정)
def update(**kwargs):

        select(kwargs.get('number'))['number'] = kwargs.get('number')
        select(kwargs.get('number'))['title'] = kwargs.get('title')
        select(kwargs.get('number'))['content'] = kwargs.get('content')
        select(kwargs.get('number'))['file'] = kwargs.get('file')
        select(kwargs.get('number'))['read_count'] = kwargs.get('read_count')

update(number= 5, title='테스트 제목7', content= '테스트 내용7', file= '/usr/post/file/img007.png', read_count=0)
print(post_info)

# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]

delete(6)
print(post_info)
