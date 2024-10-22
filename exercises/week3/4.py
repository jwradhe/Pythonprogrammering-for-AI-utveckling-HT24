import pandas as pd

df = pd.read_csv('sample_data0.csv')

names = df.groupby('City')['Performance_Score'].idxmax()
maxScoreCity = df.loc[names, ['City', 'Name', 'Performance_Score']]

print(maxScoreCity)