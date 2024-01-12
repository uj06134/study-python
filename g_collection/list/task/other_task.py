# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:07:40 2024

@author: user
"""

name_list = []
price_list = []

menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '
search_name_message_for_update = '수정하실 상품명과 가격을 입력하세요(상품명, 가격)(나가려면 엔터!): '
result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    title = "------------과일 가게-------------\n"
    menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n------------과일 가게-------------\n"
    choice = int(input(f'{title}{menu}\n메뉴를 입력하세요 : '))
    # choice변수에 입력을 받으면, 제목과 메뉴를 보여준다.

    # if choice == 1 :
    # new_name, new_price = input(append_message).split()
    # if new_name not in name_list :
    #   name_list.append(new_name)
    #   price_list.append(new_price)
    # else :
    #   result_message = append_error_message

    if choice == 1:
        # 1번 추가 메뉴로 들어왔다면
        while True:
            # 계속 상품 및 가격들을 입력할 수 있도록 반복한다. (but 엔터키를 누르면 이전 화면으로 break 함수로 탈출
            append_message = '추가하실 상품명과 가격을 입력하세요(상품명, 가격)(나가려면 엔터!): '
            input_values1 = input(append_message)
            # 추가할 상품 메세지 저장
            # 추가할 가격 메세지 저장

            if not input_values1.strip():  # 엔터키를 치게 되면(공백이 없으므로)
                break  # 이전 메뉴화면으로 돌아간다. / break 사용(1번 메뉴 종료 > 메뉴선택)

            input_values1 = input_values1.split(",")  # 입력시 상품명과 가격사이에 ,를 넣어줘야한다.

            if len(input_values1) != 2:  # 잘못된 방법으로 입력시에
                print("올바른 형식으로 입력하세요.")  # 오류 메시지 출력

                continue  # 다시 입력 즉 1번메뉴에서 다시 입력하게 한다.

            append_name, append_price = map(str, input_values1)  # 상품명 입력변수와 가격 입력 변수를 map 함수로 감싸서 input_values1에 담는다.

            if append_name in name_list:  # 추가하려는 상품명이 name_list에 있다면
                # 만약 상품명이 중복되었다면
                append_error_message = "추가 실패(중복된 상품명)"
                # 오류메시지 출력
                print(append_error_message)  # 오류 메시지 출력
            else:
                # 상품명,가격 이 중복이 아니라면 각 리스트에 저장
                name_list.append(append_name)
                price_list.append(append_price)



    elif choice == 2:
        # 2번 메뉴로 들어왔다면

        while True:
            # 수정 메뉴 화면을 계속 이용할 수 있도록 반복한다. (but 엔터키를 누르면 이전 화면으로 break 함수로 탈출

            input_values = input(search_name_message_for_update)  # 2번 메뉴 title을 보여주고 값을 입력 받는다.

            if not input_values.strip():  # 엔터키를 치게 되면(공백이 없다면)
                break  # 이전 메뉴화면으로 돌아간다. / break 사용(2번 메뉴 종료 > 메뉴선택)

            input_values = input_values.split(",")  # 입력 시에는 상품명과 가격사이에 ','을 넣어줘야 한다.

            if len(input_values) != 2:  # 위와 같이 입력을 안했을 시에는 오류 메시지 출력됨
                print("올바른 형식으로 입력하세요.")

                continue  # 다시 2번메뉴 초기화면으로 전환

            search_name_message, search_price_message = map(str, input_values)  # 상품 수정 변수와 가격 수정 변수는 map 함수로
            # 감싸져서 입력변수인 input_values를 담는다.

            if search_name_message not in name_list:  # 수정할 상품이 name_list에 있다면
                print(search_name_error_message)  # 오류 메세지 출력

            else:

                index = name_list.index(search_name_message)  # 수정된 상품과 가격을 각각의 리스트에 담는다.
                name_list[index] = search_name_message  # ''

                price_list[index] = search_price_message  # ''


    elif choice == 3:  # 3번 메뉴로 이동
        while True:  # 삭제 화면을 계속 이용할 수 있도록 반복시킨다. enter 누르면 종료되고 메인 메뉴로 이동
            delete_message = '삭제하실 상품명을 입력하세요(나가려면 엔터!): '
            delete_name = input(delete_message)

            if delete_name == "":  # 엔터키를 누르면 3번 메뉴 종료 >> 메인 메뉴 ( if not input_values.strip():와 동일)
                break

            if delete_name not in name_list:
                delete_error_message = "삭제 실패(존재하지 않는 상품명)"
                print(delete_error_message)

            else:
                # 인덱스를 찾고 인덱스에 있는 아이템을 remove,del,pop() 등으로 삭제 시킨다.
                index = name_list.index(delete_name)  # 인덱스에 아이템이 삭제된 name_list가 담긴다.
                name_list.pop(index)  # ''
                price_list.pop(index)  # ''

    elif choice == 4:  # 4번 메뉴로 이동
        search_menu = "1.상품명으로 검색\n2.가격으로 검색(나가려면 엔터!)\n"
        sh_menu = int(input(search_menu))  # 사용자에게 4번 타이틀을 보여주고 입력 받게 함

        if sh_menu == 1:  # 1번 메뉴 클릭 시
            search_name = input("검색할 상품명을 입력하세요: ")

            if search_name in name_list:  # 검색한 값이 name_list에 있으면 출력
                print(f"가격: {price_list[name_list.index(search_name)]}원")

            else:
                print("검색 결과가 없습니다.")  # 검색한 값이 없으면 break
                continue

        elif sh_menu == 2:  # 2번 메뉴 클릭 시
            search_price = float(input("검색할 가격을 입력하세요: "))  # 가격 입력 받음
            for i in range(len(price_list)):  # price_list 길이만큼 i가 반복
                if 0.5 * float(price_list[i]) <= search_price <= 1.5 * float(price_list[i]):  # i를 price_list에 담아 주면서
                    # 오차범위 +- 50 사이의 값을 조건문으로 처리

                    print(f"상품명: {name_list[i]}, 가격: {price_list[i]}원")

                else:
                    print("검색 결과가 없습니다.")  # 검색 결과가 없을 때 break
                    break

    elif choice == 5:  # 5번 메뉴 클릭 시
        print("상품 목록:")
        for i in range(len(name_list)):  # name_list 길이 만큼 반복하여 지금까지 저장된 리스트 값들을 출력
            print(f"상품명: {name_list[i]}, 가격: {price_list[i]}원")

    elif choice == 6:  # 프로그램 종료
        print("프로그램을 종료합니다.")
        break
    else:
        pass