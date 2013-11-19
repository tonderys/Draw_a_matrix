import socket
from threading import Thread

class Matrix_sender:
   TCP_IP = '127.0.0.1'
   TCP_PORT = 5005

   def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.s.send("10 10\n"
        "2 1 0 0 0 0 0 0 0 0\n"
        "1 2 1 0 0 0 0 0 0 0\n"
        "0 1 2 1 0 0 0 0 0 0\n"
        "0 0 1 2 1 0 0 0 0 0\n"
        "0 0 0 1 2 1 0 0 0 0\n"
        "0 0 0 0 1 2 1 0 0 0\n"
        "0 0 0 0 0 1 2 1 0 0\n"
        "0 0 0 0 0 0 1 2 1 0\n"
        "0 0 0 0 0 0 0 1 2 1\n"
        "0 0 0 0 0 0 0 0 1 2\n")
        self.s.close()
Matrix_sender()
