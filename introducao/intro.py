#importação das bibliotecas
import cv2

#leitura da imagem com a função imread()
imagem = cv2.imread('hamilton.jpg')

print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])

#mostra a imagem com a função imshow
cv2.imshow('Nome da janela', imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla

'''
Salvar a imagem no disco com a função imwrite()
cv2.imwrite('saida.jpg', imagem)
'''