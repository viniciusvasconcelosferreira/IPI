"""
Leitura dos dados RGB no OpenCV é no modelo BGR(Blue,Green and Red)
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/im1.jpg')
(b, g, r) = imagem[0, 0]
print('O pixel (0, 0) tem as seguintes cores:')
print(f'Vermelho: {r}, Verde: {g}, Azul: {b}')
