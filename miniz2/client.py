import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Receive data from the server and shut down
    received = sock.recv(5000)
    with open('./rcvd/Test.pdf', 'wb') as f:
            f.write(sock.recv(5000))

print("Sent:     {}".format(data))
print("Received: {}".format(received))
