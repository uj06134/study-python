# 사용자가 입력한 정수가 몇 자리수인지 출력
# 몫을 이용
count = 0
number = int(input())
while number != 0:
    number //= 10
    count +=1
print(count)

