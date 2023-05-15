vocales=['a','e','i','o','u']
C='es panvocalica'
NC='no es panvocalica'
N=int(input('Ingrese la cantidad de palabras a evaluar: '))
palabras=[]
f=1
while N!=0:
    P=str(input(f'Ingrese la {str(f+1)} a analizar: '))
    palabras.append(P)
    N-=1
    f+=1
for i in palabras:
    i.lower()
    lstLt=[]
    Z=0
    for j in i:#para analizar la palabra, habremos de diseccionarla para revisar si posee todas las vocales
        lstLt.append(j)
    for k in vocales:#a traves de la lista de vocales, revisamos que todas estas esten en la lista de letras que conforman la palabra
        if k in lstLt:#si la vocal pertenece a la palabra se suma una a la cuenta
            Z+=1
        else:
            Z+=0
    if Z==5:#si la sumatoria es igual a 5 es porque las 5 vocales estan dentro de la palabra, y se confirma que se panvolica 
        print(i,C)
    else:
        print(i,NC)