from socket import *

HOST = '127.0.0.1'  # Dirección IP local
PORT = 65432        # Puerto de conexión

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT)) # Asociar el socket a la dirección y puerto
s.listen()           # Escuchar conexiones entrantes

print(f"Servidor escuchando en {HOST}:{PORT}...")
(conn, addr) = s.accept() # Aceptar una nueva conexión
print(f"Conexión establecida con: {addr}")

while True:
    data = conn.recv(1024) # Recibir datos del cliente
    if not data: 
        break              # Detener si el cliente se desconecta
    
    msg = data.decode().upper() # Procesar los datos (agregar un asterisco)
    mensaje_invertido = msg[::-1]
    conn.send(mensaje_invertido.encode())   # Enviar la respuesta al cliente
    
conn.close() # Cerrar la conexión
s.close()    # Cerrar el socket del servidor
