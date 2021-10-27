clear all;


load('dataset4.mat')



figure(4)


subplot(4,1,1)

plot(ds4_ventilator(:,1), ds4_ventilator(:,2))

subplot(4,1,2)

plot(ds4_spirala(:,1), ds4_spirala(:,2))

subplot(4,1,3)

plot(ds4_snimac_1(:,1), ds4_snimac_1(:,2))

subplot(4,1,4)

plot(ds4_snimac_2(:,1), ds4_snimac_2(:,2))

writematrix([ds4_ventilator(:,1), ...
             ds4_ventilator(:,2), ...
             ds4_spirala(:,2), ...
             ds4_snimac_1(:,2), ...
             ds4_snimac_2(:,2)], 'dataset4.csv')

