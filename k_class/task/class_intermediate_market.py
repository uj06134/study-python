# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product:
    # 상품명, 가격
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(self.name, self.price)


# 손님
# 이름, 나이, 할인율, 잔액
class Customer:
    # 이름, 나이, 할인율, 잔액
    def __init__(self, name, age, discount=0, money=0):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money


# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Market:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell(self, customer):
        customer.money -= self.product.price * (1 - customer.discount * 0.01)
        self.stock -= 1


product = Product('사과', 5000)
customer = Customer('한동석', 20, 50, money=10000)
market = Market(product, 40)
market.sell(customer)

print(market.stock)
print(customer.money)