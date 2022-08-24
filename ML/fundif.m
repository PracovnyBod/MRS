function dQ = fundif(t,x);

R = 10^6;
C = 10^(-6);

Q = x;

dQ = -(1/(R*C)) * Q;
