import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
#Importar los ejercicios
import Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4, Ejercicio7, Ejercicio8

class Aplicacion(object):
    def __init__(self, app) -> None:
        self.__app = app
        self.contador_archivo = 0
        self.entry_matrix = list()
        # Título de la ventana
        app.title("Práctico en máquina")
        # Tamaño de la ventana
        app.geometry("1080x660")
        # Resizable es para que no se pueda maximizar la ventana 
        app.resizable(False, False)

        # Colocando título
        label_title = ctk.CTkLabel(self.__app, text="Práctico Teoría de la Información", font=("Arial", 24))
        label_title.pack(pady=10, padx=5)

        #Creando frames para colocar los botones y mostrar los resultados
        """
            Mi idea es hacer una interfaz de la siguiente manera:        
                _________   _______________________________     
                |__Ej1___|  |                              |
                |__Ej2___|  |                              |
                |__Ej3___|  |                              |
                |__Ej4___|  |    Seleccione Ejercicio      |
                |__Ej5___|  |                              |
                |__...___|  |                              |
                |__Ej9___|  |______________________________|
        """
        frame1 = ctk.CTkFrame(self.__app)
        self.frame2 = ctk.CTkFrame(self.__app)
        frame1.pack(side='left', pady=40, padx=25, fill='y')
        self.frame2.pack(side='left', pady=40, padx=25, fill='both', expand=True)
    
        # Label para mostrar el enunciado en self.frame2
        self.label_enunciado = ctk.CTkLabel(self.frame2, text="Seleccione Ejercicio...", font=("Arial", 20), wraplength=500, justify="center")
        self.label_enunciado.pack(expand=True, fill='both', anchor='center')

        # Botones sin usar un for
        self.boton1 = ctk.CTkButton(frame1, text="Ejercicio 1", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 1"))
        self.boton1.pack(pady=15)

        self.boton2 = ctk.CTkButton(frame1, text="Ejercicio 2", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 2"))
        self.boton2.pack(pady=15)

        self.boton3 = ctk.CTkButton(frame1, text="Ejercicio 3", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 3"))
        self.boton3.pack(pady=15)

        self.boton4 = ctk.CTkButton(frame1, text="Ejercicio 4", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 4"))
        self.boton4.pack(pady=15)

        self.boton5 = ctk.CTkButton(frame1, text="Ejercicio 5", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 5"))
        self.boton5.pack(pady=15)

        self.boton6 = ctk.CTkButton(frame1, text="Ejercicio 6", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 6"))
        self.boton6.pack(pady=15)

        self.boton7 = ctk.CTkButton(frame1, text="Ejercicio 7", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 7"))
        self.boton7.pack(pady=15)

        self.boton8 = ctk.CTkButton(frame1, text="Ejercicio 8", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 8"))
        self.boton8.pack(pady=15)

        self.boton9 = ctk.CTkButton(frame1, text="Ejercicio 9", command=lambda: self.mostrar_enunciado(self.frame2, "Ejercicio 9"))
        self.boton9.pack(pady=15)


    def destruir_ventana (self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def mostrar_enunciado(self, frame, ejercicio):

        if self.contador_archivo != 0:
            self.contador_archivo = 0
        # Limpia el frame antes de mostrar el nuevo enunciado
        self.destruir_ventana(frame)

        # Enunciados
        enunciados = {
            "Ejercicio 1":(
                "Escribir un programa en lenguaje a elección, que permita:\n"
                "1) Ingresar el nombre de un archivo con extensión .wav\n"
                "2) Valide que el archivo sea con el formato adecuado.\n"
                "3) Muestre los datos de la cabecera del archivo .wav"
            ),
            "Ejercicio 2": (
                "Escribir un programa en lenguaje a elección, que permita:\n"
                "1) Ingresar el nombre de un archivo con extensión .bmp\n"
                "2) Valide que el archivo sea con el formato adecuado.\n"
                "3) Muestre los datos de la cabecera del archivo .bmp\n\n"
                "Un archivo gráfico en formato BMP (bitmap) tiene la estructura que se ilustra en la siguiente figura:\n"
                "Cabecera (14 bytes)\n"
                "Propiedades de la imagen (40 bytes)\n"
                "Paleta de color (opcional - su tamaño puede variar)\n"
                "Datos de la imagen"
            ),
            "Ejercicio 3": (
                "Desarrollar una aplicación de software que calcule la entropía y redundancia, de una fuente\n"
                "con símbolos vistos en forma independiente y dependiente en O(1).\n"
                "Realizar comparaciones para diferentes archivos (*.txt, *.exe, *.zip etc.).\n"
                "\n"
                "Nota: Solo puede abrir 5 archivos"
            ),
            "Ejercicio 4": (
                "Desarrollar una aplicación de software que calcule la Capacidad de Canal de un\n"
                "canal R-ario Uniforme y No-Uniforme. El soft debe aceptar como entrada el valor de R\n"
                "que identifica al canal (R= 2 Binario, R=3 Ternario hasta R=4) los valores\n"
                "de probabilidades condicionales que representan la matriz del canal entregando\n" 
                "como salida el valor de las probabilidades independientes de cada uno de los símbolos\n"
                "de entrada que maximiza la información mutua, esto es, lograr la capacidad de canal."
            ),
            "Ejercicio 5": (
                "Este ejercicio no se encuentra hecho en esta aplicación por que se nos dificulto la\n"
                "implementación del mismo, le recomiendo que lo ejecute por terminal\n"
                "Gracias y disculpas"
            ),
            "Ejercicio 6": (
                "Genere un informe que marque las diferencias esenciales (tipo de documento, si es un formato\n"
                "comprimido o no, tamaños, calidades, etc.) entre los siguientes documentos de texto *.doc, *.docx,\n"
                "*.djvu, *.pdf, *.epub. Encuentre una aplicación que a un archivo de texto en cualquier formato pueda\n"
                "pasarlo a la mayoría de los restantes."
            ),
            "Ejercicio 7": (
                "Desarrollar un programa para comparar dos cadenas, no en forma tradicional (carácter por carácter),\n"
                "sino que implemente un algoritmo, propuesto por Ud., que determine el parecido, por ejemplo\n" 
                "de cadenas como: Juan Perez y Jaun Perez, Horacio López y Oracio López, cadenas que si se tratan en\n"
                "comparando carácter por carácter, son muy poco parecidas o incluso no se parecen en nada."
            ),
            "Ejercicio 8": (
                "Implementar un programa que valide un CUIT/CUIL ingresado por teclado."
            ),
            "Ejercicio 9": (
                "Este ejercicio no se encuentra hecho en esta aplicación por que se nos dificulto la\n"
                "implementación del mismo, le recomiendo que lo ejecute por terminal\n"
                "Gracias y disculpas"
            )
        }

        # Mostrar el enunciado centrado
        enunciado_label = ctk.CTkLabel(frame, text=enunciados.get(ejercicio, "Seleccione un ejercicio."), font=("Arial", 18), justify="center")
        enunciado_label.pack(ipady=110, anchor='center')

        # Mostrar el botón "Resolver" debajo del enunciado
        if ejercicio == 'Ejercicio 6':
            resolver_button = ctk.CTkButton(frame, text="Abrir el archivo .docx", command= lambda: self.procesar_ejercicio6(ruta=r"\Práctico Maquina\Ejercicio6(Resolución).docx"))
            resolver_button.pack(side='top',pady=10, anchor='center')

        if ejercicio != 'Ejercicio 5' and ejercicio != 'Ejercicio 6' and ejercicio != 'Ejercicio 9':
            if ejercicio == 'Ejercicio 3':
                resolver_button = ctk.CTkButton(frame, text="Ver comparacion", command= lambda: self.procesar_ejercicio6(ruta=r"\Práctico Maquina\Comparación Ejercicio 3.docx"))
                resolver_button.pack(side='top',pady=10, anchor='center')
            resolver_button = ctk.CTkButton(frame, text="Resolver", command= lambda: self.resolver_enunciado(frame, ejercicio))
            resolver_button.pack(side='top',pady=10, anchor='center')

    def resolver_enunciado (self, frame, ejercicio):
        list_file = ['Ejercicio 1','Ejercicio 2','Ejercicio 3']
        self.destruir_ventana(frame)
        if ejercicio in list_file:    
            self.label_enunciado = ctk.CTkButton(self.frame2, text="Seleccione Archivo", command=lambda: self.seleccion_archivo(ejercicio, frame))
            self.label_enunciado.pack(expand=True)
        else:
            if ejercicio == 'Ejercicio 4':
                self.procesar_ejercicio4(frame)
            elif ejercicio == 'Ejercicio 7':
                self.procesar_ejercicio7(frame)
            elif ejercicio == 'Ejercicio 8':
                self.procesar_ejercicio8(frame)

    def seleccion_archivo (self, ejercicio, frame):
        if ejercicio == "Ejercicio 1":
            types = [("WAV files", "*.wav"), ("All files", "*.*")]
        elif ejercicio == "Ejercicio 2":
            types = [("BMP files", "*.bmp"), ("All files", "*.*")]
        elif ejercicio == "Ejercicio 3":
            types = [("All files", "*.*")]

        file = filedialog.askopenfilename(title="Seleccione Archivo", filetypes=types)
        name_file = os.path.basename(file)
        if not file:
            messagebox.showerror("ERROR","No se selecciono archivo")
            return
        
        if ejercicio == "Ejercicio 1":
            self.procesar_ejercicio1(file, name_file, frame)
        elif ejercicio == "Ejercicio 2":
            self.procesar_ejercicio2(file,name_file,frame)
        elif ejercicio == "Ejercicio 3":
            self.procesar_ejercicio3(file,name_file,frame)


    def procesar_ejercicio1 (self, file, namefile, frame):

        self.destruir_ventana(frame)
        if Ejercicio1.validar_archivo_wav(file):
            cabecera = Ejercicio1.mostrar_cabecera_wav(file,namefile)
            label_cabecera = ctk.CTkLabel(self.frame2, text=cabecera, font=("Arial",18), justify="center")
            label_cabecera.pack(pady=10)
            label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 1", frame))
            label_enunciado.pack(expand=True)
        else:
            # Label para mostrar el enunciado en self.frame2
            label1 = ctk.CTkLabel(self.frame2, text=f"Error: El archivo {namefile} no es un archivo .wav valido", font=("Arial", 18), wraplength=500, justify="center")
            label1.pack(expand=True)
            label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 1", frame))
            label_enunciado.pack(expand=True)

    def procesar_ejercicio2 (self, file, namefile, frame):

        self.destruir_ventana(frame)
        if Ejercicio2.validar_archivo_bmp(file):
            cabecera = Ejercicio2.mostrar_cabecera_bmp(file,namefile)
            label_cabecera = ctk.CTkLabel(self.frame2, text=cabecera, font=("Arial",18), justify="center")
            label_cabecera.pack(pady=10)
            label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 2", frame))
            label_enunciado.pack(expand=True)
        else:
            # Label para mostrar el enunciado en self.frame2
            label1 = ctk.CTkLabel(self.frame2, text=f"Error: El archivo {namefile} no es un archivo .bmp valido", font=("Arial", 18), wraplength=500, justify="center")
            label1.pack(expand=True)
            label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 1", frame))
            label_enunciado.pack(expand=True)

    def destroy_button(self,ej):
        if ej == 'Ejercicio 3':
            self.label_enunciado.destroy()
        elif ej == 'Ejercicio 4':
            self.button_calcular.destroy()

    def retroceder_al_ej_3 (self, frame, ejercicio):
        self.destruir_ventana(frame)
        self.mostrar_enunciado(frame, ejercicio)

    def procesar_ejercicio3 (self, file, namefile, frame):

        self.destroy_button("Ejercicio 3")

        lista_mostrar = Ejercicio3.procesar_archivo(file, namefile)
        label_cabecera = ctk.CTkLabel(self.frame2, text=lista_mostrar, font=("Arial",18), justify="center")
        label_cabecera.pack(pady=10)

        self.contador_archivo += 1
        if self.contador_archivo >= 5:
            self.contador_archivo = 0
            self.destroy_button("Ejercicio 3")
            self.boton_retroceder = ctk.CTkButton(self.frame2, text="Atras", command= lambda: self.retroceder_al_ej_3(frame,"Ejercicio 3"))
            self.boton_retroceder.pack(padx=10)
        else:
            self.label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 3", frame))
            self.label_enunciado.pack(pady=10)
    
    #En esta función se procesa el eejrcicio 4
    def procesar_ejercicio4 (self, frame):

        # Botón para seleccionar canal 
        self.button_binario = ctk.CTkButton(frame, text="Canal Binario", command=lambda: self.mostrar_matriz(long=2,placex=7,placey=300,num1=10,num2=140))
        self.button_ternario = ctk.CTkButton(frame, text="Canal Ternario", command= lambda: self.mostrar_matriz(long=3,placex=22.5,placey=350))
        self.button_cuaternario = ctk.CTkButton(frame, text="Canal Cuaternario", command=lambda: self.mostrar_matriz(long=4,placex=33.8,placey=400))
        self.button_binario.grid(row=0,column=1, padx=(100, 25), pady=30, sticky="w")
        self.button_ternario.grid(row=0,column=5, padx=(100, 25), pady=30, sticky="w")
        self.button_cuaternario.grid(row=0,column=6, padx=(100, 25), pady=30, sticky="w")

    def destroy_entry (self, long):
        for row in self.entry_matrix:
            for entry in row:
                entry.destroy()
        
        if hasattr(self, 'button_calcular'):
            self.destroy_button('Ejercicio 4')

    def mostrar_matriz(self, long, placex, placey, num1 = 5, num2 = 130):
        
        if len(self.entry_matrix) != 0:
            self.destroy_entry(len(self.entry_matrix))
            #self.destroy_button("Ejercicio 4")
        
        self.entry_matrix = [[None for _ in range(long)] for _ in range(long)]
        #print(self.entry_matrix)
        # 2x2 = 10 + 140; 3x3=4x4= 5 + 130
        # Calcular el desplazamiento para centrar la matriz horizontalmente
        matrix_width = long * (num1 + num2) - 120  # Ancho total de la matriz
        offset_x = (880 - matrix_width) // 2

        for i in range(long):
            for j in range(long):
                self.entry_matrix[i][j] = ctk.CTkEntry(self.frame2, width=51)
                self.entry_matrix[i][j].place(x=offset_x + j * 120, y=150 + i * 50)
        
        # Botón para calcular
        #2x2 x=115, y=400;3x3 x=94, y=410; 4x4 x=87 y=480
        self.button_calcular = ctk.CTkButton(self.frame2, text="Calcular", command= lambda: Ejercicio4.main(self.entry_matrix))
        self.button_calcular.place(x=offset_x + long * placex, y= placey)

    def procesar_ejercicio6 (self, ruta):

        path = os.path.dirname(__file__)
        ruta_archivo = path + ruta
        
        try:
            # Intentar abrir el archivo usando la aplicación predeterminada del sistema
            if os.name == 'nt':  # Windows
                os.startfile(ruta_archivo)
            elif os.name == 'posix':  # MacOS o Linux
                subprocess.call(['open', ruta_archivo] if os.uname().sysname == 'Darwin' else ['xdg-open', ruta_archivo])
        except Exception as e:
            # Mostrar un cuadro de mensaje de error
            messagebox.showerror("Error", "Parece que hubo un problema al abrir el archivo, por favor inténtelo de manera manual.")

    def procesar_ejercicio7 (self, frame):

        self.destruir_ventana(frame)

        # Crear un frame para centrar el contenido
        frame_centro = ctk.CTkFrame(frame)
        frame_centro.pack(expand=True, fill='both')
        
        # Crear etiquetas y entradas
        texto1 = ctk.CTkLabel(frame_centro, text="Ingrese texto 1", font=("Arial", 18), wraplength=500, justify='center')
        texto2 = ctk.CTkLabel(frame_centro, text="Ingrese texto 2", font=("Arial", 18), wraplength=500, justify='center')
        cadena_uno = ctk.CTkEntry(frame_centro, width=180, height=30, justify='center') 
        cadena_dos = ctk.CTkEntry(frame_centro, width=180, height=30, justify='center')
        
        # Colocar etiquetas y entradas en el frame_centro
        texto1.pack(padx=10, pady=(20, 10))
        cadena_uno.pack(padx=15, pady=10)
        texto2.pack(padx=10, pady=(20, 10))
        cadena_dos.pack(padx=15, pady=10)

        # Botón de comparación
        boton_comparar = ctk.CTkButton(frame_centro, text="Comparar Cadenas", command=lambda: Ejercicio7.procesar_cadenas(cadena_uno, cadena_dos))
        boton_comparar.pack(pady=20)

    def procesar_ejercicio8 (self, frame):

        self.destruir_ventana(frame)
        # Crear y ubicar los widgets
        etiqueta = ctk.CTkLabel(frame, text="Ingrese el CUIT/CUIL (formato XX-XXXXXXXX-X):", font=("Arial", 18), wraplength=500, justify='center')
        etiqueta.pack(padx=10, pady=(20, 10))

        entrada_codigo = ctk.CTkEntry(frame, width=180, height=30, justify='center')
        entrada_codigo.pack(padx=15, pady=10)
        
        etiqueta_resultado = ctk.CTkLabel(frame, text="", font=("Arial", 18), wraplength=500, justify='center')
        etiqueta_resultado.pack(padx=10, pady=10)

        boton_validar = ctk.CTkButton(frame, text="Validar", command=lambda: Ejercicio8.procesar_codigo(entrada_codigo, etiqueta_resultado))
        boton_validar.pack(padx=10, pady=20)


if __name__ == '__main__':
    
    # Configuración inicial de customtkinter
    ctk.set_appearance_mode("System")  # Modo de apariencia
    ctk.set_default_color_theme("green")  # Tema de color
    root = ctk.CTk()
    Aplicacion(root)
    root.mainloop()
