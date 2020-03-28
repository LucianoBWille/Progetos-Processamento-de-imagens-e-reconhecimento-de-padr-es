import cv2 as cv
import numpy as np


class Botao():
    def __init__(self, cor, x1, x2, y1, y2):
        self.cor = cor
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


altura = 150
largura = 400
opcoes = np.ones((altura, largura, 3))
bordaV = 20
bordaH = 10
b1 = Botao((0, 0, 1), bordaH, int(largura / 2) - bordaH, bordaV, altura - bordaV)
b2 = Botao((1, 0, 0), int(largura / 2) + bordaH, largura - bordaH, bordaV, altura - bordaV)
grossura = 3
cv.rectangle(opcoes, (b1.x1, b1.y1), (b1.x2, b1.y2), (0.8, 0.8, 0.8), -1)
cv.rectangle(opcoes, (b2.x1, b2.y1), (b2.x2, b2.y2), (0.8, 0.8, 0.8), -1)
cv.rectangle(opcoes, (b1.x1, b1.y1), (b1.x2, b1.y2), b1.cor, grossura)
cv.rectangle(opcoes, (b2.x1, b2.y1), (b2.x2, b2.y2), b2.cor, grossura)
fonte = cv.FONT_HERSHEY_SIMPLEX
escala = 1
grossura = 3
cv.putText(opcoes, 'Video', (b1.x1 + 50, b1.y1 + 65), fonte, escala, b1.cor, grossura)
cv.putText(opcoes, 'Camera', (b2.x1 + 30, b2.y1 + 65), fonte, escala, b2.cor, grossura)
cv.imshow("Opcoes", opcoes)
op = True
mouse_place = (0, 0)
button_clicked = -1


def mouseControler(event, x, y, flags, userdata):
    global mouse_place
    mouse_place = (x, y)
    global op
    global b1
    global b2
    global button_clicked
    if event == cv.EVENT_LBUTTONDOWN:
        if b1.y1 < y < b1.y2:
            if b1.x1 < x < b1.x2:
                button_clicked = 'Video'
                op = False
            elif b2.x1 < x < b2.x2:
                button_clicked = 'Camera'
                op = False
        else:
            print('Clique em um botão!')


while op:
    cv.setMouseCallback('Opcoes', mouseControler)
    cv.imshow("Opcoes", opcoes)
    cv.waitKey(1)

if button_clicked == 'Camera':
    cap = cv.VideoCapture(0)
else:
    cap = cv.VideoCapture('teste.webm')

cv.destroyAllWindows()

frame = None

alpha_slider_max1 = 2
alpha_slider_max2 = 3
title_window = 'Filtro'
trackbar_name1 = 'Banda'
trackbar_name2 = 'Tamanho bloco'
tamBloco = [1, 3, 5, 7]
def on_trackbar(val):
    nada = None

button_clicked2 = 0

def mouseControler2(event, x, y, flags, userdata):
    global mouse_place
    mouse_place = (x, y)
    if event == cv.EVENT_LBUTTONDOWN:
        global button_clicked2
        button_clicked2 = True

btn = 1
ret, frame = cap.read()
cv.imshow(title_window, frame)
while(cap.isOpened()):
    ret, frame = cap.read()

    cv.createTrackbar(trackbar_name1, title_window, 0, alpha_slider_max1, on_trackbar)
    trackbar_value1 = cv.getTrackbarPos(trackbar_name1, title_window)
    b, g, r = cv.split(frame)
    if trackbar_value1 == 0:
        banda = b
    elif trackbar_value1 == 1:
        banda = g
    else:
        banda = r

    cv.createTrackbar(trackbar_name2, title_window, 0, alpha_slider_max2, on_trackbar)
    trackbar_value2 = cv.getTrackbarPos(trackbar_name2, title_window)

    if btn == 1:
        transformada = cv.blur(banda, (tamBloco[trackbar_value2], tamBloco[trackbar_value2]))
    elif btn == 2:
        transformada = cv.GaussianBlur(banda, (tamBloco[trackbar_value2], tamBloco[trackbar_value2]), 0)
    elif btn == 3:
        ddepth = cv.CV_16S
        kernel_size = 3
        transformada = cv.GaussianBlur(frame, (3, 3), 0)
        transformada = cv.cvtColor(transformada, cv.COLOR_BGR2GRAY)
        transformada = cv.Laplacian(transformada, ddepth, ksize=kernel_size)
        transformada = cv.convertScaleAbs(transformada)
    elif btn == 4:
        transformada = cv.bitwise_and(b, cv.bitwise_and(r, g))
    elif btn == 5:
        cv.imshow('b', b)
        cv.imshow('g', g)
        cv.imshow('r', r)
        transformada = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    fonte = cv.FONT_HERSHEY_SIMPLEX
    escala = 1
    grossura = 2
    f1 = cv.copyMakeBorder(frame, 5, 5, 5, 5, cv.BORDER_CONSTANT)
    t1 = cv.copyMakeBorder(transformada, 5, 5, 5, 5, cv.BORDER_CONSTANT)
    if btn != 5:
        t1 = cv.merge((t1, t1, t1))
    show = np.concatenate((f1, t1), axis=1)
    show = cv.copyMakeBorder(show, 50, 0, 0, 0, cv.BORDER_CONSTANT)
    dx = int((len(show[0])-15)/4)-2
    bt1 = Botao((255, 255, 255), 5+dx*0, 5+dx*1, 5, len(show)-len(frame)-10)
    bt2 = Botao((255, 255, 255), 5+dx*1, 5+dx*2, 5, len(show)-len(frame)-10)
    bt3 = Botao((255, 255, 255), 16+dx*2, 16+dx*3, 5, len(show)-len(frame)-10)
    bt4 = Botao((255, 255, 255), 16+dx*3, 16+dx*4, 5, len(show)-len(frame)-10)
    cv.rectangle(show, (bt1.x1, bt1.y1), (bt1.x2, bt1.y2), bt1.cor, 2)
    if btn == 1:
        cv.rectangle(show, (bt1.x1, bt1.y1), (bt1.x2, bt1.y2), bt1.cor, -1)
        cv.putText(show, 'Blur', (bt1.x1+40, bt1.y1+30), fonte, escala, bt1.cor*0, grossura)
    else:
        cv.putText(show, 'Blur', (bt1.x1+40, bt1.y1+30), fonte, escala, bt1.cor, grossura)
    cv.rectangle(show, (bt2.x1, bt2.y1), (bt2.x2, bt2.y2), bt2.cor, 2)
    if btn == 2:
        cv.rectangle(show, (bt2.x1, bt2.y1), (bt2.x2, bt2.y2), bt2.cor, -1)
        cv.putText(show, 'GaussianBlur', (bt2.x1 + 40, bt2.y1 + 30), fonte, escala, bt2.cor*0, grossura)
    else:
        cv.putText(show, 'GaussianBlur', (bt2.x1 + 40, bt2.y1 + 30), fonte, escala, bt2.cor, grossura)
    cv.rectangle(show, (bt3.x1, bt3.y1), (bt3.x2, bt3.y2), bt3.cor, 2)
    if btn == 3:
        cv.rectangle(show, (bt3.x1, bt3.y1), (bt3.x2, bt3.y2), bt3.cor, -1)
        cv.putText(show, 'Line Masks', (bt3.x1 + 40, bt3.y1 + 30), fonte, escala, bt3.cor*0, grossura)
    else:
        cv.putText(show, 'Laplace', (bt3.x1 + 40, bt3.y1 + 30), fonte, escala, bt3.cor, grossura)
    cv.rectangle(show, (bt4.x1, bt4.y1), (bt4.x2, bt4.y2), bt4.cor, 2)
    if btn == 4:
        cv.rectangle(show, (bt4.x1, bt4.y1), (bt4.x2, bt4.y2), bt4.cor, -1)
        cv.putText(show, 'And (b, g, r)', (bt4.x1 + 40, bt4.y1 + 30), fonte, escala, bt4.cor*0, grossura)
    else:
        cv.putText(show, 'And (b, g, r)', (bt4.x1+40, bt4.y1+30), fonte, escala, bt4.cor, grossura)

    cv.imshow(title_window, show)

    cv.setMouseCallback(title_window, mouseControler2)
    if button_clicked2:
        if bt1.y1 < mouse_place[1] < bt1.y2:
            if bt1.x1 < mouse_place[0] < bt1.x2:
                btn = 1
            elif bt2.x1 < mouse_place[0] < bt2.x2:
                btn = 2
            elif bt3.x1 < mouse_place[0] < bt3.x2:
                btn = 3
            elif bt4.x1 < mouse_place[0] < bt4.x2:
                btn = 4
        elif 5 < mouse_place[0] < 5 + len(frame[0]) and 55 < mouse_place[1] < 55 + len(frame):
            btn = 5
    button_clicked2 = False


    # seta a 30 fps quando video, sai com a tecla 'Esc'
    if cv.waitKey(1 if button_clicked == 'Camera' else int(1000/30)) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
