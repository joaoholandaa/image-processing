import cv2

imagem = cv2.imread('hamilton.jpg')
cv2.imshow('Original', imagem)

imagem_redimensionada = imagem[::2, ::2]
cv2.imshow('Imagem redimensionada', imagem_redimensionada)

cv2.waitKey(0)