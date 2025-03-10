# Generate Morgan Fingerprints from SMILES for Docking Data

📘 **Description:**
This repository contains a Python script that processes molecular data from a CSV file, generates Morgan fingerprints from SMILES notation using RDKit, and exports the enriched dataset to a new CSV file. This is particularly useful for cheminformatics workflows, such as virtual screening, similarity searches, or building predictive models for drug discovery.

🚀 **Features:**
- **Input:** CSV file with a column containing SMILES strings (`canonical_smiles`).
- **Output:** CSV file with an additional column for Morgan fingerprints as bit strings.
- **Customizable:** Adjust fingerprint radius and bit vector size as needed.

🔧 **Requirements:**
- Python 3.x
- Pandas
- RDKit

📂 **File Structure:**
```
├── ppar_docking.csv            # Input CSV file with SMILES
├── generate_fingerprint.py     # Python script for fingerprint generation
├── ppar_morgan.csv             # Output CSV file with fingerprints
```

⚙️ **Usage:**
1. Install the required packages:
```bash
pip install pandas rdkit
```

2. Run the script:
```bash
python generate_fingerprint.py
```

3. Check the output file (`ppar_morgan.csv`) for the generated fingerprints.

🔍 **Example:**
Input (`ppar_docking.csv`):
| id | canonical_smiles             |
|----|------------------------------|
| 1  | CC(C)CC(=O)Oc1ccccc1C(=O)O   |
| 2  | CCC(C(=O)O)Oc1ccccc1C(=O)O   |

Output (`ppar_morgan.csv`):
| id | canonical_smiles             | morgan_fingerprint               |
|----|------------------------------|----------------------------------|
| 1  | CC(C)CC(=O)Oc1ccccc1C(=O)O   | 1000100010000000000100010000...  |
| 2  | CCC(C(=O)O)Oc1ccccc1C(=O)O   | 0100001000010000000100100000...  |

💡 **Customization:**
Modify the fingerprint generation parameters in the script:
```python
fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
```
- `radius`: Neighborhood radius (default: `2`).
- `nBits`: Length of the bit vector (default: `2048`).

📘 **Applications:**
- Molecular similarity analysis
- Drug discovery and virtual screening
- Feature extraction for machine learning models

📩 **Contributing:**
Feel free to fork, submit issues, or suggest improvements through pull requests!

🔖 **License:**
This project is licensed under the MIT License.

---

Happy coding and happy drug discovery! 🚀🔬

---

Let me know if you’d like me to refine this further or add anything specific! ✌️

