import pandas as pd

df = pd.read_csv('sample_data0.csv')

privot_df = df.pivot_table(
    values='Salary',
    index='City',
    columns='Department',
    aggfunc='mean'
).astype(int)

print(privot_df)