# 🧪 Guía Práctica: Testear Ejemplos del Curso para el Acuario 3D
## Herramientas que usarás directamente en tu proyecto

---

## 📦 PASO 1: Obtener el Repositorio del Curso

### Comandos para ejecutar:

```powershell
# Ir a tu carpeta de proyecto
cd "C:\Users\56942\Desktop\proyecto grafica"

# Clonar el repositorio del curso
git clone https://github.com/PLUMAS-research/cc3501-computer-graphics.git curso-cc3501

# Entrar a la carpeta
cd curso-cc3501

# Crear y activar el entorno conda
conda env create -n grafica -f environment.yml
conda activate grafica
```

---

## 🎯 EJEMPLOS CLAVE PARA TU PROYECTO

### **Orden Recomendado de Testeo:**

```
1. hello_world          → Verificar que todo funciona
2. arcball_example      → ⭐ TU CÁMARA BASE
3. boids_abm            → ⭐ TU SISTEMA DE PECES
4. particles            → ⭐ TUS BURBUJAS
5. solar_system         → Grafos de escena
6. compositions         → Transformaciones
7. transformed_bunny    → Modelos 3D
8. image_texture        → Texturas
```

---

## 🔧 EJEMPLOS A TESTEAR

### **1. HELLO_WORLD - Verificación básica** ✅

**Propósito:** Confirmar que OpenGL funciona

**Comando:**
```powershell
python caja_de_juguetes.py hello_world
```

**Qué esperar:**
- Ventana que abre
- Posiblemente un triángulo simple
- Si esto funciona, todo lo demás funcionará

**Qué aprender:**
- Estructura básica de una aplicación OpenGL
- Loop principal
- Event handling

**Código relevante a revisar:**
```python
# Busca en: examples/hello_world.py
# Observa:
- Cómo se inicializa pyglet/OpenGL
- El main loop
- La estructura básica
```

**⏱️ Tiempo:** 2 minutos

---

### **2. ARCBALL_EXAMPLE - ⭐ TU CÁMARA** 🎥

**Propósito:** Esta será TU sistema de cámara exactamente

**Comando:**
```powershell
python caja_de_juguetes.py arcball_example
```

**Qué esperar:**
- Modelo 3D (probablemente un conejo o cubo)
- Puedes **rotar con el mouse** arrastrando
- Puedes **hacer zoom** con la rueda del mouse
- Puedes **panear** (opcional, con clic derecho)

**ACCIONES A PROBAR:**

1. **Rotar:**
   - Click izquierdo + arrastrar
   - Observa cómo el modelo gira suavemente
   - ⚡ **Inspiración:** Así rotarás tu acuario

2. **Zoom:**
   - Rueda del mouse arriba/abajo
   - Acércate y aléjate del modelo
   - ⚡ **Inspiración:** Ver peces de cerca o vista completa

3. **Resetear vista:**
   - Busca si hay tecla para resetear (R, Home, etc.)
   - Útil para demos

**Qué aprender:**
```python
# Busca en: examples/arcball_example.py
# O en: grafica/arcball.py (si existe)

# OBSERVA:
1. Cómo se maneja on_mouse_drag()
2. Cómo se calcula la view matrix
3. Los parámetros de sensibilidad
4. Cómo se combina con projection matrix
```

**CÓDIGO CLAVE A COPIAR:**
```python
# Esto es lo que copiarás casi textual:

class ArcballCamera:
    def __init__(self):
        self.distance = 5.0      # Distancia al target
        self.target = [0, 0, 0]  # Centro del acuario
        self.rotation_x = 0      # Rotación horizontal
        self.rotation_y = 0      # Rotación vertical
    
    def on_mouse_drag(self, dx, dy, buttons):
        if buttons & pyglet.window.mouse.LEFT:
            self.rotation_x += dx * 0.5
            self.rotation_y += dy * 0.5
            # Limitar rotación vertical
            self.rotation_y = max(-89, min(89, self.rotation_y))
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.distance -= scroll_y * 0.1
        self.distance = max(1.0, min(20.0, self.distance))
    
    def get_view_matrix(self):
        # Esta es la magia - genera la matriz view
        # Probablemente usa tr.lookAt() internamente
        pass
```

**⏱️ Tiempo:** 10-15 minutos

**📸 SCREENSHOTS A TOMAR:**
- Vista frontal del modelo
- Vista lateral (después de rotar)
- Vista muy cercana (zoom in)
- Vista lejana (zoom out)

**💡 NOTAS PARA TU PROYECTO:**
```
✓ La clase ArcballCamera será copiada casi sin cambios
✓ Ajustar self.distance inicial (5.0 para acuario es perfecto)
✓ self.target será el centro de tu acuario [0, 0, 0]
✓ Considerar limitar rotación vertical (no voltear boca abajo)
```

---

### **3. BOIDS_ABM - ⭐ TU SISTEMA DE PECES** 🐟

**Propósito:** Algoritmo exacto que usarás para tus peces

**Comando:**
```powershell
python caja_de_juguetes.py boids_abm
```

**Qué esperar:**
- Agentes (pájaros/puntos) moviéndose en pantalla
- Comportamiento de cardumen/bandada
- Emergen patrones complejos de reglas simples

**ACCIONES A PROBAR:**

1. **Observar patrones:**
   - Mira cómo se agrupan
   - Observa cómo evitan chocar
   - Nota cómo se alinean sus direcciones

2. **Probar parámetros (si hay sliders/UI):**
   - Número de agentes
   - Radio de percepción
   - Pesos de las reglas

3. **Buscar edge cases:**
   - ¿Qué pasa en las esquinas?
   - ¿Se quedan atrapados?
   - ¿Se apelotonan demasiado?

**Qué aprender:**
```python
# Busca en: examples/boids_abm.py

# OBSERVA:
1. Las 3 reglas principales:
   - separation (separación)
   - cohesion (cohesión)
   - alignment (alineación)

2. Cómo se buscan vecinos:
   - ¿Usan búsqueda ingenua (O(N²))?
   - ¿Usan spatial partitioning?

3. Los pesos de cada regla:
   - ¿Cuáles valores funcionan mejor?

4. Límites de velocidad:
   - max_speed, max_force

5. Cómo manejan bordes:
   - ¿Rebotan?
   - ¿Wrapping (aparecen del otro lado)?
   - ¿Fuerza de "retorno"?
```

**CÓDIGO CLAVE A ESTUDIAR:**
```python
# Estructura típica del algoritmo boids:

class Boid:
    def __init__(self):
        self.position = random_position()
        self.velocity = random_velocity()
        self.acceleration = [0, 0, 0]
        
        # Parámetros del comportamiento
        self.max_speed = 2.0
        self.max_force = 0.03
        self.perception_radius = 1.5
    
    def update(self, boids):
        # Resetear aceleración
        self.acceleration = [0, 0, 0]
        
        # Encontrar vecinos
        neighbors = self.find_neighbors(boids)
        
        # Aplicar reglas
        sep = self.separate(neighbors)
        coh = self.cohere(neighbors)
        ali = self.align(neighbors)
        
        # Acumular fuerzas con pesos
        self.acceleration += sep * 1.5
        self.acceleration += coh * 1.0
        self.acceleration += ali * 1.0
        
        # Actualizar física
        self.velocity += self.acceleration
        self.limit_velocity(self.max_speed)
        self.position += self.velocity
    
    def separate(self, neighbors):
        """Evitar estar muy cerca"""
        steering = [0, 0, 0]
        for other in neighbors:
            distance = dist(self.position, other.position)
            if distance < desired_separation:
                diff = self.position - other.position
                diff = normalize(diff)
                diff = diff / distance  # Peso por distancia
                steering += diff
        return steering
    
    def cohere(self, neighbors):
        """Moverse hacia el centro del grupo"""
        if len(neighbors) == 0:
            return [0, 0, 0]
        
        center_of_mass = average([n.position for n in neighbors])
        return self.seek(center_of_mass)
    
    def align(self, neighbors):
        """Igualar velocidad con vecinos"""
        if len(neighbors) == 0:
            return [0, 0, 0]
        
        avg_velocity = average([n.velocity for n in neighbors])
        steering = avg_velocity - self.velocity
        return steering
```

**⏱️ Tiempo:** 15-20 minutos

**📊 EXPERIMENTOS A HACER:**

| Parámetro | Valor Base | Prueba Alta | Prueba Baja | Observación |
|-----------|-----------|-------------|-------------|-------------|
| Num Boids | 50 | 200 | 10 | ¿FPS? ¿Patrones? |
| Perception Radius | 1.5 | 3.0 | 0.5 | ¿Agrupación? |
| Separation Weight | 1.5 | 3.0 | 0.5 | ¿Colisiones? |
| Max Speed | 2.0 | 5.0 | 0.5 | ¿Caos? |

**💡 NOTAS PARA TU PROYECTO:**
```
✓ Este código será la base de tu Fish class
✓ Cambiar dimensionalidad si está en 2D (añadir Z)
✓ Añadir regla extra: avoid_boundaries() para el tanque
✓ Considerar: avoid_obstacles() para rocas/plantas
✓ Los pesos (1.5, 1.0, 1.0) son un buen punto de partida
```

---

### **4. PARTICLES - ⭐ TUS BURBUJAS** 💧

**Propósito:** Sistema base para las burbujas del acuario

**Comando:**
```powershell
python caja_de_juguetes.py particles
```

**Qué esperar:**
- Partículas generándose continuamente
- Movimiento con física simple
- Vida limitada (desaparecen después de un tiempo)

**ACCIONES A PROBAR:**

1. **Observar el ciclo de vida:**
   - ¿Dónde nacen?
   - ¿Cómo se mueven?
   - ¿Cuándo mueren?

2. **Notar la física:**
   - ¿Hay gravedad?
   - ¿Velocidad inicial aleatoria?
   - ¿Aceleración?

3. **Performance:**
   - ¿Cuántas partículas simultáneas?
   - ¿FPS se mantiene estable?

**Qué aprender:**
```python
# Busca en: examples/particles.py

# OBSERVA:
1. Estructura de la clase Particle
2. Sistema de spawning (emisor)
3. Pool de partículas vs crear/destruir
4. Renderizado eficiente (instancing?)
```

**CÓDIGO CLAVE A ADAPTAR:**
```python
class ParticleSystem:
    def __init__(self):
        self.particles = []
        self.spawn_rate = 10  # partículas por segundo
        self.spawn_timer = 0
    
    def emit(self, position):
        """Crear nueva partícula"""
        particle = Particle(
            position=position,
            velocity=random_direction() * random_speed(),
            lifetime=random(2.0, 5.0)
        )
        self.particles.append(particle)
    
    def update(self, dt):
        # Spawning continuo
        self.spawn_timer += dt
        if self.spawn_timer >= 1.0 / self.spawn_rate:
            self.emit(self.emitter_position)
            self.spawn_timer = 0
        
        # Actualizar existentes
        for particle in self.particles[:]:
            particle.update(dt)
            if particle.is_dead():
                self.particles.remove(particle)
    
class Particle:
    def __init__(self, position, velocity, lifetime):
        self.position = position
        self.velocity = velocity
        self.acceleration = [0, -9.8, 0]  # Gravedad
        self.lifetime = lifetime
        self.age = 0
    
    def update(self, dt):
        self.age += dt
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
    
    def is_dead(self):
        return self.age >= self.lifetime
```

**ADAPTACIÓN PARA BURBUJAS:**
```python
class BubbleParticle(Particle):
    def __init__(self, position):
        super().__init__(
            position=position,
            velocity=[0, 0.5, 0],  # Solo suben
            lifetime=float('inf')   # Mueren al llegar arriba
        )
        self.buoyancy = 0.5  # Fuerza de flotación
        self.wobble_freq = random(1.5, 2.5)
        self.wobble_phase = random(0, 2*pi)
    
    def update(self, dt):
        # Física de burbuja
        self.velocity[1] += self.buoyancy * dt  # Flotan
        
        # Movimiento serpenteante
        wobble = sin(self.age * self.wobble_freq + self.wobble_phase)
        self.position[0] += wobble * 0.01
        
        # Actualizar posición
        self.position += self.velocity * dt
        self.age += dt
    
    def is_dead(self):
        # Muere al llegar a la superficie
        return self.position[1] > WATER_SURFACE_Y
```

**⏱️ Tiempo:** 10 minutos

**💡 NOTAS PARA TU PROYECTO:**
```
✓ Spawn burbujas en el fondo del acuario (Y = -2)
✓ X, Z aleatorios dentro del tanque
✓ Velocidad solo en Y (suben)
✓ Wobble en X y Z para realismo
✓ Tamaño variado (0.02 - 0.05 unidades)
✓ Transparencia/alpha para efecto de agua
```

---

### **5. SOLAR_SYSTEM - Grafos de Escena** 🪐

**Propósito:** Estructura jerárquica para organizar tu escena

**Comando:**
```powershell
python caja_de_juguetes.py solar_system
```

**Qué esperar:**
- Sistema solar con planetas orbitando
- Lunas orbitando planetas
- Jerarquía de transformaciones

**Qué aprender:**
```python
# Busca en: examples/solar_system.py

# OBSERVA:
1. SceneGraph o estructura de nodos
2. Transformaciones padre-hijo
3. Cómo se acumulan las matrices

# CONCEPTO:
Acuario (root)
├── Tank (contenedor)
│   ├── Walls (paredes)
│   ├── Floor (sustrato)
│   └── Water (shader especial)
├── FishSystem
│   ├── Fish1
│   ├── Fish2
│   └── ...
├── PlantSystem
│   ├── Plant1
│   └── Plant2
└── ParticleSystem (burbujas)
```

**CÓDIGO RELEVANTE:**
```python
class SceneNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.transform = identity_matrix()
    
    def add_child(self, child):
        self.children.append(child)
    
    def draw(self, parent_transform, projection, view):
        # Acumular transformación
        current_transform = parent_transform @ self.transform
        
        # Dibujar este nodo
        self.render(projection, view, current_transform)
        
        # Dibujar hijos recursivamente
        for child in self.children:
            child.draw(current_transform, projection, view)
```

**⏱️ Tiempo:** 10 minutos

**💡 APLICACIÓN EN TU PROYECTO:**
```python
# Tu escena podría ser:
aquarium = SceneNode("Aquarium")
aquarium.transform = tr.translate(0, 0, 0)  # Centro

tank = SceneNode("Tank")
tank.transform = tr.scale(4, 4, 4)  # Tamaño del tanque
aquarium.add_child(tank)

# Peces no usan grafo (se mueven independientemente)
# Pero plantas sí:
plant1 = SceneNode("Plant1")
plant1.transform = tr.translate(-1, -2, 0.5)  # Posición fija
tank.add_child(plant1)
```

---

### **6. COMPOSITIONS - Transformaciones** 🔄

**Propósito:** Entender orden de transformaciones

**Comando:**
```powershell
python caja_de_juguetes.py compositions
```

**Qué esperar:**
- Objetos transformados de diferentes formas
- Demostración de translate, rotate, scale
- Importancia del orden de operaciones

**Qué aprender:**
```python
# ORDEN IMPORTA:
# Incorrecto:
translate → rotate → scale  # El objeto se mueve en arco

# Correcto (para modelos):
scale → rotate → translate  # El objeto rota en su lugar, luego se posiciona
```

**PARA TUS PECES:**
```python
def get_fish_model_matrix(fish):
    # Orden correcto: S-R-T (Scale-Rotate-Translate)
    
    # 1. Escalar al tamaño deseado
    S = tr.scale(0.1, 0.1, 0.1)
    
    # 2. Rotar para que mire hacia su velocidad
    R = fish.get_rotation_matrix()
    
    # 3. Trasladar a su posición en el mundo
    T = tr.translate(fish.position[0], fish.position[1], fish.position[2])
    
    # Combinar: T @ R @ S (se aplica de derecha a izquierda)
    return tr.matmul([T, R, S])
```

**⏱️ Tiempo:** 5 minutos

---

### **7. TRANSFORMED_BUNNY - Modelos 3D** 🐰

**Propósito:** Cargar y renderizar modelos OBJ

**Comando:**
```powershell
python caja_de_juguetes.py transformed_bunny
```

**Qué esperar:**
- Modelo 3D (conejo de Stanford)
- Transformaciones aplicadas
- Iluminación básica

**Qué aprender:**
```python
# Si decides usar modelos OBJ para peces:

# Busca en: grafica/assets_path.py o similar
# O en el código de transformed_bunny

# Cómo cargar:
import trimesh

mesh = trimesh.load('models/fish.obj')
vertices = mesh.vertices
indices = mesh.faces
```

**⏱️ Tiempo:** 5 minutos

**💡 PARA TU PROYECTO:**
```
Opción A (Simple): Geometría procedural
- Elipsoide para el cuerpo
- Triángulos para aletas
- Rápido, suficiente

Opción B (Bonito): Modelos OBJ
- Descargar de SketchFab (free)
- Requiere aprender a cargar con trimesh
- Más tiempo, mejor resultado
```

---

### **8. IMAGE_TEXTURE - Texturas** 🎨

**Propósito:** Aplicar texturas a modelos

**Comando:**
```powershell
python caja_de_juguetes.py image_texture assets/dice.jpg
```

**Qué esperar:**
- Imagen mapeada en un cuadrado/cubo
- Coordenadas UV funcionando

**Qué aprender:**
```python
# Busca en: examples/image_texture.py

# OBSERVA:
1. Cómo se cargan texturas (PIL/Pillow)
2. Coordenadas UV (tex_coords)
3. Binding en OpenGL
4. Shaders con texturas (sampler2D)
```

**TEXTURAS PARA TU PROYECTO:**
```
Peces:
- Escamas procedurales (shader)
- O textura de pez (SketchFab, OpenGameArt)

Tanque:
- Vidrio: textura semi-transparente
- Sustrato: textura de grava/arena
- Plantas: textura verde con alpha

Agua:
- Post-process shader (opcional)
- Caustics (muy opcional)
```

**⏱️ Tiempo:** 5 minutos

---

### **9. EJEMPLOS OPCIONALES** (Si tienes tiempo)

#### **CLOTH_VERLET - Simulación física avanzada**
```powershell
python caja_de_juguetes.py cloth_verlet
```
**Utilidad:** Si quieres plantas MUY realistas con física

#### **DINO_RUNNER - Colisiones 2D**
```powershell
python caja_de_juguetes.py dino_runner
```
**Utilidad:** Detección de colisiones (peces con obstáculos)

#### **COLOR_WHEEL - Espacios de color**
```powershell
python caja_de_juguetes.py color_wheel
```
**Utilidad:** Elegir colores armoniosos para peces

---

## 📝 CHECKLIST DE TESTEO

Completa esto mientras pruebas:

### Arcball Example
- [ ] Funciona al arrastrarlo
- [ ] Zoom funciona con scroll
- [ ] Entiendo dónde está la clase ArcballCamera
- [ ] Identifiqué los parámetros clave (distance, target)
- [ ] Tomé screenshots de diferentes ángulos

### Boids ABM
- [ ] Vi el comportamiento emergente
- [ ] Identifiqué las 3 reglas en el código
- [ ] Probé diferentes números de agentes
- [ ] Entiendo cómo buscan vecinos
- [ ] Vi cómo manejan los bordes

### Particles
- [ ] Vi el spawn continuo
- [ ] Entiendo el ciclo de vida
- [ ] Identifiqué el emisor
- [ ] Vi la física aplicada
- [ ] Pensé cómo adaptarlo a burbujas

### Solar System
- [ ] Vi la jerarquía de transformaciones
- [ ] Entiendo el concepto de grafo de escena
- [ ] Pensé cómo organizar mi acuario

### Compositions
- [ ] Entiendo el orden S-R-T
- [ ] Vi ejemplos de composición incorrecta
- [ ] Sé cómo aplicarlo a mis peces

---

## 💡 INSPIRACIÓN: Lo que verás

Después de testear estos ejemplos, tendrás:

✅ **Visualmente:**
- Cámara orbital suave y profesional
- Comportamiento de grupo emergente y natural
- Partículas con física creíble
- Estructuras 3D bien organizadas

✅ **Técnicamente:**
- Código base para copiar/adaptar
- Entendimiento de cómo integrarlos
- Confianza en que es factible

✅ **Creativamente:**
- Ideas de qué ajustar para tu proyecto
- Inspiración de efectos visuales
- Claridad de qué features priorizar

---

## 🎯 DESPUÉS DE TESTEAR

### Crea un documento personal:

```markdown
# Mis Notas de los Ejemplos

## Arcball
- Archivo: examples/arcball_example.py
- Líneas clave: [anotar números de línea]
- Parámetros a cambiar:
  - distance: 5.0 → perfecto para mi acuario
  - sensitivity: probar 0.5 y 1.0
- Código a copiar: [fragmento]

## Boids
- Archivo: examples/boids_abm.py
- Pesos que funcionaron mejor: sep=1.5, coh=1.0, ali=1.0
- Número óptimo de agentes: 30-50 (buen performance)
- Modificaciones necesarias:
  - Añadir dimensión Z
  - Añadir avoid_boundaries para tanque
- Código a copiar: [fragmento]

[etc...]
```

---

## 🚀 PRÓXIMO PASO

Una vez que hayas testeado los ejemplos:

1. **Crear carpeta de proyecto:**
```powershell
mkdir acuario_interactivo
cd acuario_interactivo
```

2. **Copiar archivos relevantes:**
```powershell
# Copiar arcball
copy ..\curso-cc3501\grafica\arcball.py .\

# Copiar estructura base
copy ..\curso-cc3501\examples\arcball_example.py .\main.py
```

3. **Empezar a adaptar:**
- Renombrar variables
- Añadir tus sistemas (Fish, Bubble, Plant)
- Integrar uno por uno

---

## ⏰ TIEMPO TOTAL ESTIMADO

- Setup inicial (clonar, instalar): **15 min**
- Testeo de 8 ejemplos: **60-90 min**
- Tomar notas y screenshots: **30 min**
- **TOTAL: 2-2.5 horas**

---

## 🎬 ¡EMPECEMOS!

**Siguiente comando a ejecutar:**

```powershell
cd "C:\Users\56942\Desktop\proyecto grafica"
git clone https://github.com/PLUMAS-research/cc3501-computer-graphics.git curso-cc3501
```

**¿Listo? ¡Vamos a probarlo! 🚀**
