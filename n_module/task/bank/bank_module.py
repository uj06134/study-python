# 중복 검사
# 정확히 어떤 것을 검사할 지는 사용자에게 전달받은 key로 확인할 수 있다.
def check(*, key: str, value: str) -> dict:
    # 저장소(DB)에서 각 은행 정보를 가져온 뒤
    for bank in Bank.banks:
        # 각 은행에서 회원의 정보를 가져온다.
        for user in bank:
            # 전달받은 키워드(key)로 회원의 정보가 value와 같은 지 검사한다.
            if user[key] == value:
                # 만약 해당 회원을 찾았다면, 회원의 전체 정보를 리턴한다.
                return user
    # 해당 회원을 찾지 못했다면, None을 리턴한다.
    return None


class Bank:
    total_count = 3                                 # 은행의 수
    banks = list([] for i in range(total_count))    # 리스트를 은행의 개수만큼의 인덱스를 생성 세 개의 빈 리스트(list comprehension)

    # 생성자에 예금주, 계좌번호, 핸드폰 번호, 비밀번호, 돈 생성
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # self는 주소값, 각 회원의 object 필드에는 필드의 주소값이 담긴다.
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money


    # self에 접근하는 메소드가 아니기 때문에, staticmethod 데코레이터를 붙여서 사용한다.
    @classmethod
    # 계좌 개설
    def open_account(cls, bank_choice, **kwargs):
        # ex) bank = [신한][0](kwargs)
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # ex) 리스트 형태인 banks[0]에 kwargs(예금주, 계좌번호 등)를 딕셔너리 형태로 바꾸어 추가
        # dict을 쓴 이유: check 함수에서 원하는 key로 회원의 정보를 찾기 위해서
        cls.banks[bank_choice - 1].append(user.__dict__)
        return user

    @staticmethod
    # check()에서 key-value를 딕셔너리 형태로 리턴
    def check_account_number(account_number: str) -> dict:
        return check(key='account_number', value=account_number)

    @staticmethod
    # check()에서 key-value를 딕셔너리 형태로 리턴
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)

    # 입금
    def deposit(self, money: int):
        self.money += money                         # init에서 받아온 money += deposit에서 받은 money

    # 출금
    def withdraw(self, money: int):
        self.money -= money                         # init에서 받아온 money -= deposit에서 받은 money

    # 잔고
    def balance(self):
        return self.money                           # init에서 받아온 money(잔고) 리턴

    # 객체를 출력하면 __str__()가 실행되기 때문에, 바로 리턴값으로 출력가능
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


# Bank 상속
class ShinHan(Bank):

    # 신한 - 출금
    def deposit(self, money: int):
        money //= 2
        # 오버라이딩 (부모의 메소드를 그대로 사용하고자 할 떄)
        super().deposit(money)


class KookMin(Bank):
    # 국민 - 입금
    def withdraw(self, money: int):
        money *= 1.5
        # 오버라이딩 (부모의 메소드를 그대로 사용하고자 할 떄)
        super().withdraw(int(money))


class KaKao(Bank):
    # 카카오 - 잔고
    def balance(self):
        self.money //= 2
        # 오버라이딩 (부모의 메소드를 그대로 사용하고자 할 떄)
        return super().balance()