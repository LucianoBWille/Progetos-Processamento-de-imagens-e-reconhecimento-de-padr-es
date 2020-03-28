import cv2 as cv
import numpy as np
class Image():
    def __init__(self, nome, img):
        self.nome = nome
        if len(img[0][0]) == 1:
            self.imagem = cv.merge(img, img, img)
        else:
            self.imagem = img
def showPictures(images = list):
    quantidade = len(images)

img = cv.imread('Lenna.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.merge((gray, gray, gray))
xyz = cv.cvtColor(img, cv.COLOR_RGB2XYZ)
canvas = np.ones((300, 400, 3)) * 255
title_window = 'HighGUI'
trackbar_name = 'Color'

img1 = cv.copyMakeBorder(img, 5, 5, 5, 5, cv.BORDER_CONSTANT)
gray1 = cv.copyMakeBorder(gray, 5, 5, 5, 5, cv.BORDER_CONSTANT)
xyz1 = cv.copyMakeBorder(xyz, 5, 5, 5, 5, cv.BORDER_CONSTANT)

juntos = np.concatenate((img1, gray1, xyz1, img1), axis=1)
juntos = np.concatenate((juntos, juntos), axis=0)
show = cv.copyMakeBorder(juntos, 40, 0, 0, 0, cv.BORDER_CONSTANT)

cv.imshow('Juntos', show)

cv.waitKey(0)
cv.destroyAllWindows()
