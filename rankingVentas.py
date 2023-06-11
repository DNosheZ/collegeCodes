N=int(input())
M='El vendedor del mes es'
Vendedores={}
Alias=[]
Puntuacion=[]
while N!=0:
    In=input().split(': ')
    Puntuacion.append(int(In[1]))
    Alias.append(In[0])
    N-=1
for x in range(0,len(Alias)):
    if Alias[x] not in Vendedores:
        Vendedores[Alias[x]]=Puntuacion[x]
    else:
        Vendedores[Alias[x]]+=Puntuacion[x]
print(M,max(Vendedores, key = lambda x: Vendedores[x]))