# 코드를 4줄만 써서, 아래 데이터프레임으로 바꿔보세요.
import pandas as pd
puzzle_df = pd.read_csv('../data/puzzle.csv')

# 여기에 코드를 작성하세요
puzzle_df['A'] = puzzle_df['A'] * 2
puzzle_df.loc[:, 'B':'E'] = puzzle_df.loc[:, 'B':'E'] >= 80
# 불린값을 0과 1로 변환
puzzle_df = puzzle_df.astype(int)
puzzle_df.loc[2, 'F'] = 99

# 테스트 코드
print(puzzle_df)