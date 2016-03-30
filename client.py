import socket

HOST = '188.226.245.216'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for i in range(100):
    s.send("hello")
s.close()
