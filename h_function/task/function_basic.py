# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.
# 쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수
#
# coupon=40
# count=5
#
# 아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
# 40%쿠폰 5개
#
# 아래와 같은 상황은 없다.
# 10%쿠폰 1개, 20%쿠폰 2개

def order(*args, **kwargs):
    '''
    :param args: 주문 금액
    :param kwargs: {coupon:할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액
    '''
    result = []
    # 쿠폰 개수만큼 반복문 실행 (i = 0, i = 1)
    for i in range(kwargs['count']):
        # 주문 횟수와 쿠폰 개수가 같거나 쿠폰개수가 더 많다면
        if len(args) >= i + 1:
            # i번째 인덱스의 args(주문금액) - kwargs에서 할인율 가져오기(할인된 주문금액)
            pay = int(args[i] - (args[i] * (0.01 * kwargs['coupon'])))
            # 리턴값에 할인율이 적용된 주문 금액 차례대로 추가
            result.append(pay)
    return result
    # # comprehension
    # return [int(args[i] - (args[i] * (0.01 * kwargs['coupon']))) for i in range(kwargs['count']) if len(args) >= i + 1]

print(order(1000,1000,1000,coupon=50, count=2))