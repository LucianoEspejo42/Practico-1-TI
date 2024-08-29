"""Enunciado: Desarrollar un programa para comparar dos cadenas, no en forma tradicional (carácter por carácter), 
sino que implemente un algoritmo, propuesto por Ud., que determine el parecido, 
por ejemplo de cadenas como: Juan Perez y Jaun Perez, Horacio López y Oracio López, 
cadenas que si se tratan en comparando carácter por carácter, son muy poco parecidas o incluso no se parecen en nada.
"""

from math import floor
import tkinter as tk
from tkinter import ttk

def distancia(s1, s2):
	
	# Si las cadenas son iguales
	if (s1 == s2):
		return 1.0

	# Longitud de las dos cadenas
	l1 = len(s1)
	l2 = len(s2)

	# Maxima distancia de match permitida
	max_dist = floor(max(l1, l2) / 2) - 1

	# Contador de coincidencias
	match = 0

	# Hash para las coincidencias
	hash_s1 = [0] * len(s1)
	hash_s2 = [0] * len(s2)


	for i in range(l1):

		# Buscar coincidencias
		for j in range(max(0, i - max_dist), 
					min(l2, i + max_dist + 1)):
			
			# Si hay coincidencia
			if (s1[i] == s2[j] and hash_s2[j] == 0):
				hash_s1[i] = 1
				hash_s2[j] = 1
				match += 1
				break

	# Si no hay coincidencias
	if (match == 0):
		return 0.0

	# Cantidad de trasposiciones
	t = 0
	point = 0

	# Contar numero de ocurrencias donde dos caracteres coincidan, pero hay una tercer coincidencia entre los indices
	for i in range(l1):
		if (hash_s1[i]):

			# Encontrar el siguiente caracter coincidente
			while (hash_s2[point] == 0):
				point += 1

			if (s1[i] != s2[point]):
				t += 1
			point += 1
	t = t//2

	# Devuelve la distancia
	return (match/ l1 + match / l2 +
			(match - t) / match)/ 3.0


# Función que procesa las cadenas
def procesar_cadenas():
    cadena1 = entrada1.get()
    cadena2 = entrada2.get()
    # Aquí puedes definir la lógica que deseas aplicar a las cadenas
    resultado = f"Cadena 1: {cadena1}\nCadena 2: {cadena2}\nSimilitud: {round(distancia(cadena1, cadena2), 6)}"
    etiqueta_resultado.config(text=resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Cadenas")

# Crear y ubicar los widgets
etiqueta1 = ttk.Label(ventana, text="Ingrese la primera cadena:")
etiqueta1.pack(padx=10, pady=5)

entrada1 = ttk.Entry(ventana, width=50)
entrada1.pack(padx=10, pady=5)

etiqueta2 = ttk.Label(ventana, text="Ingrese la segunda cadena:")
etiqueta2.pack(padx=10, pady=5)

entrada2 = ttk.Entry(ventana, width=50)
entrada2.pack(padx=10, pady=5)

boton_procesar = ttk.Button(ventana, text="Calcular Distancia", command=procesar_cadenas)
boton_procesar.pack(padx=10, pady=10)

etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.pack(padx=10, pady=10)

# Iniciar el bucle principal de eventos
ventana.mainloop()
