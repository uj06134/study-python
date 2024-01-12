class Car:

    # 정적 변수(static variable)
    wheel = 4

    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + '시동 꺼짐')


mom_car = Car('Benz', 'Black', 15000)
daddy_car = Car('BMW', 'Blue', 8800)

mom_car.engine_start()
daddy_car.engine_start()

print(Car.wheel)

Car.wheel = 6

print(mom_car.wheel)

cars = [Car, Car]
mom_car = cars[0]()
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')
