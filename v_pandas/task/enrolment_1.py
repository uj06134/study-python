# 수강신청에는 다음 3개의 조건이 있습니다.
# 1) “information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
# 2) “commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
# 3) 수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.
# 기존 DataFrame에 “status”라는 이름의 column을 추가하고, 학생이 수강 가능한 상태이면 “allowed”, 수강 불가능한 상태이면 “not allowed”를 넣어주세요.
import pandas as pd
df = pd.read_csv('../data/enrolment_1.csv')

# 모든 과목 allowed로 설정
df['status'] = 'allowed'

# 1)
df.loc[(df['course name'] == 'information technology') & (df['year'] == 1), 'status'] = 'not allowed'

# 2)
df.loc[(df['course name'] == 'commerce') & (df['year'] == 4), 'status'] = 'not allowed'

# 3)
# 수강생 수
course_counts = df['course name'].value_counts()

# 람다 식
# df.loc[df['col명'].apply(lambda x : 조건), '추가 또는 수정 할 col명'] = '추가할 값'
df.loc[df['course name'].apply(lambda x: course_counts[x] < 5), 'status'] = 'not allowed'

# # 3) 해설 답안
# index(): 리스트에서 특정 요소의 인덱스를 찾는 함수
# closed_courses = list(course_counts[course_counts < 5].index)
# for course in closed_courses:
#     df.loc[df["course name"] == course, "status"] = "not allowed"

# 테스트 코드
print(df)
