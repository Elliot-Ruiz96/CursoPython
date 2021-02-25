import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = 'localhost'
puerto = 12345

msg = 'Hello world!'.encode()

sock.sendto(msg, (ip, puerto))

info, direccion = sock.recvfrom(1024)

print(f"Recibido: {info.decode()} desde {direccion}")
