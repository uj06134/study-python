# 토익 시험은 LC(듣기) 파트와 RC(독해) 파트로 이루어져 있습니다. 각 파트가 495점 만점, 총 990점이 만점입니다.
# 각 파트가 최소 250점, 총 점수가 최소 600점이 되어야 서류 전형을 합격할 수 있습니다.
# 기존 DataFrame에 “합격 여부”라는 column을 추가하고, 합격한 지원자는 불린 값 True, 불합격한 지원자는 불린 값 False를 넣어주면 됩니다.
import pandas as pd
toeic_df = pd.read_csv('../data/toeic.csv')

# 여기에 코드를 작성하세요
total_df = toeic_df['LC'] + toeic_df['RC'] > 600
min_df = toeic_df['LC'] & toeic_df['RC'] >= 250
toeic_df['합격 여부'] = total_df & min_df

# 테스트 코드
print(toeic_df)