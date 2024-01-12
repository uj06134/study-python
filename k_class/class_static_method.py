class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    # 객체로 접근하는게 아니니 self를 사용하지 않는다.
    @staticmethod
    def print_start_time_of_study():
        print('9시 떙')
        Student.status = '공부 중'

kim = Student(0, 0, 0)
lee = Student(0, 0, 0)
print(Student.status)

Student.print_start_time_of_study()

