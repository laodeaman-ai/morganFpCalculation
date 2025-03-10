import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

# Load the dataset
df = pd.read_csv('ppar_docking.csv')

# Function to generate Morgan Fingerprint from SMILES
def generate_morgan_fingerprint(smiles, radius=2, n_bits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        # Generate Morgan fingerprint with given radius and number of bits
        fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
        return fingerprint.ToBitString()  # Return fingerprint as bit string
    else:
        return None

# Apply the function to each molecule in the dataset
df['morgan_fingerprint'] = df['canonical_smiles'].apply(generate_morgan_fingerprint)

# Save the dataset with the new 'morgan_fingerprint' column
df.to_csv('ppar_morgan.csv', index=False)

# Display first few rows of the dataframe
print(df.head())
