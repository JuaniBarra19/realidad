import socket
import json
import pygame

HOST = '127.0.0.1'
PORT = 50001
black = (0, 0, 0)
red = (255, 0, 0)
screen_width = 1920
screen_height = 1080

pygame.init()


def serv():
    game_display = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Servidor escuchando en {HOST}:{PORT}")
    client_socket, addr = server_socket.accept()
  

    running = True
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Crashea arreglar
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

        data = client_socket.recv(4096)
        received_data = json.loads(data.decode('utf-8'))

        game_display.fill(black)
        if "landmarks" in received_data:
            for connection in received_data['connections']:
                start_index, end_index = connection
                start_coords = received_data['landmarks'][start_index]
                end_coords = received_data['landmarks'][end_index]

                # Ajusta las coordenadas según el tamaño de la pantalla
                start_x, start_y = int(start_coords[0] * screen_width), int(start_coords[1] * screen_height)
                end_x, end_y = int(end_coords[0] * screen_width), int(end_coords[1] * screen_height)

                # Dibuja la línea en Pygame
                pygame.draw.line(game_display, red, (start_x, start_y), (end_x, end_y), 5)

        pygame.display.flip()
        clock.tick(75)
    
    pygame.quit()

serv()