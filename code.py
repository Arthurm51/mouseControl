#importando as libs cv2 e numpy
from cv2 import cv2
import numpy as np

#abrindo a camera
camera = cv2.VideoCapture(0)

#looping "infinito", até cancelado
while True:
    #pega o frame da camera
    _, frame = camera.read()
    #transforma o frame em formato HSV
    frameHsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #declarações das variaveis da cor amarela
    lowerYellow = np.array([19, 135, 97])
    upperYellow = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor amarela no frame
    mascaraYellow = cv2.inRange(frameHsv, lowerYellow, upperYellow)
    #devolve a cor amarela apenas
    resultadoYellow = cv2.bitwise_and(frame, frame, mask=mascaraYellow)
    #deixa a imagem em tons de cinza
    frameGrayYellow = cv2.cvtColor(resultadoYellow, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshYellow = cv2.threshold(frameGrayYellow, 3, 255, cv2.THRESH_BINARY)
    #faz o contorno do objeto amarelo
    contornosYellow, _ = cv2.findContours(
        threshYellow, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #for para trabalhar com os contornos
    for contornoYellow in contornosYellow:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (x, y, w, h) = cv2.boundingRect(contornoYellow)
        #define a variavel "area" com os contornos
        areaYellow = cv2.contourArea(contornoYellow)
        #faz alguma coisa se a area for maior que 1000
        if areaYellow > 1000:
            pass

    #declarações das variaveis da cor verde
    lowerGreen = np.array([50, 68, 68])
    upperGreen = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor verde no frame
    mascaraGreen = cv2.inRange(frameHsv, lowerGreen, upperGreen)
    #devolve a cor verde apenas
    resultadoGreen = cv2.bitwise_and(frame, frame, mask=mascaraGreen)
    #deixa a imagem em tons de cinza
    frameGrayGreen = cv2.cvtColor(resultadoGreen, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshGreen = cv2.threshold(frameGrayGreen, 3, 255, cv2.THRESH_BINARY)
    #faz o contorno do objeto verde
    contornosGreen, _ = cv2.findContours(
        threshGreen, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #for para trabalhar com os contornos
    for contornoGreen in contornosGreen:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (x, y, w, h) = cv2.boundingRect(contornoGreen)
        #define a variavel "area" com os contornos
        areaGreen = cv2.contourArea(contornoGreen)
        #faz alguma coisa se a area for maior que 1000
        if areaGreen > 1000:
            pass

    #declarações das variaveis da cor vermelha
    lowerRed = np.array([0, 139, 164])
    upperRed = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor vermelha no frame
    mascaraRed = cv2.inRange(frameHsv, lowerRed, upperRed)
    #devolve a cor vermelha apenas
    resultadoRed = cv2.bitwise_and(frame, frame, mask=mascaraRed)
    #deixa a imagem em tons de cinza
    frameGrayRed = cv2.cvtColor(resultadoRed, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshRed = cv2.threshold(frameGrayRed, 3, 255, cv2.THRESH_BINARY)
    #faz o contorno do objeto vermelho
    contornosRed, _ = cv2.findContours(
        threshRed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
    #for para trabalhar com os contornos
    for contornoRed in contornosRed:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (x, y, w, h) = cv2.boundingRect(contornoRed)
        #define a variavel "area" com os contornos
        areaRed = cv2.contourArea(contornoRed)
        #faz alguma coisa se a area for maior que 1000
        if areaRed > 1000:
            pass

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(60)
    #se a tecla esc for clicada, derruba o codigo
    if key == 27:
        break


#acaba com o código
cv2.destroyAllWindows()
#libera a camera
camera.release()
