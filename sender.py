import socket
import random
from threading import Thread

class Matrix_sender:
   TCP_IP = '127.0.0.1'
   TCP_PORT = 5005

   def __init__(self):
        rows = 32
        columns = 32
        message = "%d %d "%(rows, columns)
        for i in range(0, rows):
            for j in  range(0, columns):
                message = message + "%d "%random.randrange(0,3,1)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.s.send(message)
        print message
        self.s.close()
Matrix_sender()
