from Caracter import Caracter
from tkinter import messagebox

"""
Reglas para asignar puntos:
+4      -> Igual cantidad de símbolo y mismo orden
-0.5    -> Por cada símbolo de difenrencia en longitud
+2      -> Si tienen distinta cantidad pero todos los símbolos en la misma posición
-0.5    -> Por cada símbolo en posición diferente
+0      -> No comparten el símbolo
"""

#Genera la lista de los caracteres con sus datos de interes
def GenerarListaCaracteres(cadena, caracteres1):
    aux = None
    for char in cadena:
        aux = BuscarCaracter(char, caracteres1)
        if aux != None:
            aux.incrCantidad()
            aux.appendPosition(cadena.index(char, aux.getLastPosition()+1))
            #Si una letra se repite varias veces dentro de la cadena buscamos 
            # a partir del siguiente del último encontrado            
        else:
            caracteres1.append(Caracter(char, cadena.index(char, 0)))

#Busca el caracter dentro de la lista
def BuscarCaracter(buscado, caracteres):
    for caracterObjeto in caracteres:
        if caracterObjeto.getCaracter() == buscado:
            return caracterObjeto
    return None

#Compara las listas de posiciones y resta puntos
def CompararPosiciones(pos1, pos2):
    #pos1=[1,2,3]   pos2=[2,3,4]
    #Inicializamos los puntos
    if len(pos1) == len(pos2):
        puntos = 4
    else:
        puntos = 2
    if pos1 == pos2:
        return puntos
    
    for p1 in pos1:
        if not (pos2.__contains__(p1)):
            puntos -= 0.5
        if puntos <= 0:
            return 0
    return puntos

def main (p1, p2):
    try:
        caracteres1 = []
        caracteres2 = []
        puntuacion = int(0)
        aux = None
        GenerarListaCaracteres(p1.upper(), caracteres1)
        GenerarListaCaracteres(p2.upper(), caracteres2)

        for char in caracteres1:
            aux = BuscarCaracter(char.getCaracter(), caracteres2)
            if aux != None:
                puntuacion += CompararPosiciones(char.getPositions(), aux.getPositions())
            #else: suma cero puntos
        # len(caracteres1)*4 es igual a la máxima puntiación que pueden tener
        # 0.5*(abs(len(p1) - len(p2))) es para descontar si hay longitud desigual
        puntuacion = puntuacion*100 / (len(caracteres1)*4 - 0.5*(abs(len(p1) - len(p2))))
        messagebox.showinfo("Resultado de la comparación",f"Las cadenas {p1} y {p2} tienen un parecido de: {puntuacion}%")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", f"Error en los valores ingresados: {e}")