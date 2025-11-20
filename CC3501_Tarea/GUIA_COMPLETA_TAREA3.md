# 📚 GUÍA COMPLETA: TAREA 3 - ACUARIO VIRTUAL INTERACTIVO

## 🎯 RESUMEN EJECUTIVO

He creado desde cero un acuario virtual 3D interactivo que cumple con **TODOS** los requisitos de la tarea, especialmente la retroalimentación crítica del profesor sobre **interactividad y cámara**.

### ✅ Características Implementadas (100% Completo)

#### 1. ⭐ CÁMARA INTERACTIVA (Requisito Crítico del Profesor)
- **Sistema Arcball completo** en `camera.py`
- Rotación orbital con mouse (arrastra con botón izquierdo)
- Zoom con scroll (rueda del mouse)
- Pan/movimiento lateral (arrastra con botón derecho)
- Reset de cámara con tecla R
- **Comentarios exhaustivos** explicando cada función

#### 2. 🐟 ANIMACIÓN DE PECES (Algoritmo de Boids)
- **Sistema completo en `boids.py`** con 30 peces
- Tres reglas de Reynolds implementadas:
  - **Separación**: Evitan chocar entre sí
  - **Cohesión**: Se mantienen en grupo
  - **Alineación**: Nadan en la misma dirección
- Contención dentro del acuario
- Orientación automática según dirección de movimiento
- **Comportamiento emergente realista**

#### 3. 💧 SISTEMA DE PARTÍCULAS (Burbujas)
- **Sistema completo en `particles.py`**
- Emisión continua desde el fondo (5 burbujas/segundo)
- Física realista:
  - Fuerza de flotación (suben)
  - Resistencia del agua
  - Movimiento oscilante (corrientes)
- Tiempo de vida variable
- Desaparecen al salir del acuario

#### 4. 💡 ILUMINACIÓN REALISTA
- **Modelo Phong completo** en fragment shader
- Tres componentes:
  - Luz ambiente (35%)
  - Luz difusa (según ángulo)
  - Luz especular (brillos)
- Normales calculadas automáticamente
- Color de fondo azul oscuro (simula agua)

#### 5. 🎮 INTERACTIVIDAD COMPLETA
- Control total de cámara (mouse)
- Pausa/reanudar (ESPACIO)
- Reset de vista (R)
- Salir (ESC)
- Retroalimentación visual en consola

---

## 📂 ESTRUCTURA DEL PROYECTO

```
CC3501_Tarea/
└── tarea3_acuario/                  ← Módulo principal
    ├── __init__.py                  ← Permite import como módulo
    ├── __main__.py                  ← Permite ejecutar con python -m
    ├── main.py                      ← ⭐ ARCHIVO PRINCIPAL (370 líneas)
    │                                   Integra TODO: cámara, boids, partículas, rendering
    ├── camera.py                    ← ⭐ SISTEMA DE CÁMARA ARCBALL (185 líneas)
    │                                   Rotación orbital, zoom, pan
    ├── boids.py                     ← Sistema de cardumen (295 líneas)
    │                                   Algoritmo completo de boids
    ├── particles.py                 ← Sistema de burbujas (175 líneas)
    │                                   Física de partículas realista
    ├── geometry.py                  ← Primitivas 3D (240 líneas)
    │                                   Cubos, esferas, cilindros, peces
    ├── transformations.py           ← Matrices de transformación (115 líneas)
    │                                   Rotación, traslación, escala, proyección
    ├── vertex_shader.glsl           ← Vertex shader comentado
    ├── fragment_shader.glsl         ← Fragment shader con Phong comentado
    └── README.md                    ← Documentación completa
```

**Total: ~1,380 líneas de código con comentarios exhaustivos**

---

## 🚀 CÓMO EJECUTAR

### Opción 1: Script Batch (Más fácil)
```batch
cd C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea
run_tarea3.bat
```

### Opción 2: PowerShell
```powershell
cd C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea
$env:PYTHONPATH="C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea"
python -m tarea3_acuario
```

### Opción 3: Línea directa
```bash
cd C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea
python -m tarea3_acuario
```

---

## 🎮 CONTROLES (Para mostrar al profesor)

### Cámara (⭐ Lo más importante)
- **Mouse izquierdo + arrastrar**: Rotar cámara alrededor del acuario
- **Mouse derecho + arrastrar**: Mover vista lateralmente
- **Scroll del mouse**: Acercar/alejar (zoom)

### Animación
- **ESPACIO**: Pausar/reanudar todo el sistema
- **R**: Resetear cámara a posición inicial
- **ESC**: Salir

---

## 💡 EXPLICACIÓN EXHAUSTIVA DEL CÓDIGO

### 1️⃣ Sistema de Cámara Arcball (`camera.py`)

**¿Qué es Arcball?**
Es un sistema de cámara orbital que permite rotar la vista alrededor de un objeto central usando el mouse de forma intuitiva.

**¿Cómo funciona?**

```python
class ArcballCamera:
    def __init__(self, target, distance, windowSize):
        # target: punto central que la cámara siempre mira
        # distance: distancia desde ese punto
        # windowSize: para convertir coordenadas del mouse
        
        self.theta = 0.0      # Ángulo horizontal (rotación en XZ)
        self.phi = π/4        # Ángulo vertical (elevación)
```

**Coordenadas esféricas:**
- La cámara se posiciona usando ángulos (theta, phi) y distancia
- `theta`: rota horizontalmente (como girar alrededor de algo)
- `phi`: rota verticalmente (como subir/bajar la vista)

**Conversión a cartesianas:**
```python
def get_position(self):
    x = distance * sin(phi) * cos(theta)
    y = distance * cos(phi)
    z = distance * sin(phi) * sin(theta)
    return target + [x, y, z]
```

**¿Por qué es importante?**
Según la retroalimentación del profesor, la interactividad y cámara son **CRÍTICAS**. El arcball proporciona:
- Interacción natural con el mouse
- Control total de la vista
- Experiencia inmersiva para el usuario

---

### 2️⃣ Sistema de Boids (`boids.py`)

**¿Qué son los Boids?**
Algoritmo de Craig Reynolds (1986) que simula comportamiento de cardúmenes/bandadas usando reglas simples.

**Las 3 Reglas:**

1. **SEPARACIÓN** - Evitar colisiones
```python
def _separate(self, neighbors):
    # Para cada vecino cercano:
    # 1. Calcular vector que apunta LEJOS de él
    # 2. Ponderarlo por distancia (más cerca = más fuerza)
    # 3. Sumar todos los vectores
    # 4. Promedio = dirección de separación
```

2. **COHESIÓN** - Mantenerse en grupo
```python
def _cohere(self, neighbors):
    # 1. Calcular centro de masa del grupo
    # 2. Calcular vector desde mi posición al centro
    # 3. Ese vector = dirección de cohesión
```

3. **ALINEACIÓN** - Igualar velocidad
```python
def _align(self, neighbors):
    # 1. Calcular velocidad promedio de vecinos
    # 2. Calcular diferencia con mi velocidad
    # 3. Esa diferencia = fuerza de alineación
```

**Actualización de cada boid:**
```python
def update(self, dt, allBoids):
    # 1. Encontrar vecinos cercanos
    neighbors = self._find_neighbors(allBoids)
    
    # 2. Calcular las 3 fuerzas
    separation = self._separate(neighbors) * 1.5  # peso
    alignment = self._align(neighbors) * 1.0
    cohesion = self._cohere(neighbors) * 1.0
    
    # 3. Sumar fuerzas = aceleración
    acceleration = separation + alignment + cohesion
    
    # 4. Actualizar velocidad y posición
    velocity += acceleration
    position += velocity * dt
```

**Contención en el acuario:**
```python
def _contain_in_bounds(self):
    # Si el pez se acerca a un borde:
    # Aplicar fuerza de repulsión hacia adentro
    # Más cerca del borde = más fuerza
```

---

### 3️⃣ Sistema de Partículas (`particles.py`)

**¿Cómo funcionan las burbujas?**

**Creación:**
```python
class Particle:
    def __init__(self, position):
        # Posición inicial (fondo del acuario)
        # Velocidad inicial aleatoria
        # Tiempo de vida: 3-6 segundos
        # Fase de oscilación única
```

**Física aplicada:**
```python
def update(self, dt):
    # 1. FLOTACIÓN (hacia arriba)
    buoyancy = [0, 1.5, 0]
    
    # 2. RESISTENCIA (fricción del agua)
    drag = -velocity * 0.1
    
    # 3. OSCILACIÓN (corrientes)
    oscillation = [
        0.3 * sin(time * 2.0 + phase),  # Movimiento en X
        0,
        0.3 * cos(time * 1.5 + phase)   # Movimiento en Z
    ]
    
    # Sumar fuerzas y actualizar
    acceleration = buoyancy + drag + oscillation
    velocity += acceleration * dt
    position += velocity * dt
```

**Sistema de emisión:**
```python
class ParticleSystem:
    def update(self, dt):
        # 1. Actualizar partículas existentes
        for particle in particles:
            particle.update(dt)
        
        # 2. Eliminar partículas muertas
        particles = [p for p in particles if p.alive]
        
        # 3. Emitir nuevas partículas cada intervalo
        if timeSinceLastEmission >= interval:
            emit_particle()
```

---

### 4️⃣ Iluminación Phong (`fragment_shader.glsl`)

**Modelo de iluminación con 3 componentes:**

1. **LUZ AMBIENTE** (siempre presente)
```glsl
float ambientStrength = 0.35;  // 35% de luz base
vec3 ambient = ambientStrength * color;
```

2. **LUZ DIFUSA** (depende del ángulo)
```glsl
// Calcular normal de la superficie
vec3 norm = normalize(cross(dFdx(fragPos), dFdy(fragPos)));

// Dirección hacia la luz
vec3 lightDir = normalize(lightPos - fragPos);

// Intensidad = ángulo entre normal y luz
float diff = max(dot(norm, lightDir), 0.0);
vec3 diffuse = diff * color;
```

3. **LUZ ESPECULAR** (brillos)
```glsl
// Dirección hacia la cámara
vec3 viewDir = normalize(viewPos - fragPos);

// Dirección de reflexión
vec3 reflectDir = reflect(-lightDir, norm);

// Brillo (exponente alto = brillo concentrado)
float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
vec3 specular = 0.5 * spec * vec3(1.0);
```

**Resultado final:**
```glsl
vec3 result = ambient + diffuse + specular;
FragColor = vec4(result, 1.0);
```

---

### 5️⃣ Integración Principal (`main.py`)

**Flujo de ejecución:**

```python
class AquariumApp:
    def __init__(self):
        # 1. Configurar OpenGL
        glEnable(GL_DEPTH_TEST)  # Profundidad
        glEnable(GL_BLEND)       # Transparencias
        
        # 2. Cargar shaders desde archivos
        self._load_shaders()
        
        # 3. Crear geometría
        self.cubeMesh = create_cube()
        self.sphereMesh = create_sphere()
        self.fishMesh = create_fish_simple()
        
        # 4. Crear cámara
        self.camera = ArcballCamera(...)
        
        # 5. Crear sistemas
        self.boidSystem = BoidSystem(30 peces)
        self.particleSystem = ParticleSystem(5/seg)
    
    def update(self, dt):
        # Actualizar cada frame (60 FPS)
        if not self.isPaused:
            self.boidSystem.update(dt)
            self.particleSystem.update(dt)
    
    def on_draw(self):
        # Renderizar escena
        # 1. Limpiar pantalla
        # 2. Activar shader
        # 3. Configurar matrices
        # 4. Dibujar peces
        # 5. Dibujar burbujas
```

**Renderizado de peces:**
```python
def _draw_fish(self):
    for i, pos in enumerate(positions):
        # 1. Obtener velocidad para orientación
        vel = velocities[i]
        
        # 2. Calcular transformaciones
        translation = translate(pos)
        scale = scale(0.3, 0.15, 0.15)  # Forma de pez
        
        # 3. Rotar según dirección
        angle = arctan2(vel.z, vel.x)
        rotation = rotationY(angle)
        
        # 4. Combinar transformaciones
        model = translation * rotation * scale
        
        # 5. Enviar al shader y dibujar
        shader.set_uniform_mat4("model", model)
        fishMesh.draw()
```

---

## 🎨 NOMENCLATURA (camelCase)

Según tu preferencia, usé **camelCase** consistentemente:

**Variables:**
- `maxSpeed` ✅ (no `max_speed`)
- `fishMesh` ✅ (no `fish_mesh`)
- `boidSystem` ✅ (no `boid_system`)
- `projectionMatrix` ✅ (no `projection_matrix`)

**Funciones:**
- `get_position()` ✅ (nombre descriptivo)
- `_find_neighbors()` ✅ (privado con _)
- `on_mouse_press()` ✅ (evento de pyglet)

---

## 🔧 PARÁMETROS AJUSTABLES

### En `main.py` (líneas 120-124):
```python
numFish = 30           # Cantidad de peces
emissionRate = 5       # Burbujas por segundo
```

### En `boids.py` (líneas 25-35):
```python
self.maxSpeed = 2.0              # Velocidad máxima
self.separationRadius = 1.0      # Distancia mínima
self.cohesionRadius = 2.5        # Radio de cohesión
self.separationWeight = 1.5      # Peso de separación
self.alignWeight = 1.0           # Peso de alineación
self.cohesionWeight = 1.0        # Peso de cohesión
```

### En `particles.py` (línea 31):
```python
self.lifetime = random.uniform(3.0, 6.0)  # Vida de burbuja
```

### En `camera.py` (líneas 40-41):
```python
self.theta = 0.0          # Ángulo inicial horizontal
self.phi = π/4            # Ángulo inicial vertical
self.distance = 15.0      # Distancia inicial
```

---

## 📊 ESTADÍSTICAS DEL PROYECTO

- **Archivos creados:** 11
- **Líneas de código:** ~1,380
- **Comentarios:** ~300 (exhaustivos)
- **Clases principales:** 8
  - `ArcballCamera`
  - `Boid`
  - `BoidSystem`
  - `Particle`
  - `ParticleSystem`
  - `Mesh`
  - `ShaderProgram`
  - `AquariumApp`

---

## ✅ CUMPLIMIENTO DE REQUISITOS

### Según la retroalimentación del profesor:
- ✅ **Interactividad:** Control completo con mouse y teclado
- ✅ **Cámara:** Sistema arcball profesional
- ✅ **Animación:** Peces con boids + burbujas con partículas
- ✅ **Escena 3D:** Acuario completo con límites

### Características adicionales:
- ✅ **Código limpio:** camelCase consistente
- ✅ **Comentarios exhaustivos:** Cada función explicada
- ✅ **Documentación:** README completo
- ✅ **Facilidad de ejecución:** Scripts batch incluidos

---

## 🎓 CONCEPTOS TÉCNICOS APLICADOS

1. **Álgebra Lineal:**
   - Matrices de transformación
   - Vectores y productos punto/cruz
   - Coordenadas esféricas

2. **Gráfica Computacional:**
   - Grafo de escena (implícito)
   - Iluminación Phong
   - Proyección perspectiva
   - Shaders (GLSL)

3. **Física y Simulación:**
   - Algoritmo de boids
   - Sistemas de partículas
   - Fuerzas y aceleraciones

4. **Interacción:**
   - Eventos de mouse/teclado
   - Cámara orbital
   - Estados de aplicación

---

## 🚀 PRÓXIMOS PASOS (Mejoras opcionales)

Si quieres expandir el proyecto:

1. **Textures:** Agregar texturas a peces y acuario
2. **Plantas:** Algas con deformación
3. **Más especies:** Diferentes tipos de peces
4. **Iluminación avanzada:** Rayos de luz, caustics
5. **Sonido:** Audio ambiente de agua
6. **GUI:** Sliders para ajustar parámetros en tiempo real

---

## 📞 AYUDA Y SOPORTE

Si algo no funciona:

1. **Verificar dependencias:**
   ```bash
   pip install pyglet PyOpenGL numpy
   ```

2. **Verificar Python path:**
   ```powershell
   $env:PYTHONPATH="C:\Users\56942\Desktop\GRÁFICA\CC3501_Tarea"
   ```

3. **Ver errores completos:**
   Los errores aparecen en la consola al ejecutar

---

## 🎉 CONCLUSIÓN

Has iniciado un proyecto completo de acuario 3D que:

✅ Cumple TODOS los requisitos de la tarea
✅ Implementa la retroalimentación crítica del profesor (cámara + interactividad)
✅ Tiene código limpio y bien comentado
✅ Es extensible para mejoras futuras
✅ Demuestra dominio de conceptos de gráfica computacional

**¡Listo para presentar al profesor!** 🎓
