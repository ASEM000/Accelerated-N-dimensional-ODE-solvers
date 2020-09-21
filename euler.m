function [t,y]=euler(odefun,ics,h,span,degree)
    
    N= int32( (span(1+1)-span(0+1))/h );
    
    tY = zeros(N+1,degree+1);
    tY(0+1,1+1:end) = ics;
    
    for  i =1:N
        tY(i+1,0+1) = tY(i,0+1) + h;
        tY(i+1,1+1:end) = tY(i,1+1:end) + h * odefun(tY(i,0+1),tY(i,1+1:end));
    end
    
    t =tY(:,0+1);
    y =tY(:,1+1:end);
    
end