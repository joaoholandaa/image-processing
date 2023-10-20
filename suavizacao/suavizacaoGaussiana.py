import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2,::2] #diminui a imagem

suave = np.vstack([
  np.hstack([imagem,
  cv2.GaussianBlur(imagem, ( 3, 3), 0)]),
  np.hstack([cv2.GaussianBlur(imagem, ( 5, 5), 0),
  cv2.GaussianBlur(imagem, ( 7, 7), 0)]),
  np.hstack([cv2.GaussianBlur(imagem, ( 9, 9), 0),
  cv2.GaussianBlur(imagem, (11, 11), 0)]),
])

cv2.imshow('Imagem original e suavizadas pelo filtro Gaussiano', suave)
cv2.waitKey(0)