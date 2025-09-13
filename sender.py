import socket
import time

sender = socket.socket()
sender.connect(("localhost", 9999))

frames = int(input("How many frames to send? "))

for i in range(frames):
    print("Sending:", i)
    print("Ack was received from receiver")
    sender.send(str(i).encode())
    sender.recv(1024)
    time.sleep(1)

sender.send("exit".encode())
sender.close()
