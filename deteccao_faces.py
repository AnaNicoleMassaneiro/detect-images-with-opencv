import cv2

classificador = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

imagem = cv2.imread("pessoas/pessoas3.jpg")

imageCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imageCinza, scaleFactor=1.09, minNeighbors=9, minSize=(10, 10))

for (x, y, l, a) in facesDetectadas:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)


cv2.imshow("Faces encontradas", imagem)

cv2.waitKey()