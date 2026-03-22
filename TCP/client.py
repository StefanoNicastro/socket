# Client
import socket

HOST = '127.0.0.1'  # Indirizzo del server
PORT = 65432        # Porta usata dal server

# Il costrutto 'with' assicura la chiusura automatica della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    sock_service.sendall(b'Hello, world') # invio direttamente in formato byte
    data = sock_service.recv(1024) # 1024 è la dimensione massima dei dati ricevibili

# a questo punto la socket è stata chiusa automaticamente
print('Received', data.decode())