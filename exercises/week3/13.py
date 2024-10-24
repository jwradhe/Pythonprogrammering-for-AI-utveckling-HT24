import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv')

bins = [0, 5, 15, float('inf')]  
labels = ['Junior', 'Mid', 'Senior']  
df['Experience_Category'] = pd.cut(df['Years_Experience'], bins=bins, labels=labels, right=False)

pivot_table = df.pivot_table(index='City', columns='Experience_Category', aggfunc='size', fill_value=0)
pivot_table.plot(kind='bar', stacked=True)

plt.title('Antal anställda i varje Experience_Category per Stad')
plt.xlabel('Stad')
plt.ylabel('Antal anställda')

plt.show()