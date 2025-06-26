# ✅ STEP 0: Required Libraries
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
import librosa
import numpy as np
import time
from IPython.display import display, clear_output

# ✅ STEP 1: USER INPUT
smiles = input("Enter SMILES of molecule: ")  # Example: CCO
music_file = input("Enter full path of MP3 file: ")  # Example: C:\\Users\\Dell\\Desktop\\MOLECULE DJ\\beat_music.mp3

# ✅ STEP 2: Load Molecule and Make 3D
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)
mol_block = Chem.MolToMolBlock(mol)

# ✅ STEP 3: Load Music and Detect Beats
y, sr = librosa.load(music_file)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# 👇 Fix tempo for float error
tempo_value = float(tempo) if hasattr(tempo, '__len__') else tempo

print(f"Detected tempo: {tempo_value:.2f} BPM")
print(f"Total beats detected: {len(beat_times)}")

# ✅ STEP 4: Setup Viewer
viewer = py3Dmol.view(width=400, height=400)
viewer.addModel(mol_block, 'mol')
viewer.setStyle({'stick': {'colorscheme': 'atom'}})  # 🎨 colorful atoms
viewer.zoomTo()
display(viewer.show())  # Just to display first time

# ✅ STEP 5: Animate on Beats
for beat in beat_times:
    viewer.rotate(20, 'y')            # rotate 20 degrees per beat
    clear_output(wait=True)          # clean old output
    viewer.update()                  # refresh viewer
    display(viewer.show())           # show new position
    time.sleep(60 / tempo_value)     # sync with tempo (BPM)