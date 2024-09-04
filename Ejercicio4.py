''' #Desarrollar una aplicación de software que calcule la Capacidad de Canal de un canal R-ario Uniforme y
#No-Uniforme. El soft debe aceptar como entrada el valor de R que identifica al canal (R= 2 Binario, R=3
#Ternario hasta R=4) los valores de probabilidades condicionales que representan la matriz del canal
#entregando como salida el valor de las probabilidades independientes de cada uno de los símbolos de entrada
#que maximiza la información mutua, esto es, lograr la capacidad de canal. '''


''' entradas: 
    tamaño de canal(2,3,4)
    tipo de canal(uniforme/no uniforme)
    probabilidades(1 fila para uniforme, n filas para no uniforme)
Salida:
    p(ai) para lograr capacidad de canal(p(a)equiprobables en canal uniforme/no uniforme)
    capacidad de canal
 '''
#TODO 
from tkinter import messagebox
import numpy as np
import math


def calcular_capacidad(matriz, tamanio_canal):
    try:
        maxima_entropia = 0
        probabilidad1 = 0
        probabilidad2 = 0
        for x in range(0, 100):
            probabilidades_entrada=[x/100, 1-x/100]
            
            #creo las probabilidades de entrada
            #for i in range(tamanio_canal):
             #   probabilidades_entrada.append(1/tamanio_canal)
                
            #calculo capacidad de canal
            capacidad_canal=0      
            entropia_salida=0 #H(B)
            entropia_equivocacion=0 #H(B/A)
            probabilidades_salida=[] #p(bj)
            probabilidades_condicionales=[] #p(bj/ai)
            
            #calculo H(B)
            for i in range(tamanio_canal):
                pb=0
                for j in range(tamanio_canal):
                    if(matriz[j][i]!= 0):#verificar que p(bj/ai) no sea 0
                        pb+=probabilidades_entrada[j]*matriz[j][i]
                probabilidades_salida.append(pb)
                entropia_salida+= pb*math.log2(1/pb)

            #calculo H(B/A)
            for i in range(tamanio_canal):
                pcondicional=0
                for j in range(tamanio_canal):
                    if(matriz[i][j]!= 0):#verificar que p(bj/ai) no sea 0
                        pcondicional+=probabilidades_entrada[i]*matriz[i][j]*math.log2(1/matriz[i][j])
                probabilidades_condicionales.append(pcondicional)
                entropia_equivocacion+= pcondicional
            
            #I(A,B)= H(B)-H(B/A) con p(ai) equiprobables se obtiene la informacion maxima que es la capacidad del canal
            capacidad_canal = entropia_salida-entropia_equivocacion
            if maxima_entropia<capacidad_canal:
                maxima_entropia=capacidad_canal
                probabilidad1= probabilidades_entrada[0]
                probabilidad2 = probabilidades_entrada[1]
        
        messagebox.showinfo("Resultado", f"Las probabilidades que maximizan la capacidad de canal son: {probabilidad1, probabilidad2}\nLa capacidad de canal es: {maxima_entropia}")
    except ZeroDivisionError as z:
        messagebox.showerror("Error", f"Error en los valores ingresados: {z}")  
def main (entry_matrix):
    try:
        matriz_valores = [] 
        i = 0
        for i in range(len(entry_matrix)):
            fila = []
            for j in range(len(entry_matrix)):
                valor = float (entry_matrix[i][j].get())
                fila.append(valor)
            matriz_valores.append(fila)
        matriz_numpy = np.array(matriz_valores) 
        
        # Verificar que las probabilidades sean válidas
        if not(np.all((matriz_numpy >= 0) & (matriz_numpy <= 1))):
            raise ValueError("Las probabilidades deben estar entre 0 y 1.")
        
        # Sumar cada fila de la matriz
        sumas_filas = np.sum(matriz_numpy, axis=1)  # axis=1 indica que la suma es por filas
        
        # Verificar si cada suma es aproximadamente 1 (usamos un margen de error para evitar problemas de precisión)
        todas_filas_suman_uno = np.allclose(sumas_filas, np.ones(sumas_filas.shape), atol=1e-8)
        
        if not (todas_filas_suman_uno):
            raise ValueError("Cada fila debe sumar 1.")
        
        calcular_capacidad(matriz_numpy, len(entry_matrix))

    except ValueError as e:
        messagebox.showerror("Error", f"Error en los valores ingresados: {e}")

