import socket

# Difereniciar cliente y host
server_sock = socket.socket()
host = socket.gethostname()

print(server_sock)
print(host)

port = 9999

server_sock.bind((host, port))

print('Esperando conexiones')
server_sock.listen(1)

while True:
    client_sock, addr = server_sock.accept()
    print(addr)

    print(f'Cliente conectado de la direccion: {addr}')
    msg = 'Hola' + addr[0] + ':' + str(addr[1])
    client_sock.send(msg.encode())
    client_sock.close()
