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

