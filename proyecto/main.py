import pygame
import math
from agente import Agente

# Inicialización
pygame.init()
pygame.key.set_repeat(1, 50)  # Hace que mantener las teclas sea más fluido

ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Agente Móvil con Rotación - Sesión 2 (Preparado para IA)")

clock = pygame.time.Clock()

# Crear agente
agente = Agente(400, 300, 60, angulo=30)

# Constantes
VELOCIDAD_MOVIMIENTO = 5
VELOCIDAD_ROTACION = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # === CONTROL POR TECLADO (Sesión 2) ===
    # En sesiones futuras se reemplazará por: agente.actualizar() + IA
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        rad = math.radians(agente.angulo)
        agente.x += VELOCIDAD_MOVIMIENTO * math.cos(rad)
        agente.y -= VELOCIDAD_MOVIMIENTO * math.sin(rad)

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        rad = math.radians(agente.angulo)
        agente.x -= VELOCIDAD_MOVIMIENTO * math.cos(rad)
        agente.y += VELOCIDAD_MOVIMIENTO * math.sin(rad)

    # Rotación
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        agente.angulo += VELOCIDAD_ROTACION
        agente.angulo %= 360

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        agente.angulo -= VELOCIDAD_ROTACION
        agente.angulo %= 360

    # Limitar posición
    margen = agente.tamano * 1.2
    agente.x = max(margen, min(agente.x, ANCHO - margen))
    agente.y = max(margen, min(agente.y, ALTO - margen))

    # Dibujar
    screen.fill((0, 0, 0))
    agente.dibujar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()