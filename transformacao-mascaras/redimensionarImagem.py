import cv2

imagem = cv2.imread('hamilton.jpg')

cv2.imshow('Original', imagem)

largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao = float(altura/largura)

largura_nova = 320 #em pixels
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)

imagem_redimensionada = cv2.resize(imagem, tamanho_novo, interpolation=cv2.INTER_AREA)

cv2.imshow('Resultado', imagem_redimensionada)
cv2.waitKey(0)