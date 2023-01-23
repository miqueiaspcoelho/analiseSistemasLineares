from matplotlib import pyplot as plt
import numpy as np

a=-5 #limite inferior para o vetor n
b=5 #limite superior para o vetor n 

n=np.arange(a,b) #vetor de indices (valores discretos de a até b-1)
tam=len(n)
z=tam*[0] #eixo y para o vetor n (um conjunto de pontos 0 do tamanho do vetor n)

y1=[] #Vetor de saida para função impulso
y2=[] #Vetor de saida para função degrau
y3=[] #Vetor de saida para função rampa


#------------------------Função impulso-----------------------#
titulo1='Função Impulso'
def Impulso(n):
    y=[]
    for indice in n:
        if indice!=0:
            y.append(0)
        else:
            y.append(1)
    return y

y1=Impulso(n)

print('Entrada: ',n,'\n','Saída - Função Impulso: ',y1) #Resultado da saida (Impulso)

plt.plot(n,z,'*',color='red',label='Vetor n') #Vetor de entrada
plt.plot(n,y1,'o',color='blue',alpha=0.5,label=titulo1) #Vetor de saida (gráfico)

plt.xlabel('n(indices)') #legenda eixo x
plt.ylabel('y[n]') #legenda eixo y

plt.axis([a-1,b+1,-0.1,1.5]) #limite dos eixos

plt.grid()
plt.legend()
plt.title (titulo1)
plt.show()


#-------------------------Função degrau------------------------#
titulo2='Função Degrau'
def Degrau(n):
    y=[]
    for indice in n:
        if indice < 0:
            y.append(0)
        else:
            y.append(1)
    return y

y2=Degrau(n)

print('Entrada: ',n,'\n','Saída - Função Degrau: ',y2) #Resultado da saida (Degrau)

plt.plot(n,z,'*',color='red',label='Vetor n') #Vetor de entrada
plt.plot(n,y2,'o',color='blue',alpha=0.5,label=titulo2) #Vetor de saida (gráfico)

plt.xlabel('n(indices)') #legenda eixo x
plt.ylabel('y[n]') #legenda eixo y

plt.axis([a-1,b+1,-0.1,1.5]) #limite dos eixos

plt.grid()
plt.legend()
plt.title (titulo2)
plt.show()

#-------------------------Função rampa-------------------------#
titulo3='Função Rampa'
def Rampa(n):
    y=[]
    for indice in n:
        if indice < 0:
            y.append(0)
        else:
            y.append(indice)
    return y

y3=Rampa(n)

print('Entrada: ',n,'\n','Saída - Função Rampa: ',y3) #Resultado da saida (Rampa)

plt.plot(n,z,'*',color='red',label='Vetor n') #Vetor de entrada
plt.plot(n,y3,'o',color='blue',alpha=0.5,label=titulo3) #Vetor de saida (gráfico)

plt.xlabel('n(indices)') #legenda eixo x
plt.ylabel('y[n]') #legenda eixo y

plt.axis([a-1,b+1,-0.1,b]) #limite dos eixos

plt.grid()
plt.legend()
plt.title (titulo3)
plt.show()


