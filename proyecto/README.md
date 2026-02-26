## Sesión 2

En esta sesión, se implementó una versión mejorada del agente como una clase `Agente` en el archivo `agente.py`. 

- Atributos: `x` y `y` para la posición, `tamano` para el tamaño del triángulo, y `angulo` para la orientación en grados.
- Vértices locales: Definidos como un triángulo simétrico (isósceles) relativo al centro (0,0) para facilitar la rotación.
- Método `dibujar`: Aplica rotación usando matrices trigonométricas (cos y sin) alrededor del centro, y dibuja el polígono con `pygame.draw.polygon`.
- Ángulo inicial: Configurado en 30° por defecto para que no sea 0°.
- Comentarios: Se agregaron docstrings en cada método explicando su funcionalidad.
- Otras mejoras: El dibujo incluye traslación a la posición del agente.

Esto cumple con los requisitos de funcionalidad para dibujar polígonos rotados.