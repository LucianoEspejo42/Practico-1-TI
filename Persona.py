class PersonaFija:
    def __init__(self, apNom, dir, dni, estudiosP, estudiosS, estudiosU, casa, obraSocial, trabaja, auto, jubilado):
        #Definimos el nombre con tamaño 40
        if len(apNom) < 40:
            self.ApNom = apNom + (" "*(40-len(apNom)))
        elif len(apNom) > 40:
            self.ApNom = apNom[:40]
        else:
            self.ApNom = apNom
        
        #Definimos dirección con tamaño 40
        if len(dir) < 40:
            self.Dir = dir + (" "*(40-len(dir)))
        elif len(dir) > 40:
            self.Dir = dir[:40]
        else:
            self.Dir = dir
        
        #Definimos el dni con tamaño 8
        self.Dni = dni[:8]
        
        #Definimos los campos bivaluados con S/N
        self.EstudiosP = estudiosP[0]
        self.EstudiosS = estudiosS[0]
        self.EstudiosU = estudiosU[0]
        self.Casa = casa[0]
        self.ObraSocial = obraSocial[0]
        self.Trabaja = trabaja[0]
        self.Auto = auto[0]
        self.Jubilado = jubilado[0]
    
    def Mostrar(self):
        print(f"Apellido y Nombre: {self.ApNom}\n")
        print(f"Dirección: {self.Dir}\n")
        print(f"DNI: {self.Dni}")
        print(f"Estudios Primarios: {self.EstudiosP}\tEstudios Secundarios: {self.EstudiosS}\tEestudios Universitarios: {self.EstudiosU}")
        print(f"Tiene casa: {self.Casa}\tTiene Obra Social: {self.ObraSocial}\tTiene auto:{self.Auto}")
        print(f"Es jubilado: {self.Jubilado}")

class PersonaVariable:
    def __init__(self, apNom, dir, dni, estudiosP, estudiosS, estudiosU, casa, obraSocial, trabaja, auto, jubilado):
        self.ApNom = apNom
        self.Dir = dir
        self.Dni = dni[:8]
        self.ByteBivaluado = self.Bivaluado(estudiosP, estudiosS, estudiosU, casa, obraSocial, trabaja, auto, jubilado)
    
    def Mostrar(self):
        print(f"Apellido y Nombre: {self.ApNom}")
        print(f"Dirección: {self.Dir}")
        print(f"DNI: {self.Dni}")
        #Definimos una máscara para verificar cada uno de los bits del byte en cuestión
        byteMask = int('10000000',2)
        for i in range(8):
            if self.ByteBivaluado & byteMask == 0:
                print(f"Campo {i+1}: Si")
            else:
                print(f"Campo {i+1}: No")
            byteMask = byteMask >> 1

    def Bivaluado(self, eP, eS, eU, c, oS, t, a, j):
        byte = int('00000000',2)
        if eP == 'S':
            byte = byte | int('10000000',2)
        if eS == 'S':
            byte = byte | int('01000000',2)
        if eU == 'S':
            byte = byte | int('00100000',2)
        if c == 'S':
            byte = byte | int('00010000',2)
        if oS == 'S':
            byte = byte | int('00001000',2)
        if t == 'S':
            byte = byte | int('00000100',2)
        if a == 'S':
            byte = byte | int('00000010',2)
        if j == 'S':
            byte = byte | int('00000001',2)
        return byte


