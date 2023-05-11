H=int(input())
M=int(input())
AP=str(input())
F='Faltan'
P='para las 12'
if AP=='am': 
    if H==12: 
        if M==0:
            print(F, 24*60, P) 
        elif 0<M<=59: 
            print(F, int((23*60)+(60-M)), P)
    elif 1<=H<12: 
        if M==0: 
            print(F, int((23-H)*60), P)
        elif 0<M<=59: 
            print(F, int(((24-(H+1))*60)+(60-M)), P)
elif AP=='pm': 
    if H==12: 
        if M==0:
            print(F, int(12*60), P)
        elif 0<M<=59:  
            print(F, int((11*60)+(60-M)), P)
    elif 1<=H<12:  
        if M==0: 
            print(F, (12-H)*60, P)
        elif 1<=M<59: 
            print(F, (12-(H+1))*60+(60-M), P)
