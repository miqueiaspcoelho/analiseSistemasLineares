'''
References
https://www.youtube.com/watch?v=av8E8qLZswU
https://www.youtube.com/watch?v=4rzpMA6CUPg&t=514s
https://www.youtube.com/watch?v=17cOaqrwXlo
'''
#imported libraries
import pyaudio
import wave
import time
import numpy as np
import matplotlib.pyplot as plt

from classifica import DefineOitava,Acorde

import scipy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
from scipy.fft import fft, fftfreq

#PyAudio object
audio = pyaudio.PyAudio()

#Audio Stream
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024,
    output=True
    )

#read the audio stream until it completes x seconds or the keyboard stops
data=0
frames=[]
seconds=5
start_time=time.time()
print('start recording')
try:
    while abs(time.time()- start_time)<=seconds:
      data=stream.read(1024)
      frames.append(data)
except KeyboardInterrupt:
    pass
print('stop recording')

#stop recording
stream.stop_stream()

#close audio stream
stream.close()

#terminate pyaudio object
audio.terminate()

#saving the audio in a wav file
sound_file=wave.open("myrecording.wav", "wb")

#saving in mono format
sound_file.setnchannels(1)

#bandwidth
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))

#framerate
sound_file.setframerate(44100)

#joining frames into a large byte file
sound_file.writeframes(b''.join(frames))

#open the wav file
wave_file=wave.open("myrecording.wav", "r")

#the minus 1 get all the frames will be read
raw_file=wave_file.readframes(-1)

#convert to array to be able to plot
raw_file=np.frombuffer(raw_file,np.int16)

#axis X in seconds
sampleRate = wave_file.getframerate()
x=np.linspace(0,(len(raw_file)/sampleRate),len(raw_file))
'''
#plot 1
plt.plot(x[::2],raw_file[::2]/max(raw_file),"black")
plt.xlabel('seconds')
plt.ylabel('Amplitude')
plt.title('Plot wav file - time')
#plt.show()
'''
#open, read and apply the fft in a audio signal
s_rate, signal =wavfile.read("myrecording.wav")
FFT=abs(fft(signal))
FFT=FFT/max(FFT)

freqs=fftpk.fftfreq(len(FFT),(1.0/s_rate))

#plot 2
plt.semilogx(freqs[range(len(FFT)//2)],(FFT[range(len(FFT)//2)])/max(FFT))

plt.semilogx(freqs[range(len(FFT)//2)],(FFT[range(len(FFT)//2)]))
plt.xlim(10,10**4)
plt.xlabel('Frequência (HZ)')
plt.ylabel('Amplitude')
plt.title('Plot wav file - frequency')
plt.show()

#Tuner
def Tuner(FFT,freqs):
    index=np.argmax(FFT)
    note=freqs[index]
    print(note)
    return DefineOitava(note)

#Chord
def Chord(FFT,freqs):
    #maximos=sorted(FFT)[(len(FFT)-6):]
    #maximos=sorted(FFT)[(len(FFT)-6):]
    #FFF=FFT[range(len(FFT)//2)]
    
    maximos=FFT[range(len(FFT)//2)]
    freqs=freqs[range(len(freqs)//2)]

    maximos=np.sort(FFT)
    maximos=maximos[(len(maximos)-3):]
    
            
    index0=np.argwhere((FFT[range(len(FFT)//2)])==maximos[-1])[0]
    index1=np.argwhere((FFT[range(len(FFT)//2)])==maximos[-2])[0]
    index2=np.argwhere((FFT[range(len(FFT)//2)])==maximos[-3])[0]
    
    note1=freqs[index0]
    note2=freqs[index1]
    note3=freqs[index2]
    
    print(index0,index1,index2)
    
    print(maximos)
    
    
    print(note1,note2,note3)
    
    return (DefineOitava(note1),DefineOitava(note2),DefineOitava(note3))


Tuner(FFT,freqs)
a=Chord(FFT,freqs)
Acorde(a[0],a[1],a[2])
#print('a0=',a[0],'a1=',a[1],'a2=',a[2])


