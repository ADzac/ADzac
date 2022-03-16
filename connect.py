import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)
HOST = local_ip  # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(2048)
            if not data:
                break

            conn.send("I'm Server".encode())
            f= open("test.html","w")
            l= data.decode()
            f.write(l)
            f.close()
    conn.close()

