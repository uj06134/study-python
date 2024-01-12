# try:
#     number = int(input('정수를 입력하세요.'))
#
# except ValueError as e:
#     print('정수만 입력해주세요~!')
#
# print('반드시 실행되어야 하는 문장')

# try:
#     print(10 / 0)
# # except ZeroDivisionError as e:
# # except ZeroDivisionError:
# # except Exception:
# except:
#     # print(e)
#     print('0으로 나눌 수 없습니다.')

# datas = [1, 2, 3]
#
# try:
#     print(datas[3])
#     # 위의 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요!')
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스를 확인해주세요!')
#
# else:
#     # try에 작성한 문장에서 오류가 발생하지 않는다면 실행된다.
#     print('오류가 없어요!')
#
# finally:
#     print('반드시 실행되어야 하는 문장')

# nickname = input("Enter your nickname: ")
# if nickname == '멍청이':
#     raise RuntimeError

class BadWordError(Exception):
    def __str__(self):
        return "비속어는 사용할 수 없음"

def check_bad_word(message):
    if '멍청이' in message:
        raise BadWordError()

chat = input('채팅 입력: ')
try:
    check_bad_word(chat)
except BadWordError as e:
    print(e)    