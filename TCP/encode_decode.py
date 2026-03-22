# Chiarimento sul formato di dati scambiato
# nella socket vengono inviati byte
# quindi le stringhe vanno codificate in byte con encode() prima di essere trasmesse
# ed i dati ricevuti vanno decodificati con decode() prima di essere visualizzati.

input_string = 'Hello'
print(type(input_string))

input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)

output_string = input_bytes_encoded.decode()
print(type(output_string))
print(output_string)