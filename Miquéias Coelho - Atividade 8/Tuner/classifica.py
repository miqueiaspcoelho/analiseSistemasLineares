#average
def Media(a,b):
    return (a+b)/2

#first octave
def OitavaP1(valor):
    p=[
        int(32.703196),34.647829,36.708096,38.890873,
        41.203445,43.653529,46.249303,48.999429,
        51.913087,55,58.27047,65
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.2
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.2
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7
#second octave
def OitavaP2(valor):
    p=[
        int(65.406392),69.295658,73.416192,77.781746,
        82.40689,87.307058,92.498606,97.998858,
        103.826174,110,116.54094,130
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#third octave
def OitavaP3(valor):
    p=[
        int(130.812784),138.591316,146.832384,155.563492,
        164.81378,174.614116,184.997212,195.997716,
        207.652348,220,233.08188,261 
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#fouth octave
def OitavaP4(valor):
    p=[
        int(261.625568),277.182632,293.664768,311.126984,
        329.62756,349.228232,369.994424,391.995432,
        415.304696,440,466.16376,523
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#fifth octave
def OitavaP5(valor):
    p=[
        int(523.251136),554.365264,587.329536,622.253968,
        659.25512,698.456464,739.988848,783.990864,
        830.609392,880,932.32752,1046 
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#sixth octave
def OitavaP6(valor):
    p=[
        int(1046.502272),1108.730528,1174.659072,1244.507936,
        1318.51024,1396.912928,1479.977696,1567.981728,
        1661.218784,1760,1864.65504,2093 
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6

    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1

    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#seventh octave
def OitavaP7(valor):
    p=[
        int(2093.004544),2217.461056,2349.318144,2489.015872,
        2637.02048,2793.825856,2959.955392,3135.963456,
        3322.437568,3520,3729.31008,3951.066432 
        ]
    if valor>=p[0] and valor<p[1]:
        if valor<=Media(p[0],p[1]):
            print('Dó')
            return 1
        else:
            print('Dó Sustenido/Ré bemol')
            return 1.1
    
    if valor>=p[1] and valor<p[2]:
        if valor<=Media(p[1],p[2]):
            print('Dó Sustenido/Ré bemol')
            return 1.1
        else:
            print('Ré')
            return 2
        
    if valor>=p[2] and valor<p[3]:
        if valor<=Media(p[2],p[3]):
            print('Ré')
            return 2
        else:
            print('Ré Sustenido/Mi bemol')
            return 2.1

    if valor>=p[3] and valor<p[4]:
        if valor<=Media(p[3],p[4]):
            print('Ré Sustenido/Mi bemol')
            return 2.1
        else:
            print('Mi')
            return 3
        
    if valor>=p[4] and valor<p[5]:
        if valor<=Media(p[4],p[5]):
            print('Mi')
            return 3
        else:
            print('Fá')
            return 4
    
    if valor>=p[5] and valor<p[6]:
        if valor<=Media(p[5],p[6]):
            print('Fá')
            return 4
        else:
            print('Fá Sustenido/Sol bemol')
            return 4.1

    if valor>=p[6] and valor<p[7]:
        if valor<=Media(p[6],p[7]):
            print('Fá Sustenido/Sol bemol')
            return 4.1
        else:
            print('Sol')
            return 5
    
    if valor>=p[7] and valor<p[8]:
        if valor<=Media(p[7],p[8]):
            print('Sol')
            return 5
        else:
            print('Sol Sustenido/Lá bemol')
            return 5.1

    if valor>=p[8] and valor<p[9]:
        if valor<=Media(p[8],p[9]):
            print('Sol Sustenido/Lá bemol')
            return 5.1
        else:
            print('Lá')
            return 6
    if valor>=p[9] and valor<p[10]:
        if valor<=Media(p[9],p[10]):
            print('Lá')
            return 6
        else:
            print('Lá Sustenido')
            return 6.1
    if valor>=p[10] and valor<=p[11]:
        if valor<=Media(p[10],p[11]):
            print('Lá Sustenido')
            return 6.1
        else:
            print('Si')
            return 7

#define octave
def DefineOitava(valor):
    if valor<32 or valor>3951.066432:
        return print('Fora da faixa de persepção')
    if valor>=32 and valor<=3951.066432:
        if valor>=32 and valor<65:
            print('Oitava 1')
            return OitavaP1(valor)
        elif valor>=65 and valor<130:
            print('Oitava 2')
            return OitavaP2(valor)
        
        elif valor>=130 and valor<261:
            print('Oitava 3')
            return OitavaP3(valor)
        
        elif valor>=261 and valor<523:
            print('Oitava 4')
            return OitavaP4(valor)
        
        elif valor>=523 and valor<1046:
            print('Oitava 5')
            return OitavaP5(valor)
        
        elif valor>=1046 and valor<2093:
            print('oitava 6')
            return OitavaP6(valor)
        
        elif valor>=2093 and valor<=3951.066432:
            print('Oitava 7')
            return OitavaP7(valor)
        else:
            print('Valor dentro do range, porém indeterminado')
            return 0

def Do(note1,note2,note3):
    lista=[note1,note2,note3]
    a=1
    b=3
    c=5
    x='Dó'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')

def Re(note1,note2,note3):
    lista=[note1,note2,note3]
    a=2
    b=4.1
    c=6
    x='Ré'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
    
def Mi(note1,note2,note3):
    lista=[note1,note2,note3]
    a=3
    b=5.1
    c=7
    x='Mi'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
    
def Fa(note1,note2,note3):
    lista=[note1,note2,note3]
    a=4
    b=6
    c=1
    x='Fá'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
    
def Sol(note1,note2,note3):
    lista=[note1,note2,note3]
    a=5
    b=7
    c=2
    x='Sol'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
    
def La(note1,note2,note3):
    lista=[note1,note2,note3]
    a=6
    b=1.1
    c=3
    x='Lá'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
    
def Si(note1,note2,note3):
    lista=[note1,note2,note3]
    a=7
    b=2.1
    c=4.1
    x='Si'
    if (lista.count(a)==1) and (lista.count(b)==1) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(b)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==1) and (lista.count(c)==2):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(b)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==2) and (lista.count(c)==1):
        return print('Maior possibilidade de ', x , ' maior')
    
    elif (lista.count(a)==3):
        return print('Maior possibilidade de ', x , ' maior')
#Chord
def Acorde(note1,note2,note3):
    lista=[note1,note2,note3]
    if lista.count(0)>=2:
        return print('Ou não é um acorde, ou não é um acorde maior natural, ou não é um acorde maior')
    if 1 in lista and 4 not in lista:
        Do(note1,note2,note3)
    elif 2 in lista and 5 not in lista:
        Re(note1,note2,note3)
    elif 3 in lista and 1 not in lista and 6 not in lista:
        Mi(note1,note2,note3)
    elif 4 in lista:
        Fa(note1,note2,note3)
    elif 5 in lista and 1 not in lista:
        Sol(note1,note2,note3)
    elif 6 in lista and 2 not in lista:
        La(note1,note2,note3)
    elif 7 in lista and 3 not in lista and 5 not in lista:
        Si(note1,note2,note3)
        
