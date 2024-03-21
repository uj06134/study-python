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

baby_names_df = pd.read_csv('data/popular_baby_names.csv')
# 테스트 코드
# print(baby_names_df)

# 문제 3
# 메가밀리언 측에서 2002년부터 현재(2/15/19)까지의 당첨 번호가 담긴 mega_millions.csv 파일을 공개했는데요. 이 데이터를 DataFrame에 넣어 봅시다.
# 날짜(Draw Date)가 이 DataFrame의 인덱스가 되도록 해 주세요!

import pandas as pd

lotto_df = pd.read_csv('data/mega_millions.csv', index_col=0)

# 테스트 코드
# print(lotto_df)
