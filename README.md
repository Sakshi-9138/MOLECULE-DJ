MOLECULE-DJ — Animate Molecules with Music Beats 

MOLECULE-DJ is an interactive Python-based project that combines chemistry, audio processing, and 3D animation. It takes a molecular structure (SMILES) and a music file (.MP3) as input, detects beats using Librosa, and animates the molecule in sync with the beat using RDKit and py3Dmol.



## Features

-  Beat detection from any custom `.mp3` file using Librosa
-  3D molecular structure generation from SMILES using RDKit
-  Real-time molecule rotation and animation synced with tempo
-  Works in Jupyter Notebook (with Python)
- Visualization powered by py3Dmol



##  Tech Stack

| Module     | Purpose                                |
| RDKit      | Generate 3D molecules from SMILES      |
| py3Dmol    | 3D molecular visualization in browser  |
| Librosa    | Beat detection from MP3 files          |
| Matplotlib | Plotting waveform and beats       |
| NumPy      | Efficient numerical operations         |
| Python 3.9+| Core programming language         |

##  How to Run

1. Clone the repo or download the code
2. Install dependencies (in `molenv` or any conda env):

` ```bash
conda activate molenv
pip install rdkit-pypi py3Dmol librosa matplotlib`

3.Prepare your files:
       Place your MP3 music file in the same folder. Example: beat_music.mp3
       Choose your molecule using a valid SMILES string. Example: "CCO" for ethanol

4.Run the project:
      Open the Python file (molecule_dj_final.py) in jupyter notebook

5.When prompted:
     Paste your SMILES input
     Enter your music file name, like beat_music.mp3

6.See the Magic:
     The molecule will rotate in 3D synced with the music beats.
     Py3Dmol viewer will show real-time molecular animation.

 **Make sure your Python version is 3.8+ and you're running in an environment where py3Dmol works (Jupyter Notebook recommended for full 3D rotation).**
 
