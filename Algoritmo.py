import cv2
from time import sleep

i = 120
cap = cv2.VideoCapture('In_video1.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, i)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('output.mp4', fourcc, 30, (w, h))

for _ in range(150):
    ret, im = cap.read()
    if ret == False:
        break
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(45,80,80),(65,255,255))
    mask0 = 255-mask
    im2= cv2.bitwise_and(im, im, mask=mask0)

    im_fondo = cv2.imread('fondo6.jpg')
    h,w,_ = im.shape
    im_fondo= cv2.resize(im_fondo, (w,h))
    im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask)
    im4= cv2.bitwise_or(im3, im2)


    cv2.imshow('imagen', im4)
    out.write(im4)
    cv2.waitKey(1)
    sleep(1/30)



