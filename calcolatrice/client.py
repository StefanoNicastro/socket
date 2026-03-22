import socket
import json

# Configurazione
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
s.sendto(messaggio_json.encode("UTF-8"), (SERVER_IP, SERVER_PORT))

# Ricezione della risposta dal server
data, addr = s.recvfrom(1024)
print(f"Risultato dal server: {data.decode()}")

s.close()
