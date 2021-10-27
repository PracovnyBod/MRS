clear all;


load('dataset1.mat')




figure(1)


subplot(4,1,1)

plot(ds1_ventilator(:,1), ds1_ventilator(:,2))

subplot(4,1,2)
 
plot(ds1_ventilator(:,1), ds1_spirala(:,2))

subplot(4,1,3)

plot(ds1_snimac_1(:,1), ds1_snimac_1(:,2))


subplot(4,1,4)

plot(ds1_snimac_2(:,1), ds1_snimac_2(:,2))




%%
 
pocitadlo = 1;

for konecnecasy = 60:60:660

maska = (ds1_snimac_2(:,1) > (konecnecasy - 30)) & (ds1_snimac_2(:,1) < konecnecasy);

subplot(4,1,4)
hold on
plot(ds1_snimac_2(maska,1), ds1_snimac_2(maska,2), 'r', 'LineWidth', 2 )
hold off

ustaleneVystupy(pocitadlo) = mean( ds1_snimac_2(maska,2)  );
ustaleneVstupy(pocitadlo) = mean( ds1_spirala(maska,2)  );

pocitadlo = pocitadlo + 1;

end

[ustaleneVstupy' ustaleneVystupy']




%%
 
figure(666)

plot(ustaleneVstupy, ustaleneVystupy, 'r+')






polynom = polyfit(ustaleneVstupy,ustaleneVystupy,4);

tukreslit = [0:0.1:10];
kreslipriamka = polyval(polynom,tukreslit);

hold on
plot(tukreslit, kreslipriamka, 'b-')
hold off






