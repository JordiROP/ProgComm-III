# UDP-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Server listening: {HOST} {PORT}")
    while True:
        data = s.recvfrom(1024)
        print(f"Received from client: {data}")
        if not data:
            break
        num_bits = s.sendto(data[0], data[1])
        print(f"Sent to client: {data[0]} {num_bits}")