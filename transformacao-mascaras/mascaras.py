import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
cv2.imshow('Original', imagem)

mascara = np.zeros(imagem.shape[:2], dtype = 'uint8')
(cX, cY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 255, -1)
imagem_com_mascara = cv2.bitwise_and(imagem, imagem, mask=mascara)

cv2.imshow('Máscara aplicada à imagem', imagem_com_mascara)
cv2.waitKey(0)

'''import cv2
import numpy as np

imagem = cv2.imread('hamilton.jpg')
cv2.imshow("Original", imagem)

mascara = np.zeros(imagem.shape[:2], dtype = "uint8")
(cX, cY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 180, 255, 70)
cv2.circle(mascara, (cX, cY), 70, 255, -1)
cv2.imshow("Máscara", mascara)

imagem_com_mascara = cv2.bitwise_and(imagem, imagem, mask = mascara)
cv2.imshow("Máscara aplicada à imagem", imagem_com_mascara)
cv2.waitKey(0)'''