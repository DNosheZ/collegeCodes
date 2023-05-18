N=int(input('Ingrese el numero de variables a procesar'))
lstVars=[]
l=1
while N!=0:
    P=str(input(f'Ingrese la {str(l)} variable: '))
    lstVars.append(P)
    N-=1
    l+=1
for i in lstVars:#designando una rutina por variable ingresada en la lista previa
    f=''
    lstWord=[]
    m=str(i)
    c=str(i[0])
    m=c.upper()#nos dedicamos a hacer de la primera letra, en la variable tomada, mayuscula
    for k in i:#haremos de la variable una lista de letras
        lstWord.append(k)
    lstWord[0]=m
    for l in lstWord:#asi entre toda la lista hallaremos;
        if l=='_':#las 'serpientes' a eliminar
            t=int(lstWord.index(l))
            a=str(lstWord[t+1])
            h=a.upper()#y hacer de la letra siguiente a la 'serpiente', mayuscula
            lstWord[t+1]=h
            lstWord[t]=''#suprimimos la 'serpiente'
    for b in lstWord:#a partir de la primera letra de la variable rearmamos la variable
        f+=b      
    print(f)