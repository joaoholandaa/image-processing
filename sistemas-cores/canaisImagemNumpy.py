import numpy as np
import cv2

imagem = cv2.imread('hamilton.jpg')

(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)
zeros = np.zeros(imagem.shape[:2], dtype = "uint8")

cv2.imshow('Vermelho', cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow('Verde', cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow('Azul', cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow('Original', imagem)

cv2.waitKey(0)