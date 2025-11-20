# Tarea 2: Personaje Articulado y Poses Dramáticas

## Instrucciones de Ejecución

### Opción 1: Usando Python directamente

Desde el directorio que contiene la carpeta `60910000-1`:

```bash
python -m 60910000-1
```

### Opción 2: Usando el script (Windows)

Ejecuta `run.bat`

### Opción 3: Descomprimir y ejecutar desde la raíz del repositorio

```bash
unzip 60910000-1.zip
python -m 60910000-1
```

## Dependencias

Asegúrate de tener instalado:

```bash
pip install numpy pyglet PyOpenGL
```

## Controles

- **ESPACIO**: Cambiar entre las 3 poses dramáticas
- **ESC**: Salir de la aplicación

## Características Implementadas

✅ Grafo de escena con transformaciones jerárquicas
✅ Personaje con 13 articulaciones (>6 requeridas)
✅ 3 poses dramáticas diferentes
✅ Configuración de cámara específica para cada pose
✅ Diferentes colores para cada parte del cuerpo
✅ Iluminación Phong para mejor visualización 3D

## Estructura del Proyecto

```
60910000-1/
├── __init__.py              # Punto de entrada del módulo
├── __main__.py              # Permite ejecución con python -m
├── main.py                  # Aplicación principal
├── scene_graph.py           # Grafo de escena
├── transformations.py       # Transformaciones
├── geometry.py              # Primitivas geométricas
├── vertex_shader.glsl       # Vertex shader
├── fragment_shader.glsl     # Fragment shader
└── README.md               # Documentación detallada
```

## Video/Capturas

El personaje puede alternar entre:
1. **"The Menacing Stance"**: Pose amenazante con brazos extendidos
2. **"The Pointing"**: Pose señalando dramáticamente
3. **"The Power Stance"**: Pose de poder con brazos arriba

Cada pose tiene su propia perspectiva de cámara para maximizar el efecto dramático.
