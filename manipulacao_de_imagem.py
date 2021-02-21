import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/im1.jpg')

for altura in range(0, imagem.shape[0]):
    for largura in range(0, imagem.shape[1]):
        imagem[altura, largura] = (255, 0, 0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.imwrite('imagens_processadas/im1(substituicao_por_azul).jpg', imagem)
cv2.destroyAllWindows()
