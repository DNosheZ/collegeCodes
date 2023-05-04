def A(m,n):
    if m==0:
        h=n+1
    elif m>0 and n==0:
        h=A(m-1,1)
    elif m>0 and n>0:
        h=A(m-1,A(m,n-1))
    return h
Alfa=int(input())
Beta=Alfa
P=int
lstm=[]
lstn=[]
while Alfa!=0:
    M=int(input())
    if 0<=M<=3:
        lstm.append(M)
    N=int(input())
    if 0<=N<=7*(4-M)**2:
        lstn.append(N)
    Alfa-=1
for i in range(0,Beta):
    b=lstm[i]
    y=lstn[i]
    G=A(b,y)
    print(G)
