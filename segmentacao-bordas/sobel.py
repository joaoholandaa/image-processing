import numpy as np
import cv2

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2,::2]
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(imagem, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(imagem, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

resultado = np.vstack([
  np.hstack([imagem, sobelX]),
  np.hstack([sobelY, sobel])
])

cv2.imshow('Sobel', resultado)
cv2.waitKey(0)