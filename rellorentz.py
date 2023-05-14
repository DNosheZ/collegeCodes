def function(x):
    from math import sqrt
    return sqrt(2+5*x)

def gunction(x):
    return (4+x)**3

lst=[]
P=int
while P!=0:
    P=int(input())
    if P!=0:
        lst.append(P)
for i in lst:
    if i%2==0:
        print(function(gunction(i)))
    if i%2!=0:
        print(gunction(function(i)))
    