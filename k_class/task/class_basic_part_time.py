# PartTimer

# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

class PartTimer:
    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, nickname, address='청담동'):
        self.nickname = nickname
        self.address = address
        self.total_money = 0
        # self로 쓰면 안되는 이유 값을 각각 가져야함
        PartTimer.total_of_part_timers += 1

    def calculate_money(self, hour, bonus=0):
        # 일당
        total_money = PartTimer.pay_of_hour * hour + bonus
        # 급여 총액
        self.total_money += total_money

        return total_money


ryan = PartTimer('라이언')
neo = PartTimer('네오', '역삼동')

print(ryan.total_money, ryan.nickname, ryan.address)
result = ryan.calculate_money(8, 10000)
print(ryan.total_money, ryan.nickname, ryan.address)

