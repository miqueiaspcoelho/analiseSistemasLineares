from matplotlib import pyplot as plt
import numpy as np
import math as mt

def An(n,a0): #termo An
    return a0*(2/(1+(16*n**2)))

def Bn(n,a0): #termo Bn
    return a0*(8*n/(1+(16*n**2)))

def Cn(n,a0): #termo Cn
    return 2*a0/(mt.sqrt(1+16*n**2))

def Angulo(n): #ângulo teta
    return np.arctan(-4*n)


def Fourier(n,t): #série de fourier para e^(-t/2)
    a0=(2/mt.pi)*(1 - np.exp((-mt.pi)/2))
    c0=a0
    valores=[]
    soma=0
    for tempo in t:
        soma=0
        for N in range(1,n+1):
            soma+=(Cn(N,a0))*np.cos(N*2*tempo + Angulo(N))
        valores.append(c0+soma)
    return valores

n0=1 #n0
n1=5 #n1
n2=30 #n2

Linferior=-10 #Limite inferior do tempo
Lsuperior=11 #Limite superior do tempo

'''
Modificando a quantidade de pontos dentro do mesmo intervalo, altera-se
suavemente as ondulações presentes em cada aproximação
'''
qtd_pontos=10000 #quantidade de pontos dentro do intervalo de tempo

t=np.linspace(Linferior,Lsuperior, qtd_pontos) #vetor tempo

a=Fourier(n0,t) #aproximação para n=1
b=Fourier(n1,t) #aproximação para n=5
c=Fourier(n2,t) #aproximação para n=30

plt.plot(t,a,color='black', label='Para N='+str(n0)) #n=1
plt.plot(t,b,color='red', label='Para N='+str(n1)) #n=5
plt.plot(t,c,color='blue', label='Para N='+str(n2)) #n=30

plt.legend()

plt.xlabel('t (s)')
plt.ylabel('x(t)')
plt.title('Aproximação de e^(-t/2) - Fourier')

plt.axis([min(t)-0.5,max(t)+0.5,min(a)-0.5,max(a)+0.5])
plt.show()

