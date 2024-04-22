import pandas as pd
df = pd.read_csv('../data/world_cities.csv')

# 주어진 데이터에는 총 몇 개의 도시와 몇 개의 나라가 있는지 알아맞혀 보세요.
print(df['City / Urban area'].describe())
print(df['Country'].value_counts().shape)

# 주어진 데이터에서, 인구 밀도(명/sqKm) 가 10000 이 넘는 도시는 총 몇 개인지 알아보세요.
df['Density'] = df['Population']/df['Land area (in sqKm)']
count = (df['Density'] > 10000).sum()
print(count)

# 인구 밀도가 가장 높은 도시를 알아봅시다.
print(df.sort_values('Density', ascending=False))

# 나라 이름이 기억나지 않고, 이 데이터에서 그 나라에 속한 도시가 딱 4개 들어 있었다는 것만 기억이 난다고 하네요. 이 나라는 무엇일까요?
country_counts = df['Country'].value_counts()
print(country_counts[country_counts == 4].index.tolist())