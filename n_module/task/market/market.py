from message_module import *
from market_module import *

if __name__ == '__main__':
    while True:
        # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
        choice = int(input(title + '\n' + menu))

        # 추가
        if choice == 1:
            new_name, new_price = input(append_message).split()

            if len(select_by_name(new_name)) == 0:
                insert(name=new_name, price=new_price)
                continue
            else:
                result_message = append_error_message

        # 수정
        elif choice == 2:
            name = input(search_name_message_for_update)
            if len(select_by_name(name)) != 0:
                new_name, new_price = input(update_message).split()
                if len(select_by_name(new_name)) == 0:
                    update(name, new_name, new_price)
                    continue
                else:
                    data_dict[new_name] = int(new_price)
            else:
                result_message = update_error_message1

        # 삭제
        elif choice == 3:
            name = input(delete_message)
            if len(select_by_name(name)) != 0:
                delete(name)
                continue

            else:
                result_message = delete_error_message

        # 검색
        elif choice == 4:
            choice = int(input(search_menu))

            # 상품명으로 검색
            if choice == 1:
                keyword = input(search_name_message)
                result = select_by_name(keyword)
                if len(result) != 0:
                    print(f"{result.get('name')}, {result.get('price')}")
                    continue

                else:
                    result_message = search_name_error_message

            # 가격으로 검색
            elif choice == 2:
                price_input = int(input(search_price_message))

                result = select_by_price(price_input)

                if len(result) != 0:
                    for product in result:
                        print(f"{product.get('name')}, {product.get('price')}")
                    continue

                else:
                    result_message = search_error_message

        # 목록
        elif choice == 5:
            if len(select_all()) == 0:
                result_message = no_item_message
            else:
                for name, price in data_dict.items():
                    print(f'{name}, {price}')
                    continue

        # 나가기
        elif choice == 6:
            break

        # 그 외
        else:
            result_message = error_message

        print(result_message)
        result_message = ""