import cv2
import matplotlib.pyplot as plt

i = 1

while i > 0 and i < 5: 
    if i == 1:
        im = cv2.imread('Im_ejercicio1.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(150,141,164),(150,141,164))
        fondo = 255-mask
        im2= cv2.bitwise_and(im, im, mask=fondo)

    if i == 2:
        im = cv2.imread('Im_7.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(45,160,110),(50,240,255)) #95, 64, 45
        fondo= cv2.bitwise_not(mask) 
        im2= cv2.bitwise_and(im, im, mask=fondo)

    if i == 3:
        im = cv2.imread('Im_8.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,235,100),(65,255,210)) #59.83, 255, 181.05
        fondo = 255-mask
        im2= cv2.bitwise_and(im, im, mask=fondo)

    if i == 4:
        im = cv2.imread('Im_9.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,100,90),(65,235,220)) #(61.82, 124.95, 214.2) - (56.34, 221.85, 94.35)  
        fondo= cv2.bitwise_not(mask) 
        im2= cv2.bitwise_and(im, im, mask=fondo)

    plt.figure(num = 'IMAGENES', figsize = (10, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Mascara')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.imshow(fondo, cmap='gray')
    plt.title('Fondo')
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Final')
    plt.axis('off')
    

    plt.show()
    cv2.waitKey(0)

    i = i + 1