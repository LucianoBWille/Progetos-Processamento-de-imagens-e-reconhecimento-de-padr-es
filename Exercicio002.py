import argparse
import time

import numpy as np
import cv2 as cv
import os
'''
alpha_slider_max = 4
title_window = 'HighGUI'
def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)
parser = argparse.ArgumentParser(description='Code for Adding a Trackbar to our applications tutorial.')
parser.add_argument('--input1', help='Path to the first input image.', default='LinuxLogo.jpg')
parser.add_argument('--input2', help='Path to the second input image.', default='WindowsLogo.jpg')
args = parser.parse_args()
src1 = cv.imread('Lenna.jpg')
src2 = cv.imread('imagens/Lenna HSV.jpg')
if src1 is None:
    print('Could not open or find the image: ', args.input1)
    exit(0)
if src2 is None:
    print('Could not open or find the image: ', args.input2)
    exit(0)
cv.namedWindow(title_window, flags=cv.WINDOW_GUI_EXPANDED)
trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)
# Show some stuff
on_trackbar(0)
#cv.resizeWindow(title_window, 800, 600)
# Wait until user press some key
cv.waitKey()
'''
cap = cv.VideoCapture(0)

alpha_slider_max = 2
title_window = 'HighGUI'
trackbar_name = 'Color'
cv.namedWindow(title_window)
frame = None
mouse_place = (0, 0)
button_clicked = 0
altura_botao = 40
def on_trackbar(val):
    nada = None

def mouseControler(event, x, y, flags, userdata):
    global mouse_place
    mouse_place = (x, y)
    global altura_botao
    global frame
    global button_clicked
    if event == cv.EVENT_LBUTTONDOWN:
        if y < altura_botao:
            if x < int(len(frame[0])/3):
                button_clicked = 1
            elif x < int(len(frame[0])*2/3):
                button_clicked = 2
            else:
                button_clicked = 3
        else:
            button_clicked = 0


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.setMouseCallback(title_window, mouseControler)

    if button_clicked == 0:
        convertida = frame
    elif button_clicked == 1:
        convertida = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    elif button_clicked == 2:
        convertida = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    elif button_clicked == 3:
        convertida = cv.cvtColor(frame, cv.COLOR_BGR2XYZ)

    cv.createTrackbar(trackbar_name, title_window, 0, alpha_slider_max, on_trackbar)
    trackbar_value = cv.getTrackbarPos(trackbar_name, title_window)

    if trackbar_value == 0:
        color = (255, 0, 0)
    elif trackbar_value == 1:
        color = (0, 255, 0)
    elif trackbar_value == 2:
        color = (0, 0, 255)

    cv.line(convertida, (0, altura_botao), (len(frame[0]), altura_botao), color, thickness=2)
    cv.line(convertida, (0, 0), (len(frame[0]), 0), color, thickness=2)
    cv.line(convertida, (int(len(frame[0])/3), 0), (int(len(frame[0])/3), altura_botao), color, thickness=2)
    cv.line(convertida, (int(len(frame[0])*2/3), 0), (int(len(frame[0])*2/3), altura_botao), color, thickness=2)
    cv.line(convertida, (0, 0), (0, altura_botao), color, thickness=2)
    cv.line(convertida, (int(len(frame[0])), 0), (int(len(frame[0])), altura_botao), color, thickness=2)
    #fonte = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
    fonte = cv.FONT_HERSHEY_SIMPLEX
    escala = 1
    grossura = 3
    cv.putText(convertida, 'YUV', (80, 30), fonte, escala, color, grossura)
    cv.putText(convertida, 'HSV', (int(len(frame[0])/3)+80, 30), fonte, escala, color, grossura)
    cv.putText(convertida, 'XYZ', (int(len(frame[0])*2/3)+80, 30), fonte, escala, color, grossura)

    local_Text = f'(X={mouse_place[0]:03}, Y={mouse_place[1]:03})'
    cv.putText(convertida, local_Text, (len(frame[0]) - 270, len(frame) - 15), fonte, escala, color, grossura)

    # Display the resulting frame
    cv.imshow(title_window, convertida)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()