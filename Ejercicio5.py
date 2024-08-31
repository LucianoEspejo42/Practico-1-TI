# -*- coding: latin-1 -*-

#from re import L
from persona import personaFija, personaVariable
import os
import csv

def crearFijoDat(lista, path):
    file = open(os.path.join(path, 'fijo.dat'), 'w')  # Une al path correctamente
    for p in lista:
        file.writelines([p.NomAp, p.Dir, p.Dni, p.EstudiosP, p.EstudiosS, p.EstudiosU, p.Hogar, p.ObraSocial, p.Trabaja, p.Mascota, p.Computadora])
    #file.close()  

def leerFijoDat(path):
    with open(os.path.join(path, 'fijo.dat'), 'r') as file:
        i = 1
        while True:
            NomAp = file.read(30).strip()
            if not NomAp:  # Termina si no hay m�s datos
                break
            print(f"|-----------Datos Persona {i}------------|")
            Dir = file.read(40).strip()
            Dni = file.read(8).strip()
            EstudiosP = file.read(1)
            EstudiosS = file.read(1)
            EstudiosU = file.read(1)
            Hogar = file.read(1)
            ObraSocial = file.read(1)
            Trabaja = file.read(1)
            Mascota = file.read(1)
            Computadora = file.read(1)
            imprimir = f"Nombre y Apellido: {NomAp}\nDireccion: {Dir}\nDNI: {Dni}\nEstudios Primarios: {EstudiosP}\nEstudios Secundarios: {EstudiosS}\nEstudios Universitarios: {EstudiosU}\nHogar Propio: {Hogar}\nObra Social: {ObraSocial}\nTrabaja: {Trabaja}\nMascota: {Mascota}\nComputadora: {Computadora}"
            #print(f"{NomAp}, {Dir}, {Dni}, {EstudiosP}, {EstudiosS}, {EstudiosU}, {Hogar}, {ObraSocial}, {Trabaja}, {Mascota}, {Computadora}")
            print(imprimir)
            i += 1
            
def crearVariableDat(lista, path):
    with open(os.path.join(path, 'variable.dat'), 'w') as file:
        for p in lista:
            file.write(f"{len(p.NomAp):02d}" + p.NomAp)  # Longitud y campo
            file.write(f"{len(p.Dir):02d}" + p.Dir)
            file.write(p.Dni)
            file.write(str(p.ByteBi).zfill(3))  # Asegura que el ByteBi se escribe correctamente


def leerVariableDat(path):
    with open(os.path.join(path, 'variable.dat'), 'r') as file:
        while True:
            length = file.read(2)
            if not length or not length.isdigit():
                print("Fin de archivo o longitud no valida.")
                break
            print(f"Length leido: {length}")  # Verifica el valor de length
            try:
                NomAp = file.read(int(length))
            except ValueError:
                print(f"Error: valor invalido '{length}' para conversion a int.")
                break

            length = file.read(2)
            if not length or not length.isdigit():
                print("Fin de archivo o longitud no valida.")
                break

            Dir = file.read(int(length))
            Dni = file.read(8)
            ByteBi = file.read(3).strip()  # Ajuste para leer el ByteBi de 3 d�gitos si se escribi� con zfill(3)
            print(f"{NomAp}, {Dir}, {Dni}, {ByteBi}")

def comparar_tamanios(path):
    fijo_size = os.path.getsize(os.path.join(path, 'fijo.dat'))
    variable_size = os.path.getsize(os.path.join(path, 'variable.dat'))
    print(f"Tamaño del archivo de longitud fija: {fijo_size} bytes")
    print(f"Tamaño del archivo de longitud variable: {variable_size} bytes")

if __name__ == "__main__":
    listaF = []
    listaV = []
    path = os.path.dirname(__file__) # Obtiene la ruta del script actual
    csv_path = os.path.join(path, 'file', 'persona.csv')

    with open(csv_path, newline='', encoding='utf-8', errors='replace') as File: #utf-8 para caracteres especiales
        reader = csv.reader(File, delimiter = ';')
        for f in reader:
            #print(f, len(f))  # Verifica el contenido y la cantidad de elementos en la lista `f`
            listaF.append(personaFija(*f)) # *f para desempaquetar, va por cada uno de los campos.
            listaV.append(personaVariable(*f))

    crearFijoDat(listaF, path)
    crearVariableDat(listaV, path)

    print("Datos leidos del archivo de longitud fija:")
    leerFijoDat(path)
    
    print("\nDatos leidos del archivo de longitud variable:")
    leerVariableDat(path)

    comparar_tamanios(path)
