import socket

client = socket.socket()
client.connect(('localhost', 12345))
print(client.recv(1024))
client.send(b"Hi")
client.close()