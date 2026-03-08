import pygame
from agente import Agente

pygame.init()
pygame.key.set_repeat(1, 30)

ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 3 - Agente con movimiento vectorial NumPy")

clock = pygame.time.Clock()

agente = Agente(400, 300, 60, angulo=30)

running = True
while running:
    dt = clock.tick(60) / 1000.0          # segundos reales

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    agente.mover(dt, keys)
    agente.aplicar_rebote(ANCHO, ALTO)

    screen.fill((0, 0, 0))
    agente.dibujar(screen)

    pygame.display.flip()

pygame.quit()