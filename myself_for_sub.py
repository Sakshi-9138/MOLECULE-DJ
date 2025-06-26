#required libraries
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
import librosa
import numpy as np
import time
from IPython.display import display, clear_output


#user input
smiles = input("Enter SMILES of molecules: ") 
music_file = input("Enter full path of MP3 file: ")



#load molecule and make 3D
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)
mol_block = Chem.MolToMolBlock(mol)



#load music and detect beats
y, sr = librosa.load(music_file)
tempo, beat_frames =librosa.beat.beat_track(y=y, sr=sr )
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
tempo_value = float(tempo) if hasattr(tempo, '__len__') else tempo

print(f"Detected tempo: {tempo_value:.2f} BPM")
print(f"Total beats detected: {len(beat_times)}")



#setup viewer
viewer = py3Dmol.view(width=400, height=400)
viewer.addModel(mol_block, 'mol')
viewer.setStyle({'stick': {'colorscheme': 'atom'}})
viewer.zoomTo()
display(viewer.show())



#animate on beats
for beat in beat_times:
    viewer.rotate(20, 'y')           #rotete 20 degrees per beat
    clear_output(wait=True)          #clean old output
    viewer.update()                  #refresh viewer
    display(viewer.show())           #show new position
    time.sleep(60 / tempo_value)