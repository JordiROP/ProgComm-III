# UDP-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print(f"Sending message to server") 
    s.sendto(b"Hello, world", (HOST, PORT))
    data = s.recvfrom(1024)
    print(f"Received {data}")
