import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = 'localhost'
puerto = 12345

sock.bind((ip, puerto))

while True:
    print("Esperando paquetes...")

    info, direccion = sock.recvfrom(1024)

    print(f"Mensaje: {info.decode()} desde {direccion}")

    sock.sendto('Recibido'.encode(), direccion)
