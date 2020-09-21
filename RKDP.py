
from numba import jit
import numpy as np

@jit(nopython=True)
def RKDP(odefun,ics,h,span,degree):
    
    N= int( (span[1]-span[0])/h )
    
    tY = np.zeros((N+1,degree+1))
    tY[0,1:] = ics
    
    K = np.zeros((N,6))
    
    for  i in range(N):
        tY[i+1,0] = tY[i,0] + h
        
        k1= odefun(tY[i,0]            , tY[i,1:])
        k2= odefun(tY[i,0] +h *(1/5)  , tY[i,1:] +h*((k1) *(1/5)        )) 
        k3= odefun(tY[i,0] +h *(3/10) , tY[i,1:] +h*((k1) *(3/40)       + (k2) *(9/40)        ))
        k4= odefun(tY[i,0] +h *(4/5)  , tY[i,1:] +h*((k1) *(44/55)      + (k2) *(-56/15)      +(k3)*(32/9)       ))
        k5= odefun(tY[i,0] +h *(8/9)  , tY[i,1:] +h*((k1) *(19372/6561) + (k2) *(-25360/2187) +(k3)*(64448/6561) +(k4)*(-212/729) ))
        k6= odefun(tY[i,0] +h *(1)    , tY[i,1:] +h*((k1) *(9017/3186)  + (k2) *(-355/33)     +(k3)*(46732/5247) +(k4)*(49/176)   +(k5)*(-5103/18656) ))
        
        tY[i+1,1:] = tY[i,1:] +  h *( k1*(35/384) +k2*(0) +k3*(500/1113) +k4*(125/192) +k5*(-2187/6784) +k6*(11/84) )
        
       
    return tY[:,0],tY[:,1:]
