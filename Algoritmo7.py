import cv2
import matplotlib.pyplot as plt

i = 1

while i > 0 and i < 9: 
    if i == 1:
        im = cv2.imread('Im_ejercicio1.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(150,141,164),(150,141,164))

    if i == 2:
        im = cv2.imread('Im_ejercicio2.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(27,177,182),(27,177,182))

    if i == 3:
        im = cv2.imread('Im_ejercicio3.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(89,83,142),(89,83,142))

    if i == 4:
        im = cv2.imread('Im_ejercicio4.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(160,147,167),(160,147,167))

    if i == 5:
        im = cv2.imread('Im_ejercicio5.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(58,255,238),(58,255,238))

    if i == 6:
        im = cv2.imread('Im_7.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(47,220,235),(50,240,255))  

    if i == 7:
        im = cv2.imread('Im_8.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,235,100),(65,255,210)) #59.83, 255, 181.05

    if i == 8:
        im = cv2.imread('Im_9.png')
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,(55,100,90),(65,235,220)) #(61.82, 124.95, 214.2) - (56.34, 221.85, 94.35)  

    plt.figure(num = 'IMAGENES', figsize = (10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Mascara')
    plt.axis('off')
    
    plt.show()
    cv2.waitKey(0)

    i = i + 1