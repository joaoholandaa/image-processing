import cv2

imagem = cv2.imread('hamilton.jpg')

#cria um retângulo azul por toda a largura da imagem
imagem[30:50, :] = (255, 0, 0)

#cria um quadrado vermelho
imagem[100:150, 50:100] = (0, 0, 255)

#cria um retângulo amarelo por toda a altura da imagem
imagem[:, 200:220] = (0, 255, 255)

#cria um retângulo verde da linha 150 a 300 nas colunas 250 a 350
imagem[150:300, 250:350] = (0, 250, 0)

#cria um quadrado ciano da linha 300 a 400 nas colunas 50 a 150
imagem[300:400, 50:150] = (255, 255, 0)

#cria um quadrado branco
imagem[250:350, 300:400] = (255, 255, 255)

#cria um quadrado preto
imagem[70:100, 300:450] = (0, 0, 0)

cv2.imshow('Imagem alterada',  imagem)
cv2.waitKey(0)