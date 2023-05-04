A=float(input())
B=float(input())
C=float(input())
L='es la mediana'
if C<=A<=B or B<=A<=C:
    print(A, L)
elif A<=B<=C or C<=B<=A:
    print(B, L)
elif A<=C<=B or B<=C<=A:
    print (C, L)
