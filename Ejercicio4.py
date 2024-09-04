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

SALTO = 100


def calcular_capacidad(matriz, tamanio_canal):
    try:
        maxima_entropia = 0
        probabilidades = []
        probabilidades_entrada = []
        cuaternario = 1
        ternario = 1
        binario = 1
        if tamanio_canal == 4:
            cuaternario = SALTO
            ternario = SALTO
            binario = SALTO
        elif tamanio_canal == 3:
            ternario = SALTO
            binario = SALTO
        elif tamanio_canal == 2:
            binario = SALTO
        else:
            raise Exception
        for z in range (0, cuaternario):
            p3 = z / SALTO
            for y in range (0, ternario-z):
                p2 = y/SALTO
                for x in range(0, binario-z-y):
                    p1 = x/SALTO
                    p4 = 1-p1
                    
                    probabilidades_entrada.clear()
                    if cuaternario == SALTO:
                        probabilidades_entrada.append(p3)
                        p4-= p3
                    if ternario == SALTO:
                        probabilidades_entrada.append(p2)
                        p4-= p2
                    probabilidades_entrada.append(p1)
                    probabilidades_entrada.append(p4)


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
                        if pb !=0:
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
                        probabilidades = probabilidades_entrada.copy()
        if len(probabilidades) == 0:
            for i in range(tamanio_canal):
                probabilidades.append(0)
                
        probabilidades_redondeadas = [round(p, 5) for p in probabilidades]

        messagebox.showinfo("Resultado", f"Las probabilidades que maximizan la capacidad de canal son: {probabilidades_redondeadas}\nLa capacidad de canal es: {maxima_entropia}")
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
        todas_filas_suman_uno = np.allclose(sumas_filas, np.ones(sumas_filas.shape), atol=1e-3)
        
        if not (todas_filas_suman_uno):
            raise ValueError("Cada fila debe sumar 1.")
        
        calcular_capacidad(matriz_numpy, len(entry_matrix))

    except ValueError as e:
        messagebox.showerror("Error", f"Error en los valores ingresados: {e}")

