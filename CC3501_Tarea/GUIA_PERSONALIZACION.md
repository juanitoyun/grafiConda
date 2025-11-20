# 🎨 Guía para Personalizar Tu Tarea

## 🔧 Cambios Rápidos que Puedes Hacer

### 1. Cambiar el RUT (OBLIGATORIO antes de entregar)

**Ubicación:** Nombre de la carpeta

```bash
# Renombrar la carpeta
move "60910000-1" "TU-RUT-AQUI"

# Recrear el ZIP
Compress-Archive -Path "TU-RUT-AQUI" -DestinationPath "TU-RUT-AQUI.zip" -Force
```

### 2. Modificar los Colores del Personaje

**Ubicación:** `main.py`, función `create_character()`

```python
# Ejemplo: Cambiar el color del torso
torso.color = [1.0, 0.0, 0.0]  # Rojo
torso.color = [0.0, 1.0, 0.0]  # Verde
torso.color = [1.0, 1.0, 0.0]  # Amarillo
torso.color = [0.5, 0.0, 0.5]  # Morado
```

**Partes modificables:**
- `torso.color`
- `head.color`
- `left_shoulder.color`, `right_shoulder.color`
- `left_upper_arm.color`, `right_upper_arm.color`
- `left_forearm.color`, `right_forearm.color`
- `left_hand.color`, `right_hand.color`
- `left_thigh.color`, `right_thigh.color`
- `left_shin.color`, `right_shin.color`
- `left_foot.color`, `right_foot.color`

### 3. Cambiar las Proporciones del Personaje

**Ubicación:** `main.py`, función `create_character()`

```python
# Hacer el torso más grande
torso.transform = tr.matmul([
    tr.scale(1.0, 1.5, 0.5)  # Ancho, Alto, Profundidad
])

# Hacer las piernas más largas
left_thigh.transform = tr.matmul([
    tr.translate(0, -0.6, 0),  # Más abajo
    tr.scale(0.2, 1.3, 0.2)    # Más largas
])
```

### 4. Modificar las Poses

**Ubicación:** `main.py`, función `get_poses()`

Cada rotación se define con ángulos en radianes:
- `np.pi` = 180°
- `np.pi/2` = 90°
- `np.pi/4` = 45°
- `np.pi/6` = 30°

```python
# Ejemplo: Hacer que el brazo apunte más arriba
'left_shoulder': tr.matmul([
    tr.translate(0, 0, 0),
    tr.rotationZ(np.pi/2),      # Levantar brazo 90°
    tr.rotationX(np.pi/4)       # Inclinar adelante 45°
]),
```

### 5. Cambiar las Posiciones de la Cámara

**Ubicación:** `main.py`, dentro de cada `Pose`

```python
camera_config={
    'eye': np.array([X, Y, Z], dtype=np.float32),   # Posición de la cámara
    'at': np.array([X, Y, Z], dtype=np.float32),    # Hacia dónde mira
    'up': np.array([0, 1, 0], dtype=np.float32)     # Vector arriba
}

# Ejemplos:
# Cámara cerca del frente:
'eye': np.array([0, 1, 3], dtype=np.float32),
'at': np.array([0, 1, 0], dtype=np.float32),

# Cámara desde arriba (vista de pájaro):
'eye': np.array([0, 5, 1], dtype=np.float32),
'at': np.array([0, 0, 0], dtype=np.float32),

# Cámara desde abajo (ángulo dramático):
'eye': np.array([3, -1, 3], dtype=np.float32),
'at': np.array([0, 1, 0], dtype=np.float32),
```

### 6. Agregar Más Articulaciones (Si quieres destacar)

**Ubicación:** `main.py`, función `create_character()`

```python
# Ejemplo: Agregar dedos a la mano izquierda
finger1 = left_hand.add_child(SceneGraphNode("left_finger1"))
finger1.mesh = cylinder
finger1.transform = tr.matmul([
    tr.translate(0.1, -0.3, 0),
    tr.scale(0.05, 0.3, 0.05)
])
finger1.color = [0.9, 0.7, 0.6]
```

### 7. Modificar la Iluminación

**Ubicación:** `main.py`, método `on_draw()`

```python
# Cambiar la posición de la luz
glUniform3f(
    glGetUniformLocation(program, "lightPos"),
    X, Y, Z  # Nueva posición
)

# Ejemplos:
# Luz desde la izquierda:
5.0, 3.0, -2.0

# Luz desde abajo (efecto dramático):
0.0, -5.0, 0.0

# Luz frontal:
0.0, 2.0, 10.0
```

**Ubicación:** `fragment_shader.glsl`

```glsl
// Cambiar la intensidad ambiente
float ambientStrength = 0.5;  // Más luz ambiente (0.0 a 1.0)

// Cambiar la intensidad especular
float specularStrength = 0.8;  // Más brillo (0.0 a 1.0)

// Cambiar el brillo del material
float spec = pow(max(dot(viewDir, reflectDir), 0.0), 64);  // Más brillante
```

### 8. Cambiar el Color de Fondo

**Ubicación:** `main.py`, método `__init__` de `TareaWindow`

```python
# Cambiar el color de fondo
glClearColor(R, G, B, 1.0)

# Ejemplos:
glClearColor(0.0, 0.0, 0.0, 1.0)     # Negro
glClearColor(0.2, 0.4, 0.6, 1.0)     # Azul cielo
glClearColor(0.1, 0.1, 0.1, 1.0)     # Gris oscuro
glClearColor(1.0, 1.0, 1.0, 1.0)     # Blanco
```

### 9. Agregar una Cuarta Pose (Opcional, para destacar)

**Ubicación:** `main.py`, función `get_poses()`

```python
# Al final de la lista, antes del return:
pose4 = Pose(
    name="Tu Pose Custom",
    joint_rotations={
        'torso': tr.rotationY(np.pi / 4),
        # ... tus rotaciones aquí
    },
    camera_config={
        'eye': np.array([2, 2, 3], dtype=np.float32),
        'at': np.array([0, 1, 0], dtype=np.float32),
        'up': np.array([0, 1, 0], dtype=np.float32)
    }
)

return [pose1, pose2, pose3, pose4]  # Agregar pose4
```

### 10. Cambiar el Nombre de las Poses

**Ubicación:** `main.py`, función `get_poses()`

```python
pose1 = Pose(
    name="Mi Nombre Custom",  # Cambiar aquí
    joint_rotations={...},
    camera_config={...}
)
```

## 📝 Nombres Sugeridos para Poses

- "El Pensador"
- "Saludo Militar"
- "Victoria"
- "Meditación"
- "Corriendo"
- "Saltando"
- "Defensa"
- "Ataque"
- "Celebración"
- "Sorpresa"

## 🎭 Ideas para Poses Dramáticas

### Pose de Superhéroe
```python
'left_shoulder': tr.rotationZ(np.pi/4),
'right_shoulder': tr.rotationZ(-np.pi/2),
'right_elbow': tr.rotationZ(-np.pi/3),
'left_hip': tr.rotationX(np.pi/8),
```

### Pose de Ninja
```python
'torso': tr.matmul([
    tr.rotationY(np.pi/4),
    tr.rotationX(np.pi/12)
]),
'left_shoulder': tr.rotationZ(np.pi/2),
'right_shoulder': tr.rotationZ(-np.pi/3),
```

### Pose de Baile
```python
'torso': tr.rotationY(np.pi/6),
'left_shoulder': tr.rotationZ(np.pi/3),
'right_shoulder': tr.rotationZ(-np.pi/3),
'left_hip': tr.rotationX(np.pi/8),
'right_hip': tr.rotationX(-np.pi/8),
```

## ⚠️ Consejos Importantes

1. **Siempre prueba después de cada cambio**: `python -m TU-RUT`

2. **Mantén copias de seguridad** antes de hacer cambios grandes

3. **Los ángulos en radianes**:
   - Positivo = rotación antihoraria
   - Negativo = rotación horaria

4. **Coordenadas de la cámara**:
   - X: negativo = izquierda, positivo = derecha
   - Y: negativo = abajo, positivo = arriba
   - Z: negativo = acercarse, positivo = alejarse

5. **Si algo se ve raro**:
   - Verifica que los valores RGB estén entre 0.0 y 1.0
   - Verifica que las escalas sean positivas
   - Verifica que la cámara no esté dentro del modelo

## 🐛 Debugging

Si encuentras errores:

```python
# Agregar prints para debug
print(f"Rotación aplicada: {angle}")
print(f"Color: {torso.color}")
print(f"Cámara: eye={eye}, at={at}")
```

## 📚 Referencias Rápidas

```python
# Rotaciones comunes
tr.rotationX(angle)  # Rota alrededor del eje X
tr.rotationY(angle)  # Rota alrededor del eje Y
tr.rotationZ(angle)  # Rota alrededor del eje Z

# Traslaciones
tr.translate(x, y, z)

# Escalas
tr.scale(sx, sy, sz)
tr.uniformScale(s)

# Componer transformaciones
tr.matmul([transform1, transform2, transform3])
```

## 🎉 ¡Diviértete Personalizando!

Recuerda: La tarea evalúa principalmente el **grafo de escena** y las **transformaciones jerárquicas**, no la creatividad artística. Pero agregar tu toque personal siempre es un plus. 😊
