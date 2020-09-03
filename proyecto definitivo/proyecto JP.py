import random
#crear matriz del usuario
matriz=[]
for i in range(10):
    matriz.append([])
    for x in range(10):
        matriz[i].append(0)
print (*matriz,sep="\n")

partidas_ganadas=0
partidas_perdidas=0
tam_barcos=[2,3,4,5]
total_puntos=14
partida_ganada=False
total_puntos_ene=14
partida_ganada_ene=False

#evaluar la posicion digitada por el usuario
def obtener_posiciones(matriz):
    posicion=input("Digite la posicion inicial \n")
    posfila=ord(posicion[0].lower())-97
    poscolumna=int(posicion[1:])-1
    if matriz[posfila][poscolumna]== 0:
        return [posfila,poscolumna]
    elif (posfila<0 or posfila>10 or poscolumna<0 or poscolumna>10) or matriz[posfila][poscolumna]== 1:
        print("Posicion ocupada o invalida")
        return obtener_posiciones(matriz)

posicion1 = obtener_posiciones(matriz)

#marcar la primera posicion digitada por el usuario
def marcar (matriz,posicion1):
    print(posicion1)
    matriz[posicion1[0]][posicion1[1]] = 1
    print(*matriz,sep="\n")
    return(matriz)
                
matriz = marcar(matriz,posicion1)

def direccion_barco2(matriz,posicion1):
    direccion=int(input("1.izquierda \n2.derecha \n3.arriba \n4.abajo \n"))
    if (direccion==1)and(posicion1[1] - 1 >= 0)and  matriz[posicion1[0]][(posicion1[1])-1] ==0:
        matriz[posicion1[0]][(posicion1[1])-1] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==2)and(posicion1[1] + 1 >= 0)and matriz[posicion1[0]][(posicion1[1])+1] ==0:
        matriz[posicion1[0]][(posicion1[1])+1] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==3)and(posicion1[0] - 1 >= 0)and matriz[posicion1[0]-1][(posicion1[1])] ==0:
        matriz[posicion1[0]-1][(posicion1[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==4)and(posicion1[0] + 1 >= 0)and matriz[posicion1[0]+1][(posicion1[1])]==0:
        matriz[posicion1[0]+1][(posicion1[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    else:
        print ("INVALID_NUMBER")
        return direccion_barco2(matriz,posicion1)


matriz = direccion_barco2(matriz,posicion1)
posicion2 = obtener_posiciones(matriz)
print(posicion2)
matriz = marcar (matriz,posicion2)

def direccion_barco_3(matriz,posicion2):
    direccion=int(input("1.izquierda \n2.derecha \n3.arriba \n4.abajo \n"))
    if (direccion==1)and(posicion1[1] - 2 >= 0)and  matriz[posicion2[0]][(posicion2[1])-1] ==0 and  matriz[posicion2[0]][(posicion2[1])-2]==0 :
        matriz[posicion2[0]][(posicion2[1])-1] += 1
        matriz[posicion2[0]][(posicion2[1])-2] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==2) and (posicion1[1] + 2 >= 0) and matriz[posicion2[0]][(posicion2[1])+2] == 0 and matriz[posicion2[0]][(posicion2[1])+1] == 0 :
        matriz[posicion2[0]][(posicion2[1])+1] += 1
        matriz[posicion2[0]][(posicion2[1])+2] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==3)and(posicion1[0] - 2 >= 0) and matriz[posicion2[0]-2][(posicion2[1])] == 0 and matriz[posicion2[0]-1][(posicion2[1])] == 0:
        matriz[posicion2[0]-1][(posicion2[1])] += 1
        matriz[posicion2[0]-2][(posicion2[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==4)and(posicion1[0] + 2 >= 0)and matriz[posicion2[0]+1][(posicion2[1])] == 0 and matriz[posicion2[0]+2][(posicion2[1])] == 0:
        matriz[posicion2[0]+1][(posicion2[1])] += 1
        matriz[posicion2[0]+2][(posicion2[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    else:
        print ("INVALID_NUMBER")
        return direccion_barco_3(matriz,posicion2)

matriz = direccion_barco_3(matriz,posicion2)
posicion3 = obtener_posiciones(matriz)
matriz = marcar(matriz,posicion3)

def direccion_barco_4(matriz,posicion2):
    direccion=int(input("1.izquierda \n2.derecha \n3.arriba \n4.abajo \n"))
    if (direccion==1)and(posicion1[1] - 3 >= 0)and matriz[posicion2[0]][(posicion2[1])-1] ==0 and matriz[posicion2[0]][(posicion2[1])-2] ==0 and matriz[posicion2[0]][(posicion2[1])-3] ==0:
        matriz[posicion2[0]][(posicion2[1])-1] += 1
        matriz[posicion2[0]][(posicion2[1])-2] += 1
        matriz[posicion2[0]][(posicion2[1])-3] += 1
        print(*matriz,sep="\n")
        return matriz

    elif (direccion==2) and (posicion1[1] + 3 >= 0) and matriz[posicion2[0]][(posicion2[1])+1] == 0 and matriz[posicion2[0]][(posicion2[1])+2] == 0 and matriz[posicion2[0]][(posicion2[1])+3] ==0:
        matriz[posicion2[0]][(posicion2[1])+1] += 1
        matriz[posicion2[0]][(posicion2[1])+2] += 1
        matriz[posicion2[0]][(posicion2[1])+3] += 1
        print(*matriz,sep="\n")
        return matriz

    elif (direccion==3)and(posicion1[0] - 3 >= 0)and matriz[posicion2[0]-1][(posicion2[1])] ==0 and matriz[posicion2[0]-2][(posicion2[1])] == 0 and matriz[posicion2[0]-3][(posicion2[1])] == 0:
        matriz[posicion2[0]-1][(posicion2[1])] += 1
        matriz[posicion2[0]-2][(posicion2[1])] += 1
        matriz[posicion2[0]-3][(posicion2[1])] += 1
        print(*matriz,sep="\n")
        return matriz

    elif (direccion==4)and(posicion1[0] + 3 >= 0)and matriz[posicion2[0]+1][(posicion2[1])] == 0 and matriz[posicion2[0]+2][(posicion2[1])] == 0 and matriz[posicion2[0]+3][(posicion2[1])] ==0:
        matriz[posicion2[0]+1][(posicion2[1])] += 1
        matriz[posicion2[0]+2][(posicion2[1])] += 1
        matriz[posicion2[0]+3][(posicion2[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    else:
         print ("INVALID_NUMBER")
         direccion_barco_4(matriz,posicion3)


matriz = direccion_barco_4(matriz,posicion3)
posicion40 = obtener_posiciones(matriz)
matriz = marcar(matriz,posicion40)

def direccion_barco_5(matriz,posicion1):
    direccion=int(input("1.izquierda \n2.derecha \n3.arriba \n4.abajo \n"))
    if (direccion==1)and(posicion1[1] - 4 >= 0)and matriz[posicion1[0]][(posicion1[1])-1] == 0 and matriz[posicion1[0]][(posicion1[1])-2] == 0 and matriz[posicion1[0]][(posicion1[1])-3] == 0 and matriz[posicion1[0]][(posicion1[1])-4] == 0:
        matriz[posicion1[0]][(posicion1[1])-1] += 1
        matriz[posicion1[0]][(posicion1[1])-2] += 1
        matriz[posicion1[0]][(posicion1[1])-3] += 1
        matriz[posicion1[0]][(posicion1[1])-4] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==2)and (posicion1[1] + 4 >= 0)and matriz[posicion1[0]][(posicion1[1])+1] == 0 and matriz[posicion1[0]][(posicion1[1])+3] ==0 and matriz[posicion1[0]][(posicion1[1])+2] ==0 and matriz[posicion1[0]][(posicion1[1])+1] ==0:
        matriz[posicion1[0]][(posicion1[1])+1] += 1
        matriz[posicion1[0]][(posicion1[1])+2] += 1
        matriz[posicion1[0]][(posicion1[1])+3] += 1
        matriz[posicion1[0]][(posicion1[1])+4] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==3)and(posicion1[0] - 4 >= 0)and matriz[posicion1[0]-1][(posicion1[1])]== 0 and  matriz[posicion1[0]-2][(posicion1[1])] == 0 and matriz[posicion1[0]-3][(posicion1[1])] == 0 and matriz[posicion1[0]-4][(posicion1[1])] == 0:
        matriz[posicion1[0]-1][(posicion1[1])] += 1
        matriz[posicion1[0]-2][(posicion1[1])] += 1
        matriz[posicion1[0]-3][(posicion1[1])] += 1
        matriz[posicion1[0]-4][(posicion1[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    elif (direccion==4)and(posicion1[0] + 4 >= 0) and matriz[posicion1[0]+1][(posicion1[1])]== 0 and matriz[posicion1[0]+2][(posicion1[1])] == 0 and matriz[posicion1[0]+3][(posicion1[1])] == 0 and matriz[posicion1[0]+4][(posicion1[1])] == 0:
        matriz[posicion1[0]+1][(posicion1[1])] += 1
        matriz[posicion1[0]+2][(posicion1[1])] += 1
        matriz[posicion1[0]+3][(posicion1[1])] += 1
        matriz[posicion1[0]+4][(posicion1[1])] += 1
        print(*matriz,sep="\n")
        return matriz
    else:
        print ("INVALID_NUMBER")
        return direccion_barco_5(matriz,posicion1)

matriz = direccion_barco_5(matriz,posicion40)

#pedir una posicion enemiga con el random
def pos_enemiga (matriz_enemiga):
    A = random.randint(0,9)
    B = random.randint(0,9)
    return [A,B]

#marcar el primer punto de la enemiga
def marcar_enemiga (matriz_enemiga, C):
    matriz_enemiga[C[0]][C[1]] = 1
    return(matriz_enemiga)


#pedir una direccion con el random
def direcciones():
    direccion = random.randint(1,4)
    return direccion

#valida si la posicion es correcta
def isValid(n,i, j, k):
    global matriz_enemiga
    """
    True if is a valid position, False else
    """
    ans = None
    if(n == 1):
        ans = (j-k + 1>= 0)
        if(ans):
            for e in range(j,j-k,-1):
                ans = ans and (matriz_enemiga[i][e] == 0)
    elif(n == 2):
        ans = (j+k-1<10)
        if(ans):
            for e in range(j,j+k):
                ans = ans and (matriz_enemiga[i][e] == 0)
    elif(n == 3):
        ans = (i-k+1>=0)
        if(ans):
            for e in range(i,i-k,-1):
                ans = ans and (matriz_enemiga[e][i] == 0)
    else:
        ans = (i+k-1<10)
        if(ans):
            for e in range(i,i+k):
                ans = ans and (matriz_enemiga[e][i] == 0)
    return ans

#ubica los barcos enemigos
def barcoG(k):
    global matriz_enemiga
    C = pos_enemiga (matriz_enemiga)
    N = direcciones()
    i=C[0]
    j=C[1]
    while not(isValid(N, i, j, k)):
        N = direcciones()
        C = pos_enemiga (matriz_enemiga)
        N = direcciones()
        i=C[0]
        j=C[1]
    if(N == 1):
        for e in range(j,j-k,-1):
            matriz_enemiga[i][e] = 1
    elif(N == 2):
        for e in range(j,j+k):
            matriz_enemiga[i][e] = 1
    elif(N == 3):
        for e in range(i,i-k,-1):
            matriz_enemiga[e][i] = 1
    else:
        for e in range(i,i+k):
            matriz_enemiga[e][i] = 1
matriz_enemiga= [[0 for i in range(10)] for i in range(10)]
for i in range(2,6):
    barcoG(i)
   

#hace una copia de las matrices 
copia_matriz_enemiga=[]
temp = []
for i in range (len(matriz_enemiga)):
    for j in range (len(matriz_enemiga[i])):
        temp.append(matriz_enemiga[i][j])
    copia_matriz_enemiga.append(temp)
    temp=[]

copia_matriz=[]
tempo = []
for i in range (len(matriz)):
    for j in range (len(matriz[i])):
        tempo.append(matriz[i][j])
    copia_matriz.append(tempo)
    tempo=[]
    

print("--------------------------------------------------------------")
#pide la posicion del disparo
def obtener_posiciones_disparo(copia_matriz_enemiga):
    posicion=input("Digite la posicion del disparo \n")
    posfila=ord(posicion[0].lower())-97
    poscolumna=int(posicion[1:])-1
    return [posfila,poscolumna]
    
#marca el disapro en la matriz de disparos
def marcar_disparo (copia_matriz_enemiga,disparo):
    global total_puntos
    global partida_ganada
    global partidas_ganadas
    matriz_disparo[disparo[0]][disparo[1]] = 2
    if (copia_matriz_enemiga[disparo[0]][disparo[1]] ==1):
        copia_matriz_enemiga[disparo[0]][disparo[1]]=0 
        print ("le has dado a un barco")
        total_puntos=total_puntos-1
        print ("ubicaciones restantes por encontrar: ",total_puntos)
        if total_puntos==0:
            print ("ganaste")
            partida_ganada=True
            partidas_ganadas=partidas_ganadas+1
            print("total partidas ganadas:",partidas_ganadas)
    print(*matriz_disparo,sep="\n")
    return(copia_matriz_enemiga)


#disparo enemigo
def pos_enemiga_disparo (matriz):
    A = random.randint(0,9)
    B = random.randint(0,9)
    return [A,B]
D=pos_enemiga_disparo (matriz)

#marca  el disparo enemigo
def marcar_enemiga_disparo (copia_matriz, D):
    global total_puntos_ene
    global partida_ganada_ene
    global partidas_perdidas
    if (copia_matriz[D[0]][D[1]] ==1):
        copia_matriz[D[0]][D[1]]=0 
        print ("la maquina le ha dado a un barco")
        total_puntos_ene=total_puntos_ene-1
        print ("ubicaciones restantes por encontrar la maquina: ",total_puntos_ene)
        if total_puntos_ene==0:
            print ("perdiste ha ganado la maquina")
            partida_ganada_ene=True
            partidas_perdidas=partidas_perdidas+1
            print("total partidas perdidas:",partidas_perdidas)
    return copia_matriz


#crea la matriz de disparos
matriz_disparo=[]
for i in range(10):
    matriz_disparo.append([])
    for x in range(10):
        matriz_disparo[i].append(0)
print (*matriz_disparo,sep="\n")

#while para que se disparen hasta que alguno gane
while not partida_ganada or not partida_ganada_ene:
    disparo = obtener_posiciones_disparo(matriz_enemiga)
    disparo_enemigos= marcar_disparo (copia_matriz_enemiga, disparo)
    disparo_enem = pos_enemiga_disparo (matriz)
    matriz_enemigo = marcar_enemiga_disparo (matriz, disparo_enem)
print("FUERA DEL CICLO")
