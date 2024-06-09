import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while(True):
    success, imagem = webcam.read()
    coordenadas, imgagem_maos = rastreador.findHands(imagem)
    cv2.imshow("Projeto", imagem)

    if(cv2.waitKey(1) != -1):
        break

webcam.release()
cv2.destroyAllWindows()