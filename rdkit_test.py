from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
import time


smiles =input("Enter sMILES string for the molecule:") #take input from the user
mol=Chem.MolFromSmiles(smiles)                         #converted to molecule

mol=Chem.AddHs(mol)             #added hydrogen

#3D generation
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)


#convert to molblock fir py3Dmol
mol_block=Chem.MolToMolBlock(mol)


#view the molecule
viewer=py3Dmol.view(width=400,height=400)
viewer.addModel(mol_block,"mol")
viewer.setStyle({'stick' : {}})
viewer.zoomTo()
viewer.show()



