import socket

SERVER = ("127.0.0.1", 5005)
MESSAGE = b"Honours project: UDP packet analysis"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(3)
    client.sendto(MESSAGE, SERVER)
    print(f"Sent: {MESSAGE.decode()}")

    response, address = client.recvfrom(2048)
    print(f"Response from {address}: {response.decode()}")
