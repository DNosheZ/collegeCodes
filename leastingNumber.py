lst=[]
lst2=[]
N=int(input())
L='La ficha faltante es la'
K=N-1
M=int
D=N
while K!=0:
    M=int(input())
    if K!=0:
        lst.append(M)
    else:
        continue
    K-=1
while D!=0:
    if D!=0:
        lst2.append(D)
    else:
        continue
    D-=1
for i in range(1,(N+1)): #the numbers that belongs in the list are yet prestablished
    if i in lst:#from a list we find the number that doesnt belongs there
        continue
    else:
        A=i
        break
print(L,A)