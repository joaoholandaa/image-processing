from matplotlib import pyplot as plt
import cv2

imagem = cv2.imread('hamilton.jpg')
cv2.imshow('Imagem Colorida', imagem)

#Separa os canais
canais = cv2.split(imagem)
cores = ('b', 'g', 'r')

plt.figure()
plt.title('Histograma Colorido')
plt.xlabel('Intensidade')
plt.ylabel('Número de Pixels')
for (canal, cor) in zip(canais, cores):
  #este loop executa 3 vezes, um para cada canal
  hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
  plt.plot(hist, color = cor)
  plt.xlim([0, 256])
plt.show()