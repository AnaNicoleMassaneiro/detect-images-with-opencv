import cv2

classificadorGato =  cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

imagem = cv2.imread("outros/gato3.jpg")
imageCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deletectados = classificadorGato.detectMultiScale(imageCinza, scaleFactor=1.02)

for (x, y, l, a) in deletectados:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)


cv2.imshow("Faces encontradas", imagem)

cv2.waitKey()