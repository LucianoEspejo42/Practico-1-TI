"""
Escribir un programa en lenguaje a elección, que permita:
    1) Ingresar el nombre de un archivo con extensión .bmp
    2) Valide que el archivo sea con el formato adecuado.
    3) Muestre los datos de la cabecera del archivo .bmp

Un archivo gráfico en formato BMP (bitmap) tiene la estructura que se ilustra en la siguiente figura:
                            Cabecera (14 bytes)
                    Propiedades de la imagen (40 bytes)
            Paleta de color (opcional - su tamaño puede variar)
                            Datos de la imagen
"""
import struct 

def validar_archivo_bmp (file_bmp):
    try:
        with open(file_bmp, 'rb') as file:
            bmp = file.read(2)
            if bmp[:2].decode('ascii') != 'BM':
                return False
            return True
    except Exception as e:
        print(f"Error al verificar el archivo {e}")

def mostrar_cabecera_bmp (file_bmp, name):
    try:
        with open(file_bmp, 'rb') as file:
            #Lista para mostrar por la ventana
            lista_cabecera = []
            lista_cabecera.append(f"Nombre del archivo: {name}")
            #Mostramos los datos de los primeros 14 bytes
            cabecera = file.read(14)
            lista_cabecera.append(f"Signature: {cabecera[:2].decode('ascii')}")
            file_size = struct.unpack('<I', cabecera[2:6])[0]
            lista_cabecera.append(f"File Size: {file_size} bytes")
            reserved = struct.unpack('<I', cabecera[6:10])[0]
            lista_cabecera.append(f"Reserved: {reserved}")
            data_offset = struct.unpack('<I', cabecera[10:14])[0]
            lista_cabecera.append(f"Data Offset: {data_offset}")

            #Propiedades de la imagen

            prop_img = file.read(40)
            size = struct.unpack('<I', prop_img[0:4])[0]
            lista_cabecera.append(f"Size: {size} bytes")
            width = struct.unpack('<I', prop_img[4:8])[0]
            lista_cabecera.append(f"Width: {width} px")
            height = struct.unpack('<I', prop_img[8:12])[0]
            lista_cabecera.append(f"Height: {height} px")
            planes = struct.unpack('<H', prop_img[12:14])[0]
            lista_cabecera.append(f"Planes: {planes}")
            bit_count = struct.unpack('<H', prop_img[14:16])[0]
            lista_cabecera.append(f"BitCount: {bit_count} px")
            compression = struct.unpack('<I', prop_img[16:20])[0]
            lista_cabecera.append(f"Compression: {compression}")
            image_size = struct.unpack('<I', prop_img[20:24])[0]
            lista_cabecera.append(f"ImageSize: {image_size}")
            XPixelsPerM = struct.unpack('<I', prop_img[24:28])[0]
            lista_cabecera.append(f"Resolución Horizontal: {XPixelsPerM} px/mts")
            YPixelsPerM = struct.unpack('<I', prop_img[28:32])[0]
            lista_cabecera.append(f"Resolución Vertical: {YPixelsPerM} px/mts")
            colour_used = struct.unpack('<I', prop_img[32:36])[0]
            lista_cabecera.append(f"Colores usados: {colour_used}")
            colour_imp = struct.unpack('<I', prop_img[36:40])[0]
            lista_cabecera.append(f"Colores importantes: {colour_imp}")

            return "\n".join(lista_cabecera)
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")
