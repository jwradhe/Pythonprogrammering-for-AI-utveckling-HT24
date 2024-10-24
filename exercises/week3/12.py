import numpy as np

identitetsmatris = np.eye(5)
anpassad_array = np.array([10, 20, 30, 40, 50])
np.fill_diagonal(identitetsmatris, anpassad_array)

print(identitetsmatris)