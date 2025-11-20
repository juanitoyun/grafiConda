# Análisis Comparativo: Dimensionalidad y Perspectivas del Acuario
## 2D vs 3D - Perspectivas y Vistas

---

## 🎯 Resumen Ejecutivo

**Recomendación Final:** **3D con Vista Orbital Libre (Opción 3D-A)** ✨

**Razón:** Mejor balance entre impresión visual, cobertura de técnicas del curso, y complejidad manejable. Permite mostrar dominio de gráficos 3D sin sobrecarga técnica innecesaria.

---

## 📊 TABLA COMPARATIVA GENERAL

| Aspecto | 2D | 3D |
|---------|-------|-------|
| **Complejidad Técnica** | ⭐⭐ (Baja) | ⭐⭐⭐⭐ (Alta) |
| **Impacto Visual** | ⭐⭐⭐ (Moderado) | ⭐⭐⭐⭐⭐ (Muy Alto) |
| **Cobertura del Curso** | ⭐⭐ (Limitada) | ⭐⭐⭐⭐⭐ (Completa) |
| **Tiempo de Desarrollo** | 2-3 semanas | 3-4 semanas |
| **Dificultad de Debug** | ⭐⭐ (Fácil) | ⭐⭐⭐ (Media) |
| **Potencial Portfolio** | ⭐⭐⭐ (Decente) | ⭐⭐⭐⭐⭐ (Excelente) |
| **Performance** | ⭐⭐⭐⭐⭐ (Excelente) | ⭐⭐⭐ (Depende) |
| **Escalabilidad** | ⭐⭐⭐ (Limitada) | ⭐⭐⭐⭐⭐ (Muy Alta) |

---

## 🔷 OPCIÓN 1: ACUARIO 2D

### **1.1 Vista Lateral (Perfil del Acuario)** 👁️

```
Vista del jugador:
┌─────────────────────────────┐ ← Superficie del agua
│    🐟      🐟                │
│                  🐟          │
│ 🌿    🐟             🌿  🐟  │
│ 🌿              🌿   🌿      │
│ 🌿    🪨     🪨      🌿  🪨  │
└─────────────────────────────┘
   Sustrato/Grava
```

#### **Características:**
- Peces se mueven en plano XY (horizontal, vertical)
- Plantas fijas en el fondo
- Burbujas suben en línea recta (o con wobble en X)
- Profundidad simulada con parallax o capas

#### **✅ Ventajas:**
1. **Simplicidad extrema:**
   - Matemáticas 2D: sin matrices de proyección complejas
   - Boids solo en 2 dimensiones (X, Y)
   - Colisiones 2D (AABB o círculos)
   
2. **Debugging fácil:**
   - Todo visible siempre
   - Coordenadas simples de imprimir
   - Menos cosas que pueden salir mal

3. **Performance excelente:**
   - No hay cálculos de proyección 3D
   - No hay depth buffer
   - Puede manejar 200+ peces sin problemas

4. **Estilo artístico definido:**
   - Puede verse como "juego indie 2D"
   - Estética pixel art o vector art

5. **Desarrollo rápido:**
   - MVP en 3-5 días
   - Más tiempo para pulir detalles

#### **❌ Desventajas:**
1. **Limitación de técnicas del curso:**
   - ❌ No usa matrices de proyección (perspectiva/ortogonal)
   - ❌ No practica cámara 3D (arcball, etc.)
   - ❌ No usa grafos de escena 3D
   - ⚠️ Menos "computación gráfica", más "programación de juegos"

2. **Impacto visual menor:**
   - Menos impresionante en presentación
   - Difícil competir con proyectos 3D de compañeros

3. **Restricción espacial:**
   - Peces no pueden nadar "hacia" o "desde" la cámara
   - Comportamiento boids menos natural (falta dimensión Z)

4. **Escalabilidad limitada:**
   - Difícil agregar features 3D después (gran refactor)

#### **⚙️ Implementación:**
```python
# Boids 2D simplificado
class Fish2D:
    def __init__(self):
        self.position = np.array([x, y])      # Solo 2D
        self.velocity = np.array([vx, vy])
    
    def update_boids(self, neighbors):
        # Reglas boids en 2D
        separation = self.separate_2d(neighbors)
        cohesion = self.cohere_2d(neighbors)
        alignment = self.align_2d(neighbors)
        
        self.velocity += separation + cohesion + alignment
        self.position += self.velocity * dt

# Renderizado ortogonal simple
def render():
    # No hay proyección, coordenadas del mundo = coordenadas de pantalla
    for fish in fishes:
        draw_sprite(fish.position.x, fish.position.y, fish.sprite)
```

#### **📈 Complejidad:**
- Matemáticas: ⭐⭐ (Álgebra básica)
- OpenGL: ⭐ (Sprites 2D, sin 3D pipeline)
- Algoritmos: ⭐⭐⭐ (Boids sigue siendo complejo)

#### **Tiempo Estimado:** 2 semanas

---

### **1.2 Vista Cenital/Top-Down (Desde Arriba)** 🔍

```
Vista aérea del acuario:
┌─────────────────────────────┐
│    🐟→                       │
│           🪨                 │
│  🌿              🐟↓         │
│  🌿   🐟↗               🌿   │
│              🪨    🐟←   🌿  │
│  🌿                      🌿  │
└─────────────────────────────┘
```

#### **Características:**
- Peces se mueven en plano XZ (visto desde arriba)
- Plantas son círculos/sprites (no se ve altura)
- Burbujas invisibles (o círculos crecientes)
- Típico de RTS o simuladores estratégicos

#### **✅ Ventajas:**
1. **Espacialidad natural:**
   - Más fácil ver distribución de peces
   - Buen para visualizar patrones de boids

2. **Todo visible:**
   - No hay oclusión de peces
   - Fácil contar elementos

3. **Simplicidad igual a vista lateral:**
   - Mismo nivel de complejidad matemática

#### **❌ Desventajas:**
1. **Antinatural para acuario:**
   - Los acuarios se observan de lado, no desde arriba
   - Menos inmersivo

2. **Pierde verticalidad:**
   - No se aprecia la profundidad del agua
   - Burbujas subiendo no tienen sentido visual

3. **Menos atractivo visualmente:**
   - Parece más un diagrama que una simulación

#### **🎯 Uso Recomendado:**
Solo si el proyecto fuera una "vista de tanque de peces científico" o "simulador de biología marina". **No recomendado para este proyecto**.

---

### **1.3 Vista 2.5D (Falsa 3D con Parallax)** 🎭

```
Capas con profundidad simulada:
┌─────────────────────────────┐
│ [Capa Frente]  🐟  (grande)  │
│ [Capa Media]     🐟  (normal)│
│ [Capa Fondo]   🐟    (chico) │
│ 🌿              🌿       🌿  │ ← Parallax en plantas
└─────────────────────────────┘
```

#### **Características:**
- 3-4 capas de profundidad discretas
- Peces en capa frontal se ven más grandes
- Parallax scrolling al mover cámara
- Ejemplos: *Hollow Knight*, *Rayman*

#### **✅ Ventajas:**
1. **Sensación de profundidad:**
   - Más inmersivo que 2D puro
   - Efecto visual atractivo con poco esfuerzo

2. **Híbrido 2D/3D:**
   - Matemáticas 2D
   - Apariencia casi 3D

3. **Performance:**
   - Casi tan eficiente como 2D puro

#### **❌ Desventajas:**
1. **Movimiento limitado:**
   - Peces "saltan" entre capas (no fluido)
   - Sigue siendo fundamentalmente 2D

2. **No usa técnicas 3D del curso:**
   - Parallax no está en el temario
   - Sigue sin proyecciones 3D

#### **🎯 Uso Recomendado:**
Interesante, pero **no cubre suficientes técnicas del curso**. Mejor ir full 2D o full 3D.

---

## 🔶 OPCIÓN 2: ACUARIO 3D

### **2.1 Vista Orbital Libre (Arcball Camera)** 🌍 ⭐ **RECOMENDADO**

```
Vista 3D con cámara libre:

    ╱────────────╲
   ╱  🐟     🐟   ╲     Usuario puede:
  │   🌿  🐟  🌿   │    - Rotar (mouse drag)
  │  🐟   🪨   🐟  │    - Zoom (scroll)
  │   🌿     🌿    │    - Pan (right drag)
   ╲              ╱
    ╲────────────╱
```

#### **Características:**
- Cámara orbita alrededor del acuario (arcball)
- Usuario controla punto de vista libremente
- Acuario en el centro (origen)
- Paredes semi-transparentes para ver interior

#### **✅ Ventajas:**

1. **Máxima cobertura de técnicas del curso:**
   - ✅ Proyección perspectiva/ortogonal
   - ✅ Matrices de transformación (model-view-projection)
   - ✅ Grafos de escena
   - ✅ Cámara 3D (arcball - hay ejemplo en el curso!)
   - ✅ Iluminación 3D (Phong, normales)
   - ✅ Depth buffer y Z-fighting
   - ✅ Transparencias (alpha blending)
   - ✅ Culling (frustum, backface)

2. **Impacto visual máximo:**
   - Muy impresionante en demos
   - Perspectiva crea sensación de realismo
   - Puedes mostrar desde cualquier ángulo

3. **Interactividad natural:**
   - Explorar el acuario es intuitivo
   - Control de cámara ya implementado (`arcball_example.py`)

4. **Boids en 3D es más natural:**
   - Peces nadan en todas direcciones (XYZ)
   - Comportamiento más realista
   - Más cercano a la realidad

5. **Escalabilidad:**
   - Fácil agregar más features 3D
   - Base sólida para futuro portfolio

6. **Alineado con el curso:**
   - CC3501 es "Computación Gráfica 3D"
   - Demuestra dominio del contenido

#### **❌ Desventajas:**

1. **Complejidad mayor:**
   - Matrices 4x4 (MVP: Model-View-Projection)
   - Coordenadas homogéneas
   - Transformaciones compuestas

2. **Debugging más difícil:**
   - Peces pueden estar "detrás" de la cámara
   - Problemas de Z-fighting
   - Normales incorrectas difíciles de detectar

3. **Performance:**
   - Más cálculos por frame
   - Depth sorting, alpha blending costoso

4. **Curva de aprendizaje:**
   - Requiere entender pipeline 3D
   - Más tiempo inicial de setup

#### **⚙️ Implementación:**

```python
class AquariumScene3D:
    def __init__(self):
        # Usar arcball del curso
        self.camera = ArcballCamera()
        self.camera.position = [0, 0, 5]  # 5 unidades alejado
        self.camera.target = [0, 0, 0]     # Mirando al centro
        
        # Proyección perspectiva
        self.projection = perspective(
            fov=45,                   # Campo de visión
            aspect=width/height,
            near=0.1,                 # Plano cercano
            far=100                   # Plano lejano
        )
    
    def render(self):
        # Pipeline 3D completo
        view = self.camera.get_view_matrix()
        
        for fish in self.fishes:
            # MVP transform
            model = fish.get_model_matrix()  # Posición + rotación del pez
            mvp = self.projection @ view @ model
            
            shader.set_uniform("u_mvp", mvp)
            fish.draw()

# Boids 3D
class Fish3D:
    def __init__(self):
        self.position = np.array([x, y, z])      # 3D!
        self.velocity = np.array([vx, vy, vz])
        self.forward = np.array([0, 0, 1])       # Dirección que mira
    
    def update_orientation(self):
        # Pez mira hacia donde se mueve
        if np.linalg.norm(self.velocity) > 0.01:
            self.forward = normalize(self.velocity)
        
        # Calcular matriz de rotación para alinear el modelo
        # (esto es complejo pero importante para realismo)
        self.rotation = look_at_rotation(self.forward)
```

#### **📈 Complejidad:**
- Matemáticas: ⭐⭐⭐⭐ (Álgebra lineal, transformaciones)
- OpenGL: ⭐⭐⭐⭐ (Pipeline completo)
- Algoritmos: ⭐⭐⭐ (Boids 3D)

#### **Tiempo Estimado:** 3.5-4 semanas

#### **🎓 Técnicas del Curso Cubiertas:**
```
✅ Transformaciones (tema 8)
✅ Proyecciones (tema 9)
✅ Cámara arcball (ejemplos)
✅ Iluminación Phong (tema 13)
✅ Grafos de escena (tema 8)
✅ Texturas 3D (tema 11)
✅ Boids 3D (tema 16 - boids)
✅ Partículas 3D (tema 15)
✅ Deformación de mallas (tema 17)
```

---

### **2.2 Vista Fija Frontal (Cámara Estática de Frente)** 📸

```
Cámara fija mirando el acuario:

   Usuario ve siempre desde aquí
          ↓
        👁️
        │
    ┌───┴───┐
    │ 🐟 🐟 │  ← Acuario
    │🌿  🌿 │
    └───────┘
```

#### **Características:**
- Cámara NO se mueve
- Siempre miras el acuario de frente
- Similar a un acuario real en tu casa
- Renderizado 3D pero vista fija

#### **✅ Ventajas:**

1. **Simplicidad visual:**
   - No hay que controlar cámara
   - Composición fija (más fácil hacer bonita)

2. **Performance mejor:**
   - View matrix constante (se calcula una vez)
   - Frustum culling más simple

3. **Usa técnicas 3D:**
   - Sigue siendo 3D completo
   - Proyección, iluminación, etc.

4. **Realistic:**
   - Así se ven acuarios en vida real

#### **❌ Desventajas:**

1. **Menos interactividad:**
   - No puedes explorar
   - Menos engagement del usuario

2. **Oclusión de peces:**
   - Peces atrás quedan ocultos
   - No ves todo el ecosistema

3. **No usa arcball:**
   - Pierdes una técnica del curso
   - Menos "wow factor"

4. **Limitación de presentación:**
   - Solo puedes mostrar un ángulo
   - Menos flexible para demo

#### **⚙️ Implementación:**

```python
class FixedCameraAquarium:
    def __init__(self):
        # Cámara fija
        self.camera_pos = np.array([0, 0, 5])  # Siempre aquí
        self.camera_target = np.array([0, 0, 0])
        self.camera_up = np.array([0, 1, 0])
        
        # View matrix se calcula UNA VEZ
        self.view = look_at(self.camera_pos, 
                           self.camera_target, 
                           self.camera_up)
        
        # Projection también constante
        self.projection = perspective(45, aspect, 0.1, 100)
    
    def update(self, dt):
        # View y projection NO cambian
        # Solo se actualizan los peces
        for fish in self.fishes:
            fish.update(dt)
    
    def render(self):
        # View y projection siempre iguales
        for fish in self.fishes:
            model = fish.get_model_matrix()
            mvp = self.projection @ self.view @ model
            shader.set_uniform("u_mvp", mvp)
            fish.draw()
```

#### **📈 Complejidad:**
- Matemáticas: ⭐⭐⭐ (Transformaciones 3D, sin arcball)
- OpenGL: ⭐⭐⭐⭐ (Pipeline 3D completo)
- Algoritmos: ⭐⭐⭐ (Boids 3D)

#### **Tiempo Estimado:** 3 semanas

#### **🎯 Uso Recomendado:**
Buena opción si el arcball te parece muy complejo, pero **pierdes interactividad**. Vista orbital es mejor.

---

### **2.3 Vista Primera Persona (Inside the Tank)** 🤿

```
Cámara dentro del agua:

   ╱────────────────╲
  ╱  🐟→   ← 🐟     ╲
 │    👁️              │  ← Tú estás aquí
 │  🐟  ↑   🌿   🐟   │
  ╲   🌿      🌿    ╱
   ╲────────────────╱
```

#### **Características:**
- Cámara dentro del acuario
- Controles FPS (WASD + mouse)
- Peces nadan a tu alrededor
- Perspectiva submarina

#### **✅ Ventajas:**

1. **Inmersión máxima:**
   - Experiencia única
   - Te sientes "dentro"
   
2. **Wow factor:**
   - Muy impresionante en demo
   - Original

3. **Shaders interesantes:**
   - Efecto underwater (niebla, cáusticas)
   - Post-processing relevante

#### **❌ Desventajas:**

1. **Contexto confuso:**
   - ¿Por qué estás dentro del acuario?
   - Menos coherente narrativamente

2. **No ves el ecosistema completo:**
   - Solo ves peces cercanos
   - Pierdes vista general

3. **Controles FPS complejos:**
   - No hay ejemplo en el curso
   - Tienes que implementar desde cero

4. **Mareo potencial:**
   - Movimiento rápido en espacios cerrados

#### **🎯 Uso Recomendado:**
Interesante pero **muy complejo y desviado del concepto**. No recomendado.

---

### **2.4 Vista Cenital 3D (Top-Down con Profundidad)** 🛰️

```
Cámara desde arriba en 3D:

      👁️ (cámara arriba)
       ↓
    ╭─────╮
    │🐟🐟🐟│  ← Ves peces desde arriba
    │🌿 🌿│    pero con profundidad Z
    ╰─────╯
```

#### **Características:**
- Cámara arriba del acuario mirando hacia abajo
- Sigue siendo 3D (peces tienen coordenada Z)
- Pero vista es top-down
- Puede incluir zoom y pan

#### **✅ Ventajas:**

1. **Visualización clara de boids:**
   - Ves patrones emergentes fácilmente
   - Bueno para análisis científico

2. **No hay oclusión:**
   - Todos los peces visibles

3. **Usa 3D:**
   - Proyección, iluminación, etc.

#### **❌ Desventajas:**

1. **Antinatural para acuario:**
   - Acuarios no se ven desde arriba

2. **Pierde verticalidad:**
   - No aprecias la profundidad del agua

3. **Menos atractivo:**
   - Vista más "técnica" que bonita

#### **🎯 Uso Recomendado:**
Solo si el proyecto fuera una "simulación científica de boids". **No recomendado**.

---

### **2.5 Vista Isométrica (Falsa Ortogonal)** 📐

```
Vista isométrica clásica:
        
      ╱│╲
     ╱ │ ╲
    ╱──┼──╲
   │ 🐟│🐟 │
   │ 🌿│🌿 │
   ╲───┼───╱
    ╲  │  ╱
     ╲ │ ╱
```

#### **Características:**
- Proyección ortogonal (no hay perspectiva)
- Vista diagonal (45° típicamente)
- Estilo RTS/gestión (SimCity, Age of Empires)

#### **✅ Ventajas:**

1. **Estética clara:**
   - Paralelas se mantienen paralelas
   - Bueno para mediciones

2. **Sin distorsión perspectiva:**
   - Peces del fondo igual tamaño que del frente

3. **Usa proyección ortogonal:**
   - Técnica del curso (alternativa a perspectiva)

#### **❌ Desventajas:**

1. **Menos realista:**
   - No es como vemos el mundo
   - Antinatural

2. **Limitaciones visuales:**
   - No hay sensación de profundidad
   - Menos inmersivo

3. **No aprovecha perspectiva:**
   - Proyección perspectiva es más interesante técnicamente

#### **🎯 Uso Recomendado:**
Interesante académicamente pero **menos impresionante visualmente**. No recomendado.

---

## 📊 COMPARATIVA EXHAUSTIVA: TODAS LAS OPCIONES

| Opción | Complejidad | Impacto Visual | Técnicas Curso | Tiempo | Interactividad | Realismo | Portfolio |
|--------|-------------|----------------|----------------|---------|----------------|----------|-----------|
| **2D Lateral** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 2 sem | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **2D Top-Down** | ⭐⭐ | ⭐⭐ | ⭐⭐ | 2 sem | ⭐⭐ | ⭐ | ⭐⭐ |
| **2.5D Parallax** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | 2.5 sem | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **3D Orbital** ✨ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 3.5 sem | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **3D Fija Frontal** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 3 sem | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **3D Primera Persona** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 4+ sem | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **3D Top-Down** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | 3 sem | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **3D Isométrica** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | 3 sem | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

---

## 🏆 RANKING FINAL

### **1. 3D Vista Orbital (Arcball)** 🥇
**Puntaje Total: 95/100**

**Por qué gana:**
- ✅ Máxima cobertura de técnicas (100%)
- ✅ Impresionante visualmente (100%)
- ✅ Hay ejemplo base en el curso (`arcball_example.py`)
- ✅ Interactividad natural
- ✅ Mejor para portfolio
- ⚠️ Complejidad manejable (no excesiva)

**Ideal para:** Demostrar dominio completo de gráficos 3D

---

### **2. 3D Vista Fija Frontal** 🥈
**Puntaje Total: 80/100**

**Por qué segundo:**
- ✅ Sigue usando técnicas 3D importantes
- ✅ Más simple que orbital (menos debugging)
- ✅ Vista natural de acuario
- ⚠️ Menos interactividad
- ⚠️ No usa arcball

**Ideal para:** Si te preocupa la complejidad pero quieres 3D

---

### **3. 2D Vista Lateral** 🥉
**Puntaje Total: 60/100**

**Por qué tercero:**
- ✅ Desarrollo muy rápido
- ✅ Permite enfocarte en boids y partículas
- ✅ Excelente performance
- ❌ Cubre pocas técnicas del curso
- ❌ Menos impresionante

**Ideal para:** Si tienes muy poco tiempo o problemas técnicos

---

## 🎯 MI RECOMENDACIÓN DETALLADA

### **Opción Recomendada: 3D Vista Orbital (Arcball)** ✨

#### **Justificación:**

1. **Alineación con el curso:**
   - CC3501 es un curso de computación gráfica **3D**
   - El temario completo está orientado a 3D
   - Ejemplo `arcball_example.py` ya existe

2. **Relación esfuerzo/beneficio:**
   - Sí, es más complejo que 2D
   - Pero la curva de aprendizaje es manejable
   - El curso te preparó para esto

3. **Diferenciación:**
   - Muchos harán proyectos simples 2D
   - 3D orbital te destacará positivamente

4. **Futuro:**
   - Skill transferible a otros proyectos
   - Impresionante en portfolio
   - Base sólida si quieres expandir después

#### **Plan de Mitigación de Riesgos:**

**Riesgo 1: "Arcball es muy complejo"**
- **Solución:** El curso ya tiene `arcball_example.py`
- **Acción:** Estudiar ese ejemplo primero (2-3 horas)
- **Backup:** Puedes copiar la clase casi directamente

**Riesgo 2: "Matrices 3D me confunden"**
- **Solución:** Usar librería del curso (`grafica`)
- **Acción:** `tr.matmul()` y funciones ya implementadas
- **Backup:** No necesitas implementar matemáticas desde cero

**Riesgo 3: "Debugging 3D es difícil"**
- **Solución:** Modo debug visual
```python
if DEBUG:
    draw_axis_at_origin()         # Ver ejes XYZ
    draw_bounding_boxes()          # Ver límites
    draw_camera_frustum()          # Ver qué ve la cámara
    draw_fish_forward_vectors()   # Ver direcciones
```

**Riesgo 4: "No me da el tiempo"**
- **Solución:** MVP en 2D primero, migrar a 3D
- **Semana 1:** Boids 2D funcionando
- **Semana 2:** Convertir a 3D (sorprendentemente fácil)
```python
# De 2D a 3D es añadir una dimensión
position_2d = np.array([x, y])       # Antes
position_3d = np.array([x, y, 0])    # Después (Z=0 inicialmente)
```

---

## 📋 PLAN HÍBRIDO (Mejor de Ambos Mundos)

### **Estrategia: Empezar 2D, Migrar a 3D** 🔄

```
SEMANA 1: Fundación 2D (MVP rápido)
├─ Boids 2D funcional
├─ Partículas 2D
├─ Renderizado ortogonal simple
└─ ✅ Checkpoint: Tienes algo funcionando

SEMANA 2: Transición a 3D
├─ Añadir coordenada Z a posiciones
├─ Implementar cámara arcball
├─ Añadir proyección perspectiva
├─ Adaptar boids a 3D (añadir reglas Z)
└─ ✅ Checkpoint: Ahora es 3D

SEMANA 3-4: Pulir 3D
├─ Iluminación Phong
├─ Texturas
├─ Plantas 3D con deformación
└─ Features extras
```

**Ventajas de este approach:**
1. ✅ Tienes MVP rápido (respaldo)
2. ✅ Migración 2D→3D es más fácil que empezar en 3D
3. ✅ Si fallas en 3D, tu 2D ya funciona
4. ✅ Aprendes ambos paradigmas

**Código de migración:**
```python
# ANTES (2D):
class Fish2D:
    def __init__(self):
        self.pos = np.array([random(), random()])  # XY
        self.vel = np.array([random(), random()])

# DESPUÉS (3D) - cambios mínimos:
class Fish3D:
    def __init__(self):
        self.pos = np.array([random(), random(), random()])  # XYZ
        self.vel = np.array([random(), random(), random()])
    
    # Las funciones de boids son IDÉNTICAS (trabajan con vectores)
    # separación, cohesión, alineación NO cambian!
```

---

## 🛠️ IMPLEMENTACIÓN RECOMENDADA PASO A PASO

### **FASE 1: Setup 3D Base (Días 1-3)**

```python
# main.py - Estructura inicial
import grafica.transformations as tr
from arcball import ArcballCamera  # Del ejemplo del curso

class AquariumApp:
    def __init__(self):
        # Window setup
        self.width = 1280
        self.height = 720
        
        # Cámara arcball (copiar de arcball_example.py)
        self.camera = ArcballCamera()
        self.camera.distance = 5.0  # 5 unidades alejado
        
        # Proyección perspectiva
        self.projection = tr.perspective(
            45,                          # FOV
            self.width/self.height,      # Aspect
            0.1,                         # Near
            100                          # Far
        )
        
        # Sistemas
        self.fish_system = FishSystem(num_fish=30)
        self.aquarium = AquariumTank()
    
    def on_mouse_drag(self, x, y, dx, dy, buttons):
        # Arcball maneja esto
        self.camera.on_mouse_drag(dx, dy, buttons)
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        # Zoom
        self.camera.distance -= scroll_y * 0.1
    
    def update(self, dt):
        self.fish_system.update(dt)
    
    def draw(self):
        # Clear
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        
        # Get view matrix from camera
        view = self.camera.get_view_matrix()
        
        # Draw aquarium
        self.aquarium.draw(self.projection, view)
        
        # Draw fish
        self.fish_system.draw(self.projection, view)
```

**Checkpoint Día 3:** Ves un cubo (acuario) que puedes rotar con el mouse ✅

---

### **FASE 2: Boids 3D (Días 4-7)**

```python
class Fish:
    def __init__(self):
        # Posición 3D aleatoria dentro del tanque
        self.position = np.random.uniform(-2, 2, size=3)
        self.velocity = np.random.uniform(-0.5, 0.5, size=3)
        self.max_speed = 2.0
        self.perception_radius = 1.5
    
    def update_boids(self, neighbors, tank_bounds):
        # Acumulador de fuerzas
        acceleration = np.zeros(3)
        
        # Regla 1: Separación
        if len(neighbors) > 0:
            separation = self.separate(neighbors)
            cohesion = self.cohere(neighbors)
            alignment = self.align(neighbors)
            
            acceleration += separation * 1.5
            acceleration += cohesion * 1.0
            acceleration += alignment * 1.0
        
        # Regla 5: Mantener dentro del tanque
        boundary = self.avoid_boundaries(tank_bounds)
        acceleration += boundary * 2.0
        
        # Aplicar aceleración
        self.velocity += acceleration * dt
        
        # Limitar velocidad
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed
        
        # Actualizar posición
        self.position += self.velocity * dt
    
    def separate(self, neighbors):
        """Evitar apiñamiento"""
        steering = np.zeros(3)
        for other in neighbors:
            diff = self.position - other.position
            dist = np.linalg.norm(diff)
            if 0 < dist < 0.5:  # Distancia mínima
                steering += diff / (dist ** 2)  # Inversamente prop.
        return steering
    
    def cohere(self, neighbors):
        """Moverse al centro del grupo"""
        if len(neighbors) == 0:
            return np.zeros(3)
        center = np.mean([n.position for n in neighbors], axis=0)
        return (center - self.position) * 0.01
    
    def align(self, neighbors):
        """Igualar velocidad con vecinos"""
        if len(neighbors) == 0:
            return np.zeros(3)
        avg_vel = np.mean([n.velocity for n in neighbors], axis=0)
        return (avg_vel - self.velocity) * 0.1
    
    def avoid_boundaries(self, bounds):
        """Rebotar en paredes del tanque"""
        steering = np.zeros(3)
        margin = 0.3
        
        # Límites: bounds = {min: [-2,-2,-2], max: [2,2,2]}
        for i in range(3):
            if self.position[i] < bounds['min'][i] + margin:
                steering[i] = 1.0
            elif self.position[i] > bounds['max'][i] - margin:
                steering[i] = -1.0
        
        return steering * 0.5
    
    def get_model_matrix(self):
        """Matriz de transformación para renderizar"""
        # Trasladar a la posición
        translate = tr.translate(self.position[0], 
                                self.position[1], 
                                self.position[2])
        
        # Rotar para que mire hacia su velocidad
        # (esto es complejo, puedes simplificarlo inicialmente)
        rotation = self.get_rotation_to_face_velocity()
        
        # Escalar el modelo
        scale = tr.uniformScale(0.1)  # Pez de 0.1 unidades
        
        return tr.matmul([translate, rotation, scale])
    
    def get_rotation_to_face_velocity(self):
        """Orientar pez hacia su dirección de movimiento"""
        if np.linalg.norm(self.velocity) < 0.01:
            return tr.identity()
        
        forward = self.velocity / np.linalg.norm(self.velocity)
        
        # Calcular ángulo en XZ (horizontal)
        angle_xz = np.arctan2(forward[0], forward[2])
        
        # Calcular ángulo vertical
        angle_y = np.arcsin(forward[1])
        
        # Combinar rotaciones
        rot_y = tr.rotationY(angle_xz)
        rot_x = tr.rotationX(-angle_y)
        
        return tr.matmul([rot_y, rot_x])
```

**Checkpoint Día 7:** Peces nadando en 3D con comportamiento boids ✅

---

### **FASE 3: Elementos del Ecosistema (Días 8-14)**

```python
# Partículas (burbujas)
class BubbleSystem:
    def __init__(self):
        self.bubbles = []
        self.spawn_rate = 5  # burbujas por segundo
        self.spawn_timer = 0
    
    def update(self, dt):
        # Spawning
        self.spawn_timer += dt
        if self.spawn_timer > 1.0 / self.spawn_rate:
            self.spawn_bubble()
            self.spawn_timer = 0
        
        # Update existing
        for bubble in self.bubbles[:]:
            bubble.update(dt)
            if bubble.position[1] > 3.0:  # Superficie
                self.bubbles.remove(bubble)
    
    def spawn_bubble(self):
        # Burbuja nace en el fondo, posición aleatoria XZ
        pos = np.array([
            np.random.uniform(-1.5, 1.5),  # X
            -2.0,                           # Y (fondo)
            np.random.uniform(-1.5, 1.5)   # Z
        ])
        self.bubbles.append(Bubble(pos))

class Bubble:
    def __init__(self, position):
        self.position = position
        self.velocity = np.array([0, 0.5, 0])  # Sube
        self.age = 0
        self.size = np.random.uniform(0.02, 0.05)
    
    def update(self, dt):
        self.age += dt
        
        # Movimiento serpenteante
        wobble_x = np.sin(self.age * 2) * 0.05
        wobble_z = np.cos(self.age * 1.5) * 0.05
        
        self.position += self.velocity * dt
        self.position[0] += wobble_x
        self.position[2] += wobble_z

# Plantas
class Plant:
    def __init__(self, position):
        self.base_position = position
        self.vertices = self.create_plant_geometry()
        self.time = np.random.uniform(0, 6.28)  # Offset random
    
    def create_plant_geometry(self):
        # Cilindro simple (8 segmentos verticales)
        vertices = []
        height = 0.8
        radius = 0.05
        segments = 8
        
        for i in range(segments + 1):
            y = (i / segments) * height
            # Círculo en cada nivel
            for angle in np.linspace(0, 2*np.pi, 16):
                x = radius * np.cos(angle)
                z = radius * np.sin(angle)
                vertices.append([x, y, z])
        
        return np.array(vertices)
    
    def update(self, dt):
        self.time += dt
    
    def get_deformed_vertices(self):
        """Deformación sinusoidal (viento/corriente)"""
        deformed = self.vertices.copy()
        
        for i, vertex in enumerate(deformed):
            # Más deformación arriba (proporcional a Y)
            height_factor = vertex[1] / 0.8
            
            # Offset sinusoidal
            offset_x = np.sin(self.time + vertex[2]) * height_factor * 0.1
            offset_z = np.cos(self.time * 0.7 + vertex[0]) * height_factor * 0.1
            
            deformed[i][0] += offset_x
            deformed[i][2] += offset_z
        
        return deformed
```

**Checkpoint Día 14:** Burbujas subiendo, plantas ondeando ✅

---

## ⚡ OPTIMIZACIONES (Si FPS < 30)

### **1. Quadtree para Búsqueda de Vecinos**

```python
class Quadtree:
    """Spatial partitioning para búsqueda eficiente de vecinos"""
    def __init__(self, bounds, capacity=4):
        self.bounds = bounds  # {min: [x,y,z], max: [x,y,z]}
        self.capacity = capacity
        self.points = []
        self.divided = False
        self.children = []
    
    def insert(self, fish):
        if not self.contains(fish.position):
            return False
        
        if len(self.points) < self.capacity:
            self.points.append(fish)
            return True
        
        if not self.divided:
            self.subdivide()
        
        for child in self.children:
            if child.insert(fish):
                return True
        
        return False
    
    def query_radius(self, position, radius):
        """Encuentra todos los peces dentro del radio"""
        found = []
        
        # Check si el radio intersecta este nodo
        if not self.intersects_sphere(position, radius):
            return found
        
        # Check puntos en este nodo
        for fish in self.points:
            if np.linalg.norm(fish.position - position) <= radius:
                found.append(fish)
        
        # Recursivo en hijos
        if self.divided:
            for child in self.children:
                found.extend(child.query_radius(position, radius))
        
        return found

# Uso en el sistema de peces
class FishSystem:
    def update(self, dt):
        # Reconstruir quadtree cada frame
        self.quadtree = Quadtree(self.tank_bounds)
        for fish in self.fishes:
            self.quadtree.insert(fish)
        
        # Actualizar cada pez
        for fish in self.fishes:
            # Búsqueda eficiente de vecinos
            neighbors = self.quadtree.query_radius(
                fish.position, 
                fish.perception_radius
            )
            fish.update_boids(neighbors, self.tank_bounds)
```

**Ganancia:** O(N²) → O(N log N)

---

### **2. Frustum Culling**

```python
def draw(self):
    view = self.camera.get_view_matrix()
    frustum = Frustum(self.projection, view)
    
    for fish in self.fishes:
        # Solo dibujar si está en el frustum
        if frustum.contains_point(fish.position):
            fish.draw(self.projection, view)
```

---

## 📝 RESUMEN FINAL

### **Configuración Recomendada:**

```yaml
Dimensionalidad: 3D
Vista: Orbital (Arcball Camera)
Interactividad: Mouse drag (rotar), scroll (zoom)
Proyección: Perspectiva (FOV 45°)
Tank Bounds: [-2, 2] en cada eje
Número de Peces: 30-50 inicialmente
Optimización: Quadtree si FPS < 30

Técnicas Cubiertas:
  - Transformaciones 3D (model-view-projection)
  - Proyección perspectiva
  - Cámara arcball
  - Boids 3D
  - Sistemas de partículas 3D
  - Deformación de mallas
  - Iluminación Phong
  - Texturas
  - Alpha blending (paredes del tanque)
  - Depth testing
```

---

## 🎬 CONCLUSIÓN

**Haz 3D con vista orbital.** Es la opción que:
- ✅ Maximiza aprendizaje del curso
- ✅ Mejor impresión en evaluación
- ✅ Complejidad manejable con ejemplos del curso
- ✅ Resultado más impresionante
- ✅ Mejor para portfolio futuro

**Si tienes dudas:** Empieza 2D simple, migra a 3D en semana 2. El código de boids es casi idéntico.

**¡Buena suerte! 🐠✨**
