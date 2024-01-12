from bank_module import *
from message_module import *


if __name__ == '__main__':
    while True:
        # 은행 메뉴
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        if bank_choice < 1 or bank_choice > len(Bank.banks):
            continue

        while True:
            # 나가기
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
            # 개설한 은행에서만 입금 가능
            elif menu_choice == 2:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if isinstance(user.get('object'), ShinHan):
                    # 신한은행 회원이 아니라면,
                    if bank_choice != 1:
                        print('개설한 은행에서만 입금 서비스를 사용 할 수 있습니다')
                        continue
                # 계좌 번호가 있으면
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
                # 계좌번호가 있으면
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