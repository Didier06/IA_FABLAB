import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coordonnées des atomes (en Angströms)
oxygene = [0, 0, 0]
hydrogene1 = [0.96, 0, 0]
hydrogene2 = [-0.24, 0.93, 0]

# Création de la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dessiner les atomes
ax.scatter(*oxygene, color='red', s=100, label='Oxygène')
ax.scatter(*hydrogene1, color='blue', s=50, label='Hydrogène')
ax.scatter(*hydrogene2, color='blue', s=50)

# Dessiner les liaisons
ax.plot([oxygene[0], hydrogene1[0]], [oxygene[1], hydrogene1[1]], [oxygene[2], hydrogene1[2]], color='black')
ax.plot([oxygene[0], hydrogene2[0]], [oxygene[1], hydrogene2[1]], [oxygene[2], hydrogene2[2]], color='black')

# Configuration de la vue
ax.set_xlabel('X (Å)')
ax.set_ylabel('Y (Å)')
ax.set_zlabel('Z (Å)')
ax.set_title('Molécule d\'eau (H₂O) en 3D')

# Afficher la légende
ax.legend()

# Afficher le graphique
plt.show()
