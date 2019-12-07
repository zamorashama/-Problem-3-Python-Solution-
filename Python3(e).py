import numpy as np


def Python3(e):
    for n in range(len(e)):
        
        f = np.polyfit(e[:,0], e[:,1],n)
    
        g = np.polyval(f, e[:,0])
        
        P = np.linalg.norm(e[:,1] - g)
        
        x = [n,P]
        
        if n==0:
            
            y = x
            
        elif y[1] >= x[1]:
            
            z = x[0]
            
    P = np.polyfit(e[:,0],e[:,1],z)
    
    print('Coefficients: ',P)