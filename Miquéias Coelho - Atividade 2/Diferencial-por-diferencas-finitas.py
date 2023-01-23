from matplotlib import pyplot as plt #Biblioteca utilizada

'''
A função recebe dois parâmetros, x e t para assim realizar a diferenciação
por meio das diferenças finitas.
'''
def Diferencial(x,t):
    contador=1
    fx=0
    y=[]
    for posicao in range(0,len(x)):
        if contador<len(x):
           fx=(x[contador]-x[posicao])/(t[contador]-t[posicao])
           y.append(fx)
           if len(y)==1: #duplicação do primeiro termo
               y.append(fx)
        contador+=1
    return y

#----VALORES DE TESTE----#
#x=[0,0,1,0,0] #vetor x1 
#t=[-2,-1,0,1,2] #vetor t1 

#x=[0,0,1,1,0,0,0] #vetor x2 
#t=[-2,-1,-0.5,0,0.5,1,2] #vetor t2 

#x=[1,2,4,16] #vetor x3 
#t=[-2,-1,0,1] #vetor t3 
#------------------------#

y=Diferencial(x,t)
plt.plot(t,y,color='red',label='Sinal de Saida') #Sinal de Saída
plt.plot(t,x,'b--',label='Sinal de Entrada') #Sinal de Entrada
plt.xlabel('t') #eixo horizontal
plt.ylabel('y(t)') #eixo vertical
plt.axis([min(t)-1,max(t)+1,min(y)-1,1.5*max(y)]) #limite dos eixos
plt.grid() #grade

plt.legend()
plt.title('y(t)=dx(t)/dt')

plt.show()
