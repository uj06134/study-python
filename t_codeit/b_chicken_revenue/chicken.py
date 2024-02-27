# 밑에 나와 있는 chicken.txt 파일을 보세요. 제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다.
# data 폴더의 chicken.txt 파일을 읽어 들이고, 12월 코빠닭의 하루 평균 매출을 출력하세요. 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.

total_price = 0
with open('chicken.txt', 'r', encoding='utf-8') as file_data:
    for line in file_data:
        strip_data = line.strip()  # 문자열 공백 제거
        split_data = strip_data.split("일: ")  # 문자열 나누기
        day = int(split_data[0])
        price = int(split_data[1])
        total_price += price

    average_daily_sales = total_price / day  # 하루 평균 매출
    # print(f'12월 하루 평균 매출: {average_daily_sales}원')
    rounded_average = round(average_daily_sales, 2)  # 반올림하여 소수점 둘째 자리까지 표시
    print(f'12월 하루 평균 매출: {rounded_average}원')

# 실행결과
# 12월 코빠닭의 하루 평균 매출: 501916.13원