%%%%%%%%%%%%%%%%%%%%%%%%
% Amostragem de Sinais %
%%%%%%%%%%%%%%%%%%%%%%%%

clear all;
close all;
clc;

% Freq��ncia do sinal (em Hertz)
fc = 1;

% Freq��ncia de amostragem (em Hertz)
fa = 8;

% Per�odo de amostragem (em segundos)
Ta = 1/fa;

% Intervalo de simula��o (em segundos)
ti = 0;  % Tempo inicial
tf = 1;  % Tempo final
t = ti:Ta:tf;

% Simula a fun��o cont�nua
tcont = ti:1/(100*fa):tf;
ycont = 3*sin(2*pi*fc.*tcont);

% Amostragem do sinal
y = 3*sin(2*pi*fc.*t);

% Mostra a fun��o cont�nua (simulada) e
% sobrep�e o sinal em tempo discreto
set(gca,'FontSize',14)
h = plot(tcont, ycont)
set(h,'LineWidth',1)
hold on
h = stem(t,y,'or','LineWidth',1,'MarkerEdgeColor','k','MarkerFaceColor','g')
xlabel('t (s)')
ylabel('y(t)')
title('Amostragem')
h = legend('Sinal cont�nuo', 'Sinal em tempo discreto')
set(h,'FontSize',12);
grid on


