from Tkinter import *
from time import *
import socket
from threading import Thread

class Draw_a_matrix:
    TCP_IP = 'localhost'
    TCP_PORT = 5005
    buffer_size = 1024 
    
    def __init__(self):
        self.top_window = Tk()
        self.canvas = Canvas(self.top_window, width = "640", height = "640")
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
        print "nathin'"

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
                for i in range (0,self.rows+1):
                    for j in range (0, self.columns+1):
                        if parsed_data[i*10+j+2] == 0:
                            self.controller.canvas.create_rectangle(i*20,j*20,i*21,j*21, fill="white")
                        if parsed_data[i+j+2] == 1:
                            self.controller.canvas.create_rectangle(i*20,j*20,i*21,j*21, fill="black")
                        if parsed_data[i+j+2] == 2:
                            self.controller.canvas.create_rectangle(i*20,j*20,i*21,j*21, fill="green")
                conn.close()    


    def parse_list_from_string(self, string):
        return [int(s) for s in string.split() if s.isdigit()]

matrix_drawer = Draw_a_matrix()
matrix_drawer.top_window.mainloop()
