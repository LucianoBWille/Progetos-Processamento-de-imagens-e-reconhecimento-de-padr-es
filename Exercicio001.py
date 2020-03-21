from __future__ import print_function
from __future__ import division
import argparse
import numpy as np
import cv2
#from matplotlib import pyplot as plt
import os

def splitter(img, name):
    ch1, ch2, ch3 = cv2.split(img)
    title = name + '-Channel 1'
    cv2.imshow(title, ch1)
    title = name + '-Channel 2'
    cv2.imshow(title, ch2)
    title = name + '-Channel 3'
    cv2.imshow(title, ch3)
    # save images
    cv2.imwrite('imagens//' + name + '.jpg', img)
    cv2.imwrite('imagens//' + name + '-Channel 1.jpg', ch1)
    cv2.imwrite('imagens//' + name + '-Channel 2.jpg', ch2)
    cv2.imwrite('imagens//' + name + '-Channel 3.jpg', ch3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def histogramer(src, name):
    bgr_planes = cv2.split(src)
    histSize = 256
    histRange = (0, 256)  # the upper boundary is exclusive
    accumulate = False
    b_hist = cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
    g_hist = cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
    r_hist = cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)
    hist_w = 256
    hist_h = 256
    bin_w = int(round(hist_w / histSize))
    maior = max([max(b_hist), max(g_hist), max(r_hist)])
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    for i in range(1, histSize):
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (b_hist[i - 1]))
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (b_hist[i]))
        cv2.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (255, 0, 0), thickness=bin_w)
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (g_hist[i - 1]))
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (g_hist[i]))
        cv2.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (0, 255, 0), thickness=bin_w)
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (r_hist[i - 1]))
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (r_hist[i]))
        cv2.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (0, 0, 255), thickness=bin_w)
    cv2.imshow(name + '-Histograma', histImage)
    cv2.imwrite('imagens//' + name + '-Histograma.jpg', histImage)
def histogramer1channel(src, name):
    histSize = 256
    histRange = (0, 256)  # the upper boundary is exclusive
    accumulate = False
    hist = cv2.calcHist(src, [0], None, [histSize], histRange, accumulate=accumulate)
    hist_w = 256
    hist_h = 256
    bin_w = int(round(hist_w / histSize))
    maior = max(hist)
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    for i in range(1, histSize):
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (hist[i - 1]))
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (hist[i]))
        cv2.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (255, 255, 255), thickness=bin_w)
    cv2.imshow(name + '-Histograma', histImage)
    cv2.imwrite('imagens//' + name + '-Histograma.jpg', histImage)
op = 1
initFlag = True
while op != 0:
    op = int(input('''     =================
     | 0 - Sair       |
     | 1 - HSV        |
     | 2 - HLS        |
     | 3 - CIE LAB    |
     | 4 - CIE LUV    |
     | 5 - XYZ        |
     | 6 - YCrCb      |
     | 7 - YUV        |
     | 8 - GRAY       |
     =================
     Opção: '''))
    if op == 0:
        break
    nomeArq = input('Digite o nome da imagem: ')
    nomeTmp = nomeArq
    nome = nomeArq
    image = cv2.imread(nomeArq + '.jpg')
    nome = nome.capitalize()
    cv2.imshow(nome, image)
    histogramer(image, nome)
    os.system('clear')
    if op == 1:  # HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        nome = nome + ' HSV'
        cv2.imshow(nome, hsv)
        histogramer(hsv, nome)
        splitter(hsv, nome)
        del hsv
    if op == 2:  # HLS
        hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
        nome = nome + ' HLS'
        cv2.imshow(nome, hls)
        histogramer(hls, nome)
        splitter(hls, nome)
        del hsv
    elif op == 3:  # Lab
        lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
        nome = nome + ' LAB'
        cv2.imshow(nome, lab)
        histogramer(lab, nome)
        splitter(lab, nome)
        del lab
    elif op == 4:  # LUV
        luv = cv2.cvtColor(image, cv2.COLOR_RGB2LUV)
        nome = nome + ' LUV'
        cv2.imshow(nome, luv)
        histogramer(luv, nome)
        splitter(luv, nome)
        del luv
    elif op == 5:  # XYZ
        xyz = cv2.cvtColor(image, cv2.COLOR_RGB2XYZ)
        nome = nome + ' XYZ'
        cv2.imshow(nome, xyz)
        histogramer(xyz, nome)
        splitter(xyz, nome)
        del xyz
    elif op == 6:  # YCrCb
        YCrCb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
        nome = nome + ' YCrCb'
        cv2.imshow(nome, )
        histogramer(YCrCb, nome)
        splitter(YCrCb, nome)
        del YCrCb
    elif op == 7:  # YUV
        yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
        nome = nome + ' YUV'
        cv2.imshow(nome, yuv)
        histogramer(yuv, nome)
        splitter(yuv, nome)
        del yuv
    elif op == 8:  # GRAY
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        nome = nome + ' GRAY'
        histogramer1channel(gray, nome)
        cv2.imshow(nome, gray)
        cv2.imwrite('imagens//' + nome + '.jpg', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        del gray
    else:
        print('Opção Inválida')
        cv2.destroyAllWindows()
