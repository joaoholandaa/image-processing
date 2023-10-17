import cv2 

imagem = cv2.imread('hamilton.jpg')

recorte = imagem[300:400, 300:400]

cv2.imshow('Recorte da imagem', recorte)
cv2.waitKey(0)