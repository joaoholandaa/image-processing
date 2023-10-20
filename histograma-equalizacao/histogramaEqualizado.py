from matplotlib import pyplot as plt
import cv2

imagem = cv2.imread('hamilton.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(imagem)

plt.figure()
plt.title('Histograma Equalizado')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de Pixels')
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title('Histograma Original')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de Pixels')
plt.hist(imagem.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()

cv2.imshow('Histograma Original', imagem)
cv2.imshow('Histograma Equalizado', h_eq)

cv2.waitKey(0)