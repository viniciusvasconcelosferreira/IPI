import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/im1.jpg')
for y in range(0, imagem.shape[0], 1):  # percorre as linhas
    for x in range(0, imagem.shape[1], 1):  # percorre as colunas
        imagem[y, x] = (0, (x * y) % 256, 0)  # (B,G,R)
        # imagem[y, x] = ((x * y) % 256, (x * y) % 256, (x * y) % 256)  # (B,G,R)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
