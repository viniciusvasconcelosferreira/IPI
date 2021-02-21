import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem_original = cv2.imread('imagens/im1.jpg')
cv2.imshow("Imagem original", imagem_original)
for y in range(0, imagem_original.shape[0]):  # percorre linhas
    for x in range(0, imagem_original.shape[1]):  # percorre colunas
        imagem_original[y, x] = (x % 256, y % 256, x % 256)
cv2.imshow("Imagem modificada", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
