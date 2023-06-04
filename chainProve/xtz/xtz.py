conversaciones=open('conversaciones.txt','r')
opsMay=['Sin embargo','No obstante','Ahora bien','Aun asi']
opsMn=['sin embargo','no obstante','ahora bien','aun asi']
causMay=['Por tanto','Dado que','Por consiguiente','Asi pues','Por ende']
causMn=['por tanto','dado que','por consiguiente','asi pues','por ende']
Caus='Causativos'
Ops='Opositivos'
for h in conversaciones:
    h=h.replace(',', ' ')
    h=h.replace('.', ' ')
    O=0
    C=0
    for t in opsMay:#veiwing for opositives
        if t in h:
            O+=1
        else:
            pass
    for a in opsMn:#veiwing for opostives
        if a in h:
            O+=1
        else:
            pass 
    for o in causMay:#veiwing for causatives
        if o in h:
            C+=1
        else:
            pass
    for e in causMn:#veiwing for causatives
        if e in h:
            C+=1
        else:
            pass  
    print(Ops,O,Caus,C)#for each causative & opostive founded we count it appearence in the row of words              
conversaciones.close()