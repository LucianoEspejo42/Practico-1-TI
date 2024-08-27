import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import os
#Importar los ejercicios
import Ejercicio1, Ejercicio2, Ejercicio3

class Aplicacion(object):
    def __init__(self, app) -> None:
        self.__app = app
        self.contador_archivo = 0
        # Título de la ventana
        app.title("Práctico en máquina")
        # Tamaño de la ventana
        app.geometry("1080x660")
        # Resizable es para que no se pueda maximizar la ventana 
        app.resizable(False, False)

        # Colocando título
        label_title = ctk.CTkLabel(app, text="Práctico Teoría de la Información", font=("Arial", 24))
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
        frame1 = ctk.CTkFrame(app)
        self.frame2 = ctk.CTkFrame(app)
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
            )
        }

        # Mostrar el enunciado centrado
        enunciado_label = ctk.CTkLabel(frame, text=enunciados.get(ejercicio, "Seleccione un ejercicio."), font=("Arial", 18), justify="center")
        enunciado_label.pack(ipady=110, anchor='center')

        # Mostrar el botón "Resolver" debajo del enunciado
        resolver_button = ctk.CTkButton(frame, text="Resolver", command= lambda: self.resolver_enunciado(frame, ejercicio))
        resolver_button.pack(side='top',pady=10, anchor='center')

    def resolver_enunciado (self, frame, ejercicio):
        list_file = ['Ejercicio 1','Ejercicio 2','Ejercicio 3']
        self.destruir_ventana(frame)
        if ejercicio in list_file:
            self.label_enunciado = ctk.CTkButton(self.frame2, text="Seleccione Archivo", command=lambda: self.seleccion_archivo(ejercicio, frame))
            self.label_enunciado.pack(expand=True)

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

    def destroy_button(self):
        self.label_enunciado.destroy()

    def retroceder_al_ej_3 (self, frame, ejercicio):
        self.destruir_ventana(frame)
        self.mostrar_enunciado(frame, ejercicio)

    def procesar_ejercicio3 (self, file, namefile, frame):
        self.destroy_button()
        lista_mostrar = Ejercicio3.procesar_archivo(file, namefile)
        label_cabecera = ctk.CTkLabel(self.frame2, text=lista_mostrar, font=("Arial",18), justify="center")
        label_cabecera.pack(pady=10)

        self.contador_archivo += 1
        if self.contador_archivo >= 5:
            self.contador_archivo = 0
            self.destroy_button()
            self.boton_retroceder = ctk.CTkButton(self.frame2, text="Atras", command= lambda: self.retroceder_al_ej_3(frame,"Ejercicio 3"), bg_color='red')
            self.boton_retroceder.pack(padx=10)
        else:
            self.label_enunciado = ctk.CTkButton(self.frame2, text="Seleccionar otro archivo", command=lambda: self.seleccion_archivo("Ejercicio 3", frame))
            self.label_enunciado.pack(pady=10)
            

if __name__ == '__main__':
    root = ctk.CTk()
    Aplicacion(root)
    root.mainloop()
