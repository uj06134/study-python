# keyword arguments

# def introduce(**intro):
#     print(intro)
#     print(type(intro))
#     print(f'name: {intro["name"]}')
#
#
# info_dict = {
#     'name': '한동석'
# }
#
# introduce(name='한동석')
# introduce(**info_dict)

# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')


order_info(3000, 2000, 1000, name='한동석')

# 국어, 영어, 수학 점수의 평균 구하기
# kwargs를 사용
# def average(**kwargs):
#     kor = kwargs['kor']
#     eng = kwargs['eng']
#     math = kwargs['math']
#     return (kor + eng + math) / 3
#
#
# print(average(kor=100, eng=30, math=22))

# 국어, 영어, 수학 점수의 평균 구하기
# 사용자가 원하는 자리수(round)에서 반올림해준다.
# 자리수를 받지 않았다면, 기본값을 리턴한다.
# def average(**kwargs):
#     kor, eng, math = kwargs.get('kor'), kwargs.get('eng'), kwargs.get('math')
#     total = kor + eng + math
#     avg = total / 3
#
#     if "round" in kwargs:
#         return round(avg, kwargs['round'])
#
#     return avg
#
# print(average(kor=100, eng=30, math=22, round=3))

# 반드시 key와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 한다.
# def average(*, kor, eng, math):
#     return (kor + eng + math) / 3
#
#
# print(average(kor=100, eng=30, math=22))

# 주문 총 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    '''
    주문 총 가격과 주문한 회원의 정보 출력
    :param args: 주문 가격들
    :param kwargs: 회원의 정보
    '''
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')

# 함수 설명
help(order_info)