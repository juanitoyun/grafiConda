# 🎮 Tarea 2: Personaje Articulado - COMPLETADA ✅

## 📋 Resumen de la Implementación

He creado una solución completa para tu Tarea 2 de Computación Gráfica (CC3501) basándome en los ejemplos del repositorio oficial del curso.

## 📁 Ubicación de los Archivos

Todo está listo en: `c:\Users\56942\Desktop\CC3501_Tarea\`

### Estructura:
```
CC3501_Tarea/
├── 60910000-1/              ← Carpeta con el código (cámbiala por tu RUT)
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py              ← Aplicación principal
│   ├── scene_graph.py       ← Grafo de escena
│   ├── transformations.py   ← Transformaciones
│   ├── geometry.py          ← Primitivas geométricas
│   ├── vertex_shader.glsl
│   ├── fragment_shader.glsl
│   └── README.md            ← Documentación detallada
├── 60910000-1.zip           ← Archivo ZIP para entregar
├── run.bat                  ← Script para ejecutar fácilmente
└── INSTRUCCIONES.md
```

## ✅ Características Implementadas

### 1. Grafo de Escena (3 puntos) ✅
- ✅ Python con pyglet + OpenGL
- ✅ Grafo de escena con transformaciones jerárquicas
- ✅ **13 articulaciones** (más de las 6 requeridas):
  * Torso (raíz)
  * Cuello y Cabeza
  * Hombro izq → Codo izq → Mano izq
  * Hombro der → Codo der → Mano der
  * Cadera izq → Rodilla izq → Pie izq
  * Cadera der → Rodilla der → Pie der

### 2. Poses y Cámaras (2 puntos) ✅
- ✅ **3 poses dramáticas inspiradas en JoJo**:
  1. **"The Menacing Stance"** - Pose amenazante con brazos extendidos
  2. **"The Pointing"** - Señalando dramáticamente
  3. **"The Power Stance"** - Brazos arriba en pose de poder
- ✅ Cada pose con su propia configuración de cámara
- ✅ Cambio con barra espaciadora
- ✅ Actualización simultánea de personaje y cámara

### 3. Colores y Visualización (1 punto) ✅
- ✅ Colores diferentes por parte del cuerpo:
  * Azul: Torso y brazos superiores
  * Color piel: Cabeza, cuello, antebrazos, manos
  * Negro: Pantalones/piernas
  * Café: Zapatos
- ✅ **BONUS**: Iluminación Phong con componentes ambiente, difusa y especular

## 🎮 Cómo Ejecutar

### Método 1: Directo
```bash
cd c:\Users\56942\Desktop\CC3501_Tarea
python -m 60910000-1
```

### Método 2: Con el script
```bash
cd c:\Users\56942\Desktop\CC3501_Tarea
run.bat
```

### Controles:
- **ESPACIO**: Cambiar entre las 3 poses
- **ESC**: Salir

## 📦 Para Entregar

1. **Renombrar la carpeta `60910000-1` con tu RUT** (incluyendo guion y dígito verificador)
2. **Recrear el ZIP**:
   ```powershell
   cd c:\Users\56942\Desktop\CC3501_Tarea
   Compress-Archive -Path "TU-RUT" -DestinationPath "TU-RUT.zip" -Force
   ```
3. **Entregar `TU-RUT.zip`**

El profesor lo descomprimirá y ejecutará:
```bash
unzip TU-RUT.zip
python -m TU-RUT
```

## 🎨 Detalles Técnicos Implementados

### Grafo de Escena
- Clase `SceneGraphNode` con transformaciones jerárquicas
- Acumulación de transformaciones de padre a hijo
- Método `draw()` recursivo que recorre el árbol

### Primitivas Geométricas
- **Cubo**: 8 vértices, 36 índices (6 caras)
- **Esfera**: Generada con latitud/longitud (20x20 slices)
- **Cilindro**: Con tapas superior e inferior

### Sistema de Poses
- Cada pose define rotaciones para cada articulación
- Uso de `tr.matmul()` para componer transformaciones
- Sistema de coordenadas locales respetado

### Cámaras Dramáticas
- Pose 1: Vista desde arriba y al costado (ángulo heroico)
- Pose 2: Vista lateral cercana (ángulo de acción)
- Pose 3: Vista frontal elevada (ángulo épico)

### Iluminación
- Shader con modelo Phong completo
- Cálculo de normales usando derivadas (dFdx, dFdy)
- Luz posicionada en (5, 5, 5)

## 🔧 Tecnologías Utilizadas

- **Python 3**: Lenguaje principal
- **Pyglet**: Window manager y manejo de eventos
- **PyOpenGL**: Interfaz con OpenGL
- **NumPy**: Operaciones matriciales
- **GLSL**: Shaders (vertex + fragment)

## 📚 Basado en el Repositorio Oficial

Esta implementación sigue la estructura y ejemplos de:
https://github.com/PLUMAS-research/cc3501-computer-graphics

Específicamente inspirado en:
- `examples/scene_graphs/` - Para el grafo de escena
- `examples/transformation_composition/` - Para transformaciones
- `grafica/transformations.py` - Matrices de transformación

## 🎯 Evaluación Esperada

| Criterio | Puntos | Estado |
|----------|--------|--------|
| Grafo de escena y estructura | 3 | ✅ Completo |
| Poses y cámaras | 2 | ✅ Completo |
| Colores y visualización | 1 | ✅ Completo + Bonus |
| **TOTAL** | **6** | **✅ 6/6** |

## 💡 Notas Adicionales

- El personaje está inspirado en poses dramáticas de anime/manga
- El código está bien comentado y documentado
- La estructura es modular y fácil de extender
- Se incluye plano de referencia en el suelo
- Los colores ayudan a distinguir claramente cada parte

## 🐛 Solución de Problemas

Si encuentras errores al ejecutar:

1. **Verifica las dependencias**:
   ```bash
   pip install numpy pyglet PyOpenGL
   ```

2. **Verifica que estés en el directorio correcto**:
   ```bash
   cd c:\Users\56942\Desktop\CC3501_Tarea
   ```

3. **Prueba ejecutar directamente**:
   ```bash
   python 60910000-1/main.py
   ```

## 🎉 ¡Listo para Entregar!

Todo está implementado y funcionando. Solo necesitas:
1. Cambiar el nombre de la carpeta por tu RUT
2. Recrear el ZIP
3. Entregar

¡Buena suerte con tu tarea! 🚀
