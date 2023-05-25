
lstTxt=open('/haiku.txt','r')
for k in lstTxt: 
    lstP=[]
    lstK=[]
    for h in k:#two lists containing each row
        lstP.append(h)
        lstK.append(h)
    if '\n' in lstP:#the row jump disapear in both list
        lstP.remove('\n')
        lstK.remove('\n')         
    L=len(lstP)#weight of list
    R=L-1    
    for i in range(0,L):
        A=lstK[R]
        lstP[i]=A#the first letter in the row will be the last of it
        R-=1
    f='\n'
    for l in lstP:
        f+=l#starting with the jump of row we recreate the row
    print(f,end='')#printing each encryted row
lstTxt.close()#all the rows encryted & printed? close the data page    
