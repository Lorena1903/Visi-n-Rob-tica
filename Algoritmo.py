import cv2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

i = 1

while i > 0 and i < 5:
    if i == 1:
        im = cv2.imread('Im_ejercicio1.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(150,141,164),(150,141,164))
        mask0 = 255-mask
        im2= cv2.bitwise_and(im, im, mask=mask0)

        im_fondo = cv2.imread('fondo1.jpg')
        h,w,_ = im.shape
        im_fondo= cv2.resize(im_fondo, (w,h))
        im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask)
        im4= cv2.bitwise_or(im3, im2)


    if i == 2:
        im = cv2.imread('Im_7.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(45,160,110),(50,240,255)) #95, 64, 45
        mask0= cv2.bitwise_not(mask)
        im2= cv2.bitwise_and(im, im, mask=mask0)

        im_fondo = cv2.imread('fondo2.jpg')
        h,w,_ = im.shape
        im_fondo= cv2.resize(im_fondo, (w,h))
        im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask)
        im4= cv2.bitwise_or(im3, im2)

    if i == 3:
        im = cv2.imread('Im_8.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,235,100),(65,255,210)) #59.83, 255, 181.05
        mask0 = 255-mask
        im2= cv2.bitwise_and(im, im, mask=mask0)

        im_fondo = cv2.imread('fondo3.jpg')
        h,w,_ = im.shape
        im_fondo= cv2.resize(im_fondo, (w,h))
        im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask)
        im4= cv2.bitwise_or(im3, im2)


    if i == 4:
        im = cv2.imread('Im_9.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,100,90),(65,235,220)) #(61.82, 124.95, 214.2) - (56.34, 221.85, 94.35)
        mask0= cv2.bitwise_not(mask)
        im2= cv2.bitwise_and(im, im, mask=mask0)

        im_fondo = cv2.imread('fondo4.jpg')
        h,w,_ = im.shape
        im_fondo= cv2.resize(im_fondo, (w,h))
        im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask)
        im4= cv2.bitwise_or(im3, im2)

    plt.figure(num = 'IMAGENES', figsize = (6, 11))
    gs = GridSpec(3, 2)

    plt.subplot(gs[0, 0])
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.title('Imagen original')
    plt.axis('off')

    plt.subplot(gs[0, 1])
    plt.imshow(cv2.cvtColor(im_fondo, cv2.COLOR_BGR2RGB))
    plt.title('Fondo')
    plt.axis('off')

    plt.subplot(gs[1, 0])
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.title('Imagen filtrada \n por la mascaraN')
    plt.axis('off')

    plt.subplot(gs[1, 1])
    plt.imshow(cv2.cvtColor(im3, cv2.COLOR_BGR2RGB))
    plt.title('Fondo filtrado \n por la mascara')
    plt.axis('off')

    plt.subplot(gs[2, :])
    plt.imshow(cv2.cvtColor(im4, cv2.COLOR_BGR2RGB))
    plt.title('Imagen final')
    plt.axis('off')

    plt.subplots_adjust(left=0.05, right=0.95, top=0.99, bottom=0.08, wspace=0.2, hspace=0.2)
    plt.subplots_adjust(hspace=0.2)

    plt.show()
    cv2.waitKey(0)

    i = i + 1