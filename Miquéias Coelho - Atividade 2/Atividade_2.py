from matplotlib import pyplot as plt #biblioteca gráfica

#x=[0,0,1,0,0] #vetor x1 (entrada-1)
#t=[-2,-1,0,1,2] #vetor t1 (entrada-1)

#x=[0,0,1,1,0,0,0] #vetor x2 (entrada-2)
#t=[-2,-1,-0.5,0,0.5,1,2] #vetor t2 (entrada-2)

x=[1,2,4,16] #vetor x3 (entrada-3)
t=[-2,-1,0,1] #vetor t3 (entrada-3)

y=[] #saída do sistema

i=1 #contadotr

'''
Dentro do laço foi implementado o método das
diferenças finitas, dessa forma podemos estimar a derivada
mediante os pontos conhecidos, pontos que são relativos aos
vetores de entrada
ps.: para garantir uma quantidade de termos na saida,
o primeiro termo é duplicado uma única vez logo no início
do laço.
As diferenças finitas geram entradas-1 pontos de saída, por isso
foi feita a duplicação do termo inicial para correta construção do algoritmo
com a função plt.plot
'''
for n in range(0,len(x)):
    if i<len(x):
       fx=(x[i]-x[n])/(t[i]-t[n])
       y.append(fx)
       if len(y)==1: #duplicação do primeiro termo
           y.append(fx)
    i+=1

plt.plot(t,y,color='red',label='Sinal de Saida') #Sinal de Saída
plt.plot(t,x,'b--',label='Sinal de Entrada') #Sinal de Entrada

plt.xlabel('t') #eixo horizontal
plt.ylabel('y(t)') #eixo vertical
plt.axis([min(t)-1,max(t)+1,min(y)-1,1.5*max(y)]) #limite dos eixos
plt.grid() #grade

plt.legend()
plt.title('y(t)=dx(t)/dt')

plt.show()
