#importando as libs cv2, numpy e pyautogui juntamente com a função moveTo
from cv2 import cv2
import numpy as np
import pyautogui
from pyautogui import moveTo

#abrindo a camera
camera = cv2.VideoCapture(0)
#criação da variavel para derrubar o programa
acabar = 0
#looping "infinito", até ser cancelado
while True:
    #pega o frame da camera
    _, frameInv = camera.read()
    #inverte a camera
    frame = cv2.flip(frameInv, 1)
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
        (xYellow, yYellow, wYellow, hYellow) = cv2.boundingRect(contornoYellow)
        #define a variavel "area" com os contornos
        areaYellow = cv2.contourArea(contornoYellow)
        #analisa se a area em amarelo é maior que 2000 e se for, usa ela como mouse.
        if areaYellow > 2000:       
            pyautogui.moveTo(xYellow,yYellow)
        

    #declarações das variaveis da cor roxa
    lowerPurple = np.array([104, 54, 105])
    upperPurple = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor roxa no frame
    mascaraPurple = cv2.inRange(frameHsv, lowerPurple, upperPurple)
    #devolve a cor roxa apenas
    resultadoPurple = cv2.bitwise_and(frame, frame, mask=mascaraPurple)
    #deixa a imagem em tons de cinza
    frameGrayPurple = cv2.cvtColor(resultadoPurple, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshPurple = cv2.threshold(frameGrayPurple, 3, 255, cv2.THRESH_BINARY)
    #faz o contorno do objeto roxo
    contornosPurple, _ = cv2.findContours(
        threshPurple, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #for para trabalhar com os contornos
    for contornoPurple in contornosPurple:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xPurple, yPurple, wPurple, hPurple) = cv2.boundingRect(contornoPurple)
        #define a variavel "area" com os contornos
        areaPurple = cv2.contourArea(contornoPurple)
        #analisa se a area roxa é maior que 1000, se for, da um clique com o botão direito nas posições x e y da area amarela, no caso o mouse.
        if areaPurple > 1000:
            pyautogui.click(xYellow,yYellow,button='right')
        

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
        (xRed, yRed, wRed, hRed) = cv2.boundingRect(contornoRed)
        #define a variavel "area" com os contornos
        areaRed = cv2.contourArea(contornoRed)
        #analisa se a area vermelha é maior que 1000, se for, da um clique com o botão esquerdo nas posições x e y da area amarela, no caso o mouse.
        if areaRed > 1000:
            pyautogui.click(xYellow,yYellow,button='left')

    #declarações das variaveis da cor rosa
    lowerPink = np.array([164, 66, 0])
    upperPink = np.array([255, 255, 255])
    #cria a mascara em preto e branco para captar somente a cor rosa no frame
    mascaraPink = cv2.inRange(frameHsv, lowerPink, upperPink)
    #devolve a cor rosa apenas
    resultadoPink = cv2.bitwise_and(frame, frame, mask=mascaraPink)
    #deixa a imagem em tons de cinza
    frameGrayPink = cv2.cvtColor(resultadoPink, cv2.COLOR_BGR2GRAY)
    #deixa a imagem melhor, menos poluida
    _, threshPink = cv2.threshold(frameGrayPink, 3, 255, cv2.THRESH_BINARY)
    #faz o contorno do objeto rosa
    contornosPink, _ = cv2.findContours(
        threshPink, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    
    
    
    #for para trabalhar com os contornos
    for contornoPink in contornosPink:
        # boundingRect retorna o ponto inicial de x, y e os tamanhos de largura e altura
        (xPink, yPink, wPink, hPink) = cv2.boundingRect(contornoPink)
        #define a variavel "area" com os contornos
        areaPink = cv2.contourArea(contornoPink)
        #Caso apareça a cor rosa, a variavel acabar será igual a um e ela acaba com o programa.
        if areaPink > 1000:
            acabar = 1
            
    #mostra o frame na camera
    cv2.imshow("Camera", frame)
    #atualiza a camera a 60 fps
    key = cv2.waitKey(60)
    #se a variavel acabar for igual a 1, acaba o programa
    if acabar == 1:
        break


#acaba com o código
cv2.destroyAllWindows()
#libera a camera
camera.release()
