from matplotlib import pyplot as plt
import cv2

imagem = cv2.imread('hamilton.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #converte P&B
cv2.imshow('Imagem P&B', imagem)

#função calcHist para calcular o histograma da imagem
h = cv2.calcHist([imagem], [0], None, [256], [0, 256])

plt.figure()
plt.title('Histograma P&B')
plt.xlabel('Intensidade')
plt.ylabel('Qted de pixels')
plt.plot(h)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)