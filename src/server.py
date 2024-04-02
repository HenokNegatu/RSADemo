import socket
import RSA from rda
# Define server and client behavior (modify for your needs)
SERVER_ADDRESS = ('localhost', 5000)  # Server address and port
filename = 'data.txt'  # File to exchange (same on both sides)

def send_file(address, filename):
  """
  Sends a file to the specified address using a socket connection.
  """
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect(address)
    # Open the file in binary mode for any kind of data
    with open(filename, 'rb') as f:
      data = f.read()
      sock.sendall(data)
  finally:
    sock.close()

def receive_file(address, filename):
  """
  Receives a file from the specified address using a socket connection.
  """
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.bind(address)  # Bind to the address for receiving
    sock.listen(1)
    conn, addr = sock.accept()
    with open(filename, 'wb') as f:
      data = conn.recv(1024)  # Receive data in chunks
      while data:
        f.write(data)
        data = conn.recv(1024)
  finally:
    sock.close()

# Example usage (uncomment for server or client mode)

# Server mode (listens for incoming connections)
# receive_file(SERVER_ADDRESS, filename)

# Client mode (sends the file)
send_file(SERVER_ADDRESS, filename)

print(f"File exchange for '{filename}' completed.")
