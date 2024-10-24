import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv')

department_counts = df['Department'].value_counts()

satisfaction_mapping = {'High': 3, 'Medium': 2, 'Low': 1}
df['Satisfaction_Numeric'] = df['Satisfaction_Level'].map(satisfaction_mapping)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))


# Linje-diagram
axs[0, 0].plot(df['Years_Experience'], df['Salary'], marker='o')
axs[0, 0].set_title('Lön över År av Erfarenhet')
axs[0, 0].set_xlabel('År av Erfarenhet')
axs[0, 0].set_ylabel('Lön')

# Spridningsdiagram
axs[0, 1].scatter(df['Training_Hours'], df['Performance_Score'], color='orange')
axs[0, 1].set_title('Prestanda Poäng vs Tränings timmar')
axs[0, 1].set_xlabel('Tränings timmar')
axs[0, 1].set_ylabel('Prestanda Poäng')

# Stapeldiagram
axs[1, 0].bar(department_counts.index, department_counts.values, color='green')
axs[1, 0].set_title('Antal anställda i varje Avdelning')
axs[1, 0].set_xlabel('Avdelning')
axs[1, 0].set_ylabel('Antal anställda')
axs[1, 0].tick_params(axis='x', rotation=45)  # Rotera x-axeln för bättre läsbarhet

# Histogram
axs[1, 1].hist(df['Satisfaction_Numeric'].dropna(), bins=3, color='blue', alpha=0.7, edgecolor='black')
axs[1, 1].set_title('Fördelning av Tillfredsställelse')
axs[1, 1].set_xlabel('Tillfredsställelse (1-Low, 2-Medium, 3-High)')
axs[1, 1].set_ylabel('Antal anställda')

plt.tight_layout()
plt.show()