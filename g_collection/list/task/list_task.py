# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

title = "과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

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
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품명과 중복되지 않는다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 수정할 상품명 입력
        name = input(search_name_message_for_update)
        # 상품목록에 수정할 상품명이 있으면
        if name in name_list:
            # 상품명과 가격을 동시에 입력받아 저장
            new_name, new_price = input(update_message).split()
            # 상품명이 중복되지 않는다면 수정할 상품명의 인덱스 번호 저장
            if new_name not in name_list:
                index = name_list.index(name)
                # 인데스 번호를 통해 상품명과 가격 추가
                name_list[index], price_list[index] = new_name, new_price
                continue

            # 상품명이 중복된 경우
            else:
                result_message = update_error_message2
        # 상품목록에 수정할 상품명이 존재하지 않을 경우
        else:
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 상품명 입력
        name = input(delete_message)
        # 상품목록에 삭제할 상품명이 있으면 삭제할 상품명의 인덱스 번호 저장
        if name in name_list:
            index = name_list.index(name)
            # 해당 인덱스 번호의 상품명과 가격 삭제
            del name_list[index]
            del price_list[index]
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        # 상품목록에 삭제할 상품명이 없다면 에러메세지 출력
        else:
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 상품명 or 가격 검색 (1 or 2)
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            name = input(search_name_message)
            # 상품목록에 상품명이 있으면 인덱스 번호 저장 후 해당 번호의 상품명, 가격 출력
            if name in name_list:
                index = name_list.index(name)
                print(f'{name_list[index]}, {price_list[index]}')
                continue

            # 상품목록에 상품명이 없는경우 -> 검색결과 x
            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            price = int(input(search_price_message))
            # 오차 범위는 ±50%로 설정
            min = price * 0.5
            max = price * 1.5
            # 오차범위 ±50%인 가격목록에서 가격을 하나씩 뽑아 result_index에 인데스번호 저장
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]
            # result_index의 길이가 0이 아니면 즉 가격의 인덱스가 하나라도 있다면
            if len(result_index) != 0:
                # 반복묵을 돌려 해당 인덱스에 해당되는 상품명과 가격을 모두 출력
                for i in result_index:
                    print(f'{name_list[i]}, {price_list[i]}')
                    continue
            # result_index의 길이가 0, 즉 해당되는 인덱스가 하나도 없다. -> 검색결과 x
            else:
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 상품목록의 길이가 0인경우 -> 상품목록이 없는경우
        if len(name_list) == 0:
            result_message = no_item_message
        # 상품목록이 있는 경우
        else:
            # 반복문으로 상품목록의 개수만큼 반복, 상품목록(상품명, 가격) 출력
            for i in range(len(name_list)):
                print(f'{name_list[i]}, {price_list[i]}')
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        result_message = error_message
    # 일괄처리로 해당하는 에러메세지 출력
    print(result_message)
    result_message = ""