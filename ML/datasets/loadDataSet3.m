clear all;


load('dataset3.mat')





figure(3)


subplot(4,1,1)

plot(ds3_ventilator(:,1), ds3_ventilator(:,2))

subplot(4,1,2)

plot(ds3_spirala(:,1), ds3_spirala(:,2))

subplot(4,1,3)

plot(ds3_snimac_1(:,1), ds3_snimac_1(:,2))

subplot(4,1,4)

plot(ds3_snimac_2(:,1), ds3_snimac_2(:,2))


writematrix([ds3_ventilator(:,1), ...
             ds3_ventilator(:,2), ...
             ds3_spirala(:,2), ...
             ds3_snimac_1(:,2), ...
             ds3_snimac_2(:,2)], 'dataset3.csv')