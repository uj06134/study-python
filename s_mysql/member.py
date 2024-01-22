from member_module import *
import hashlib

if __name__ == '__main__':
    # 아직 모르는 값 자리에 %s를 작성한다.
    insert_query = "insert into tbl_member(email, password, name) \
                    values (%s, %s, %s)"

    # 암호화
    password = '7890'
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))
    insert_params = ['lss1234@naver.com', encryption.hexdigest(), '이순신']
    # save(insert_query, insert_params)

    # 회원 정보 전체 조회
    find_all_query = "select email, password, name from tbl_member"
    # members = find_all(find_all_query)
    # print(members)

    # 이메일로 회원 1명 조회
    find_by_id_query = "select email, password, name from tbl_member where email = %s"
    params = ['lss1234@naver.com']
    # member = find_by_id(find_by_id_query, params)
    # print(member)

    # 회원 정보 수정, email에 gmail이 포함되어 있으면, 이름 뒤에 님을 붙인다.
    update_query = "update tbl_member " \
                   "set name = concat(name, '님') " \
                   "where email like concat('%%', %s, '%%')"
    update_params = ['gmail']
    # update(update_query, update_params)

    # gmail 이메일을 가진 회원 삭제
    delete_query = "delete from tbl_member where email like concat('%%', %s, '%%')"
    delete_params = ['gmail']

    # delete(delete_query, delete_params)
