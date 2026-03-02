# Sesión 2 - Agente Móvil con Rotación y Preparación para IA

Implementación completa del agente triangular controlado por teclado usando **Pygame** y la clase `Agente`.

## Características implementadas
- Triángulo isósceles rotado correctamente alrededor de su centro
- Movimiento hacia adelante/atrás relativo a su orientación
- Rotación suave izquierda/derecha
- Límites de pantalla (no sale del área)
- Indicador visual de dirección (círculo rojo en la proa)
- **Preparación para IA** (nuevos métodos listos para comportamientos inteligentes)

## Controles
- **W / ↑** → Avanzar  
- **S / ↓** → Retroceder  
- **A / ←** → Girar izquierda  
- **D / →** → Girar derecha  

## Estructura del proyecto
- `agente.py` → Clase `Agente` (atributos + dibujar + métodos IA)
- `main.py`  → Bucle principal y control por teclado

## Preparación para IA (15 puntos)
Se agregaron los siguientes métodos en la clase `Agente`:
- `actualizar(self, dt)` → Listo para lógica autónoma
- `set_direccion(nuevo_angulo)` → Control externo por IA
- `get_frente()` → Posición de la punta (para sensores/colisiones)

Esto permite reemplazar fácilmente el teclado por cualquier comportamiento inteligente en sesiones futuras.

## Requisitos
- Python 3.x
- Pygame (`pip install pygame`)

## Cómo ejecutar
```bash
cd proyecto
python main.py