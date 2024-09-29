import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def mostrarIm(Im, Ig):
    plt.figure(figsize=(7, 2.5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(Im, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(Ig, cmap='gray')
    plt.title('Imagen en escala de grises')
    plt.axis('off')
    plt.show()


Im = cv2.imread('imagen3.png')
Ig = cv2.cvtColor(Im, cv2.COLOR_BGR2GRAY)

op = 1
while op != '0':
    os.system('cls')
    if op == 1:
        mostrarIm(Im, Ig)
    try:
        op = int(input("\nSelecciona el tipo de histograma que deseas calcular:\n"
               "3 - Térciales           10 - Deciles\n"
               "4 - Cuartiles           100 - Percentiles\n"
               "5 - Quintiles           256 - Valores de píxeles\n\n"
               "Ingresa el número correspondiente: _").strip())
    except ValueError:
        print("*Error: Debes ingresar un número entero*")
    if op == 3 or op == 4 or op == 5 or op == 10 or op == 100 or op == 256:
        [M,N]=Ig.shape[0:2]
        if op == 3:
            hist = cv2.calcHist([Ig],[0],None,[3],[0,256]).flatten()
        if op ==4:
            hist = cv2.calcHist([Ig],[0],None,[4],[0,256]).flatten()
        if op == 5:
            hist = cv2.calcHist([Ig],[0],None,[5],[0,256]).flatten()
            maxElement = np.argmax(hist)
            if maxElement == 4 and hist[4] > 0.3:
                print('sobreexpuesta')
            elif maxElement == 0 and hist[0] > 0.3:
                print('subexpuesta')
            else:
                print('buena exposición')
        if op ==10:
            hist = cv2.calcHist([Ig],[0],None,[10],[0,256]).flatten()
        if op == 100:
            hist = cv2.calcHist([Ig],[0],None,[100],[0,256]).flatten()
        if op == 256:
            hist = cv2.calcHist([Ig],[0],None,[256],[0,256]).flatten()
        
        plt.figure(figsize=(4, 3))
        plt.bar(range(len(hist)), hist)

        plt.show()

    else:
        print("\nOpción no valida, vuelve a intentarlo")
    
    op = int(input("\nPresiona '1' para mostrar las imagenes _\nPresiona '0' para salir _").strip())
