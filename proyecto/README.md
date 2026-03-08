# Sesión 2 y 3 - Agente Móvil con Rotación y Rebote en Bordes

Implementación completa del agente triangular controlado por teclado usando **Pygame** y la clase `Agente`.

## Características implementadas
- Triángulo isósceles rotado correctamente alrededor de su centro
- Movimiento hacia adelante/atrás relativo a su orientación
- Rotación suave izquierda/derecha
- **Rebote real en los 4 bordes** con reflexión correcta del ángulo (nuevo)
- Indicador visual de dirección (círculo rojo en la proa)
- **Preparación para IA** (métodos listos para comportamientos inteligentes)

## Controles
- **W / ↑** → Avanzar  
- **S / ↓** → Retroceder  
- **A / ←** → Girar izquierda  
- **D / →** → Girar derecha  

## Rebote en bordes
Se implementó el método `aplicar_rebote()` dentro de la clase `Agente`.  
Al chocar contra cualquier borde, el agente **refleja su ángulo** correctamente (como en billar) y rebota de forma natural.

## Estructura del proyecto
- `agente.py` → Clase `Agente` (con rebote y métodos IA)
- `main.py`  → Bucle principal

## Preparación para IA
Métodos agregados: `actualizar()`, `set_direccion()` y `get_frente()`.

# Sesión 4 - Movimiento vectorial suave con NumPy

## Características principales
- Movimiento **constante** en cualquier dirección (incluidas diagonales) gracias a vectores unitarios y delta time
- Uso de **NumPy** para posición, dirección y cálculos vectorizados
- Velocidad independiente del framerate (suave en cualquier equipo)
- Rebote real en bordes (refleja ángulo correctamente)
- Preparado para comportamientos IA (métodos `actualizar`, `set_direccion`, `get_frente`)

## Ventajas de usar vectores y NumPy en esta sesión
- Dirección siempre normalizada → velocidad constante (no más rápido en diagonal)
- Cálculos vectorizados → código más limpio y potencialmente más rápido
- Posición como `np.array` → facilita futuras operaciones (rotaciones, colisiones, etc.)
- `dt` (delta time) → movimiento frame-rate independiente

## Cómo ejecutar
```bash
cd proyecto
python main.py