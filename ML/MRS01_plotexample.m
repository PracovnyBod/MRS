% Parametre
R = 10^6;
C = 10^-6;
Q_0 = 2*10^-6;


% Súradnice bodov na x osi
plotData_x = 0:0.1:5;

% Výpočet hodnôt na y osi v zmysle danej časovej funkcie
plotData_y = Q_0 * exp( ( -1.0/(R*C)) * plotData_x );

% Kreslenie grafu
plot(plotData_x,plotData_y)
xlabel('čas [sec]')
ylabel('Q [Coulomb]')



