from Persona import PersonaFija, PersonaVariable
import os
import csv

def CrearDatFijo(lista, path):
    file = open(path+"\\DatPersonasFijo.dat", "w")
    for p in lista:
        file.writelines([p.ApNom, p.Dir, p.Dni, p.EstudiosP, p.EstudiosS, p.EstudiosU, p.Casa, p.ObraSocial, p.Trabaja, p.Auto, p.Jubilado])
    file.close

def LeerDatFijo(path):
    file = open(path+"\\DatPersonas.dat", "r")
    for p in file:
        print(p)

def CrearDatVariable(lista, path):
    file = open(path+"\\DatPersonasVariable.dat", "w")
    for p in lista:
        file.write(str(len(p.ApNom)))
        file.write(p.ApNom)
        file.write(str(len(p.Dir)))
        file.write(p.Dir)
        file.write(p.Dni)
        file.write(str(p.ByteBivaluado))
    file.close()


if __name__ == "__main__":
    listaF = []
    listaV = []
    path = os.path.dirname(__file__)
    with open(os.path.join(path+"\\DatosPersonas.csv")) as File:
        reader = csv.reader(File, delimiter=';')
        for f in reader:
            #Creamos las dos listas al mismo tiempo para despues escribir los archivos
            listaF.append(PersonaFija(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))
            listaV.append(PersonaVariable(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10]))
        File.close
    
    for d in listaV:
        d.Mostrar()
        print("\n")
    
    CrearDatFijo(listaF, path)
    LeerDatFijo(path)
    CrearDatVariable(listaV, path)