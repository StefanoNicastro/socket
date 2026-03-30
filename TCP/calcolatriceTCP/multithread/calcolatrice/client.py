# Client
import socket
import json

HOST = '127.0.0.1'  # Indirizzo del server
PORT = 65432        # Porta usata dal server

# Il costrutto 'with' assicura la chiusura automatica della socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    
    #Chiedo dati e creo json 
    # Input dell'utente
    primoNumero = float(input("Inserisci il primo numero: "))
    operazione = input("Inserisci l'operazione (simbolo + - * /): ")
    secondoNumero = float(input("Inserisci il secondo numero: "))

    # Creazione del pacchetto JSON
    messaggio = {
        "primoNumero": primoNumero,
        "operazione": operazione,
        "secondoNumero": secondoNumero
    }
    
    # Serializzazione e invio
    messaggio_json = json.dumps(messaggio)
    
    sock_service.sendall(messaggio_json.encode("UTF-8"))
    data = sock_service.recv(1024) # 1024 è la dimensione massima dei dati ricevibili

# a questo punto la socket è stata chiusa automaticamente
print('Received', data.decode())