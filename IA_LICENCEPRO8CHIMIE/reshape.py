import numpy as np

# Création d'un tableau numpy à une dimension
x = np.array([1, 2, 3, 4, 5, 6])

print("Tableau d'origine :")
print(x)

# Réorganisation du tableau en un tableau à deux dimensions
x_reshape = x.reshape(-1, 1)

print("\nTableau réorganisé :")
print(x_reshape)
print(x_reshape[0][1])