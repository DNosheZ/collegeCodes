Dck=[]
Index=[]
N=int(input())
while N!=0:#se ingresa las respuestas de los encuestados
  T=str(input()) #el formato de respuesta es:   
  T=T.split(' ')#[sexo, edad, percepcion del alcalde, calif del 1 al 10 de la pizza]
  T[1]=int(T[1])
  T[3]=int(T[3])
  Dck.append(T)
  N-=1
D=len(Dck)
Dck.sort(key = lambda x: (-x[3],-x[1]))#se organiza la lista en orden descendente, teniendo en cuenta edad y calificacion de la pizza

for e in Dck:
    if e[2] == 'positiva':#si la percepcion del alcalde es positiva, este dato sera mostrado
        e[2] = e[2].upper()
        Index.append(e)
for i in Index:
   print(str(i[1]),i[2],str(i[3]))