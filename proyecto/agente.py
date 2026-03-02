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

    # === NUEVOS MÉTODOS PARA PREPARACIÓN IA ===
    def actualizar(self, dt=1/60):
        """Método preparado para actualizaciones autónomas en futuras sesiones (IA)."""
        pass

    def set_direccion(self, nuevo_angulo):
        """Permite cambiar la orientación del agente desde fuera (útil para IA)."""
        self.angulo = nuevo_angulo % 360

    def get_frente(self):
        """Devuelve la posición exacta de la punta (para sensores o colisiones futuras)."""
        rad = math.radians(self.angulo)
        fx = self.x + self.tamano * math.cos(rad)
        fy = self.y - self.tamano * math.sin(rad)
        return fx, fy

    # ==== NUEVO: REBOTE EN BORDES ====
    def aplicar_rebote(self, ancho, alto):
        """
        Aplica rebote real en los bordes de la pantalla.
        - Invierte la dirección del agente usando reflexión de ángulo.
        - Mantiene el agente dentro de los límites.
        """
        margen = self.tamano * 1.2
        reboto = False

        # Rebote en paredes verticales (izquierda y derecha)
        if self.x < margen:
            self.x = margen
            self.angulo = 180 - self.angulo
            reboto = True
        elif self.x > ancho - margen:
            self.x = ancho - margen
            self.angulo = 180 - self.angulo
            reboto = True

        # Rebote en paredes horizontales (arriba y abajo)
        if self.y < margen:
            self.y = margen
            self.angulo = -self.angulo
            reboto = True
        elif self.y > alto - margen:
            self.y = alto - margen
            self.angulo = -self.angulo
            reboto = True

        if reboto:
            self.angulo %= 360