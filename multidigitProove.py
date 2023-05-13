N=int
lstPrima=[1,2,3,4,5]
lstR=[]
M='Multidigito'
NM='No es multidigito'
while N!=0:
    N=int(input())
    if N!=0:
        lstR.append(N)
    else:
        break
for i in lstR:
    Z=0
    k=str(i)
    lstN=[]
    for h in k:
        t=int(h)
        lstN.append(t)
    for m in lstPrima:
        if m in lstN:
            Z+=1
        else:
            Z+=0
    if Z==5:
        print(M)
    else:
        print(NM)