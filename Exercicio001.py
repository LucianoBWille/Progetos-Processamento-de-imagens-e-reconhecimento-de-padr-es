from __future__ import print_function
from __future__ import division
import argparse
import numpy as np
import cv2 as cv
import os


def splitter(img, name):  # divide a imagem nos tres canais e salva cada um deles (além da repassada)
    ch1, ch2, ch3 = cv.split(img)
    title = name + '-Channel 1'
    cv.imshow(title, ch1)
    title = name + '-Channel 2'
    cv.imshow(title, ch2)
    title = name + '-Channel 3'
    cv.imshow(title, ch3)
    # save images
    cv.imwrite('imagens//' + name + '.jpg', img)
    cv.imwrite('imagens//' + name + '-Channel 1.jpg', ch1)
    cv.imwrite('imagens//' + name + '-Channel 2.jpg', ch2)
    cv.imwrite('imagens//' + name + '-Channel 3.jpg', ch3)
    cv.waitKey(0)
    cv.destroyAllWindows()


def histogramer(src, name):  # Gera uma imagem com os histogramas dos tres canais combinados
    bgr_planes = cv.split(src)  # divide a imagem nos tres canais de cor
    histSize = 256
    histRange = (0, 256)  # the upper boundary is exclusive
    accumulate = False
    b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)  # Calcula o histograma do canal 1
    g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)  # Calcula o histograma do canal 2
    r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)  # Calcula o histograma do canal 3
    hist_w = 256
    hist_h = 256
    bin_w = int(round(hist_w / histSize))
    maior = max([max(b_hist), max(g_hist), max(r_hist)])  # Encontra o valor da maior aparição de cor
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)  # cria uma imagem preta onde o histograma será desenhado

    for i in range(1, histSize):
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (b_hist[i - 1]))  # y1 e y2 são a quantidade de pixeis de certa
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (b_hist[i]))      # cor ajustada a altura do histograma
        cv.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (255, 0, 0), thickness=bin_w)  # gera a linha Azul do Histograma
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (g_hist[i - 1]))  # y1 e y2 são a quantidade de pixeis de certa
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (g_hist[i]))      # cor ajustada a altura do histograma
        cv.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (0, 255, 0), thickness=bin_w)  # gera a linha Verde do Histograma
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (r_hist[i - 1]))  # y1 e y2 são a quantidade de pixeis de certa
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (r_hist[i]))      # cor ajustada a altura do histograma
        cv.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (0, 0, 255), thickness=bin_w)  # gera a linha Vermelha do Histograma
    cv.imshow(name + '-Histograma', histImage)
    cv.imwrite('imagens//' + name + '-Histograma.jpg', histImage)


def histogramer1channel(src, name):
    histSize = 256
    histRange = (0, 256)  # the upper boundary is exclusive
    accumulate = False
    hist = cv.calcHist(src, [0], None, [histSize], histRange, accumulate=accumulate)  # Calcula o histograma
    hist_w = 256
    hist_h = 256
    bin_w = int(round(hist_w / histSize))
    maior = max(hist)  # Encontra o valor da maior aparição de cor
    histImage = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)  # cria uma imagem preta onde o histograma será desenhado

    for i in range(1, histSize):
        y1 = hist_h - 1 - int(((hist_h - 2) / maior) * (hist[i - 1]))  # y1 e y2 são a quantidade de pixeis de certa
        y2 = hist_h - 1 - int(((hist_h - 2) / maior) * (hist[i]))      # cor ajustada a altura do histograma
        cv.line(histImage, (bin_w * (i - 1), y1), (bin_w * (i), y2), (255, 255, 255), thickness=bin_w)  # gera a linha do Histograma
    cv.imshow(name + '-Histograma', histImage)
    cv.imwrite('imagens//' + name + '-Histograma.jpg', histImage)


op = 1
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
     | 9 - ORIGINAL   |
     =================
     Opção: '''))
    if op == 0:
        break
    nomeArq = input('Digite o nome da imagem: ')
    nomeTmp = nomeArq
    nome = nomeArq
    image = cv.imread(nomeArq + '.jpg')
    nome = nome.capitalize()
    cv.imshow(nome, image)
    histogramer(image, nome)
    os.system('clear')
    if op == 1:  # HSV
        hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        nome = nome + ' HSV'
        cv.imshow(nome, hsv)
        histogramer(hsv, nome)
        splitter(hsv, nome)
        del hsv
    if op == 2:  # HLS
        hls = cv.cvtColor(image, cv.COLOR_RGB2HLS)
        nome = nome + ' HLS'
        cv.imshow(nome, hls)
        histogramer(hls, nome)
        splitter(hls, nome)
        del hsv
    elif op == 3:  # Lab
        lab = cv.cvtColor(image, cv.COLOR_RGB2LAB)
        nome = nome + ' LAB'
        cv.imshow(nome, lab)
        histogramer(lab, nome)
        splitter(lab, nome)
        del lab
    elif op == 4:  # LUV
        luv = cv.cvtColor(image, cv.COLOR_RGB2LUV)
        nome = nome + ' LUV'
        cv.imshow(nome, luv)
        histogramer(luv, nome)
        splitter(luv, nome)
        del luv
    elif op == 5:  # XYZ
        xyz = cv.cvtColor(image, cv.COLOR_RGB2XYZ)
        nome = nome + ' XYZ'
        cv.imshow(nome, xyz)
        histogramer(xyz, nome)
        splitter(xyz, nome)
        del xyz
    elif op == 6:  # YCrCb
        YCrCb = cv.cvtColor(image, cv.COLOR_RGB2YCrCb)
        nome = nome + ' YCrCb'
        cv.imshow(nome, )
        histogramer(YCrCb, nome)
        splitter(YCrCb, nome)
        del YCrCb
    elif op == 7:  # YUV
        yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
        nome = nome + ' YUV'
        cv.imshow(nome, yuv)
        histogramer(yuv, nome)
        splitter(yuv, nome)
        del yuv
    elif op == 8:  # GRAY
        gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        nome = nome + ' GRAY'
        histogramer1channel(gray, nome)
        cv.imshow(nome, gray)
        cv.imwrite('imagens//' + nome + '.jpg', gray)
        cv.waitKey(0)
        cv.destroyAllWindows()
        del gray
    elif op == 9:
        splitter(image, nome)
    else:
        print('Opção Inválida')
        cv.destroyAllWindows()
