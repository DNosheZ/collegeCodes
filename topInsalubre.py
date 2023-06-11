a=open('tex.txt','r')
Dck=[]
Top=[]
N=int(input())
while N!=0:
    Emp=str(input())
    Emp=Emp.split()
    Emp[1]=int(Emp[1])
    Emp[2]=int(Emp[2])
    Emp[31]=int(Emp[3])
    Emp[4]=int(Emp[4])
    Dck.append(Emp)
    N-=1
for T in Dck:
    IMC=round(T[1]/(T[2])**2,1)
    T.append(IMC)
for i in Dck:
    if (i[5]>25 and i[3]>100 and i[4]>150):
        Top.append(i)
Top=Top.sort(key = lambda x: -x[5] -x[3] -x[4] -x[0])
L=len(Top)
for h in range(3,L):
    F=Top[h]
    Top=Top.remove(F)
for j in Top:
    print((Top.index(j))+1,j[0],j[5])