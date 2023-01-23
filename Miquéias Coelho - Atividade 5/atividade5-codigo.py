from matplotlib import pyplot as plt
import numpy as np

'''
1-Avaliação do valor de delta por meio de Bhaskara
2-Para cada valor de delta há um sistema matricial correspondente
2.1-Os sistemas decorrem de y(t) e y'(t), para a resolução dos sistemas foi
utilizada uma abordagem analítica fundamentada no método de eliminação de Gauss-Jordan,
dessa forma as constantes c1 e c2 surgem após a resolução desse sistema matricial
'''
def edoSegundaOrdem (a,b,c,t0,y0,yd):
    delta=(b**2) - (4 * a * c)
    r1= (-b + (delta)**0.5)/(2*a)
    r2= (-b - (delta)**0.5)/(2*a)


    if delta > 0:
        w1=np.exp(r1*t0)
        w2=np.exp(r2*t0)
        w3=r1*w1
        w4=r2*w2
        
        A=[[w1 , w2,  y0],
           [w3 , w4, yd]]
        
    if delta < 0:
        
        w1= (np.exp(r1.real*t0))*(np.cos(r1.imag*t0))
        w2= (np.exp(r1.real*t0))*(np.sin(r1.imag*t0))
        w3= (r1.real*w1) - (r1.imag*w2)
        w4= (r1.real*w2) + (r1.imag*w1)
        
        A=[[w1 , w2 , y0 ],
           [w3 , w4 , yd]]
        
    if delta == 0:
        r=r1
        w1=np.exp(r*t0)
        w2=t0*w1
        w3=r*w1
        w4=w1+t0*w3

        A=[[w1 , w2 , y0],
          [w3 , w4 , yd]]

    B= (( (A[0][0] * A[1][1]) - (A[1][0] * A[0][1]) ) / (A[0][0]))

    C= (( (A[0][0] * A[1][2]) - (A[1][0] * A[0][2]) ) / (A[0][0]))

    D= (( B * (A[0][2]/A[0][0]) ) - ( C * (A[0][1]/A[0][0]) ) ) / B

    c1= D

    c2= C / B

    return delta,r1,r2,c1,c2,A

'''
1-Aqui ocorre a geração do gráfico ao informarmos os parâmetros necessários,
parâmetros que em sua maioria decorrem da função acima
'''

def plotaGrafico(delta,r1,r2,c1,c2,faixa,cor,linha):
    Y=0
    if delta > 0:
        t=np.linspace(0,faixa,5000)
        Y=c1*(np.exp(r1*t))+c2*(np.exp(r2*t))
        grafico=plt.plot(t,Y,linha,color=cor,label='Delta > 0')
        plt.xlabel('t') #legenda eixo x
        plt.ylabel('Y(t)') #legenda eixo y
        plt.legend()
        
    if delta < 0:
        t=np.linspace(0,faixa,5000)
        Y=c1*((np.exp(r1.real*t))*(np.cos(r1.imag*t)) + c2*((np.exp(r1.real*t))*(np.sin(r1.imag*t))))
        grafico=plt.plot(t,Y,linha,color=cor,label='Delta < 0')
        plt.xlabel('t') #legenda eixo x
        plt.ylabel('Y(t)') #legenda eixo y
        plt.legend()

    if delta==0:
        t=np.linspace(0,faixa,5000)
        Y=c1*(np.exp(r1*t))+(c2*t)*(np.exp(r1*t))
        grafico=plt.plot(t,Y,linha,color=cor,label='Delta == 0')
        plt.xlabel('t') #legenda eixo x
        plt.ylabel('Y(t)') #legenda eixo y
        plt.legend()
    return grafico


#--------VALORES PARA TESTE------------------#
#Delta > 0
#a=1
#b=5
#c=6
#t0=0
#y0=2
#yd=3

#Delta  < 0
#a=16
#b=-8
#c=145
#t0=0
#y0=-2
#yd=1

#a=1
#b=0
#c=9
#t0=0
#y0=1
#yd=1

#Delta = 0
#a=1
#b=-1
#c=0.25
#t0=0
#y0=2
#yd=1/3
#---------------------------------------------#

#------VALORES PROPOSTOS NA ATIVIDADE----------#
#Valores da edo A
a=1
b=0
c=1

#Valores da edo B
a1=1
b1=0.125
c1=1

#Condições comuns a ambas
t0=0
y0=2
yd=0

resultadoA=edoSegundaOrdem(a,b,c,t0,y0,yd) #Resolução da primeira edo (A)
resultadoB=edoSegundaOrdem(a1,b1,c1,t0,y0,yd) #Resolução da segunda edo (B)

deltaA=resultadoA[0] #Delta da equação caracteristica da edo A
r1A=resultadoA[1] #raiz 1 (A)
r2A=resultadoA[2] #raiz 2 (A)
c1A=resultadoA[3] #constante c1 (A)
c2A=resultadoA[4] #constante c2 (A)
AA=resultadoA[5]  #Matriz que gerou o sistema matricial(A)

deltaB=resultadoB[0] #Delta da equação caracteristica da edo B
r1B=resultadoB[1] #raiz 1 (B)
r2B=resultadoB[2] #raiz 2 (B)
c1B=resultadoB[3] #constante c1 (B)
c2B=resultadoB[4] #constante c2 (B)
AB=resultadoB[5]  #Matriz que gerou o sistema matricial(B)

#Resultados para a edo A
print('Valor de delta: ',deltaA)
print('Valor de r1: ',r1A)
print('Valor de r2: ',r2A)
print('Valor de c1: ',c1A)
print('Valor de c2: ',c2A)
print('Matriz A: ',AA)

#Resultados para a edo B
print('Valor de delta: ',deltaB)
print('Valor de r1: ',r1B)
print('Valor de r2: ',r2B)
print('Valor de c1: ',c1B)
print('Valor de c2: ',c2B)
print('Matriz A: ',AB)

graficoA=plotaGrafico(deltaA,r1A,r2A,c1A,c2A,50,'blue','--') #gráfico da edo A
graficoB=plotaGrafico(deltaB,r1B,r2B,c1B,c2B,50,'black','') #gráfico da edo B
plt.grid()
plt.title('E.D.O 2º Ordem')
plt.show()

