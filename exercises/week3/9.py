import numpy as np

matris1 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])

matris2 = np.array([[16, 15, 14, 13],
                    [12, 11, 10, 9],
                    [8, 7, 6, 5],
                    [4, 3, 2, 1]])

resultat = np.multiply(matris1, matris2)

print(resultat)