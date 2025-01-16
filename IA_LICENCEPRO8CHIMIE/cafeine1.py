from rdkit import Chem
from rdkit.Chem import Draw

# Définir la structure SMILES de la caféine
caffeine_smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"

# Convertir la chaîne SMILES en molécule
caffeine_mol = Chem.MolFromSmiles(caffeine_smiles)

# Dessiner la molécule
img = Draw.MolToImage(caffeine_mol)

# Afficher l'image
img.show()