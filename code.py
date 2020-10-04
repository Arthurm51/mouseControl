#importando as libs cv2 e numpy
import cv2
import numpy as np

#abrindo a camera
camera = cv2.VideoCapture(0)

#looping "infinito", até cancelado
while True:
    #pega o frame da camera
    _, frame = camera.read()
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBlue = np.array([255, 255, 204])
    upperBlue = np.array([255, 0, 0])
    mascara = cv2.inRange(frameHsv, lowerBlue, upperBlue)
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)
    frameGray = cv2.cvtColor(resultado, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(frameGray, 3, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (x, y, w, h) = cv2.boundingRect(contorno)
        area = cv2.contourArea(contorno)
        if area > 1000:
            cv2.putText(frame, "Verde Detectado", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
            cv2.rectangle(frame, (5, 40), (400, 100), (0, 255, 255), 2)
            cv2.drawContours(frame, contorno, -1, (0, 0, 0), 5)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(60)
    if key == 27:
        break

cv2.destroyAllWindows()
camera.release()
#