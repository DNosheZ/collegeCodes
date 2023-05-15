lstPf1=['ix','us','ic','as','af','','ez','a']#lista de prefijos reconociblos
lstPf2=['is','ax']
lstNames=[]
lstGnt=['Galo','Romano','Godo','Griego','Normando','Breton','Hispano','Indio']#lista de origenes ordenados en el orden de sus prefijos asociados
D='Desconocido'
N=int(input('Ingresa la cantidad de nombres que vamos a evaluar: '))
f=1
while N!=0:#aqui se ingresan los nombres a analizar
    P=str(input(f'Ingresa el {str(f)} nombre a analizar: '))
    lstNames.append(P)
    N-=1
    f+=1
for i in lstNames:
    k=len(i)
    m=i[k-2]+i[k-1]#con este pedazo extraemos el prefijo en el nombre a analizar
    if i[k-1]==lstPf1[7]: #dado que poseemos un prefijo con una letra analizamos si la ultima letra del nombre corresponde a este prefijo para asi nombrarlo
        print(lstGnt[7])
    elif m in lstPf1: #caso cotrario al previo se analiza si el prefijo hallado pertenece a uno de los existentes en la lista
        r=lstPf1.index(m)
        print(lstGnt[r])
    elif (m not in lstPf1) and (m in lstPf2):
        print(lstGnt[5]) #dado que dos prefijos corresponden al mismo origen, se hace un reconocedor preciso para este
    else:#caso contrario a los previos, le origen del nombre es desconocido
        print(D)