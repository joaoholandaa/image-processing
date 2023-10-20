import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2, ::2] #diminui a imagem

suave = np.vstack([
  np.hstack([imagem, cv2.blur(imagem, (3,3))]),
  np.hstack([cv2.blur(imagem, (5,5)), cv2.blur(imagem, (7,7))]),
  np.hstack([cv2.blur(imagem, (9,9)), cv2.blur(imagem, (9,9))])
])

cv2.imshow('Imagens suavizadas (Blur)', suave)
cv2.waitKey(0)