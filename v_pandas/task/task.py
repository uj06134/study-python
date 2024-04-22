# 문제1
# DataFrame을 만들고 출력해 보세요.
# column은 name, birthday, occupation 총 3개입니다.

import pandas as pd
star_list = [['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'],
             ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'],
             ['Harry Potter', 'July 31, 1980', 'Wizard'],
             ['Ji-Sung Park', 'February 25, 1981', 'Footballer']]

star_df = pd.DataFrame(star_list, columns=['name', 'birthday', 'occupation'])
# 테스트 코드
# print(star_df)

# 문제2
# 조사 결과가 data 폴더의 popular_baby_names.csv라는 파일에 담겨 있는데요.
# 안에 있는 정보를 DataFrame으로 읽어 들이고, DataFrame을 출력해 주세요.

import pandas as pd
baby_names_df = pd.read_csv('../data/popular_baby_names.csv')
# 테스트 코드
# print(baby_names_df)

# 문제 3
# 메가밀리언 측에서 2002년부터 현재(2/15/19)까지의 당첨 번호가 담긴 mega_millions.csv 파일을 공개했는데요. 이 데이터를 DataFrame에 넣어 봅시다.
# 날짜(Draw Date)가 이 DataFrame의 인덱스가 되도록 해 주세요!

import pandas as pd
lotto_df = pd.read_csv('../data/mega_millions.csv', index_col=0)
# 테스트 코드
# print(lotto_df)

# 문제 4
# 1) ID 1의 무게를 200으로 변경하세요.
# 2) ID 21의 row를 삭제하세요.
# 3) ID 20의 row를 추가하세요. ID 20의 키는 70, 무게는 200입니다.

import pandas as pd
body_df = pd.read_csv('../data/body_imperial1.csv', index_col=0)
# 1)
body_df.loc[1, 'Weight (Pound)'] = 200
# 2)
body_df.drop(21, axis = 'index', inplace = True)
# 3)
body_df.loc[20] = [70, 200]
# 테스트 코드
# print(body_df)

# 문제 5
# 1) '비만도' column을 추가하고, 모든 ID에 대해 '정상'으로 설정해주세요.
# 2) 'Gender' column의 값을 ID 0~10까지는 'Male' 11~20까지는 'Female'로 변경하세요.

import pandas as pd
body_df2 = pd.read_csv('../data/body_imperial2.csv', index_col=0)
# 1)
body_df2['비만도'] = '정상'
# 2)
body_df2.loc[0:10, 'Gender'] = 'Male'
body_df2.loc[11:20, 'Gender'] = 'Female'

# 테스트 코드
print(body_df2)
