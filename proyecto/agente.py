import math
import pygame
import numpy as np

class Agente:
    def __init__(self, x, y, tamano, angulo=30):
        """
        Inicializa el agente con posición, tamaño y ángulo inicial (en grados).
        """
        self.pos = np.array([float(x), float(y)], dtype=np.float32)
        self.tamano = tamano
        self.angulo = angulo % 360                 # grados
        self.velocidad = 180.0                     # píxeles por segundo (ajustable)
        self.vel_vector = np.array([0.0, 0.0], dtype=np.float32)

    def actualizar_direccion(self):
        """Calcula el vector unitario de dirección actual usando trigonometría."""
        rad = math.radians(self.angulo)
        self.vel_vector = np.array([
            math.cos(rad),
            -math.sin(rad)              # negativo porque Y crece hacia abajo en pygame
        ], dtype=np.float32)

    def mover(self, dt: float, teclas):
        """
        Mueve al agente usando vector normalizado y delta time.
        dt → tiempo transcurrido en segundos
        """
        self.actualizar_direccion()

        # Movimiento relativo al frente
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.pos += self.vel_vector * self.velocidad * dt

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.pos -= self.vel_vector * self.velocidad * dt

        # Rotación (grados por segundo)
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.angulo += 120.0 * dt
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.angulo -= 120.0 * dt

        self.angulo %= 360

    def aplicar_rebote(self, ancho: int, alto: int):
        """
        Rebote real con reflexión del ángulo al chocar contra bordes.
        """
        margen = self.tamano * 1.2
        reboto = False

        # Izquierda / Derecha
        if self.pos[0] < margen:
            self.pos[0] = margen
            self.angulo = 180 - self.angulo
            reboto = True
        elif self.pos[0] > ancho - margen:
            self.pos[0] = ancho - margen
            self.angulo = 180 - self.angulo
            reboto = True

        # Arriba / Abajo
        if self.pos[1] < margen:
            self.pos[1] = margen
            self.angulo = -self.angulo
            reboto = True
        elif self.pos[1] > alto - margen:
            self.pos[1] = alto - margen
            self.angulo = -self.angulo
            reboto = True

        if reboto:
            self.angulo %= 360

    def dibujar(self, screen, color_base=(0, 180, 0), color_frente=(255, 50, 50)):
        """
        Dibuja el triángulo rotado alrededor de su centro.
        Versión corregida: convierte explícitamente a float nativo para evitar
        problemas de compatibilidad con NumPy en pygame.draw.polygon
        """
        vertices_locales = [
            (0, -self.tamano),                     # frente
            (-self.tamano / 2, self.tamano / 2),   # izquierda
            (self.tamano / 2, self.tamano / 2)     # derecha
        ]

        rad = math.radians(self.angulo)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        vertices = []
        for lx, ly in vertices_locales:
            # Rotación
            rx = lx * cos_a - ly * sin_a
            ry = lx * sin_a + ly * cos_a
            # Suma posición + conversión explícita a float nativo de Python
            px = float(self.pos[0] + rx)
            py = float(self.pos[1] + ry)
            vertices.append((px, py))

        # Ahora sí es compatible con pygame
        pygame.draw.polygon(screen, color_base, vertices)
        pygame.draw.polygon(screen, (255, 255, 255), vertices, width=3)

        # Círculo en la punta (frente)
        fx, fy = vertices[0]
        pygame.draw.circle(screen, color_frente, (int(fx), int(fy)), 10)

    # Métodos preparados para IA futura
    def actualizar(self, dt=1/60):
        """Placeholder para comportamientos autónomos."""
        pass

    def set_direccion(self, nuevo_angulo):
        self.angulo = nuevo_angulo % 360

    def get_frente(self):
        rad = math.radians(self.angulo)
        return self.pos + self.tamano * np.array([math.cos(rad), -math.sin(rad)])