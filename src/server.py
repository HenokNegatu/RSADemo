import socket
import rsa
import pickle
from colorama import Fore, Back, Style

HOST = 'localhost'  # Replace with server's IP address if needed
PORT = 5000         # Server port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.settimeout(10)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Only allow one connection at a time
print(f"Server listening on {Fore.CYAN}{HOST}:{PORT}{Style.RESET_ALL}")

#key generation phase
encdec = rsa.RSA()
(public, private)=encdec.generate_keypair()
print(f"public {Fore.CYAN}{public}{Style.RESET_ALL}, private {Fore.CYAN}{private}{Style.RESET_ALL}")

while True:
  client_socket, address = server_socket.accept()
  print(f"Connected by {address[0]}")
  try:

    #key exchange phase
    client_public_key = pickle.loads(client_socket.recv(1024))
    print(f'recieved clients public key {Back.LIGHTGREEN_EX}{Fore.BLACK}{client_public_key}{Style.RESET_ALL}')
    client_socket.send(pickle.dumps(public))

    while True:
      # Receive message from client
      message = pickle.loads(client_socket.recv(1024))
      message = encdec.decryptPipline(message)
      if message:
        # Send response to client
        response = f"Server: {message}"
        client_socket.sendall(pickle.dumps(response))
      else:
        break  # Client disconnected
  except ConnectionAbortedError:
    pass  # Handle client disconnection gracefully
  finally:
    client_socket.close()
    print(f"Client {address[0]} disconnected")
