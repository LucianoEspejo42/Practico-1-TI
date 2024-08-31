class personaFija:
    def __init__(self, nomAp, dir, dni, estudiosP, estudiosS, estudiosU, hogar, obraSocial, trabaja, mascota, computadora):
        #Definimos los tama�os para cada atributo
        if len(nomAp) < 30:
            self.NomAp = nomAp + ' ' * (30 - len(nomAp))
        elif len(nomAp) > 30:
            self.NomAp = nomAp[:30]
        else:
            self.NomAp = nomAp

        if len(dir) < 40:
            self.Dir = dir + ' ' * (40 - len(dir))
        elif len(dir) > 40:
            self.Dir = dir[:40]
        else:
            self.Dir = dir

        self.Dni = dni[:8]

        self.EstudiosP = estudiosP[0]
        self.EstudiosS = estudiosS[0]
        self.EstudiosU = estudiosU[0]
        self.Hogar = hogar[0]
        self.ObraSocial = obraSocial[0]
        self.Trabaja = trabaja[0]
        self.Mascota = mascota[0]
        self.Computadora = computadora[0]

    def Mostrar(self):
        print(f"Nombre y Apellido: {self.NomAp}\n")
        print(f"Direccion: {self.Dir}\n")
        print(f"DNI: {self.Dni}\n")
        print(f"Estudios Primarios: {self.EstudiosP}\n")
        print(f"Estudios Secundarios: {self.EstudiosS}\n")
        print(f"Estudios Universitarios: {self.EstudiosU}\n")
        print(f"Tiene hogar propio: {self.Hogar}\n")
        print(f"Tiene Obra Socual: {self.ObraSocial}\n")
        print(f"Trabaja: {self.Trabaja}\n")
        print(f"Tiene mascotas: {self.Mascota}\n")
        print(f"Tiene computadora: {self.Computadora}\n")

class personaVariable:
    def __init__(self, nomAp, dir, dni, estudiosP, estudiosS, estudiosU, hogar, obraSocial, trabaja, mascota, computadora):
        self.NomAp = nomAp
        self.Dir = dir
        self.Dni = dni[:8]
        self.ByteBi = self.Bi(estudiosP, estudiosS, estudiosU, hogar, obraSocial, trabaja, mascota, computadora)

    def Mostrar(self):
        print(f"Nombre y Apellido: {self.NomAp}")
        print(f"Direccion: {self.Dir}")
        print(f"DNI: {self.Dni}")
        #Mascara para el byte que contiene cada bit
        byteMasc = int('10000000',2)
        campos = [
            "Estudios Primarios",
            "Estudios Secundarios",
            "Estudios Universitarios",
            "Hogar Propio",
            "Obra Social",
            "Trabaja",
            "Tiene Mascotas",
            "Tiene Computadora"
        ]
        for i in range(8):
            if self.ByteBi & byteMasc == 0:
                print(f"{campos[i]}: No")
            else:
                print(f"{campos[i]}: Si")
            byteMasc = byteMasc >> 1

    def Bi(self, eP, eS, eU, hP, oS, t, m, c):
        byte = int('00000000',2)
        if eP == 'S':
            byte = byte | int('10000000',2) #10000000 = 128 en b
        if eS == 'S':
            byte = byte | int('01000000',2) #01000000 = 64 en b
        if eU == 'S':
            byte = byte | int('00100000',2) #00100000 = 32 en b
        if hP == 'S':
            byte = byte | int('00010000',2) #00010000 = 16 en b
        if oS == 'S':
            byte = byte | int('00001000',2) #00001000 = 8 en b
        if t == 'S':
            byte = byte | int('00000100',2) #00000100 = 4 en b
        if m == 'S':
            byte = byte | int('00000010',2) #00000010 = 2 en b
        if c == 'S':
            byte = byte | int('00000001',2) #00000001 = 1 en b
        return byte