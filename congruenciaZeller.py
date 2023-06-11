N=int(input())
def Zeller(x):
    y=x[2]
    d=x[0]
    Meses={'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12,'enero':13,'febrero':14}
    dia={0:'sabado',1:'domingo',2:'lunes',3:'martes',4:'miercoles',5:'jueves',6:'viernes'}
    if x[1]=='enero' or x[1]=='febrero':
        y-=1
    m=Meses[x[1]]
    Congruencia=(d+((13*(m+1)//5)+y+(y//4)-(y//100)+(y//400)))%7
    return print(dia[Congruencia])
fechas=[]
for i in range(N):
    In=input().split('-')
    In[0]=int(In[0])
    In[2]=int(In[2])
    fechas.append(In)
for fecha in fechas:
    Zeller(fecha)