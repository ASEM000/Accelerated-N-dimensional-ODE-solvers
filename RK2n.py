
import numpy as np

def RK2n(odefun,ics,h,span,degree):
    
    N= int( (span[1]-span[0])/h )
    
    tY = np.zeros((N+1,degree+1))
    tY[0,1:] = ics
    
    
    for  i in range(N):
        tY[i+1,0] = tY[i,0] + h

        k1= odefun(tY[i,0],tY[i,1:])
        k2= odefun(tY[i,0] +h,tY[i,1:] +(h*k1))
        
        tY[i+1,1:] = tY[i,1:] + h*(1/2) * (k1+k2)
        
    return tY[:,0],tY[:,1:]
