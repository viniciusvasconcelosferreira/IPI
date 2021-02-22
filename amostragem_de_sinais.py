import numpy as np
from matplotlib import pyplot as plt

# Freqüência do sinal (em Hertz)
fc = 1

# Freqüência de amostragem (em Hertz)
fa = 8

# Período de amostragem (em segundos)
Ta = 1 / fa

# Intervalo de simulação (em segundos)
ti = 0  # Tempo inicial
tf = 1  # Tempo final
t = np.arange(ti, tf, Ta)

tcont = np.arange(ti, tf, (1 / (100 * fa)))  # Simula a função contínua
aux = np.multiply(fc, tcont)
aux_pi = 2 * np.pi
ycont = 3 * np.sin(np.multiply(aux_pi, aux))  # Simula a função contínua

y = 3 * np.sin(2 * np.pi * np.multiply(fc, t))  # Amostragem do sinal

# Mostra a função contínua (simulada) e sobrepõe o sinal em tempo discreto
plt.plot(tcont, ycont)
plt.rcParams.update({'font.size': 14})
plt.stem(t, y)
plt.xlabel('t (s)')
plt.ylabel('y (s)')
plt.title('Amostragem')
plt.legend(('Sinal contínuo', 'Sinal em tempo discreto'))
plt.show()
