# ✅ INSTRUCCIONES FINALES - Cómo Ejecutar los Ejemplos

## 🎯 TODO ESTÁ LISTO

- ✅ Repositorio clonado
- ✅ Entorno virtual creado
- ✅ Dependencias instaladas (incluyendo PyVista)

---

## 🚀 CÓMO EJECUTAR (Método más simple)

### Opción 1: Usar CMD (Recomendado para Windows)

1. Abre **CMD** (no PowerShell):
   - Presiona `Win + R`
   - Escribe `cmd`
   - Presiona Enter

2. Navega a la carpeta:
```cmd
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
```

3. Ejecuta cualquier ejemplo:
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py arcball_example
```

---

## 📝 EJEMPLOS LISTOS PARA EJECUTAR

### 1️⃣ Arcball (Tu Cámara) ⭐⭐⭐⭐⭐
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py arcball_example
```
**Controles:**
- Click izquierdo + arrastra → Rotar
- Scroll → Zoom in/out

### 2️⃣ Boids (Tus Peces) ⭐⭐⭐⭐⭐
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py boids_abm
```
**Observa:** Comportamiento de grupo emergente

### 3️⃣ Partículas (Tus Burbujas) ⭐⭐⭐⭐⭐
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py particulas
```
**Observa:** Spawn continuo, física, ciclo de vida

### 4️⃣ Sistema Solar (Grafos de Escena)
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py solar_system
```

### 5️⃣ Transformaciones (Bunny)
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py transformed_bunny
```

### 6️⃣ Composición de Transformaciones
```cmd
venv_grafica\Scripts\python.exe caja_de_juguetes.py compositions
```

---

## 🎨 ALTERNAT IVA: Usar Visual Studio Code

1. Abre VS Code
2. Abre la carpeta: `C:\Users\56942\Desktop\proyecto grafica\curso-cc3501`
3. Abre la terminal integrada (Ctrl + ñ)
4. Cambia a CMD:
   - Click en la flechita al lado de "powershell"
   - Selecciona "Command Prompt"
5. Ejecuta los comandos de arriba

---

## 📸 LO QUE VERÁS

### Arcball Example:
- Ventana con un modelo 3D (bunny o similar)
- Puedes rotarlo libremente
- Zoom in/out fluido

### Boids ABM:
- Agentes (puntos) moviéndose
- Se agrupan naturalmente
- Evitan chocar entre sí

### Partículas:
- Partículas apareciendo continuamente
- Se mueven con física
- Desaparecen después de un tiempo

---

## 🐛 SI ALGO FALLA

### "No abre ventana"
- Espera 5-10 segundos, puede tardar en cargar
- Verifica que no haya errores en la consola

### "ModuleNotFoundError: [módulo]"
```cmd
venv_grafica\Scripts\python.exe -m pip install [módulo]
```

### "OpenGL Error"
- Actualiza drivers de tu GPU
- Verifica que tu sistema soporte OpenGL 3.3+

---

## 📋 CHECKLIST DE TESTEO

Mientras exploras cada ejemplo:

### Arcball Example
- [ ] Se abre la ventana
- [ ] Puedo rotar con el mouse
- [ ] Puedo hacer zoom con scroll
- [ ] Entiendo cómo se siente la cámara
- [ ] Identifiqué los parámetros de control

**Notas:**
```
- Sensibilidad de rotación: _______
- Límites de zoom: _______
- ¿Tiene limitación vertical? Sí/No
```

### Boids ABM
- [ ] Veo agentes moviéndose
- [ ] Observo comportamiento de grupo
- [ ] Identifico separación (no chocan)
- [ ] Identifico cohesión (se agrupan)
- [ ] Identifico alineación (misma dirección)

**Notas:**
```
- Número de agentes: ~_______
- ¿Es 2D o 3D? _______
- ¿Cómo manejan los bordes? _______
```

### Partículas
- [ ] Veo partículas aparecer
- [ ] Observo movimiento (física)
- [ ] Noto cuándo desaparecen
- [ ] Verifico performance (FPS)

**Notas:**
```
- Rate de spawn: ~_______/seg
- Tiempo de vida: ~_______seg
- ¿Hay gravedad? Sí/No
```

---

## 📂 ARCHIVOS DEL CÓDIGO

Después de testear, lee estos archivos:

### Arcball
```
examples\arcball\__init__.py
```
Busca:
- Clase `ArcballCamera`
- Métodos `on_mouse_drag`, `on_mouse_scroll`
- Parámetros `distance`, `target`

### Boids
```
examples\boids-abm\app.py
examples\boids-abm\world.py
```
Busca:
- Las 3 reglas: `separate`, `cohere`, `align`
- Pesos de las reglas
- `perception_radius`

### Partículas
```
examples\particles\app.py
```
Busca:
- Clase `Particle`
- Sistema de spawning
- Actualización de física

---

## 🎯 OBJETIVO

Al terminar de testear, deberías tener:

1. ✅ Experiencia visual de cómo funciona cada sistema
2. ✅ Notas de parámetros importantes
3. ✅ Ideas de cómo adaptarlos a tu acuario
4. ✅ Lista de archivos para leer mañana

---

## ⏰ TIEMPO ESTIMADO

- Arcball: **10 minutos** (probar controles, tomar notas)
- Boids: **15 minutos** (observar patrones, experimentar)
- Partículas: **10 minutos** (ver ciclo completo)
- **TOTAL: 35-45 minutos**

---

## 📞 SIGUIENTE PASO DESPUÉS DE TESTEAR

1. **Crear documento de notas:**
   - `mis_observaciones.md`
   - Anota lo que viste, qué te gustó, qué copiarás

2. **Mañana: Leer código**
   - 30 min en cada ejemplo crítico
   - Identificar clases y funciones clave

3. **Pasado mañana: Diseñar tu proyecto**
   - Estructura de clases
   - Diagrama de componentes
   - Plan de desarrollo

---

## 🚀 ¡ADELANTE!

**Ejecuta ahora en CMD:**

```cmd
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
venv_grafica\Scripts\python.exe caja_de_juguetes.py arcball_example
```

**¡Disfruta explorando! 🐟💧✨**

---

## 💡 TIPS FINALES

- **Toma screenshots** de momentos interesantes
- **Anota valores** que veas en consola
- **Experimenta** con los controles
- **No te preocupes** si algo no entiendes ahora
- **Diviértete** - Estos ejemplos son interactivos y visuales

---

## 📚 DOCUMENTOS CREADOS

Ya tienes estos archivos de referencia:

1. `README_EMPEZAR_AQUI.md` - Guía principal
2. `EJEMPLOS_DISPONIBLES.md` - Lista completa
3. `INSTRUCCIONES_EJECUCION.md` - Este archivo
4. `ideas_proyecto.md` - Ideas clasificadas
5. `acuario_6W_analisis.md` - Análisis 6W
6. `comparativa_dimensiones_perspectivas.md` - 2D vs 3D
7. `guia_ejemplos_curso.md` - Guía detallada

---

**¿Listo? ¡A ejecutar los ejemplos! 🎮**
