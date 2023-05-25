cadena=open('cadena.txt', 'r')#from our library we export the main data
CC='cadena completa'
CR='cadena rota'
for a in cadena:#we review each row
    lstCd=[]
    G=0
    for b in a:
        lstCd.append(b)
        if b==' ':#watching for spaces
            G+=1
        elif b=='\n':
            lstCd.remove(b)#eliminate jump of rows, isn't necesary '\/0_0\/'
    D=int
    H=0
    L=len(lstCd)
    for c in range(0,L):
        k=lstCd[c]
        if k==' ':#where the previos word last 2  letters union & next word firts 2  letters union are the same
            E=lstCd[c-2]+lstCd[c-1]
            F=lstCd[c+1]+lstCd[c+2]
            if E==F:#if they are, we have a ring for the chain
                H+=1
            elif E!=F:#if not, maybe the previos word last  3 letters union & next word firts 3  letters union art the same
                I=lstCd[c-3]+lstCd[c-2]+lstCd[c-1]
                J=lstCd[c+1]+lstCd[c+2]+lstCd[c+3]
                if I==J:
                    H+=1
                else:
                    H+=0 #else, we start breaking the chain of simiar lastters/initial
        
    if G==H: #we say that the chain is complete, if we have many rings has spaces between rows
        print(CC)
    else:#we have a broken chain
        print(CR)
cadena.close#closing page of library