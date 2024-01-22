# [종합 실습]
# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고
#
# 신한
#    입금 시 수수료 50%
# 국민
#    출금 시 수수료 50%
# 카카오
#    잔액조회 재산 반토막
#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
#
# banks 컴프리헨션으로 2차원 리스트 만들기
# check에다 중복검사를 하고 중복검사 서비스 통일

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

    # 어떤 은행에서 개설하는 지를 bank_choice로 전달받는다.
    # 개설에 필요한 모든 회원정보는 **kwargs로 받는다.
    @classmethod
    # 계좌 개설
    def open_account(cls, bank_choice, **kwargs):
        # ex) bank = [신한][0](kwargs)
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # ex) 리스트 형태인 banks[0]에 kwargs(예금주, 계좌번호 등)를 딕셔너리 형태로 바꾸어 추가
        # dict을 쓴 이유: check 함수에서 원하는 key로 회원의 정보를 찾기 위해서
        cls.banks[bank_choice - 1].append(user.__dict__)
        return user

    # self에 접근하는 메소드가 아니기 때문에, staticmethod 데코레이터를 붙여서 사용한다.
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

# 이 파일이 실행하는 파일이다.
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 재설정\n" \
           "6. 나가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        # 은행 나가기
        if bank_choice == 4:
            break
        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 못하게 막아준다.
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 메뉴 나가기
            menu_choice = int(input(menu))
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)
                # 계좌번호 입력
                while True:
                    account_number = input(account_number_message)
                    # None은 False값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 접근한다.
                    if Bank.check_account_number(account_number) is None:
                        break
                # 휴대폰 번호 입력
                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break
                # 비밀번호 입력
                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break
                # 돈 입력
                money = int(input(money_message))
                # user는 입력받은 정보를 사용하여 새로운 은행 계좌를 개설
                user = Bank.open_account(bank_choice,
                                         owner=owner,
                                         account_number=account_number,
                                         phone=phone,
                                         password=password,
                                         money=money
                                         )
                print(user)

                # 입금
            elif menu_choice == 2:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)

                if isinstance(user['object'], ShinHan):
                    # 선택된 은행이 1(신한은행)이 아니라면,
                    if bank_choice != 1:
                        print('개설한 은행에서만 입금 서비스를 사용 할 수 있습니다')
                        continue
                # 해당 회원을 찾았다면,
                if user is not None:
                    if user['password'] == input(password_message):
                        deposit_money = int(input(deposit_message))
                        # user 딕셔너리에서 object키를 통해 해당 객체에 접근
                        user['object'].deposit(deposit_money)

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                print('들어옴')
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                # 해당 회원을 찾았다면,
                if user is not None:
                    if user['password'] == input(password_message):
                        withdraw_money = int(input(withdraw_message))
                        # 국민은행의 경우 출금할 금액을 1.5배로 계산하고, 해당 금액이 계좌 잔액보다 작거나 같은지 확인
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            # user 딕셔너리에서 object키를 통해 해당 객체에 접근
                            user['object'].withdraw(withdraw_money)
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                # 해당 회원을 찾았다면,
                if user is not None:
                    if user['password'] == input(password_message):
                        # user 딕셔너리에서 object키를 통해 해당 객체에 접근
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                # 해당 회원을 찾았다면,
                if user is not None:
                    if user['phone'] == input(phone_message) and user['password'] == input(password_message):
                        # 만약 비밀번호와 핸드폰 번호가 일치하면, 새로운 계좌번호를 입력 받음
                        new_account_number = input("새로운 계좌번호를 입력하세요: ")
                        # 사용자의 계좌번호를 새로운 값으로 업데이트
                        user['object'].account_number = new_account_number
                        print("계좌번호가 재설정되었습니다")
                    else:
                        print("잘못된 비밀번호 또는 핸드폰 번호입니다")
                else:
                    print(error_message)

