import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2,::2] #diminui a imagem

suave = np.vstack([
np.hstack([imagem,
  cv2.medianBlur(imagem, 3)]),
  np.hstack([cv2.medianBlur(imagem, 5),
  cv2.medianBlur(imagem, 7)]),
  np.hstack([cv2.medianBlur(imagem, 9),
  cv2.medianBlur(imagem, 11)]),
])

cv2.imshow("Imagem original e suavizadas pela mediana", suave)
cv2.waitKey(0)