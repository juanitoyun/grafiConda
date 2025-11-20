# Análisis 6W - Simulador de Acuario Interactivo 🐠
## Proyecto CC3501 - Computación Gráfica

---

## 📋 Las 6W del Proyecto

### 1. **WHAT - ¿Qué es el proyecto?**

**Definición Técnica:**
Un simulador de ecosistema acuático 3D en tiempo real que combina múltiples técnicas de computación gráfica para crear una experiencia visual inmersiva e interactiva.

**Componentes Principales:**
- **Sistema de comportamiento inteligente**: Peces que nadan usando algoritmos de boids (separación, cohesión, alineación)
- **Sistema de partículas**: Burbujas ascendentes con física realista
- **Elementos deformables**: Plantas acuáticas que se mueven con "corrientes" simuladas
- **Entorno 3D**: Pecera/tanque con paredes, sustrato, decoraciones
- **Sistema de iluminación**: Luz cáustica simulada, sombras, reflejos
- **Interfaz interactiva**: Control de cámara, alimentación de peces, ajuste de parámetros

**Características Visuales:**
- Renderizado en tiempo real (mínimo 30 FPS)
- Múltiples especies de peces con diferentes comportamientos
- Efectos de agua (transparencia, refracción, cáusticas)
- Animaciones procedurales (peces nadando, plantas ondulando)

---

### 2. **WHY - ¿Por qué este proyecto?**

**Justificación Académica:**
1. **Cobertura amplia del curso**: Integra 6-7 técnicas diferentes vistas en CC3501
2. **Escalabilidad**: Permite desarrollo incremental (mínimo viable → versión completa)
3. **Ejemplos base disponibles**: `boids_abm` en la caja de juguetes
4. **Complejidad adecuada**: Desafiante pero factible en el tiempo disponible

**Ventajas Técnicas:**
- ✅ **Modularidad**: Cada componente (peces, plantas, burbujas) es independiente
- ✅ **Debugging visual**: Los problemas se ven inmediatamente
- ✅ **Optimización natural**: Quadtree para boids, frustum culling para plantas
- ✅ **Extensibilidad**: Fácil agregar más features sin romper lo existente

**Valor Diferencial:**
- 🎨 **Alto impacto visual**: Resulta atractivo con esfuerzo moderado
- 🎮 **Interactividad**: No es solo una animación pasiva
- 🔬 **Emergencia**: El comportamiento complejo surge de reglas simples
- 💼 **Portfolio**: Proyecto demostrable y visualmente impresionante

**Motivación Personal:**
- Permite creatividad en diseño de especies y entorno
- Balance entre lógica (algoritmos) y arte (visualización)
- Satisfacción inmediata al ver el ecosistema "vivir"

---

### 3. **HOW - ¿Cómo se implementará?**

#### **A) Arquitectura Técnica**

```
┌─────────────────────────────────────────┐
│         MAIN LOOP (60 FPS)              │
├─────────────────────────────────────────┤
│  1. Input Handler                       │
│     - Camera controls                   │
│     - Fish feeding interactions         │
│     - Parameter adjustments             │
├─────────────────────────────────────────┤
│  2. Update Phase                        │
│     ├─ Boids System (fish behavior)    │
│     ├─ Particle System (bubbles)       │
│     ├─ Deformation (plant animation)   │
│     └─ Collision Detection              │
├─────────────────────────────────────────┤
│  3. Render Phase                        │
│     ├─ Scene Graph                      │
│     ├─ Lighting calculations            │
│     ├─ Texture mapping                  │
│     └─ Post-processing (water effect)   │
└─────────────────────────────────────────┘
```

#### **B) Pipeline de Desarrollo (4 fases)**

**FASE 1: Fundación (Semana 1) - MVP**
```python
# Objetivo: Pecera básica funcional
- [ ] Crear geometría del tanque (cubo con paredes transparentes)
- [ ] Implementar cámara orbital (arcball)
- [ ] Cargar/crear modelo simple de pez (triángulo o modelo OBJ básico)
- [ ] Implementar boids básico (3 reglas: separación, cohesión, alineación)
- [ ] Spawear 20-30 peces
- [ ] Iluminación Phong simple
```
**Entregable**: Peces nadando en un cubo sin colisiones con paredes

**FASE 2: Comportamiento (Semana 2)**
```python
# Objetivo: Comportamiento realista
- [ ] Bounding box del tanque (peces rebotan en paredes)
- [ ] Variación en velocidad de peces
- [ ] Orientación del pez según dirección de movimiento
- [ ] Animación de cola/aletas (rotación sinusoidal simple)
- [ ] Diferentes "especies" (tamaño, velocidad, color)
- [ ] Obstáculos en el tanque (rocas)
- [ ] Evitación de obstáculos en boids
```
**Entregable**: Peces que nadan naturalmente evitando paredes y obstáculos

**FASE 3: Ecosistema (Semana 3)**
```python
# Objetivo: Elementos ambientales
- [ ] Sistema de partículas para burbujas
- [ ] Plantas acuáticas (cilindros con deformación)
- [ ] Deformación sinusoidal de plantas (simulación corriente)
- [ ] Sustrato (fondo del tanque)
- [ ] Texturas para peces, plantas, sustrato
- [ ] Mejora de iluminación (luz desde arriba, cáusticas opcionales)
```
**Entregable**: Ecosistema completo y visualmente rico

**FASE 4: Interacción y Pulido (Semana 4)**
```python
# Objetivo: Interactividad y calidad
- [ ] Sistema de alimentación (click → comida cae → peces la persiguen)
- [ ] UI para parámetros (cantidad peces, velocidad corriente)
- [ ] Optimización con Quadtree (si FPS < 30)
- [ ] Efectos de post-procesamiento (underwater shader)
- [ ] Sonido ambiental (burbujas, agua)
- [ ] Polish: sombras, mejores texturas, transiciones suaves
```
**Entregable**: Proyecto completo y pulido

#### **C) Tecnologías y Técnicas del Curso**

| Componente | Técnica CC3501 | Archivo Referencia | Complejidad |
|------------|----------------|-------------------|-------------|
| Peces | **Boids + ABM** | `boids_abm.py` | Media |
| Burbujas | **Sistemas de Partículas** | `particles.py` | Baja |
| Plantas | **Deformación de Mallas** | Transformaciones | Baja |
| Tanque | **Grafos de Escena** | `solar_system.py` | Baja |
| Cámara | **Arcball** | `arcball_example.py` | Baja |
| Obstáculos | **Detección de Colisiones** | `dino_runner.py` | Media |
| Optimización | **Quadtree** | Tema de boids | Alta* |

*Opcional según performance

#### **D) Stack Técnico**

**Lenguaje y Librería Base:**
- Python 3.x
- OpenGL (via pyglet o similar, según el curso)
- Grafica library (del curso)

**Librerías Adicionales:**
```python
# Ya incluidas en environment.yml del curso
numpy          # Operaciones vectoriales para boids
pyglet         # OpenGL wrapper
trimesh        # Carga de modelos OBJ (opcional)
```

**Estructura de Archivos:**
```
acuario_interactivo/
├── main.py                 # Entry point
├── models/
│   ├── fish.py            # Clase Fish + comportamiento boids
│   ├── particle_system.py # Burbujas
│   ├── plant.py           # Plantas deformables
│   └── aquarium.py        # Contenedor
├── shaders/
│   ├── fish.vert          # Vertex shader peces
│   ├── fish.frag          # Fragment shader peces
│   └── water.frag         # Post-process agua
├── assets/
│   ├── textures/          # Texturas
│   └── models/            # Modelos OBJ (si se usan)
└── utils/
    ├── camera.py          # Arcball camera
    └── boids.py           # Algoritmo boids genérico
```

#### **E) Algoritmos Clave**

**1. Boids (Reynolds, 1987):**
```python
def update_boid(fish, neighbors, obstacles):
    # Regla 1: Separación (evitar apiñamiento)
    separation = avoid_crowding(neighbors)
    
    # Regla 2: Cohesión (moverse hacia el centro del grupo)
    cohesion = move_to_center(neighbors)
    
    # Regla 3: Alineación (igualar velocidad)
    alignment = match_velocity(neighbors)
    
    # Regla 4: Evitar obstáculos
    avoidance = avoid_obstacles(obstacles)
    
    # Regla 5: Boundaries del tanque
    boundary = bound_position(fish.position, tank_size)
    
    # Combinar fuerzas con pesos
    velocity = (separation * 1.5 + 
                cohesion * 1.0 + 
                alignment * 1.0 + 
                avoidance * 2.0 + 
                boundary * 1.5)
    
    return velocity
```

**2. Deformación de Plantas:**
```python
def deform_plant(vertex_position, time, wind_strength):
    # Deformación sinusoidal basada en altura
    height_factor = vertex_position.y / plant_height
    offset_x = sin(time + vertex_position.z) * height_factor * wind_strength
    offset_z = cos(time * 0.7 + vertex_position.x) * height_factor * wind_strength
    
    return vertex_position + vec3(offset_x, 0, offset_z)
```

**3. Sistema de Partículas (Burbujas):**
```python
class Bubble:
    def update(self, dt):
        # Física simple
        self.velocity.y += buoyancy * dt  # Flotan hacia arriba
        self.position += self.velocity * dt
        
        # Oscilación horizontal (movimiento serpenteante)
        self.position.x += sin(self.age * wobble_freq) * wobble_amount
        
        # Eliminar si sale del agua
        if self.position.y > water_surface:
            self.destroy()
```

---

### 4. **WHO - ¿Para quién y quién lo hace?**

#### **A) Usuario Final**

**Usuario Primario:**
- **Profesor y auxiliares de CC3501** (evaluadores)
- Buscan: Correcta aplicación de técnicas, creatividad, calidad técnica

**Usuario Secundario:**
- **Compañeros de curso** (presentación/demo)
- Buscan: Impacto visual, características interesantes

**Usuario Potencial:**
- **Reclutadores/Portfolio** (futuro)
- Buscan: Complejidad técnica, UI pulida, proyecto terminado

#### **B) Desarrollador**

**Rol:** Estudiante de CC3501
**Habilidades Requeridas:**
- ✅ Conocimientos de OpenGL (del curso)
- ✅ Programación en Python
- ✅ Álgebra lineal (transformaciones, vectores)
- ✅ Debugging visual
- 📚 A aprender: Algoritmos de boids, sistemas de partículas

**Equipo:** Individual (o dupla, según reglas del curso)

---

### 5. **WHEN - ¿Cuándo se desarrollará?**

#### **Timeline del Curso**
```
Fecha Actual: 12 Noviembre 2025
┌──────────────────────────────────────────────────────┐
│ SEMANA 1: 12-18 Nov                                  │
│ ├─ Lun-Mar: Aprobación propuesta                     │
│ └─ Mié-Dom: FASE 1 (MVP - Fundación)                 │
├──────────────────────────────────────────────────────┤
│ SEMANA 2: 19-25 Nov                                  │
│ └─ FASE 2 (Comportamiento)                           │
├──────────────────────────────────────────────────────┤
│ SEMANA 3: 26 Nov - 2 Dic                             │
│ └─ FASE 3 (Ecosistema)                               │
├──────────────────────────────────────────────────────┤
│ SEMANA 4: 3-9 Dic                                    │
│ └─ FASE 4 (Interacción y Pulido)                     │
├──────────────────────────────────────────────────────┤
│ SEMANA 5: 10-15 Dic                                  │
│ └─ Buffer/Testing/Documentación                      │
├──────────────────────────────────────────────────────┤
│ ~16-20 Dic: Entrega final (último día de clases)    │
└──────────────────────────────────────────────────────┘
```

#### **Distribución de Tiempo Semanal**
- **Días de semana**: 2 hrs/día de trabajo enfocado (10 hrs/semana)
- **Fin de semana**: 4-6 hrs de trabajo intensivo
- **Total**: ~16-20 hrs/semana × 4-5 semanas = 64-100 hrs totales

#### **Hitos Críticos**
- ✅ **18 Nov**: Propuesta aprobada → Iniciar desarrollo
- 🎯 **25 Nov**: MVP funcionando (demo checkpoint)
- 🎯 **2 Dic**: Features principales completas
- 🎯 **9 Dic**: Proyecto completo, iniciar pulido
- 🚀 **~17 Dic**: Entrega final

---

### 6. **WHERE - ¿Dónde se implementará/ejecutará?**

#### **A) Entorno de Desarrollo**

**Hardware Mínimo:**
- CPU: Cualquier procesador moderno (i5 o equivalente)
- GPU: Integrada suficiente (Intel HD, o dedicada para mejor experiencia)
- RAM: 4 GB (8 GB recomendado)
- OS: Windows/Linux/macOS (multiplataforma via Python)

**Software:**
```bash
# Entorno del curso
conda activate grafica

# IDE/Editor
- VS Code (con extensiones Python, GLSL)
- PyCharm (alternativa)

# Control de versiones
git + GitHub (backup y portfolio)
```

#### **B) Entorno de Ejecución**

**Instalación:**
```bash
# Ya está en el environment.yml del curso
cd proyecto_acuario/
python acuario_interactivo.py
```

**Plataforma objetivo:**
- Computadores del laboratorio de computación
- Laptop personal del estudiante
- Máquina del profesor (evaluación)

**Requisitos de Runtime:**
- Python 3.8+
- OpenGL 3.3+ compatible GPU
- Resolución mínima: 1280×720
- Target FPS: 30-60 (depende de cantidad de peces)

#### **C) Contexto de Presentación**

**Demo en clase:**
- Proyector (resolución variable)
- Audio (si se implementa)
- Control interactivo en vivo

**Entrega:**
- Repositorio Git con código fuente
- README con instrucciones
- Video demo (opcional pero recomendado)
- Documento técnico explicando implementación

---

## 🔄 IMPLICANCIAS EN EL PROCEDIMIENTO

### **1. Implicancias de Diseño**

#### **A) Modularidad Obligatoria**
**Por qué:** Múltiples sistemas independientes (peces, plantas, burbujas)
**Cómo afecta:**
- ✅ Cada componente debe ser una clase separada
- ✅ Interfaces claras entre módulos
- ✅ Permite desarrollo y testing independiente
- ⚠️ Requiere planificación inicial de arquitectura

**Ejemplo:**
```python
# ❌ EVITAR: Todo en un archivo monolítico
# ✅ HACER: Separación de responsabilidades
class AquariumScene:
    def __init__(self):
        self.fish_system = FishSystem()      # Maneja boids
        self.particle_sys = ParticleSystem() # Burbujas
        self.plant_manager = PlantManager()  # Plantas
        self.camera = ArcballCamera()        # Cámara
```

#### **B) Performance Crítico**
**Por qué:** Muchos objetos actualizándose cada frame (50+ peces + 100+ burbujas)
**Cómo afecta:**
- ✅ Necesidad de perfilado temprano (`cProfile`)
- ✅ Implementar optimizaciones si FPS < 30:
  - Spatial partitioning (Quadtree/Octree)
  - Frustum culling
  - LOD para peces lejanos
- ⚠️ No optimizar prematuramente (solo si necesario)

**Decisión de diseño:**
```python
# Si hay 100+ peces, usar Quadtree para búsqueda de vecinos
if num_fish > 50:
    neighbors = quadtree.query_radius(fish.pos, perception_radius)
else:
    # Búsqueda ingenua OK para pocos peces
    neighbors = [f for f in all_fish if distance(f, fish) < radius]
```

#### **C) Escalabilidad de Features**
**Por qué:** Tiempo limitado, priorización esencial
**Cómo afecta:**
- ✅ Definir versión **mínima viable** vs **completa** desde día 1
- ✅ Features como "nice to have" no bloquean entrega

**Priorización:**
```
🔴 CRÍTICO (Debe estar):
  - Boids funcional
  - Peces renderizados
  - Cámara móvil

🟡 IMPORTANTE (Debería estar):
  - Plantas
  - Burbujas
  - Texturas
  - Iluminación decente

🟢 OPCIONAL (Sería genial):
  - Cáusticas de agua
  - Sombras
  - Audio
  - Alimentación interactiva
```

---

### **2. Implicancias de Desarrollo**

#### **A) Testing Visual Continuo**
**Por qué:** Los bugs gráficos no se ven en unit tests
**Cómo afecta:**
- ✅ Ejecutar el programa cada 30-60 minutos de código
- ✅ Tener valores de debug visuales (bounding boxes, vectores de dirección)
- ✅ Screenshot de progreso diario

**Herramientas de debug:**
```python
# Toggle de visualización
if DEBUG_MODE:
    draw_boid_vectors()      # Mostrar dirección de peces
    draw_collision_bounds()  # Mostrar bounding boxes
    draw_quadtree_grid()     # Visualizar spatial partitioning
    print_fps()              # Monitor de performance
```

#### **B) Versionado Incremental**
**Por qué:** Fácil romper todo con un cambio
**Cómo afecta:**
- ✅ Git commits frecuentes con mensajes descriptivos
- ✅ Tags para versiones funcionales (`v0.1-mvp`, `v0.2-boids`)
- ✅ Poder revertir a versión estable

**Flujo de trabajo:**
```bash
git checkout -b feature/bubble-particles
# Desarrollar sistema de partículas
git commit -m "Add bubble particle system with physics"
git checkout main
git merge feature/bubble-particles
git tag v0.3-particles
```

#### **C) Documentación Inline**
**Por qué:** El código de gráficos puede ser críptico (muchas matrices, transformaciones)
**Cómo afecta:**
- ✅ Comentar ecuaciones y algoritmos no obvios
- ✅ Docstrings en clases y funciones principales
- ✅ README con arquitectura del proyecto

**Ejemplo:**
```python
def calculate_boid_separation(fish, neighbors):
    """
    Implementa la regla de separación de Reynolds (1987).
    Los peces evitan estar muy cerca entre sí.
    
    Args:
        fish: Pez actual
        neighbors: Lista de peces vecinos dentro del perception radius
    
    Returns:
        Vector de steering para alejarse del centro de masa cercano
    """
    steering = np.array([0.0, 0.0, 0.0])
    for neighbor in neighbors:
        distance = np.linalg.norm(fish.position - neighbor.position)
        if distance < SEPARATION_DISTANCE:
            # Fuerza inversamente proporcional a la distancia
            steering += (fish.position - neighbor.position) / distance
    return steering
```

---

### **3. Implicancias de Algoritmos**

#### **A) Boids Requiere Spatial Queries Eficientes**
**Problema:** Cada pez necesita encontrar vecinos cercanos
**Complejidad naïve:** O(N²) - inviable con 100+ peces a 60 FPS

**Solución:**
```python
# FASE 1-2: Búsqueda ingenua (OK para <30 peces)
def find_neighbors_naive(fish):
    return [f for f in all_fish if distance(f, fish) < RADIUS]

# FASE 4: Quadtree (necesario para 50+ peces)
class Quadtree:
    def query_radius(self, position, radius):
        # O(log N) en promedio
        pass
```

**Implicancia:** Dejar espacio en la arquitectura para cambiar el algoritmo después

#### **B) Deformación de Plantas: CPU vs GPU**
**Decisión:** ¿Calcular deformación en Python o en Vertex Shader?

**Opción 1: CPU (más simple)**
```python
# Pro: Fácil de debuggear
# Con: Más lento con muchas plantas
for vertex in plant.vertices:
    vertex.x += sin(time + vertex.y) * wind_strength
```

**Opción 2: GPU (más eficiente)**
```glsl
// Vertex Shader
// Pro: Muy rápido, paralelo
// Con: Más difícil de debuggear
vec3 deformed = position;
deformed.x += sin(u_time + position.y) * u_wind;
gl_Position = projection * view * model * vec4(deformed, 1.0);
```

**Implicancia:** Empezar CPU (FASE 1-2), migrar a GPU si es necesario (FASE 4)

#### **C) Física de Burbujas: Realismo vs Performance**
**Decisión:** ¿Qué tan realista debe ser la física?

```python
# Opción Simple (suficiente):
bubble.y += RISE_SPEED * dt
bubble.x += sin(bubble.age) * WOBBLE

# Opción Realista (overkill):
# - Volumen de burbuja afecta velocidad
# - Turbulencia del agua
# - Coalescencia de burbujas
# - Presión del agua
# → Demasiado complejo para este proyecto
```

**Implicancia:** Simplificar física cuando no es el foco del proyecto

---

### **4. Implicancias de Assets y Recursos**

#### **A) Modelos 3D**
**Opción 1: Modelar en Blender**
- Pro: Control total, aprendizaje
- Con: Mucho tiempo (4-6 hrs por modelo decente)

**Opción 2: Usar geometría procedural simple**
```python
# Pez = Elipsoide + Triángulos para aletas
fish_body = create_ellipsoid(radius_x=0.2, radius_y=0.1, radius_z=0.05)
tail = create_triangle(size=0.1)
# Pro: Rápido, suficiente para demo
# Con: Menos realista
```

**Opción 3: Assets gratuitos (SketchFab, TurboSquid free)**
- Pro: Alta calidad, rápido
- Con: Posible incompatibilidad de formato, licensing

**Implicancia:** Empezar con geometría simple, mejorar si hay tiempo

#### **B) Texturas**
**Fuentes:**
- OpenGameArt.org (CC0)
- Textures.com (free tier)
- Procedural (ruido Perlin para escamas)

**Workflow:**
```python
# FASE 1-2: Colores sólidos
fish.color = (1.0, 0.5, 0.0)  # Naranja

# FASE 3: Texturas
fish.texture = load_texture('assets/fish_scales.png')
```

---

### **5. Implicancias de Interactividad**

#### **A) Input Handling**
**Controles mínimos:**
```python
# Cámara (arcball)
- Mouse drag: Rotar
- Scroll: Zoom
- Right click drag: Pan

# Interacción
- Click: Alimentar peces (opcional)
- Keys 1-5: Cambiar vista predefinida
- Space: Pause simulación
```

**Implicancia:** UI simple evita complejidad innecesaria

#### **B) Parámetros Ajustables**
**Opción 1: Hardcoded (inicial)**
```python
NUM_FISH = 30
BOID_SEPARATION_WEIGHT = 1.5
```

**Opción 2: Config file (mejor)**
```json
{
  "num_fish": 30,
  "boid_params": {
    "separation": 1.5,
    "cohesion": 1.0,
    "alignment": 1.0
  }
}
```

**Opción 3: GUI en tiempo real (ideal)**
```python
# Con imgui o similar
if imgui.slider_int("Num Fish", num_fish, 10, 100):
    fish_system.respawn(num_fish)
```

**Implicancia:** Opción 2 (config) es buen balance tiempo/utilidad

---

### **6. Implicancias de Evaluación**

#### **A) Criterios del Curso (asumidos)**
- ✅ Correcta implementación de técnicas (40%)
- ✅ Creatividad y diseño (20%)
- ✅ Calidad visual (20%)
- ✅ Complejidad técnica (10%)
- ✅ Documentación/presentación (10%)

**Implicancia en desarrollo:**
```
Prioridad 1: Que las técnicas funcionen correctamente
  → Boids debe mostrar comportamiento emergente
  → Partículas deben tener física coherente
  → Deformación debe ser visible y controlada

Prioridad 2: Que se vea bien
  → Iluminación, texturas, colores armoniosos
  → Animaciones suaves

Prioridad 3: Documentación
  → README explicando técnicas usadas
  → Comentarios en código complejo
```

#### **B) Demo Day**
**Preparación:**
- Script de demo (30-60 segundos)
- Vistas preparadas que muestren mejor ángulo
- Backup: Video grabado si falla en vivo

**Qué mostrar:**
1. Vista general del acuario (10 seg)
2. Zoom a peces mostrando boids (15 seg)
3. Plantas moviéndose (5 seg)
4. Burbujas subiendo (5 seg)
5. Interacción (alimentar peces) (15 seg)

---

## 📊 Tabla Resumen de Implicancias

| Aspecto | Implicancia Principal | Acción Requerida |
|---------|----------------------|------------------|
| **Arquitectura** | Modularidad obligatoria | Diseñar clases separadas desde día 1 |
| **Performance** | Optimización condicional | Perfilar en FASE 2, optimizar en FASE 4 si necesario |
| **Testing** | Visual y continuo | Ejecutar programa cada hora de desarrollo |
| **Assets** | Geometría simple inicial | Empezar con primitivas, mejorar después |
| **Algoritmos** | Boids puede ser O(N²) | Implementar Quadtree solo si FPS < 30 |
| **Física** | Simplificar cuando posible | Burbujas/plantas no necesitan física compleja |
| **Versionado** | Git commits frecuentes | Mínimo 1 commit/día, tags en hitos |
| **Interactividad** | UI simple suficiente | Cámara + 1-2 interacciones, no más |
| **Documentación** | Comentar algoritmos no obvios | Docstrings + README + inline comments |
| **Evaluación** | Funcionalidad > Belleza | Primero que funcione, luego que se vea bonito |

---

## 🎯 Checklist de Decisiones Críticas

Antes de empezar a programar, decidir:

- [ ] **¿Cuántos peces en la versión mínima?** (Recomendado: 20-30)
- [ ] **¿Geometría procedural o modelos OBJ?** (Recomendado: Procedural primero)
- [ ] **¿Implementar Quadtree desde el inicio?** (Recomendado: No, solo si FPS < 30)
- [ ] **¿Plantas estáticas o animadas?** (Recomendado: Animadas, es fácil)
- [ ] **¿Sistema de alimentación?** (Recomendado: Sí, es fácil y divertido)
- [ ] **¿Cáusticas de agua?** (Recomendado: No, muy complejo)
- [ ] **¿Audio?** (Recomendado: Solo si sobra tiempo)
- [ ] **¿Usar Git?** (Recomendado: SÍ, obligatorio)

---

## 🚀 Próximos Pasos Inmediatos

1. **Hoy (12 Nov):**
   - [ ] Enviar propuesta al profesor (usar párrafo de `ideas_proyecto.md`)
   - [ ] Crear repositorio Git
   - [ ] Configurar entorno `conda activate grafica`

2. **Mañana (13 Nov):**
   - [ ] Estudiar `boids_abm.py` del curso
   - [ ] Probar ejemplo: `python caja_de_juguetes.py boids_abm`
   - [ ] Diseñar estructura de clases (diagrama simple)

3. **Esta Semana (14-18 Nov):**
   - [ ] Implementar FASE 1 (MVP)
   - [ ] Checkpoint viernes: ¿Ves peces nadando?

---

**¿Listo para empezar? Este análisis 6W te da un mapa completo del proyecto. ¡Buena suerte! 🐠✨**
