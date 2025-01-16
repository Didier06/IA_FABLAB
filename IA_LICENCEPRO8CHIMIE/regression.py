import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Définition des points expérimentaux
x_exp = np.array([1, 2, 3, 4, 5])
y_exp = np.array([2, 3, 5, 7, 11])

# Création d'un modèle de régression linéaire
modele = LinearRegression()

# Réorganisation des données pour la régression
x_exp_reshape = x_exp.reshape(-1, 1)

# Entraînement du modèle
modele.fit(x_exp_reshape, y_exp)

# Prédiction des valeurs pour la droite de régression
x_pred = np.linspace(0, 6, 100).reshape(-1, 1)
y_pred = modele.predict(x_pred)

# Affichage des points expérimentaux et de la droite de régression
plt.scatter(x_exp, y_exp, label='Points expérimentaux')
plt.plot(x_pred, y_pred, label='Droite de régression', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Régression linéaire')
plt.legend()
plt.show()

# Affichage des coefficients de la droite de régression
print('Coefficient de pente (a) :', modele.coef_[0])
print('Coefficient d\'ordonnée à l\'origine (b) :', modele.intercept_)