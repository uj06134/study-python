# def set_key(key):
#     formatting = ''
#
#     # 클로저
#     def set_value(value):
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formatting_name = set_name("한동석")
# print(formatting_name)
#
# # '나이: 00살'
# set_name = set_key('나이')
# formatting_age = set_name("20살")
# print(formatting_age)
#
# print(f'{formatting_name}\n{formatting_age}')

# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.


def set_topic(**kwargs):
    result = 0
    # 입력값에 name
    if 'name' in kwargs:
        def set_format(sep=', '):
            formatting = f'name{sep}{kwargs.get("name")}'
            return formatting
        result = set_format
    else:
        def set_format(sep=', '):
            formatting = f'{kwargs.get("topic")}{sep}{kwargs.get("point")}'
            return formatting
        result = set_format

    return result

print(set_topic(name='한동석')())
print(set_topic(topic='지구 온난화', point='오존층 파괴를 막기 위해 인간이 해야할 일')())


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.
def set_product(*args):
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break

    def select_all():
        return args

    return {'insert': insert, 'update': update, 'select_all': select_all}


products = [
    {'name': '마우스', 'price': 5000},
    {'name': '키보드', 'price': 25000}
]

product_service = set_product(*products)
print(products)
product_service.get('insert')(name='모니터', price=80000)
print(product_service.get('select_all')())
product_service.get('update')(name='키보드', price=20000, number=2)
print(product_service.get('select_all')())

