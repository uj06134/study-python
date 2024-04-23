# 1)
# 같은 크기의 강의실이 필요한 과목에 대해 알파벳 순서대로 방 번호를 배정하세요.
# 예를 들어 "Auditorium"이 필요한 과목으로 “arts”, “commerce”, “science” 세 과목이 있다면,
# “arts”는 “Auditorium-1”, “commerce”는 “Auditorium-2”, “science”는 “Auditorium-3” 순서로 방 배정이 되어야 합니다.
# 2)
# status column이 “not allowed”인 수강생은 room assignment column을 그대로 “not assigned”로 남겨둡니다.
# "not allowed"인 수강생의 room assignment 상태가 변경되지 않도록 유의해주세요.
# 3)
# room assignment column의 이름을 room number로 바꿔주세요.

import pandas as pd
df = pd.read_csv('../data/enrolment_3.csv')

# 1)
# Auditorium 강의실 번호 붙이기
selected_courses_auditorium = df[(df['room assignment'] != 'not assigned') & (df['room assignment'] == 'Auditorium')]['course name'].sort_values().unique()
count = 1
for course in selected_courses_auditorium:
    df.loc[df["course name"] == course, "room assignment"] = f"Auditorium-{count}"
    count += 1

# Large room 강의실 번호 붙이기
selected_courses_large = df[(df['room assignment'] != 'not assigned') & (df['room assignment'] == 'Large room')]['course name'].sort_values().unique()
count = 1
for course in selected_courses_large:
    df.loc[df["course name"] == course, "room assignment"] = f"Large-{count}"
    count += 1

# Medium room 강의실 번호 붙이기
selected_courses_medium = df[(df['room assignment'] != 'not assigned') & (df['room assignment'] == 'Medium room')]['course name'].sort_values().unique()
count = 1
for course in selected_courses_medium:
    df.loc[df["course name"] == course, "room assignment"] = f"Medium-{count}"
    count += 1

# Small room 강의실 번호 붙이기
selected_courses_small = df[(df['room assignment'] != 'not assigned') & (df['room assignment'] == 'Small room')]['course name'].sort_values().unique()
count = 1
for course in selected_courses_small:
    df.loc[df["course name"] == course, "room assignment"] = f"Small-{count}"
    count += 1

# 2)
df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'

# 3)
df.rename(columns={'room assignment' : 'room number'}, inplace=True)

# 테스트 코드
print(df)