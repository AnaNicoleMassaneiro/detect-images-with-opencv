import cv2

classificador = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

imagem = cv2.imread("pessoas/beatles.jpg")

imageCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imageCinza)

print(len(facesDetectadas))