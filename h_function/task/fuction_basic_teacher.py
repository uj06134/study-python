def use_coupon(*pay, **kwargs):
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    # 만약 쿠폰이 있다면
    if 'coupon' in kwargs:
        return [
            # 1 - (할인율 * 0.01) * 주문금액[i] i=
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            for i in
            # 만약 쿠폰의 개수가 주문 횟수보다 적거나 같다면 쿠폰의 개수만큼 돌리고 아니라면 주문 횟수만큼 돌려라
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]

    return None

help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=2)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')
