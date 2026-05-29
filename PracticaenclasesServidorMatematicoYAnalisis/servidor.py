from socket import *

HOST = '127.0.0.1'  # Dirección IP local
PORT = 65432        # Puerto de conexión

# Crear socket TCP
s = socket(AF_INET, SOCK_STREAM)

# Asociar el socket a la dirección IP y puerto
s.bind((HOST, PORT))

# Poner el servidor en modo escucha
s.listen()

print(f"Servidor escuchando en {HOST}:{PORT}...")
print("Esperando conexión de un cliente...")

# El servidor acepta UNA sola conexión
conn, addr = s.accept()
print(f"Conexión establecida con: {addr}")

while True:
    data = conn.recv(1024)  # Recibir datos del cliente

    if not data:
        print("El cliente cerró la conexión.")
        break

    mensaje = data.decode()
    print(f"Mensaje recibido: {mensaje}")

    mensaje_mayuscula = mensaje.upper()
    mensaje_invertido = mensaje_mayuscula[::-1]

    conn.send(mensaje_invertido.encode())

conn.close()
s.close()

print("Servidor cerrado.")