import cv2

classificacaoFace = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
classificacaoOlhos = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

image = cv2.imread("pessoas/faceolho.jpg")
imagemCinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificacaoFace.detectMultiScale(imagemCinza)

for (x, y, l, a) in facesDetectadas:
    image = cv2.rectangle(image, (x, y), (x + l, y + a), (0, 0, 255), 2)
    regiao = image[y:y + a, x:x + l]

    regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    olhosDetectados = classificacaoOlhos.detectMultiScale(regiaoCinzaOlho)
    for (xo, yo, lo, ao) in olhosDetectados:
        cv2.rectangle(regiao, (xo, yo), (xo + lo, yo + ao), (255, 0, 255), 2)
    print(olhosDetectados)


cv2.imshow("Faces encontradas", image)

cv2.waitKey()