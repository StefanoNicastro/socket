import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

print("Server in attesa di dati...")

while True:
    # Ricevo i dati
    data, addr = s.recvfrom(1024)
    if not data:
        break
    
    # Decodifica JSON
    stringa_ricevuta = data.decode()
    dati = json.loads(stringa_ricevuta)
    
    n1 = dati["primoNumero"]
    op = dati["operazione"]
    n2 = dati["secondoNumero"]
    

    risultato = 0
    if op == '+':
        risultato = n1 + n2
    elif op == '-':
        risultato = n1 - n2
    elif op == '*':
        risultato = n1 * n2
    elif op == '/':
        risultato = n1 / n2 if n2 != 0 else "Errore: Divisione per zero"
    else:
        risultato = "Operazione non valida"

    # Invio del risultato al client
    s.sendto(str(risultato).encode(), addr)
