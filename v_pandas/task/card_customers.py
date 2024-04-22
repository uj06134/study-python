# 데이터의 중요성을 깨달은 “삼송카드”와 “현디카드”가 협업을 하기로 결정했습니다.
# 두 회사의 데이터를 활용해서, 사람들의 요일별 문화생활비를 분석해보려 합니다.

import pandas as pd

samsong_df = pd.read_csv('../data/samsong.csv')
hyundee_df = pd.read_csv('../data/hyundee.csv')

# 여기에 코드를 작성하세요
result_samsong_df = samsong_df.loc[:, ['요일', '문화생활비']]
result_hyundee_df = hyundee_df.loc[:, ['문화생활비']]

# 수평 방향(axis=1)으로 데이터프레임을 연결
result_df = pd.concat([result_samsong_df, result_hyundee_df], axis=1)
result_df.columns = ['day', 'samsong', 'hyundee']
print(result_df)

# 해설
# DataFrame을 만드는 여러 방법 중에 딕셔너리 활용
combined_df = pd.DataFrame({
    'day': samsong_df['요일'],
    'samsong': samsong_df['문화생활비'],
    'hyundee': hyundee_df['문화생활비']
})
print(combined_df)