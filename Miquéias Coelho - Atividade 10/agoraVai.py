import pyaudio
import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fftpk
from scipy.fft import fft, fftfreq
import control.matlab
import math
import warnings

#para não exibir alguns avisos que estava aparecendo ao usar tf e lsim
warnings.filterwarnings('ignore', '.*return_x specified*', )
warnings.filterwarnings('ignore', '.*Non-zero initial condition given for*', )

'''
Violão de nylon utilizado para testes - afinação padrão - afinado com afinador de clip
Acordes maiores naturais
Formatos padrões/convencionais, exceto Ré, nele o formato que melhor funcionou
foi no formato de dó.
Acorde de si foi preciso tocar 4 vezes, sendo reconhecido na quarta vez
Acorde de sol foi tocado 2 vezes, na primeira o sistema sem filtro acertou
porém o com filtro não, na segunda vez ambos acertaram

cada nota recebeu um identificador
do=1
do#=1.1
re=2
re#=2.2
mi=3
fa=4
fa#=4.1
sol=5
sol#=5.1
la=6
la#=6.1
si=7
'''


def GravarAudio(tempo):
    #Objeto de audio
    audio = pyaudio.PyAudio()

    #Configuraçoes da gravaçao
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024,
        output=True
        )

    #gravando microfone
    data=0
    frames=[]
    seconds=tempo
    start_time=time.time()
    print('Luz câmera,ação! Gravando.')
    try:
        while abs(time.time()- start_time)<=seconds:
          data=stream.read(1024,exception_on_overflow = False)
          frames.append(data)
    except KeyboardInterrupt:
        pass
    print('Corta.\n')
    stream.stop_stream()

    #fechando o audio
    stream.close()
    
    #transformando para frames
    frames=b''.join(frames)
    data=np.frombuffer(frames,dtype=np.int16)
    
    #finalizando o objeto de audio
    audio.terminate()
    return data


def TransformadaFourier(data):
    FFT=abs(fft(data))#transformada e modulo

    freqs=fftpk.fftfreq(len(FFT),(1.0/44100))#frequencia
    freqs=freqs[:(len(freqs)//2)]#parte positiva

    
    FFT=FFT[0:(len(FFT)//2)]#parte positiva
    return freqs,FFT

def DefineGrafico():
    fig, (plot1,plot3) = plt.subplots(2)
    
    plot1.set_ylabel('|amplitude|')
   
    plot3.set_xlabel('frequência')
    plot3.set_ylabel('|amplitude|')
    
    return fig,plot1,plot3

def Filtro(data):
    tam=len(data)
    #Condições iniciais
    fc=200
    C=1
    R=(1/(2*math.pi*C*fc))
    tau=R*C
    y0=[[0]] # ordem no código é: y'[0] e depois y[0] /  nesse exemplo  y'[0]=0 e y[0]=2
    
    tempo =np.linspace(0,(len(data)/44100),len(data))

    #Função de transferência, sRC/sRC+1
    num_ft=[tau,0]
    den_ft=[tau,1]
    func_trans=control.matlab.tf(num_ft, den_ft)
    print(func_trans)
    #Simulação usando a função lsim
    yout, t, xout = control.matlab.lsim(func_trans, data, tempo, y0)
    return yout

def OitavaP3(nota,grafico):
    p=[
        130,138,146,155,
        164,174,184,195,
        207,220,233,245 
        ]
    if nota>=p[0] and nota<p[1]:
        grafico.set_title('Dó')
        return 1
        
    elif nota>=p[1] and nota<p[2]:
        grafico.set_title('Dó Sustenido/Ré bemol')
        return 1.1
    
    elif nota>=p[2] and nota<p[3]:
        grafico.set_title('Ré')
        return 2
    
    elif nota>=p[3] and nota<p[4]:
        grafico.set_title('Ré Sustenido/Mi bemol')
        return 2.1
    
    elif nota>=p[4] and nota<p[5]:
        grafico.set_title('Mi')
        return 3
    
    elif nota>=p[5] and nota<p[6]:
        grafico.set_title('Fá')
        return 4
    
    elif nota>=p[6] and nota<p[7]:
        grafico.set_title('Fá Sustenido/Sol bemol')        
        return 4.1
    
    elif nota>=p[7] and nota<p[8]:
        grafico.set_title('Sol')
        return 5
    
    elif nota>=p[8] and nota<p[9]:
        grafico.set_title('Sol Sustenido/Lá bemol')
        return 5.1
    
    elif nota>=p[9] and nota<p[10]:
        grafico.set_title('Lá')
        return 6
    
    elif nota>=p[10] and nota<p[11]:
        grafico.set_title('Lá Sustenido')
        return 6.1
    
    elif nota>=p[11]:
        grafico.set_title('Si')
        return 7
    
def OitavaP4(nota,grafico):
    p=[
        260,277,293,311,
        329,349,369,391,
        415,440,466,493
        ]        

    if nota>=p[0] and nota<p[1]:
        grafico.set_title('Dó')
        return 1
        
    elif nota>=p[1] and nota<p[2]:
        grafico.set_title('Dó Sustenido/Ré bemol')
        return 1.1
    
    elif nota>=p[2] and nota<p[3]:
        grafico.set_title('Ré')
        return 2
    
    elif nota>=p[3] and nota<p[4]:
        grafico.set_title('Ré Sustenido/Mi bemol')
        return 2.1
    
    elif nota>=p[4] and nota<p[5]:
        grafico.set_title('Mi')
        return 3
    
    elif nota>=p[5] and nota<p[6]:
        grafico.set_title('Fá')
        return 4
    
    elif nota>=p[6] and nota<p[7]:
        grafico.set_title('Fá Sustenido/Sol bemol')        
        return 4.1
    
    elif nota>=p[7] and nota<p[8]:
        grafico.set_title('Sol')
        return 5
    
    elif nota>=p[8] and nota<p[9]:
        grafico.set_title('Sol Sustenido/Lá bemol')
        return 5.1
    
    elif nota>=p[9] and nota<p[10]:
        grafico.set_title('Lá')
        return 6
    
    elif nota>=p[10] and nota<p[11]:
        grafico.set_title('Lá Sustenido')
        return 6.1
    
    elif nota>=p[11]:
        grafico.set_title('Si')
        return 7
    
def Classificador(valor,grafico):
    if valor<130 or valor>523:
        #print('Nota fora do range:',valor)
        grafico.set_title('Fora do range')
        return 0
        
    else:
        if valor>=130 and valor <260:
            return OitavaP3(valor,grafico)
        elif valor>=260 and valor<=523:
            return OitavaP4(valor,grafico)

def Acorde(triade,grafico):
    do={1,3,5}
    re={2,4.1,6}
    
    mi={3,5.1,7}
    fa={4,6,1}
    
    sol={5,7,2}
    la={6,1.1,3}
    
    si={7,2.1,4.1}
    
    if do.intersection(triade)==do:
        return grafico.set_title('Acorde de Dó')
    elif re.intersection(triade)==re:
        return grafico.set_title('Acorde de Ré')
    elif mi.intersection(triade)==mi:
        return grafico.set_title('Acorde de Mi')
    elif fa.intersection(triade)==fa:
        return grafico.set_title('Acorde de Fá')
    elif sol.intersection(triade)==sol:
        return grafico.set_title('Acorde de Sol')
    elif la.intersection(triade)==la:
        return grafico.set_title('Acorde de Lá')
    elif si.intersection(triade)==si:
        return grafico.set_title('Acorde de Si')
    else:
        return grafico.set_title('Acorde não identificado')

'''OBJETOS GRÁFICOS'''
fig, plot1,  plot3,  = DefineGrafico()

'''GUARDANDO AUDIO'''
data=GravarAudio(5)

'''###############################################################'''
'''SEM FILTRO'''
#print('Sem filtro\n')

tf1=TransformadaFourier(data) #transformada sobre o audio original
freqs=tf1[0] #frequências
FFT=tf1[1] #módulo da transformada

#notaSF=freqs[np.argmax(FFT)] #frequência de pico
#Classificador(notaSF,plot1)#classificando a nota

PLOT1, = plot1.semilogx(freqs,FFT/10**4,'black',label="Sem filtro") #plotando gráfico 1

#Classificando o acorde 
picosSF=np.sort(FFT) #ordenando de forma crescente
picosSF=picosSF[::-1] #array na ordem decrescente
picosSF=picosSF[0:21] #pegando 21 valores
triadeSF=set() #conjunto
for f in picosSF:
    index=np.argwhere(FFT==f)
    frequencia=int(freqs[index][0][0])
    nota=Classificador(frequencia,plot1)
    if nota != None:
        triadeSF.add(nota)
Acorde(triadeSF,plot1)
#print('Notas de pico sem utilizar filtro=',triadeSF)

'''##################################################################'''
'''COM FILTRO'''
#print('\nCom filtro\n')
print('Função de transferência - Utilizada \n')

faudio=Filtro(data) #aplicando filtro no audio original

tf2=TransformadaFourier(faudio) #transformada sobre o audio com filtro
freqs1=tf2[0] #frequências
FFT1=tf2[1] #módulo da transformada

#notaCF=freqs1[np.argmax(FFT1)] #frequência de pico
#Classificador(notaCF,plot3) #classificando a nota

PLOT2, = plot3.semilogx(freqs1,FFT1/10**4,'r',label="Com filtro") #plotando gráfico 2

#Classificando o acorde 
picosCF=np.sort(FFT1) #ordenando de forma crescente
picosCF=picosCF[::-1] #array na ordem decrescente
picosCF=picosCF[0:21] #pegando 21 valores
triadeCF=set() #conjunto
for f1 in picosCF:
    index1=np.argwhere(FFT1==f1)
    frequencia1=int(freqs1[index1][0][0])
    nota1=Classificador(frequencia1,plot3)
    if nota1 != None:
        triadeCF.add(nota1)
Acorde(triadeCF,plot3)

#print('Notas de pico usando filtro',triadeCF)
plot1.legend()
plot3.legend()
plt.show() #exibindo os gráficos

'''
Referências
1-https://www.youtube.com/watch?v=x51Oh7jIL9k
2-Código compartilhado pelo professor na atividade 9
3-Suprimir avisos em Python - defstack.com
4-Remover duplicatas da lista em Python defstack.com
'''
