import pandas as pd

df = pd.read_csv('sample_data0.csv')

salaryDepartment = df.groupby('Department')['Salary'].mean().round(0).astype(int)

print(salaryDepartment)