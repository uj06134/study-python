# 람다(lambda): 이름이 없는 함수, 일회성
# lambda 매개변수, ... : 리턴값

# 일반 함수
# def add(number1, number2):
#     return number1 + number2

# 익명 함수
# lambda number1, number2 : number1 + number2

# 사용 예시
# print(list(map(lambda number: number + 2, [1, 2, 3, 4])))

# 실습
# 아래의 list의 각 요소에 2를 곱하여 변경
datas = [2, 4, 6, 8]
print(list(map(lambda number: number * 2, datas)))

# 각 경로 앞에 '/app'를 붙여준다.
urls = ['/game', '/news', '/fashion', '/ranking']
print(list(map(lambda url: '/app' + url, urls)))

# filter(function, iterator)
# 1~10까지 중 짝수만 출력
print(list(filter(lambda number: number % 2 == 0, [i + 1 for i in range(10)])))

# ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
# 'game' 서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
print(list(filter(lambda url: url.split("/")[-1] == 'game',urls)))