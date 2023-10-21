import mahotas
import numpy as np
import cv2

imagem = cv2.imread('hamilton.jpg')
imagem = imagem[::2, ::2]
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(imagem, (7,7), 0)
T = mahotas.thresholding.otsu(suave)
temp = imagem.copy()
temp[temp>T] = 255
temp[temp<255] = 0
temp = cv2.bitwise_not(temp)

T = mahotas.thresholding.rc(suave)
temp2 = imagem.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)

resultado = np.vstack([
  np.hstack([imagem, suave]),
  np.hstack([temp, temp2])
])

cv2.imshow("Binarização com método Otsu e Riddler-Calvard", resultado)
cv2.waitKey(0)