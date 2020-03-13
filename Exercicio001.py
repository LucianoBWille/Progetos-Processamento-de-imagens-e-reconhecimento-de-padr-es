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
op = 1
initFlag = True
while op != 0:
    op = int(input('''     =================
     | 0 - Sair      |
     | 1 - HSV       |
     | 2 - LAB       |
     | 3 - LUV       |
     | 4 - XYZ       |
     | 5 - YUV       |
     | 6 - YCrCb     |
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
    os.system('clear')
    if op == 1:  # HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        nome = nome + ' HSV'
        cv2.imshow(nome, hsv)
        splitter(hsv, nome)
        del hsv
    elif op == 2:  # Lab
        lab = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
        nome = nome + ' LAB'
        cv2.imshow(nome, lab)
        splitter(lab, nome)
        del lab
    elif op == 3:  # LUV
        luv = cv2.cvtColor(image, cv2.COLOR_RGB2LUV)
        nome = nome + ' LUV'
        cv2.imshow(nome, luv)
        splitter(luv, nome)
        del luv
    elif op == 4:  # XYZ
        xyz = cv2.cvtColor(image, cv2.COLOR_RGB2XYZ)
        nome = nome + ' XYZ'
        cv2.imshow(nome, xyz)
        splitter(xyz, nome)
        del xyz
    elif op == 5:  # YUV
        yuv = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
        nome = nome + ' YUV'
        cv2.imshow(nome, yuv)
        splitter(yuv, nome)
        del yuv
    elif op == 6:  # YCrCb
        YCrCb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
        nome = nome + ' YCrCb'
        cv2.imshow(nome, YCrCb)
        splitter(YCrCb, nome)
        del YCrCb
    else:
        print('Opção Inválida')
        cv2.destroyAllWindows()
        
