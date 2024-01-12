class Magic:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    # def __str__(self):
    #     return f'{self.__repr__()}, __repr__() 사용됨.'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# print(Magic().__repr__())
# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다 .
# print(Magic().__str__())
# 따라서, 생략해서 작성하면 __str__()이 붙게된다.


# print(Magic())

magic = Magic('magic')
print(magic)

class Student:
    def __init__(self, number, score):
        self.number = number
        self.score = score

    def __add__(self, other):
        return self.score + other.score

    # 순차적 검사
    def __eq__(self, other):
        # 먼저 주소 비교부터 실행 (repr을 붙이지 않으면 검사불가)
        if self.__repr__() == other.__repr__():
            return True

        # 타입 비교
        # isinstance(객체, 타입): 전달한 객체가 전달한 타입일 경우 True. 아니면 False
        if isinstance(other, Student):
            # 값 비교
            return self.number == other.number

        return False


std1 = Student(1,30)
std2 = Student(1,50)

# add 메소드
total = std1.__add__(std2)
total2 = std1 + std2
print(total)
print(total2)

# dict 메소드
print(std1.__dict__)
print(std1.__dict__.__getitem__('score'))

# 두 결과의 값 비교
print(std1 == std2)
