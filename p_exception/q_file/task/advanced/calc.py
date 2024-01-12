# 사용하는 메인 모듈을 기준으로 경로를 작성해야한다.
from q_file.task.advanced.log import log_time


class Calculator:
    def __init__(self, number: int):
        # 사용자가 원하는 연산기호를 oper에 담기 위해 준비해놓는다.
        self.oper = None
        # 연산할 첫 번째 정수
        self.number = number

    def calc(self, other: int, oper: str, error_code: str=""):
        '''

        :param other: 연산할 두 번째 정수
        :param oper: 연산할 연산 기호
        :param error_code: 오류 발생 시 오류 코드
        :return: 결과값(연산결과 또는 None)
        '''

        # 전달받은 연산기호에 알맞은 인덱스 번호를 설정한다.
        oper_number = {'+': 0, '-': 1, '*': 2, '/': 3}
        # 전달받은 연산기호를 self.oper에 담아준다.
        self.oper = oper
        # 실행가능한 함수들을 list에 저장해놓는다.
        operations = [self.__add__, self.__sub__, self.__mul__, self.__floordiv__, self.write_error]
        # 만약 error_code가 있을 경우 write_error함수를 동작시키고
        # error_code가 없을 경우 알맞은 연산 메소드를 실행시킨다.
        return operations[oper_number[oper] if not error_code else 4](other, error_code=error_code)

    @log_time
    # self, other는 *args로 전달되고,
    # error_code는 **kwargs로 전달된다.
    def __add__(self, other, **kwargs):
        return self.number + other

    @log_time
    def __sub__(self, other, **kwargs):
        return self.number - other

    @log_time
    def __mul__(self, other, **kwargs):
        return self.number * other

    @log_time
    def __floordiv__(self, other, **kwargs):
        # 몫과 나머지 모두 구현
        return self.number // other, self.number % other

    # error_code가 있을 때(에러가 발생했을 때), 
    # log에 error를 기록할 수 있도록 도와주는 도구로 사용
    # 즉, log_time()을 실행하기 위해 제작된 함수
    @log_time
    def write_error(self, other, **kwargs):
        pass

