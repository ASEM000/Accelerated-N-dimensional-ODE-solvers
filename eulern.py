
from numba import jit
import numpy as np

def eulern(odefun,ics,h,span,degree):
    
    N= int( (span[1]-span[0])/h )
    
    tY = np.zeros((N+1,degree+1))
    tY[0,1:] = ics

    for  i in range(N):
        tY[i+1,0] = tY[i,0] + h
        tY[i+1,1:] = tY[i,1:] + h * odefun(tY[i,0],tY[i,1:])
        
    return tY[:,0],tY[:,1:]
