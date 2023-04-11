# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
 # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print(cv2.__version__)

imagem = cv2.imread('Frx_nG6XsAEb1y_.jpeg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow("CINZA", imagemCinza)
cv2.waitKey()