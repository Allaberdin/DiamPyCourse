import socket

sock = socket.socket()

sock.bind(("", 12345))
sock.listen(1)

print("Server was launched")
working = True
while working:
    conn, addr = sock.accept()
    print(f"Connected client: {addr}")
    data = conn.recv(1024)
    if data == "/stop":
        working = False
    else:
        conn.send(data)
    conn.close()
print("Server was terminated")
sock.close()
