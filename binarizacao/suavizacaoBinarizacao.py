import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem_redimensionada = imagem[::2, ::2]
imagem_cinza = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(imagem_cinza, (7,7), 0) #aplica blur
(T, bin) = cv2.threshold(suave, 100, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 100, 255, cv2.THRESH_BINARY_INV)

resultado = np.vstack([
  np.hstack([suave, bin]),
  np.hstack([binI, cv2.bitwise_and(imagem_cinza, imagem_cinza, mask=binI)])
])

cv2.imshow('Binarização da imagem', resultado)
cv2.waitKey(0)