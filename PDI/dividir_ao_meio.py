import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/im1.jpg')
imagem_2 = cv2.imread('imagens/im1.jpg')

for y in range(0, imagem.shape[0], 1):  # percorre linhas
    for x in range(0, imagem.shape[1], 1):  # percorre colunas
        imagem[y, int(imagem.shape[1] / 2)] = (0, 255, 255)
        imagem_2[int(imagem.shape[0] / 2), x] = (0, 255, 255)

# cv2.imshow("Imagem modificada", imagem)
cv2.imshow("Imagem modificada", np.hstack([imagem, imagem_2]))
cv2.waitKey(0)
