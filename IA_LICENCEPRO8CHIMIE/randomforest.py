import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Étape 1 : Génération des données moléculaires
def generate_molecular_data(smiles_list):
    data = []
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            mw = Descriptors.MolWt(mol)  # Poids moléculaire
            logp = Descriptors.MolLogP(mol)  # LogP (hydrophobie)
            data.append([smiles, mw, logp])
    return pd.DataFrame(data, columns=["SMILES", "MolecularWeight", "LogP"])

# Exemple de SMILES
smiles_list = [
    "CCO",       # Éthanol
    "CCOCC",     # Éther diéthylique
    "CCCC",      # Butane
    "CC(=O)O",   # Acide acétique
    "CCCCCCCC",  # Octane
]

# Générer des données moléculaires
df = generate_molecular_data(smiles_list)

# Ajouter une étiquette (1 = soluble, 0 = insoluble, hypothétique ici)
df['Solubility'] = [1, 1, 0, 1, 0]

# Étape 2 : Analyse exploratoire
print("Données moléculaires :")
print(df)

# Visualisation
plt.scatter(df['MolecularWeight'], df['LogP'], c=df['Solubility'], cmap='coolwarm')
plt.xlabel("Poids moléculaire")
plt.ylabel("LogP")
plt.title("Relation entre poids moléculaire et solubilité")
plt.colorbar(label="Solubilité (1=soluble, 0=insoluble)")
plt.show()

# Étape 3 : Préparation des données
X = df[["MolecularWeight", "LogP"]]
y = df["Solubility"]

# Diviser en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Étape 4 : Modèle d'apprentissage
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prédictions
y_pred = model.predict(X_test)

# Étape 5 : Évaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitude : {accuracy:.2f}")
print("\nRapport de classification :")
print(classification_report(y_test, y_pred))

# Étape 6 : Prédiction pour de nouvelles molécules
new_smiles = ["C(CCl)Cl", "C1=CC=CC=C1O"]  # Exemple : Dichlorométhane et Phénol
new_data = generate_molecular_data(new_smiles)
predictions = model.predict(new_data[["MolecularWeight", "LogP"]])

print("\nPrédictions pour de nouvelles molécules :")
for smiles, pred in zip(new_smiles, predictions):
    print(f"Molécule {smiles} - Soluble : {'Oui' if pred == 1 else 'Non'}")