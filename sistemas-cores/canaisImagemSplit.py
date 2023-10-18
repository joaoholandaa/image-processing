import cv2

imagem = cv2.imread('hamilton.jpg')

(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)

cv2.imshow('Vermelho', canalVermelho)
cv2.imshow('Verde', canalVerde)
cv2.imshow('Azul', canalAzul)
cv2.waitKey(0)