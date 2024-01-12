# 인간(부모)
# 이름, 나이

# 걷기(walk)
# '두 발로 걷습니다' 출력
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('두 발로 걷습니다.')

# 원숭이(자식)
# 이름, 나이, 동물원 이름

# 걷기(walk)
# '두 발로 걷습니다', '네 발로 걷습니다' 출력
class Monkey(Person):
    # zoo를 추가하기 위해 직접 자식생성자를 선언
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        self.zoo = zoo

    def walk(self):
        # 부모의 메소드를 그대로 사용하고자 할 떄
        super().walk()
        # 자식의 메소드에서 추가할 내용 작성
        print('네 발로 걷습니다.')

kingkong = Monkey('킹콩', 90, '에버랜드')
kingkong.walk()
