"""
Clase caracter almacena:
Caracter    -> En mayúscula porque no hace diferencia a la hora de comparar el contenido
Cantidad    -> El total de apariciones que tiene
Posiciones  -> Las posiciones donde se ubica a lo largo de la cadena
"""
class Caracter:
    def __init__(self, c, position):
        self.caracter = str(c).upper()
        self.cantidad = int(1)
        self.posiciones = [position]
    
    def getCaracter(self):
        return self.caracter
    
    def getCantidad(self):
        return self.cantidad
    
    def incrCantidad(self):
        self.cantidad += 1
    
    def appendPosition(self, newPosition):
        self.posiciones.append(newPosition)
    
    def getPositions(self):
        return self.posiciones
    
    def getLastPosition(self):
        return self.posiciones[-1]