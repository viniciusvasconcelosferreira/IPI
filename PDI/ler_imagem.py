"""
Imagens são compostas por canais/dimensões que indicam o padrão RGB de sua composição

Caso a imagem seja preto e branco, haverá somente dois canais.

imagem.shape - imprime uma tupla contendo as informações da imagem lida

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('../imagens/im1.jpg')
cv2.imshow('Visualizar imagem', imagem)
print(f'Altura em pixels: {imagem.shape[0]}')
print(f'Largura em pixels: {imagem.shape[1]}')
print(f'Quantidade de canais: {len(imagem.shape)}')
cv2.waitKey(0)
cv2.destroyAllWindows()
