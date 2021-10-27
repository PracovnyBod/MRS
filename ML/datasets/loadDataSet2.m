clear all;


load('dataset2.mat')





figure(2)


subplot(4,1,1)

plot(ds2_ventilator(:,1), ds2_ventilator(:,2))

subplot(4,1,2)

plot(ds2_spirala(:,1), ds2_spirala(:,2))

subplot(4,1,3)

plot(ds2_snimac_1(:,1), ds2_snimac_1(:,2))

subplot(4,1,4)

plot(ds2_snimac_2(:,1), ds2_snimac_2(:,2))



writematrix([ds2_ventilator(:,1), ...
             ds2_ventilator(:,2), ...
             ds2_spirala(:,2), ...
             ds2_snimac_1(:,2), ...
             ds2_snimac_2(:,2)], 'dataset2.csv')