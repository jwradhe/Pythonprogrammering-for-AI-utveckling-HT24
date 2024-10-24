import numpy as np

# Definiera matris A och vektor b
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

# Lös systemet Ax = b
x = np.linalg.solve(A, b)

print("Lösningen x är:")
print(x)