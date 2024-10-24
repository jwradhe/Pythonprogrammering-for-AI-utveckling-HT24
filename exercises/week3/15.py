import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv')

plt.figure(figsize=(10, 6)) 
sns.violinplot(x='Department', y='Performance_Score', data=df, inner='quartile')

plt.title('Fördelning av Performance Scores över olika Avdelningar')
plt.xlabel('Avdelning')
plt.ylabel('Performance Score')

plt.show()