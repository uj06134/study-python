# 동물
# 이름, 나이, 성별, 음식 개수, 체력 개수
# 먹기, 산책하기

class Animal:
    def __init__(self, name, age, gender, feed_count=1, life=1):
        self.name = name
        self.age = age
        self.gender = gender
        self.feed_count = feed_count
        self.life = life

    # 음식 1개 소모, 체력 1개 획득
    def eat(self):
        self.feed_count -= 1
        self.life += 1

    # 체력 1개 소모, 음식 1개 획득
    def walk(self):
        self.life -= 1
        self.feed_count += 1

tiger = Animal(name='호랑이', age=10, gender='수컷')
tiger.eat()

print(tiger.name, tiger.age, tiger.gender, tiger.feed_count, tiger.life)

