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

## Cómo ejecutar
```bash
cd proyecto
python main.py