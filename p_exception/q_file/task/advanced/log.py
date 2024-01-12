import datetime


def log_time(original_function):

    def logging(*args, **kwargs):
        self, other = args
        error_code = kwargs.get('error_code')
        with open('log.txt', 'a', encoding='utf-8') as file:
            # 만약 error_code가 없다면,
            if not error_code:
                # 원래 함수를 실행시킨다.
                result = original_function(*args, **kwargs)
                # 현재 시간을 알맞은 형식으로 변환하여 담는다.
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                # 나눗셈이라면,
                if self.oper == '/':
                    # 몫과 나머지를 각각 따로 담는다.
                    value, rest = result
                    # 아래 형식으로 log 파일을 작성한다.
                    file.write(f'{self.number} {self.oper} {other} = {value}, {rest}\tKST{now}\n')
                else:
                    # 나눗셈이 아니라면, 아래 형식으로 log 파일을 작성한다.
                    file.write(f'{self.number} {self.oper} {other} = {result}\tKST{now}\n')

                # 연산 결과를 리턴한다.
                return result
            else:
                # error_code가 있을 때, 아래 형식으로 log 파일을 작성한다.
                now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                file.write(f'{error_code}\tKST{now}\n')

        # error_code가 있을 때 None을 리턴한다.
        return None

    return logging
