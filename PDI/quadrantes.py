"""
Indice que pode ser 0(zero) para a componente azul,
1 (um) para a componente verde e 2(dois) para a componente vermelha
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem_original = cv2.imread('imagens/im1.jpg')
imagem_modificada = cv2.imread('imagens/im1.jpg')

imagem_modificada[0:256, 0:346, 2] = 0
# imagem_modificada[0:altura/2,0:largura/2,indice RGB]
imagem_modificada[0:256, 346:692, 1] = 0
# imagem_modificada[0:altura/2,largura/2:largura_total,indice RGB]
imagem_modificada[256:691, 346:692, 0] = 0
# imagem_modificada[altura/2:altura_total,largura/2:largura_total,indice RGB]

cv2.imshow("Imagem Original / Imagem modificada", np.hstack([imagem_original, imagem_modificada]))
cv2.waitKey(0)
print(
    f'Altura, largura e canais: {imagem_original.shape}')  # A imagem tem 512 pontos em y, 820 em x , e cada ponto contem três bytes
print(f'Total de bytes da imagem: {imagem_original.size}')  # Total de bytes da imagem
print(f'Datatype utilizado: {imagem_original.dtype}')  # cada dado de cor corresponde a um byte
