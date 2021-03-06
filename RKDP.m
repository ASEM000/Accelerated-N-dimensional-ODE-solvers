function [t,y]=RKDP(odefun,ics,h,span,degree)
    
    N= int32( (span(1+1)-span(0+1))/h );
    
    tY = zeros(N+1,degree+1);
    tY(0+1,1+1:end) = ics;

    for  i =1:N
        tY(i+1,0+1) = tY(i,0+1) + h;
        
        k1= odefun(tY(i,0+1)            , tY(i,1+1:end));
        k2= odefun(tY(i,0+1) +h *(1/5)  , tY(i,1+1:end) +h*((k1) *(1/5)        )) ;
        k3= odefun(tY(i,0+1) +h *(3/10) , tY(i,1+1:end) +h*((k1) *(3/40)       + (k2) *(9/40)        ));
        k4= odefun(tY(i,0+1) +h *(4/5)  , tY(i,1+1:end) +h*((k1) *(44/55)      + (k2) *(-56/15)      +(k3)*(32/9)       ));
        k5= odefun(tY(i,0+1) +h *(8/9)  , tY(i,1+1:end) +h*((k1) *(19372/6561) + (k2) *(-25360/2187) +(k3)*(64448/6561) +(k4)*(-212/729) ));
        k6= odefun(tY(i,0+1) +h *(1)    , tY(i,1+1:end) +h*((k1) *(9017/3186)  + (k2) *(-355/33)     +(k3)*(46732/5247) +(k4)*(49/176)   +(k5)*(-5103/18656) ));
        
        tY(i+1,1+1:end) = tY(i,1+1:end) +  h *( k1*(35/384) +k2*(0+1) +k3*(500/1113) +k4*(125/192) +k5*(-2187/6784) +k6*(11/84) );
        
        
        
    end
    
    t =tY(:,0+1);
    y =tY(:,1+1:end);
    
end