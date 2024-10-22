# Använd funktionen pd.melt() för att omforma DataFrame:n, och gör 'Salary' och 'Performance_Score' kolumnerna till variabler.

import pandas as pd

df = pd.read_csv('sample_data0.csv')

df_melted = pd.melt(df, id_vars=['Name', 'Age'], value_vars=['Salary', 'Performance_Score'], 
                    var_name='variable', value_name='value')

print(df_melted)