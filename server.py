import socket

server = socket.socket()
server.bind(('localhost', 12345))
server.listen(1)
client, _ = server.accept()
client.send(b"Hello")
print(client.recv(1024))
client.close(); server.close()