# Tarea 3: Acuario Virtual Interactivo

## 📝 Descripción

Simulación 3D de un acuario con peces que se mueven usando algoritmos de boids, burbujas flotantes con sistema de partículas, iluminación realista y **cámara interactiva** (requisito crítico según retroalimentación del profesor).

## 🎮 Controles (INTERACTIVIDAD)

### Cámara (Arcball) - ⭐ CRÍTICO
- **Mouse izquierdo + arrastrar**: Rotar cámara alrededor del acuario
- **Mouse derecho + arrastrar**: Mover vista lateralmente (pan)
- **Scroll del mouse**: Zoom in/out

### Controles adicionales
- **ESPACIO**: Pausar/reanudar animación
- **R**: Resetear cámara a posición inicial
- **ESC**: Salir de la aplicación

## 🚀 Cómo Ejecutar

### Opción 1: Script batch
```bash
cd C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea
run_tarea3.bat
```

### Opción 2: Línea de comandos
```bash
cd C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea
python -m tarea3_acuario
```

## 📦 Estructura del Proyecto

```
tarea3_acuario/
├── __init__.py              # Módulo principal
├── __main__.py              # Punto de entrada
├── main.py                  # Aplicación principal (integra todo)
├── camera.py                # Sistema de cámara arcball (⭐ CRÍTICO)
├── boids.py                 # Sistema de boids para peces
├── particles.py             # Sistema de partículas para burbujas
├── geometry.py              # Primitivas geométricas (cubos, esferas, etc.)
├── transformations.py       # Matrices de transformación
├── vertex_shader.glsl       # Vertex shader
└── fragment_shader.glsl     # Fragment shader (iluminación Phong)
```

## ✅ Características Implementadas

### 1. ⭐ Cámara Interactiva (CRÍTICO según profesor)
- ✅ Sistema arcball completo
- ✅ Rotación orbital con mouse
- ✅ Zoom con scroll
- ✅ Pan (movimiento lateral)
- ✅ Reset de cámara

### 2. Animación de Peces (Boids)
- ✅ Sistema de boids con 3 reglas:
  - Separación: evitar colisiones
  - Cohesión: mantener el grupo junto
  - Alineación: nadar en la misma dirección
- ✅ Contención dentro del acuario
- ✅ Orientación según dirección de movimiento

### 3. Sistema de Partículas (Burbujas)
- ✅ Emisión continua desde el fondo
- ✅ Flotación realista
- ✅ Movimiento oscilante (simula corrientes)
- ✅ Tiempo de vida variable

### 4. Iluminación
- ✅ Modelo Phong con:
  - Luz ambiente
  - Luz difusa
  - Luz especular
- ✅ Normales calculadas automáticamente

### 5. Interactividad
- ✅ Control total de cámara
- ✅ Pausa/reanudar animación
- ✅ Reset de vista

## 🔧 Dependencias

```bash
pip install pyglet PyOpenGL numpy
```

## 📖 Explicación del Código

### Sistema de Cámara (`camera.py`)
El sistema arcball permite rotar la cámara alrededor del acuario de forma intuitiva. Usa coordenadas esféricas (theta, phi) para posicionar la cámara a una distancia fija del centro.

**Componentes clave:**
- `get_position()`: Calcula posición de cámara en coordenadas esféricas
- `get_view_matrix()`: Genera matriz de vista para OpenGL
- `on_mouse_drag()`: Actualiza ángulos según movimiento del mouse

### Sistema de Boids (`boids.py`)
Implementa el algoritmo de Craig Reynolds para simular comportamiento de cardumen.

**Reglas:**
1. **Separación**: Cada pez mantiene distancia mínima con vecinos
2. **Cohesión**: Los peces se mueven hacia el centro del grupo
3. **Alineación**: Los peces igualan su velocidad con la del grupo

### Sistema de Partículas (`particles.py`)
Simula burbujas que flotan en el agua.

**Fuerzas aplicadas:**
- Flotación: fuerza constante hacia arriba
- Resistencia: fricción del agua
- Oscilación: movimiento sinusoidal para simular corrientes

### Shaders
**Vertex Shader:** Transforma vértices usando matrices model-view-projection

**Fragment Shader:** Implementa iluminación Phong:
- Componente ambiente: iluminación base
- Componente difusa: depende del ángulo con la luz
- Componente especular: brillos en superficies

## 🎨 Variables Ajustables (camelCase según preferencia)

En `main.py`:
- `numFish`: Cantidad de peces (línea 120)
- `emissionRate`: Burbujas por segundo (línea 124)

En `boids.py`:
- `maxSpeed`: Velocidad máxima de peces
- `separationWeight`, `alignWeight`, `cohesionWeight`: Pesos de las reglas

En `particles.py`:
- `lifetime`: Tiempo de vida de burbujas
- Fuerzas en `update()`: ajustar flotación y oscilación

## 📚 Conceptos Utilizados

- **Grafo de escena implícito**: Transformaciones jerárquicas
- **Coordenadas esféricas**: Para la cámara arcball
- **Algoritmos de agentes**: Sistema de boids
- **Sistemas de partículas**: Simulación de burbujas
- **Iluminación Phong**: Rendering realista
- **Vectores y matrices**: Transformaciones 3D

## 🎓 Autor

Juan Ignacio Reyes Marchant  
RUT: 21.211.977-6  
Curso: CC3501 - Modelación y Computación Gráfica

---

## 📝 Notas de Implementación

### ¿Por qué arcball?
Según la retroalimentación del profesor, la **interactividad y la cámara** son elementos críticos. El sistema arcball proporciona:
- Interacción intuitiva con el mouse
- Rotación suave alrededor del objeto
- Control completo de la vista

### Nomenclatura
Se usó **camelCase** para variables según preferencia especificada:
- `maxSpeed` en lugar de `max_speed`
- `fishMesh` en lugar de `fish_mesh`
- `boidSystem` en lugar de `boid_system`

### Comentarios
El código incluye comentarios exhaustivos explicando:
- Qué hace cada función
- Por qué se usan ciertos valores
- Cómo funcionan los algoritmos
- Parámetros ajustables
