import math
import pygame

class Agente:
    def __init__(self, x, y, tamano, angulo=30):
        """
        Inicializa el agente con posición (x, y), tamaño y ángulo inicial diferente de 0.
        """
        self.x = x
        self.y = y
        self.tamano = tamano
        self.angulo = angulo  # en grados

    def dibujar(self, screen, color_base=(0, 180, 0), color_frente=(255, 50, 50)):
        """
        Dibuja el triángulo rotado alrededor de su centro.
        - Cuerpo en color_base (verde oscuro)
        - Círculo rojo en el vértice frontal para indicar dirección de movimiento
        """
        # Vértices locales (triángulo simétrico apuntando "arriba" en reposo)
        vertices_locales = [
            (0, -self.tamano),                     # frente (punta)
            (-self.tamano / 2, self.tamano / 2),   # izquierda
            (self.tamano / 2, self.tamano / 2)     # derecha
        ]

        # Rotación
        rad = math.radians(self.angulo)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        vertices = []
        for lx, ly in vertices_locales:
            rx = lx * cos_a - ly * sin_a
            ry = lx * sin_a + ly * cos_a
            vertices.append((self.x + rx, self.y + ry))

        # Dibujar triángulo relleno
        pygame.draw.polygon(screen, color_base, vertices)
        # Borde blanco
        pygame.draw.polygon(screen, (255, 255, 255), vertices, width=3)
        # Círculo rojo en el frente
        fx, fy = vertices[0]
        pygame.draw.circle(screen, color_frente, (int(fx), int(fy)), 10)