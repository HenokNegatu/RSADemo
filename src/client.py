import socket
import rsa
import pickle

HOST = 'localhost'  # Server's IP address
PORT = 5000         # Server port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

#key generation phase
encdec = rsa.RSA()
(public, private)=encdec.generate_keypair()
print(f"public {public} private {private}")

#key exchange phase
client_socket.send(pickle.dumps(public))
servers_public_key = pickle.loads(client_socket.recv(1024))
print(f"recieved servers public key {servers_public_key}")

while True:
  # Send message to server
  message = input("You: ")

  message = encdec.encryptPipline(servers_public_key, message)
  client_socket.sendall(pickle.dumps(message))

  # Receive response from server
  response = pickle.loads(client_socket.recv(1024))
  if response:
    print(response)
  else:
    break  # Server disconnected

client_socket.close()
print("Disconnected from server")
