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
def conexiones(socket_cliente):
    peticion = socket_cliente.recv(1024)
    print ("[*] Mensaje recibido: %s" % peticion)
    respuesta = commands.getoutput(peticion)
    socket_cliente.send(respuesta)
    socket_cliente.close()
ip = "0.0.0.0"
puerto = 5555
max_conexiones = 5
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, puerto))
servidor.listen(max_conexiones)
print ("[*] Esperando conexiones en %s:%d" % (ip, puerto))
cliente, direccion = servidor.accept()
while True:
    print ("[*] Conexion establecida con %s:%d" % (direccion[0] , direccion[1]))
    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro
    #la cantidad de bytes para recibir
    recibido = cliente.recv(1024)
    #Si el mensaje recibido es la palabra close se cierra la aplicacion
    if recibido == "close":
        break
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print (str(direccion[0]) + " dice: ", recibido)
    #Devolvemos el mensaje al cliente
    cliente.send(recibido)
print ("Adios.")
#Cerramos la instancia del socket cliente y servidor
cliente.close()
servidor.close()