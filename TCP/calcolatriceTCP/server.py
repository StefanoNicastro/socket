# Server
import socket
import json

# Configurazione del server
IP = "127.0.0.1"
PORT = 65432
DIM_BUFFER = 1024

# Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    
    # Binding della socket alla porta specificata
    sock_server.bind((IP, PORT))
    
    # Metti la socket in ascolto per le connessioni in ingresso
    sock_server.listen()
    print(f"Server in ascolto su {IP}:{PORT}...")
    
    # Loop principale del server
    while True:
        # accetta le connessioni
        sock_service, address_client = sock_server.accept()
        
        with sock_service as sock_client:
            # Leggi i dati inviati dal client
            dati = sock_client.recv(DIM_BUFFER).decode()
            dati=json.loads(dati)
            
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
            
            # Stampa il messaggio ricevuto e invia una risposta al client
            print(f"Ricevuto messaggio dal client {sock_client}: {dati}")
            sock_client.sendall(str(risultato).encode())