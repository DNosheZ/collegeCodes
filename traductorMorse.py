def morse(x):
     Dck={' ':'/','A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','.':'.-.-.-',',':'-.-.--'}
     B=x.upper()
     traduccion=''
     for y in B:
         traduccion+=Dck[y]+' '
     return print(traduccion)
N=int(input())
lst=[]
while N!=0:
     frase=str(input())
     lst.append(frase)
     N-=1
for palabra in lst:
    morse(palabra)
    print('')