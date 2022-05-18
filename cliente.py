# Cliente el servidor de Prolog
import socket
import sys


class Conecta():
    host = 'localhost'
    port = 50000
    s: socket.socket

    def __init__(self):
        # Crea socket
        print('Creando socket')
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Error al crear el socket')
            sys.exit()

        print('Obteniendo dir ip')
        try:
            remote_ip = socket.gethostbyname(self.host)
        except socket.gaierror:
            print('Error, direccion no encontrada')
            sys.exit()

        # Conectandose al sistema
        print(f'Conectandose al servidor {self.host} en el puerto {self.port}')
        self.s.connect((remote_ip, self.port))

    # TODO:
    def query(self, reinas):
        # Haciendo una query ¿pertenece 3 a la lista [2,3,4,5]
        # Pide los datos
        # elem = ''

        query = bytes(f'{reinas}.\n', 'ascii')  # dos lineas

        try:
            self.s.sendall(query)
        except socket.error:
            print('Error de comunicacion')

        reply = self.s.recv(256)
        print(reply)
        return reply

        # Lo de las listas
        # while elem != 'fin':
        #     # lista = input('Dame la lista:')
        #     # elem = input('Dame el elemento:')

        #     query = bytes(f'{lista}.\n{elem}.\n', 'ascii')  # dos lineas

        #     try:
        #         self.s.sendall(query)
        #     except socket.error:
        #         print('Error de comunicacion')

        #     reply = self.s.recv(256)
        #     print(reply)

        # Lo del metro
        # while elem != 'fin':
        #     elem = input('Dame la estacion:')
        #     query = bytes(f'{elem}.\n', 'ascii')

        #     try:
        #         self.s.sendall(query)
        #     except socket.error:
        #         print('Error de comunicacion')

        #     reply = self.s.recv(512)
        #     print(reply)

        self.s.close()
