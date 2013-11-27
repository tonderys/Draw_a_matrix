from Tkinter import *
from time import *
import socket

WIDTH = 640
HEIGHT = 640

class Draw_a_matrix:
    TCP_IP = '192.168.56.2'
    TCP_PORT = 10001
    
    def __init__(self):
        self.top_window = Tk()
        self.canvas = Canvas(self.top_window, width = WIDTH, height = HEIGHT)
        self.canvas.grid(row = 0, column = 0)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.TCP_IP, self.TCP_PORT))
        self.top_window.mainloop()
        while 1:
            self.sock.sendall("wyskakuj z mapy")
            data = self.sock.recv(4096)
            parsed_data = self.parse_list_from_string(data)
            self.columns = parsed_data[0]
            self.rows = parsed_data[1] 
            pixel_width = WIDTH / self.columns
            pixel_height = HEIGHT / self.rows
            for y in range (0, self.rows):
                for x in range (0, self.columns):
                    if parsed_data[y * self.columns + x + 2] == 0:
                        color = 'white'
                    if parsed_data[y * self.columns + x + 2] == 1:
                        color = 'black'
                    if parsed_data[y * self.columns + x + 2] == 2:
                        color = 'green'
                    Y = y * pixel_height
                    X = x * pixel_width
                    self.canvas.create_rectangle(Y, X, Y + pixel_height, X + pixel_width, fill=color)
            sleep(1)

    def parse_list_from_string(self, string):
        return [int(s) for s in string.split() if s.isdigit()]

matrix_drawer = Draw_a_matrix()
