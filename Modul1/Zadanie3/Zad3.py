from scipy.io import wavfile
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
sampFreq, snd = wavfile.read("sound2.wav")

snd = snd / (2.**15)
s1 = snd[:,0] 
timeArray = np.arange(0, snd.shape[0], 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  
plt.plot(timeArray, s1, color='k')
plt.ylabel('Amplitude')
plt.xlabel('Time (ms)')
plt.rcParams["figure.figsize"] = [16,10]