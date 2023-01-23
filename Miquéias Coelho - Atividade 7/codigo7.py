import numpy as np
import matplotlib.pyplot as plt
import pyaudio as py
import struct
from scipy.fftpack import fft
import time

'''
referência
Realtime Audio Spectrum Analyser Using Python 3 | Part 2
https://www.youtube.com/watch?v=E_QLQyHf_Yw&t=208s

ps.: Professor, infelizmente a precisão ficou bem ruim e eu não soube como melhorar
testei aqui usando o violão e um teclado virtual e algumas vezes as notas batem
mas na maioria da uma diferente de 1 tom 
'''

def NotasMusicais(valor,grafico):
    notas=[261.81278,
           277.18263,
           293.66477,
           311.12698,
           329.62756,
           349.22823,
           369.99442,
           391.99544,
           415.3047,
           440,
           466.16376,
           493.8833]
   
    if valor<notas[0] or valor>notas[11]*2**7:
        grafico.set_title("Nota nenhuma")
        #print('Valor=',valor,'nota nenhuma')

    if valor>=notas[0] and valor<=notas[1]:
        grafico.set_title("C ")
        #print('Valor=',valor,'C')
        
    if valor>= notas[1] and valor<=notas[2]:
        grafico.set_title("C#  ")
        #print('Valor=',valor,'C#')
        time.sleep(5)
    if valor>= notas[2] and valor<=notas[3]:
        grafico.set_title("D  ")
        #print('Valor=',valor,'D')
   
    if valor>= notas[3] and valor<=notas[4]:
        grafico.set_title("D#  ")
        #print('Valor=',valor,'D#')
       
    if valor>= notas[4] and valor<=notas[5]:
        grafico.set_title("E  ")
        #print('Valor=',valor,'E')
        
    if valor>= notas[5] and valor<=notas[6]:
        grafico.set_title("F  ")
        #print('Valor=',valor,'F')
        
    if valor>= notas[6] and valor<=notas[7]:
        grafico.set_title("F#  ")
        #print('Valor=',valor,'F#')
        
    if valor>= notas[7] and valor<=notas[8]:
        grafico.set_title("G  ")
        #print('Valor=',valor,'G')
        
    if valor>= notas[8] and valor<=notas[9]:
        grafico.set_title("G#  ")
        #print('Valor=',valor,'G#')
        
    if valor>= notas[9] and valor<=notas[10]:
        grafico.set_title("A  ")
        #print('Valor=',valor,'A')
        
    
    if valor>= notas[10] and valor<=notas[11]:
        grafico.set_title("A#  ")
        #print('Valor=',valor,'A#')
        
    if valor >= notas[11] and valor<=notas[11]+0.05:
        grafico.set_title("B  ")
        #print('Valor=',valor,'B')
        

CHUNK = 1024*2 #passo (número de amostras por segundo)
FORMAT = py.paInt16 #formato do audio 16bits
CHANNELS = 1 #canais
RATE = 44100 #hertz

audio=py.PyAudio() #objeto de audio

microfone=audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
    )
fig, (ax1,ax2) = plt.subplots(2)
dados_byte=0
dados_convertidos=0
transformada=0
modulo_transformada=0
modulo_maximo=0

#1-Inicia
#Estamos plotando o gráfico da entrada de som no tempo
x = np.arange(0,2*CHUNK,2) #Valor para X, sendo sempre potências de 2
line, = ax1.plot(x,(np.random.rand(CHUNK)),'r') #classe gráfico
ax1.set_xlim(0,CHUNK+2)#limite para X
ax1.set_ylim(-32000, 32000) #limite para Y
ax1.set_xlabel('Tempo') #legenda do eixo X
ax1.set_ylabel('Amplitude do sinal') #legenda do eixo Y
#1-Finaliza

#2-Inicia
x_fft = np.linspace(0,RATE, CHUNK) #Valor para X nas frequências, indo de 0 a RATE e contendo 1024 pontos dentro
line_fft, = ax2.semilogx(x_fft,np.random.rand(CHUNK),'b') #classe gráfico para frequências (escala logaritmica)
ax2.set_ylim(0,1) #limite para Y
ax2.set_xlim(20,RATE/2) #limite para X, porém, na forma de decibeis
ax2.set_xlabel('Hz') #legenda do eixo X
ax2.set_ylabel('Amplitude do sinal (módulo)') #legenda do eixo Y
#2-Finaliza


fig.show()

while True:
    dados_byte=microfone.read(CHUNK) #lendo as informações do microfone (dados binário)
    dados_convertidos=struct.unpack(str(CHUNK) + 'h', dados_byte) #(dados inteiros)
    transformada=np.fft.fft(dados_convertidos) #transformada
    
    line.set_ydata(dados_convertidos) #colocando no objeto Line2d (line) valores para y (TEMPO)
    line_fft.set_ydata(np.abs(transformada)*2/(32000*CHUNK))
    
   
    modulo_transformada=abs(transformada) #modulo
    modulo_maximo=max(modulo_transformada)//10000
    
    NotasMusicais(modulo_maximo,ax1)
    fig.canvas.draw() #redesenha a figura sempre que ocorrem modificações
    fig.canvas.flush_events() #a cada evento redesenha com o draw
    

    
 
