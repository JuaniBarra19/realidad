import multiprocessing
import time
import socket
import pygame

host = "127.0.0.1" 
port = 50001 

def server():
    process = multiprocessing.current_process()
    print(f"Proceso cliente (PID: {process.pid})")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Esperando una conexión entrante...")

    # Aceptar la conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión establecida con {client_address}")

    # Recibir datos del cliente
    data = client_socket.recv(1024)
    print(f"Mensaje del cliente: {data.decode('utf-8')}")
    response = "Hola, soy el servidor. ¡Gracias por conectarte!"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
    server_socket.close()

def client():
    process = multiprocessing.current_process()
    print(f"Proceso cliente (PID: {process.pid})")
    time.sleep(4)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectar al servidor
    client_socket.connect((host, port))

    # Enviar datos al servidor
    message = "Hola, soy el cliente. ¿Cómo estás?"
    client_socket.send(message.encode('utf-8'))

    # Recibir una respuesta del servidor
    response = client_socket.recv(1024)
    print(f"Respuesta del servidor: {response.decode('utf-8')}")

    # Cerrar la conexión
    client_socket.close()

def graph():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=server)
    proceso2 = multiprocessing.Process(target=client)
    proceso3 = multiprocessing.Process(target=graph)

    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()