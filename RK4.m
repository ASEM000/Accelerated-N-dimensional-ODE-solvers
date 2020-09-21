function [t,y]=RK4(odefun,ics,h,span,degree)
    
    N= int32( (span(1+1)-span(0+1))/h );
    
    tY = zeros(N+1,degree+1);
    tY(0+1,1+1:end) = ics;

    for  i =1:N
        tY(i+1,0+1) = tY(i,0+1) + h;
        
        k1= odefun(tY(i,0+1)       , tY(i,1+1:end));
        k2= odefun(tY(i,0+1) +(h/2), tY(i,1+1:end) +(h*k1)/2 );
        k3= odefun(tY(i,0+1) +(h/2), tY(i,1+1:end) +(h*k2)/2);
        k4= odefun(tY(i,0+1) +(h)  , tY(i,1+1:end) +(h*k3));
        
        tY(i+1,1+1:end) = tY(i,1+1:end) + h*(1/6) * (k1+2*k2+2*k3+k4);
        
        
    end
    
    t =tY(:,0+1);
    y =tY(:,1+1:end);
    
end