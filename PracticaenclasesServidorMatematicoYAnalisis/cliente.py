from socket import *

HOST = '127.0.0.1'  # Dirección IP del servidor local
PORT = 65432        # Mismo puerto que el servidor

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Conectado al servidor.")
print("Escribe mensajes para enviarlos al servidor.")
print("Escribe 'salir' para terminar.\n")

while True:
    msg = input("Cliente: ")

    if msg.lower() == 'salir':
        print("Cerrando conexión...")
        break

    s.send(msg.encode())

    data = s.recv(1024)
    print(f"Servidor: {data.decode()}")

s.close()
print("Cliente cerrado.")