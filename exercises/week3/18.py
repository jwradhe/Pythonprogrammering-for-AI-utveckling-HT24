import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Steg 1: Ladda data
# Skapa en exempeldataframe
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6],
    'D': [5, 3, 6, 7, 8]
}
df = pd.DataFrame(data)

# Steg 2: Beräkna korrelationsmatrisen
correlation_matrix = df.corr()

# Steg 3: Skapa heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Korrelationsmatris')
plt.show()