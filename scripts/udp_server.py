import socket

HOST = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    data, client_address = server.recvfrom(2048)
    message = data.decode("utf-8", errors="replace")

    print(f"Client: {client_address}")
    print(f"Received: {message}")

    server.sendto(b"UDP test response received", client_address)
