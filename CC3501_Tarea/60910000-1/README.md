# Tarea 2: Personaje Articulado y Poses Dramáticas

**CC3501 - Computación Gráfica**

## Descripción

Este proyecto implementa un personaje articulado usando transformaciones jerárquicas y un grafo de escena en OpenGL. El personaje puede alternar entre 3 poses dramáticas, cada una con su propia configuración de cámara.

## Características Implementadas

### 1. Estructura del Personaje y Grafo de Escena (3 puntos)
- ✅ Uso de Python con pyglet para comunicación con OpenGL
- ✅ Implementación de grafo de escena para representar la jerarquía del personaje
- ✅ Personaje con **13 articulaciones**:
  - Torso (raíz)
  - Cuello y Cabeza
  - Brazo izquierdo: hombro, codo, mano
  - Brazo derecho: hombro, codo, mano
  - Pierna izquierda: cadera, rodilla, pie
  - Pierna derecha: cadera, rodilla, pie
- ✅ Cada parte puede rotar respecto a su conexión con la parte padre

### 2. Poses y Cambios de Cámara (2 puntos)
- ✅ **3 poses diferentes**:
  1. **"The Menacing Stance"**: Pose amenazante estilo JoJo con brazos en posición dramática
  2. **"The Pointing"**: Pose señalando con el brazo extendido
  3. **"The Power Stance"**: Pose de poder con ambos brazos levantados
- ✅ Cada pose tiene su propia configuración de cámara
- ✅ Cambio entre poses con la barra espaciadora
- ✅ Actualización simultánea de personaje y cámara

### 3. Colores y Visualización (1 punto)
- ✅ Diferentes colores para cada parte del cuerpo:
  - Azul para el torso y parte superior de brazos
  - Color piel para cabeza, cuello, antebrazos y manos
  - Negro para pantalones/piernas
  - Café para los zapatos
- ✅ Sombreado Phong implementado para mejor visualización 3D

## Estructura del Proyecto

```
60910000-1/
├── __init__.py              # Punto de entrada del módulo
├── __main__.py              # Permite ejecución con python -m
├── main.py                  # Aplicación principal
├── scene_graph.py           # Implementación del grafo de escena
├── transformations.py       # Matrices de transformación
├── geometry.py              # Primitivas geométricas (cubo, esfera, cilindro)
├── vertex_shader.glsl       # Vertex shader
├── fragment_shader.glsl     # Fragment shader con iluminación Phong
└── README.md               # Este archivo
```

## Instalación y Ejecución

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalar Dependencias

```bash
pip install numpy pyglet PyOpenGL
```

### Ejecutar el Programa

Desde la raíz del proyecto (donde está la carpeta `60910000-1`):

```bash
python -m 60910000-1
```

O si estás dentro de la carpeta:

```bash
python main.py
```

## Controles

- **ESPACIO**: Cambiar entre las 3 poses dramáticas
- **ESC**: Salir de la aplicación

## Implementación Técnica

### Grafo de Escena

El personaje utiliza un grafo de escena jerárquico donde:
- Cada nodo tiene una transformación local
- Las transformaciones se acumulan de padre a hijo
- Permite animaciones complejas manteniendo relaciones jerárquicas

### Transformaciones Jerárquicas

Las poses se definen mediante rotaciones aplicadas a las articulaciones:
```python
pose = {
    'left_shoulder': rotationZ(angle),
    'left_elbow': rotationZ(angle),
    # ... más articulaciones
}
```

### Sistema de Cámara

Cada pose define:
- `eye`: Posición de la cámara
- `at`: Punto hacia donde mira
- `up`: Vector arriba

Esto permite perspectivas dramáticas que realzan cada pose.

## Detalles de Implementación

### Primitivas Geométricas

Se implementaron tres primitivas básicas:
1. **Cubo**: Para el torso y pies
2. **Esfera**: Para articulaciones (hombros, codos, rodillas) y cabeza
3. **Cilindro**: Para extremidades (brazos, piernas)

### Iluminación

Modelo de iluminación Phong con:
- Componente ambiente (30%)
- Componente difusa
- Componente especular
- Cálculo de normales automático usando derivadas

## Notas de Diseño

- Las poses están inspiradas en el estilo dramático de anime/manga
- Los colores ayudan a distinguir claramente cada parte del cuerpo
- El sistema es extensible para agregar más poses
- El grafo de escena permite fácil modificación de la estructura del personaje

## Autor

RUT: 60910000-1 (ejemplo - Universidad de Chile)

## Licencia

Este proyecto es parte de la Tarea 2 del curso CC3501 - Computación Gráfica.
