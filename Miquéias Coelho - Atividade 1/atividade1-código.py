from matplotlib import pyplot as plt
import numpy as np

io=0.05001 #corrente inicial, logo em t=0 io=0
v=10 #tensão constante de 10 volts
r=200 #resistência de 200 ohms
l=100 #indutor de 100 Henry

#t=np.arange(0,100) #eixo x, tempo variando de 0 a 100 segundos
t=np.linspace(0,10,1000) #linspace funciona bem melhor, pois posso dizer a quantidade de pontos dentro do intervalo
i=(v/r)+(np.exp((-r/l)*t))*(io-(v/r))


#plt.plot(t,(t-t+0.05))
plt.plot(t,i,color='blue')
plt.ylabel('CORRENTE (A)') #texto do eixo Y
plt.xlabel('TEMPO (s)') #texto do eixo X
plt.title('Circuito RL - I x T') #título
#plt.axis([-1,10,0,0.06]) #limite dos eixos
plt.show()

