import socket

s = socket.socket()
host = socket.gethostname()

port = 9999

s.connect((host, port))

msg_recv = s.recv(1024).decode()

print(msg_recv)

s.close()
