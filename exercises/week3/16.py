import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv')

department_counts = df['Department'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%', startangle=140)

plt.title('Andel anställda i varje Avdelning')
plt.axis('equal')
plt.show()

print(department_counts)