#Enunciado: Implementar un programa que valide un CUIT/CUIL ingresado por teclado.

import tkinter as tk
from tkinter import ttk
import re

import re
from argparse import ArgumentParser


class Cuit:
  # Codigo de verificacion
  VERIFICATION_CODE  = '5432765432'
  MESSAGES = {
      'valid'          : 'El código «{cuit}», es válido.',
      'invalid'        : ('Introdujo «{cuit}» y éste no es un número de '
                          'CUIT válido.'),
      'invalid_chars'  : ('Solo puede introducir: números, guiones'
                          'medios, puntos o espacios.'),
      'invalid_length' : 'El número de CUIT debe tener 11 dígitos.'
  }


  def __init__(self, cuit):
    self.cuit   = str(cuit)
    self.number = self.filter_chars()


  def validate_digits(self):
    return True if len(self.number) == 11 else False


  def validate_chars(self):
    '''Valida si la infomración pasada por parámetro es adecuada.
    Caracteres válidos (0-9-.\s)
    '''
    try:
      regex   = re.compile(r'^([0-9\-\.\s]+)$')
      matches = re.search(regex, self.cuit)
      if matches:
          return True
      return False
    except:
      return False


  def filter_chars(self):
    '''Limpia el valor de cualquier caracter que no sea un número.
    '''
    regex  = re.compile(r'[^0-9]')
    subst  = ''
    result = re.sub(regex, subst, self.cuit, 0)
    return result


  def digito_verificador(self):
    """Calcula el dígito verificador.

    Digitos verificadores, por cada uno debe multiplicarse los numeros
    del cuit respectivamente.

    Returns:
      [int] -- Número verificador
    """
    cuit = self.number
    digito_verificador = None

    v1 = 0
    for i in range(10):
      v1 += int(Cuit.VERIFICATION_CODE[i]) * int(cuit[i])

    # obtengo el resto
    v2 = v1 % 11
    # 11 menos el resto
    v3 = 11 - v2
    # si el ressultado de v3 es == 11. El valor es 0
    if v3 == 11:
      digito_verificador = 0
    # si v3 es igual a 10. El valor es 9
    elif v3 == 10:
      # return False
      digito_verificador = 9
    # en todos los demas casos es el v3
    else:
      digito_verificador = v3

    return digito_verificador


  def is_valid_digito_verificador(self):
    """Valida que el número verificador coincida con el del número de
    CUIL ingresado.

    Returns:
      bool
    """
    digito_verificador = self.digito_verificador()
    if int(self.number[-1:]) == digito_verificador:
      return True

    return False


  def messages(self):
    """Mensajes de validación.
    """
    mensajes = []
    if self.is_valid():
      mensajes.append(self.MESSAGES.get('valid').format(cuit=self.cuit))
    else:
      mensajes.append(self.MESSAGES.get('invalid').format(cuit=self.cuit))

    if not self.validate_chars():
      mensajes.append(self.MESSAGES.get('invalid_chars'))

    if not self.validate_digits():
      mensajes.append(self.MESSAGES.get('invalid_length'))

    return mensajes


  def is_valid(self):
    num = self.number
    if self.validate_chars()\
        and self.validate_digits()\
        and self.is_valid_digito_verificador():
      return True

    return False


# Función para procesar la entrada del usuario
def procesar_codigo():
    codigo = Cuit(entrada_codigo.get())
    if (codigo.is_valid()):
        etiqueta_resultado.config(text="El CUIT/CUIL es válido.")
    else:
        etiqueta_resultado.config(text="El CUIT/CUIL no es válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Validador de CUIT/CUIL")

# Crear y ubicar los widgets
etiqueta = ttk.Label(ventana, text="Ingrese el CUIT/CUIL (formato XX-XXXXXXXX-X):")
etiqueta.pack(padx=10, pady=5)

entrada_codigo = ttk.Entry(ventana, width=25)
entrada_codigo.pack(padx=10, pady=5)

boton_validar = ttk.Button(ventana, text="Validar", command=procesar_codigo)
boton_validar.pack(padx=10, pady=10)

etiqueta_resultado = ttk.Label(ventana, text="")
etiqueta_resultado.pack(padx=10, pady=10)

# Iniciar el bucle principal de eventos
ventana.mainloop()
