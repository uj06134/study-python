# 강의실은 규모에 따라 “Auditorium”, “Large room”, “Medium room”, “Small room” 총 4가지 종류가 있습니다.
# 1) 80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
# 2) 40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
# 3) 15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
# 4) 5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
# 5) 폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다.
import pandas as pd
df = pd.read_csv('../data/enrolment_2.csv')

# 수강생 수
course_counts = df['course name'].value_counts()
# 1) 람다
df.loc[df['course name'].apply(lambda x: course_counts[x] >= 80), 'room assignment'] = 'Auditorium'

# 2) 람다
df.loc[df['course name'].apply(lambda x: 80 > course_counts[x] >= 40), 'room assignment'] = 'Large room'

# 3) 리스트
medium_room_list = list(course_counts[(course_counts >= 15) & (course_counts < 40)].index)
for course in medium_room_list:
    df.loc[df["course name"] == course, "room assignment"] = "Medium room"

# 4) 리스트
small_room_list = list(course_counts[(course_counts >= 5) & (course_counts < 15)].index)
for course in small_room_list:
    df.loc[df["course name"] == course, "room assignment"] = "Small room"

# 5)
df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'

# 테스트 코드
print(df)