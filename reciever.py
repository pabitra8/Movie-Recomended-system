import socket

receiver = socket.socket()
receiver.bind(("localhost", 9999))
receiver.listen(1)

conn, _ = receiver.accept()

while True:
    frame = conn.recv(1024).decode()
    if frame == "exit":
        break
    print("Received:", frame)
    conn.send(frame.encode())

print("All frames were received successfully")
conn.close()
receiver.close()
