import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('imagens/im1.jpg', 0)
cv2.imshow('Visualizar imagem', imagem)
cv2.waitKey(0)
cv2.imwrite('imagens_processadas/im1(escala_de_cinza).jpg', imagem)
cv2.destroyAllWindows()
