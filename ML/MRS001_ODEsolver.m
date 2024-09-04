
Q_0 = 2 * 10^(-6);

[t,y] = ode45('fundif',[0 5],[Q_0]);

plot(t,y)


