import numpy as np
import cv2

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2,::2]
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(imagem, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
resultado = np.vstack([imagem, lap])

cv2.imshow('Filtro Laplaciano', resultado)
cv2.waitKey(0)