from socket import *

HOST = '26.122.88.172'  # Dirección IP del servidor (local)
PORT = 65432        # Mismo puerto que el servidor

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # Conectar al servidor

print("Conectado al servidor.")
print("Escribe mensajes ('salir' para terminar).")

while True:
    msg = input("Cliente: ")
    if msg.lower() == 'salir':
        print("Cerrando conexión...")
        break
    s.send(msg.encode())
    data = s.recv(1024)
    print(f"Servidor: {data.decode()}")
# Cerrar conexión