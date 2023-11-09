import pygame
import sys
import random
import os

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animación Pygame")

# Definir colores
black = (0, 0, 0)

# Obtener la ruta completa del archivo de imagen
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "rombo.png")

# Definir clase para representar un rombo con una imagen como sprite
class Rhombus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 120
        # Cargar la imagen
        self.image = pygame.image.load(image_path).convert_alpha()
        # Escalar la imagen al tamaño del rombo
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.original_image = self.image  # Almacenar la imagen original
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.size)
        self.rect.y = 0
        self.angle = 0  # Nuevo atributo para el ángulo de rotación

    def update(self):
        self.rect.y += 1.0
        self.angle += 2  # Ajusta la velocidad de rotación aquí
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

# Grupo para almacenar los sprites de rombos
all_rhombuses = pygame.sprite.Group()

# Bucle principal
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Crear nuevos rombos de forma aleatoria y agregar al grupo de sprites
    if random.randint(0, 100) < 5:
        rhombus = Rhombus()
        all_rhombuses.add(rhombus)

    # Limpiar la pantalla
    screen.fill(black)

    # Actualizar y dibujar todos los rombos
    all_rhombuses.update()
    all_rhombuses.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de la animación
    clock.tick(75)


