yt = dsolve('D3y + 5.4*D2y + 9.7*Dy + 5.592*y = 2*exp(-1.2*t)','y(0)=1','Dy(0)=1','D2y(0)=1')

ezplot(yt,[0 10])