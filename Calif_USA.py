N=float(input())
Perc='El porcentaje'
Cor='corresponde a la calificacion'
if N>=90:
    C='A'
elif 90>N>=80:
    C='B'
elif 80>N>=70:
    C='C'
elif 70>N>=60:
    C='D'
elif 60>N>=40:
    C='E'
elif 40>N:
    C='F'
print(Perc, N, Cor, C)
