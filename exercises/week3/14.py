import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv')

numeric_columns = df.select_dtypes(include=['float64', 'int64'])
sns.pairplot(numeric_columns)

plt.show()