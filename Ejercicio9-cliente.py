"""Enunciado:
En la actualidad, muchos de los procesos que se ejecutan en una computadora requiere obtener o enviar información a otros procesos que se 
localizan en una computadora diferente, o en la misma. Para lograr esta comunicación se utilizan los protocolos de comunicación TCP y UDP. 
Una implementación de comunicación entre procesos, se puede realizar utilizando sockets.
Los sockets son una forma de comunicación entre procesos que se encuentran en diferentes máquinas de una red, 
los sockets proporcionan un punto de comunicación por el cual se puede enviar o recibir información entre procesos.
Los sockets tienen un ciclo de vida dependiendo si son sockets de servidor, que esperan a un cliente para establecer una comunicación, 
o socket cliente que busca a un socket de servidor para establecer la comunicación.
Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un servidor y un cliente en lenguaje Python), 
que permita desde el cliente, enviar un archivo comprimido utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.
"""

import socket
#Servidor y Cliente se ejecutan en la misma máquina, conocida como localhost
#su dirección es 127.0.0.1
servidor = "127.0.0.1"
puerto = 5555
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
Mensaje = "hola mundo"
cliente.send(Mensaje.encode('utf-8'));
respuesta = cliente.recv(4096)
print ("[*] Respuesta recibida: "+str(respuesta))
Mensaje = "Mande frutas"
cliente.send(Mensaje.encode('utf-8'))
respuesta = cliente.recv(4096)
print ("[*] Respuesta recibida: "+str(respuesta))
cliente.close()