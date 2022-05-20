# Correr el servidor de swipl con el comando
# swipl -l Servi.pl -g true -g servidor

# Cliente el servidor de Prolog
import socket
import sys
import ast


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
        if (reinas == "" or reinas == "3" or reinas == "2" or int(reinas) <= 0):
            # self.s.close()
            return []

        query = bytes(f'{reinas}.\n', 'ascii')  # dos lineas

        # try:
        #     self.s.sendall(b'1.\n')
        # except socket.error:
        #     print('Error de comunicacion')

        # self.s.recv(8192)

        try:
            self.s.sendall(query)
        except socket.error:
            print('Error de comunicacion')

        reply = self.s.recv(16384)
        # print(reply.decode())

        try:
            # print(ast.literal_eval(reply.decode()))
            return ast.literal_eval(reply.decode())
        except:
            # print("No se hizo el parser")
            return []


# coneccion = Conecta()

# while (True):
#     reinas = input("Numero de reinas ")
#     print(coneccion.query(reinas))
