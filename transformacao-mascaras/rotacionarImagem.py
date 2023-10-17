import cv2 

imagem = cv2.imread('hamilton.jpg')

(alt, lar) = imagem.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro

M = cv2.getRotationMatrix2D(centro, 45, 1.0) #30 graus
imagem_rotacionada = cv2.warpAffine(imagem, M, (lar,alt))

cv2.imshow('Imagem Rotacionada em 45 graus', imagem_rotacionada)
cv2.waitKey(0)