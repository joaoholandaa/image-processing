import cv2

imagem = cv2.imread('hamilton.jpg')
cv2.imshow('Original', imagem)
flip_horizontal = imagem[::-1, :] #comando equivalente abaixo
#flip_horizontal = cv2.flip(imagem, 1)
cv2.imshow('Flip Horizontal', flip_horizontal)

flip_vertical = imagem[:, ::-1] #comando equivalente abaixo
#flip_vertical = cv2.flip(imagem, 0)
cv2.imshow('Flip Vertical', flip_vertical)

flip_hv = imagem[::-1, ::-1] #comando equivalente abaixo
#flip_hv = cv2.flip(imagem, -1)
cv2.imshow('Flip Horizontal e Vertical', flip_hv)

cv2.waitKey(0)