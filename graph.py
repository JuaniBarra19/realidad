import time
import socket
import pygame

host = "127.0.0.1" 
port = 50001 

class Graph():
    def __init__(self):
        pygame.init()
        self.game = pygame.display.set_mode([500, 500])
        self.game.fill((255, 255, 255))

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        self.client_socket, client_address = server_socket.accept()

    def screen(self):
        running = True
        while running:
            data = self.client_socket.recv(1024)
            print(f"{data.decode('utf-8')}") 
            data = int(data)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.draw.circle(self.game, (0, 0, 255), (data*5, 250), 75)
            pygame.display.flip()

        pygame.quit()


a = Graph()
a.screen()