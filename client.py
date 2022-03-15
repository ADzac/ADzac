import socket

HOST = input("Server's IP Address: ")  # The server's hostname or IP address
PORT = 54236  # The port used by the server

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world\n")
    data = s.recv(2048)
    s.send("I'm Client".encode())

print(f"Received {data!r}")
