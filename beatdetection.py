import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display


# file_path = input("Enter music file name:")
file_path = "beat_music.mp3"

#load the audio 
y,sr=librosa.load(file_path)
print("Music loaded")


#Detect tempo and beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print("Tempo:" ,tempo, "BPM")
print(" Beat frame positions:", beat_frames)


#Convert beat frames to times(in seconds)
beat_times=librosa.frames_to_time(beat_frames,sr=sr)
print("Beat times in seconds:",beat_times)


#plot beats on waveform
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr, alpha=0.6)
plt.vlines(beat_times, -1,1 ,color='r' , linestyle= '--' ,label='Beats')
plt.title(" Music Beat Detection")
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()
plt.show()


#save beat times in file
with open("beat_times.txt" , "w") as f:
    for t in beat_times:
        f.write(str(t) + "\n")