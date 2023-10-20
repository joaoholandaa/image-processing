import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2,::2] #diminui a imagem

suave = np.vstack([
np.hstack([imagem,
  cv2.bilateralFilter(imagem, 3, 21, 21)]),
  np.hstack([cv2.bilateralFilter(imagem, 5, 35, 35),
  cv2.bilateralFilter(imagem, 7, 49, 49)]),
  np.hstack([cv2.bilateralFilter(imagem, 9, 63, 63),
  cv2.bilateralFilter(imagem, 11, 77, 77)])
])

cv2.imshow('Imagem original e suavizadas pelo filtro bilateral', suave)
cv2.waitKey(0)