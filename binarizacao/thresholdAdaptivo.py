import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2, ::2]
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(imagem, (7,7), 0)
bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY_INV, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY_INV, 21, 5)

resultado = np.vstack([
  np.hstack([imagem, suave]),
  np.hstack([bin1, bin2])
])

cv2.imshow('Binarização adaptiva da imagem', resultado)
cv2.waitKey(0)