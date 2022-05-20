# Para correr esta aplicación:
# Primero: Correr el servidor de swipl con el comando:
# swipl -l Servi.pl -g true -g servidor
# Luego ejecutar la gui:
# python GUIClase.py

# Cliente el servidor de Prolog
import socket  # Librería para conectarse al server
import sys     # Interactuar con el sistema
import ast     # Compilar string a lista


class Conecta():
    # Dirección del servidor de prolog
    host = 'localhost'
    # Puerto del servidor de prolog
    port = 50000
    # Creamos un socket para leer el stack
    s: socket.socket

    def __init__(self):
        # Crea socket
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Error al crear el socket')
            sys.exit()

        # Obtener las dirección del socket
        try:
            remote_ip = socket.gethostbyname(self.host)
        except socket.gaierror:
            print('Error, direccion no encontrada')
            sys.exit()

        # Conectandose al sistema
        print(f'Conectandose al servidor {self.host} en el puerto {self.port}')
        self.s.connect((remote_ip, self.port))

    # Función que le manda un string al socket de prolog y obtiene una solución
    def query(self, reinas):
        # Mandamos una petición al servidor
        # Esta petición contiene el número de reinas, un punto y el char enter
        # Convertimos este string es bytes, para que pueda ser
        #   interpretado por el socket
        query = bytes(f'{reinas}.\n', 'ascii')

        # Envia la petición al servidor
        try:
            self.s.sendall(query)
        except socket.error:
            print('Error de comunicacion')

        # Leemos la respuesta que mandó el servidor en el socket
        reply = self.s.recv(16384)

        # La respuesta viene en formato de bytes, tratamos de
        #   convertirla a una lista de números
        try:
            return ast.literal_eval(reply.decode())
        except SyntaxError:
            return []
