import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class Conversor():
    def __init__(self, localArq):
        self.local_arquivo = localArq
        self.imgOriginal = cv.imread(localArq, cv.IMREAD_COLOR)
        arqtxt = str(localArq).split('/')
        arqtxt = arqtxt[-1]
        nome = arqtxt.split('.')[0]
        self.local = '/'.join(arqtxt[:-1])
        self.nome = nome
        self.extencao = arqtxt.split('.')[1]
    def exibeImagens(self):
        cv.imshow('Imagem', self.imgOriginal)
    def bgr2hsv(self):
        self.hsv = cv.cvtColor(self.imgOriginal, cv.COLOR_BGR2HSV)
    def bgr2lab(self):
        self.lab = cv.cvtColor(self.imgOriginal, cv.COLOR_BGR2LAB)
    def bgr2luv(self):
        self.luv = cv.cvtColor(self.imgOriginal, cv.COLOR_BGR2LUV)

conv = Conversor('imagens/Lenna XYZ.jpg')
print(conv.local)
conv.exibeImagens()
conv.bgr2hsv()
cv.imshow('HSV', conv.hsv)
cv.waitKey(0)
cv.destroyAllWindows()
