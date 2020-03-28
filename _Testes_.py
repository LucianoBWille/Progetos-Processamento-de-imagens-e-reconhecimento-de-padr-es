from __future__ import print_function
from __future__ import division
import argparse
import numpy as np
import cv2 as cv


def converter(img, formatoSaida, formatoEntrada='RGB'):
    comando = eval(f'cv.COLOR_{formatoEntrada}2{formatoSaida}')
    return cv.cvtColor(img, comando)


class Image():
    def __init__(self, nome, tipo, img):
        self.nome = nome
        self.tipo = tipo
        self.imagem = img



original = Image('Lenna', 'RGB', cv.imread('Lenna.jpg'))
'''
xyz = Image('Lenna', 'XYZ', converter(original.imagem, 'XYZ', formatoEntrada=original.tipo))
cv.imshow(f'{original.nome} {original.tipo}', original.imagem)
cv.imshow(f'{xyz.nome} {xyz.tipo}', xyz.imagem)
cv.waitKey(0)
cv.destroyAllWindows()
hist = cv.calcHist([original.imagem], [0], None, [256], [0, 256])
print(hist)
cv.imshow('histograma', hist)
cv.waitKey(0)
cv.destroyAllWindows()
'''
'''
parser = argparse.ArgumentParser(description='Code for Histogram Calculation tutorial.')
parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
args = parser.parse_args()
'''
'''
#src = cv.imread(cv.samples.findFile(args.input))
src = original.imagem
if src is None:
    print('Could not open or find the image:', args.input)
    exit(0)
bgr_planes = cv.split(src)
histSize = 256
histRange = (0, 256)  # the upper boundary is exclusive
accumulate = False
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
hist_w = 512
hist_h = 512
bin_w = int(round( hist_w/histSize ))
maior = max([max(b_hist), max(g_hist), max(r_hist)])
histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

for i in range(1, histSize):
    y1 = hist_h - 1 - int(((hist_h-2)/maior)*(b_hist[i-1]))
    y2 = hist_h - 1 - int(((hist_h-2)/maior)*(b_hist[i]))
    cv.line(histImage, ( bin_w*(i-1), y1 ), ( bin_w*(i), y2 ), ( 255, 0, 0), thickness=2)
    y1 = hist_h - 1 - int(((hist_h-2)/maior)*(g_hist[i-1]))
    y2 = hist_h - 1 - int(((hist_h-2)/maior)*(g_hist[i]))
    cv.line(histImage, ( bin_w*(i-1), y1 ), ( bin_w*(i), y2 ), ( 0, 255, 0), thickness=2)
    y1 = hist_h - 1 - int(((hist_h-2)/maior)*(r_hist[i-1]))
    y2 = hist_h - 1 - int(((hist_h-2)/maior)*(r_hist[i]))
    cv.line(histImage, ( bin_w*(i-1), y1), ( bin_w*(i), y2 ), ( 0, 0, 255), thickness=2)
cv.imshow('Source image', src)
cv.imshow('calcHist Demo', histImage)
image = cv.merge((b_hist, g_hist, r_hist))
cv.imshow('Merged', image)
cv.waitKey(0)
cv.destroyAllWindows()
'''
'''
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
canvas = np.ones((altura, largura, 3))
bordaV = 20
bordaH = 10
b1 = Botao((0, 0, 1), bordaH, int(largura/2)-bordaH, bordaV, altura-bordaV)
b2 = Botao((1, 0, 0), int(largura/2)+bordaH, largura-bordaH, bordaV, altura-bordaV)
grossura = 3
cv.rectangle(canvas, (b1.x1, b1.y1), (b1.x2, b1.y2), (0.8, 0.8, 0.8), -1)
cv.rectangle(canvas, (b2.x1, b2.y1), (b2.x2, b2.y2), (0.8, 0.8, 0.8), -1)
cv.rectangle(canvas, (b1.x1, b1.y1), (b1.x2, b1.y2), b1.cor, grossura)
cv.rectangle(canvas, (b2.x1, b2.y1), (b2.x2, b2.y2), b2.cor, grossura)
fonte = cv.FONT_HERSHEY_SIMPLEX
escala = 1
grossura = 3
cv.putText(canvas, 'Video', (b1.x1+50, b1.y1+65), fonte, escala, b1.cor, grossura)
cv.putText(canvas, 'Camera', (b2.x1+30, b2.y1+65), fonte, escala, b2.cor, grossura)
cv.imshow("Canvas", canvas)
cv.waitKey(0)
'''

cap = cv.VideoCapture(0)

fundo = cv.imread('Captura.jpg')
altura = 640
largura = 480
base = fundo
cv.rectangle(base, (0, 0), (640, 480), (250, 250, 250), -1)


def compara(cor1, cor2):
    tolerancia = 100
    if cor2[0]-tolerancia < cor1[0] < cor2[0]+tolerancia and \
            cor2[1]-tolerancia < cor1[1] < cor2[1]+tolerancia and \
            cor2[2]-tolerancia < cor1[2] < cor2[2]+tolerancia:
        return [0, 255, 0]
    else:
        return [cor1[0], cor1[1], cor1[2]]
while(cap.isOpened()):
    ret, frame = cap.read()

    b, g, r = cv.split(frame)
    B, G, R = cv.split(fundo)
    ret, thresh1 = cv.threshold(b, 127, 255, cv.THRESH_TRUNC)
    ret, thresh2 = cv.threshold(g, 127, 255, cv.THRESH_TRUNC)
    ret, thresh3 = cv.threshold(r, 127, 255, cv.THRESH_TRUNC)
    ret, thresh4 = cv.threshold(B, 127, 255, cv.THRESH_TRUNC)
    ret, thresh5 = cv.threshold(G, 127, 255, cv.THRESH_TRUNC)
    ret, thresh6 = cv.threshold(R, 127, 255, cv.THRESH_TRUNC)

    ch1 = cv.bitwise_and(thresh1, thresh4)
    ch2 = cv.bitwise_and(thresh2, thresh5)
    ch3 = cv.bitwise_and(thresh3, thresh6)

    ch11 = cv.bitwise_not(ch1)
    mascara1 = cv.subtract(ch11, ch1)

    ch21 = cv.bitwise_not(ch2)
    mascara2 = cv.subtract(ch21, ch2)

    ch31 = cv.bitwise_not(ch3)
    mascara3 = cv.subtract(ch31, ch3)

    mascara = cv.add(mascara1, mascara2)
    mascara = cv.add(mascara, mascara3)
    for i in range(0, 10):
        mascara = cv.add(mascara, mascara1)
        mascara = cv.add(mascara, mascara2)
        mascara = cv.add(mascara, mascara3)

    ret, mascara = cv.threshold(mascara, 127, 255, cv.THRESH_BINARY)

    mascara = cv.bitwise_not(mascara)

    ch1 = cv.subtract(b, mascara)
    ch2 = cv.add(g, mascara)
    ch3 = cv.subtract(r, mascara)

    transformada = cv.merge((ch1, ch2, ch3))

    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('p'):
        fundo = frame
        cv.imwrite('Captura.jpg', fundo)

cap.release()
cv.destroyAllWindows()