# 방송사 시청률 받아오기
import pandas as pd
df = pd.read_csv('../data/broadcast.csv', index_col=0)

# loc와 iloc의 차이
# loc: 데이터 프레임의 행 또는 컬럼의 label이나 boolean array로 인덱싱하는 방법
# iloc: 데이터 프레임의 행이나 컬럼의 인덱스 값으로 접근

# 문제 1
# 2016년도에 KBS방송국의 시청률
print(df.loc[2016, 'KBS'])
print(df.iloc[5, 0])

# 문제 2
# JTBC의 시청률(한 줄)
print(df['JTBC'])
print(df.loc[:, 'JTBC'])

# 문제 3
# SBS와 JTBC의 시청률(여러 줄)
print(df[['SBS', 'JTBC']])
print(df.loc[:, ['SBS', 'JTBC']])

# 문제 4
# KBS에서 SBS까지, 연도는 2012년부터 2017년까지의 시청률
print(df.loc[2012:2017,'KBS':'SBS'])

# 문제 5
# KBS에서 시청률이 30이 넘은 데이터
boolean_KBS = df['KBS'] > 30
print(df.loc[boolean_KBS, 'KBS'])

# 문제 6
# SBS가 TV CHOSUN보다 더 시청률이 낮았던 시기의 데이터
boolean_result = df['SBS'] < df['TV CHOSUN']
print(df.loc[boolean_result, ['SBS','TV CHOSUN']])
