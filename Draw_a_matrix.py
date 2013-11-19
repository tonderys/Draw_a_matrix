from Tkinter import *
from time import *
import socket
from threading import Thread

WIDTH = 640
HEIGHT = 640

class Draw_a_matrix:
    TCP_IP = 'localhost'
    TCP_PORT = 5005
    buffer_size = 4096 
    
    def __init__(self):
        self.top_window = Tk()
        self.canvas = Canvas(self.top_window, width = WIDTH, height = HEIGHT)
        self.canvas.grid(row = 0, column = 0)
        self.drawer = self.Drawing_thread(self)
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
        self.drawer.start()
        self.sock.bind((self.TCP_IP, self.TCP_PORT))
        self.sock.listen(5)

    class Drawing_thread(Thread):
        def __init__(self, controller):
            Thread.__init__(self)
            self.controller = controller
            self.setDaemon(True)

        def run(self):
            while 1:
                conn,addr = self.controller.sock.accept()
                data = conn.recv(self.controller.buffer_size)
                parsed_data = self.controller.parse_list_from_string(data)
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
                        self.controller.canvas.create_rectangle(Y, X, Y + pixel_height, X + pixel_width, fill=color)
                conn.close()    


    def parse_list_from_string(self, string):
        return [int(s) for s in string.split() if s.isdigit()]

matrix_drawer = Draw_a_matrix()
matrix_drawer.top_window.mainloop()