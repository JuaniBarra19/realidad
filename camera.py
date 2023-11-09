import time
import socket
import random

host = "127.0.0.1" 
port = 50001 

class Camera():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def image(self):
        for i in range(random.randint(10, 20)):
            time.sleep(0.5)
            message = str(i)
            self.client_socket.send(message.encode('utf-8'))


a = Camera()
a.image()