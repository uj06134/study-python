#%%
# 중복 검사
# 핸드폰 번호와 계좌 번호를 검사할 수 있다.
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
    # 은행의 개수
    total_count = 3
    # 은행의 개수만큼 저장공간을 확보해준다.
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # 각 회원의 object 필드에는 필드의 주소값이 담긴다.
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 어떤 은행에서 개설하는 지를 bank_choice로 전달받는다.
    # 개설에 필요한 모든 회원정보는 **kwargs로 받는다.
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        # 회원이 어떤 은행에서 개설하는 지 알 수 없다.
        # 전달받은 bank_choice를 통해 정확히 은행을 선택할 수 있게 된다.
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 은행 DB에 고객의 정보를 담을 때, dict 타입으로 변환해서 담는다.
        # check 함수에서 원하는 key로 회원의 정보를 찾기 위해서!
        cls.banks[bank_choice - 1].append(user.__dict__)
        # 개설된 회원 정보를 리턴한다.
        return user

    # self에 접근하는 메소드가 아니기 때문에,
    # staticmethod 데코레이터를 붙여서 사용한다.
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check 함수에서 검사할 key와 value를 전달한다.
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone: str) -> dict:
        # check 함수에서 검사할 key와 value를 전달한다.
        return check(key='phone', value=phone)

    def deposit(self, money: int):
        self.money += money

    def withdraw(self, money: int):
        self.money -= money

    def balance(self):
        return self.money

    # 객체를 출력하면 __str__()가 실행되기 때문에,
    # 편하고 빠르게 회원 정보를 확인할 수 있다.
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


class ShinHan(Bank):
    # Overriding
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)


class KookMin(Bank):
    # Overriding
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    # Overriding
    def balance(self):
        self.money //= 2
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
           "5. 계좌 번호 재설정\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

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

        # 나가기
        if bank_choice == 4:
            break

        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 못하게 막아준다.
        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))

            # 은행 메뉴로 돌아가기
            if menu_choice == 6:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    # None은 False값이지만, 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break

                money = int(input(money_message))

                # 계좌가 개설된다.
                # 어떤 은행에서 개설했는 지를 bank_choice에 담아서 전달한다.
                # open_account()는 회원의 정보를 **kwargs로 받기 때문에 모두 풀어서 전달해준다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)

                # 재정의한 __str__()이 사용되고, 회원의 전체 정보를 확인한다.
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능(신한은행)
            elif menu_choice == 2:
                account_number = input(account_number_message)
                # 계좌번호 검색 결과가 user에 담긴다.
                user = Bank.check_account_number(account_number)
                # 해당 회원을 찾았다면,
                if user is not None:
                    # 비밀번호를 검사한다.
                    if user['password'] == input(password_message):
                        # 신한은행 회원인지 검사한다.
                        if isinstance(user.get('object'), ShinHan):
                            # 현재 선택된 은행이 신한은행이 아니라면,
                            if bank_choice != 1:
                                # 신한은행 회원은 신한은행에서만 입금이 가능하다고 안내해준다.
                                print('개설한 은행에서만 입금 서비스를 사용하실 수 있습니다.')
                                # 입금 서비스를 이용하지 못하도록 막아준다.
                                continue


                        # 입금 서비스
                        deposit_money = int(input(deposit_message))
                        # 계좌 개설 시 담아놓은 self(객체)를 통해 메소드를 접근한다.
                        user['object'].deposit(deposit_money)

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        # 출금액을 입력받는다.
                        withdraw_money = int(input(withdraw_message))
                        # 로그인한 회원의 은행이 국민은행이라면,
                        # 출금 수수료가 50%이기 때문에, 잔액 검사시 1.5를 곱해준다.
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)
                        else:
                            print(error_message)
                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                phone = input(phone_message)
                user = Bank.check_phone(phone)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            account_number = input(account_number_message)
                            if Bank.check_account_number(account_number) is None:
                                break
                        # 새롭게 설정한 계좌번호로 등록한다.
                        # 계좌를 개설할 때 __dict__로 저장했다.
                        # 이 때 __dict__를 수정하는 것보다, 객체로 직접 접근해서 바꾸는 것이 안전하다.
                        # 결국, __dict__도 self를 받아서 만들어진 객체이므로, 뿌리인 self로 접근하는 것이 좋다.
                        user.get('object').account_number = account_number
                        continue

                print('핸드폰 번호 혹은 비밀번호를 다시 확인해주세요.')

            else:
                print(error_message)