
import numpy as np

def RK3n(odefun,ics,h,span,degree):
    
    N= int( (span[1]-span[0])/h )
    
    tY = np.zeros((N+1,degree+1))
    tY[0,1:] = ics
    
    
    for  i in range(N):
        tY[i+1,0] = tY[i,0] + h

        k1= odefun(tY[i,0]        ,tY[i,1:])
        k2= odefun(tY[i,0] +(h/2) ,tY[i,1:] +(h*k1)/2)
        k3= odefun(tY[i,0] +h     ,tY[i,1:] -h*k1 + 2*h*k2 )
        
        tY[i+1,1:] = tY[i,1:] + h*(1/6) * (k1+4*k2+k3)
        
    return tY[:,0],tY[:,1:]
