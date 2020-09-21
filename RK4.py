
from numba import jit
import numpy as np

@jit(nopython=True)
def RK4(odefun,ics,h,span,degree):
    
    N= int( (span[1]-span[0])/h )
    
    tY = np.zeros((N+1,degree+1))
    tY[0,1:] = ics
    
    
    for  i in range(N):
        tY[i+1,0] = tY[i,0] + h

        k1= odefun(tY[i,0]       , tY[i,1:])
        k2= odefun(tY[i,0] +(h/2), tY[i,1:] +(h*k1)/2 )
        k3= odefun(tY[i,0] +(h/2), tY[i,1:] +(h*k2)/2)
        k4= odefun(tY[i,0] +(h)  , tY[i,1:] +(h*k3))
        
        tY[i+1,1:] = tY[i,1:] + h*(1/6) * (k1+2*k2+2*k3+k4)
        
    return tY[:,0],tY[:,1:]
