# Ideas de Proyecto - Tarea 3 CC3501
## Computación Gráfica y Modelamiento

---

## Matriz de Clasificación: Factibilidad & Facilidad vs Ocio & Entretenimiento

### 🟢 ZONA ÓPTIMA: Alta Factibilidad + Alto Entretenimiento
*Proyectos con mejor equilibrio para buenos resultados*

#### 1. **Simulador de Acuario Interactivo** 🐠
- **Técnicas**: Boids (comportamiento de peces), partículas (burbujas), iluminación, texturas
- **Descripción**: Acuario 3D con peces que se mueven usando algoritmos de boids, plantas que se deforman con el "agua", burbujas ascendentes, y control de cámara interactiva
- **Factibilidad**: 8/10 - Boids ya tiene ejemplos en el curso
- **Entretenimiento**: 8/10 - Visualmente atractivo y relajante
- **Tiempo estimado**: 2-3 semanas

#### 2. **Juego de Billar/Pool Simplificado** 🎱
- **Técnicas**: Detección de colisiones, física de cuerpos rígidos (pymunk), ray-casting para el taco
- **Descripción**: Mesa de billar con bolas que colisionan físicamente, taco que se apunta con el mouse, vista top-down o 3D
- **Factibilidad**: 8/10 - Pymunk simplifica la física
- **Entretenimiento**: 9/10 - Muy satisfactorio visualmente
- **Tiempo estimado**: 2 semanas

#### 3. **Visualizador de Música con Partículas** 🎵
- **Técnicas**: Sistemas de partículas, deformaciones, análisis de audio FFT
- **Descripción**: Partículas que reaccionan a la música en tiempo real, creando patrones visuales. Diferentes modos de visualización (ondas, explosiones, espiral)
- **Factibilidad**: 7/10 - Audio puede ser complejo pero hay librerías
- **Entretenimiento**: 9/10 - Muy visual y personalizable
- **Tiempo estimado**: 2-3 semanas

#### 4. **Generador Procedural de Árboles 3D** 🌳
- **Técnicas**: L-Systems, curvas (troncos y ramas), texturas, deformación por viento
- **Descripción**: Sistema que genera árboles proceduralmente con parámetros ajustables, animación de viento, diferentes especies
- **Factibilidad**: 7/10 - L-Systems requiere estudio pero están bien documentados
- **Entretenimiento**: 7/10 - Resultados sorprendentes
- **Tiempo estimado**: 2-3 semanas

#### 5. **Simulador de Telas Interactivo** 👕
- **Técnicas**: Deformación, integración de Verlet, colisiones, texturas
- **Descripción**: Tela que se puede colgar, rasgar, o interactuar con objetos. El curso ya tiene ejemplos de tela
- **Factibilidad**: 8/10 - Hay ejemplos base (cloth_verlet, cloth_pymunk)
- **Entretenimiento**: 8/10 - Muy satisfactorio visualmente
- **Tiempo estimado**: 2 semanas

---

### 🔵 MODERADO: Factibilidad Media + Entretenimiento Alto
*Requieren más esfuerzo pero tienen gran potencial*

#### 6. **Mini Golf 3D** ⛳
- **Técnicas**: Física (pymunk), curvas (para el terreno), colisiones, texturas, iluminación
- **Descripción**: Juego de mini golf con múltiples niveles, obstáculos, rampas curvas
- **Factibilidad**: 6/10 - Diseño de niveles puede tomar tiempo
- **Entretenimiento**: 9/10 - Muy rejugable
- **Tiempo estimado**: 3-4 semanas

#### 7. **Simulador de Planetario/Sistema Solar Mejorado** 🪐
- **Técnicas**: Grafos de escena, órbitas (curvas), texturas, shaders (anillos de Saturno), partículas (cometas)
- **Descripción**: Expansión del ejemplo solar_system con más detalle, colisiones de asteroides, cámara libre
- **Factibilidad**: 7/10 - Hay ejemplo base
- **Entretenimiento**: 7/10 - Educativo y bonito
- **Tiempo estimado**: 2-3 semanas

#### 8. **Laberinto Procedural con Ray Tracing** 🔦
- **Técnicas**: Ray tracing (iluminación), generación procedural, colisiones
- **Descripción**: Laberinto generado aleatoriamente con iluminación realista, sombras, antorcha que llevas
- **Factibilidad**: 6/10 - Ray tracing puede ser pesado
- **Entretenimiento**: 8/10 - Atmósfera inmersiva
- **Tiempo estimado**: 3-4 semanas

#### 9. **Simulador de Fluidos (Grid-based)** 💧
- **Técnicas**: Sistemas de partículas, deformación, shaders
- **Descripción**: Simulación de agua en 2D o 3D simple, con obstáculos interactivos
- **Factibilidad**: 5/10 - Fluidos son complejos
- **Entretenimiento**: 9/10 - Muy visual
- **Tiempo estimado**: 4 semanas

---

### 🟡 SEGURO: Alta Factibilidad + Entretenimiento Moderado
*Proyectos más simples pero sólidos*

#### 10. **Editor de Curvas Bézier Interactivo** ✏️
- **Técnicas**: Curvas de Bézier, superficies, extrusión
- **Descripción**: Herramienta para crear y editar curvas/superficies con puntos de control, exportar mallas
- **Factibilidad**: 9/10 - Tema bien acotado
- **Entretenimiento**: 6/10 - Más técnico que visual
- **Tiempo estimado**: 1-2 semanas

#### 11. **Visualizador de Fractales 3D** 📐
- **Técnicas**: Ray marching, shaders, matemáticas fractales (Mandelbulb, Menger Sponge)
- **Descripción**: Renderizado de fractales 3D con zoom y rotación interactiva
- **Factibilidad**: 7/10 - Ray marching requiere estudio
- **Entretenimiento**: 7/10 - Impresionante pero estático
- **Tiempo estimado**: 2-3 semanas

#### 12. **Galería de Arte Virtual** 🖼️
- **Técnicas**: Modelado 3D, texturas, iluminación, cámara libre
- **Descripción**: Sala de museo donde puedes caminar y ver cuadros/esculturas, diferentes salas temáticas
- **Factibilidad**: 8/10 - Principalmente modelado y carga de assets
- **Entretenimiento**: 6/10 - Depende del contenido
- **Tiempo estimado**: 2 semanas

---

### 🟠 AMBICIOSO: Factibilidad Baja + Entretenimiento Alto
*Proyectos desafiantes, mejor con experiencia previa*

#### 13. **Motor de Destrucción de Edificios** 💥
- **Técnicas**: Detección de colisiones, fragmentación de mallas, física de cuerpos rígidos, partículas
- **Descripción**: Edificio que se destruye de forma realista cuando colisionas objetos contra él
- **Factibilidad**: 4/10 - Fragmentación es compleja
- **Entretenimiento**: 10/10 - Muy satisfactorio
- **Tiempo estimado**: 4-5 semanas

#### 14. **Ray Tracer con Múltiples Efectos** 🌟
- **Técnicas**: Ray tracing completo, reflexiones, refracciones, sombras suaves, anti-aliasing
- **Descripción**: Ray tracer desde cero con múltiples efectos de iluminación avanzada
- **Factibilidad**: 5/10 - Computacionalmente intensivo
- **Entretenimiento**: 7/10 - Resultados impresionantes pero renders lentos
- **Tiempo estimado**: 4 semanas

#### 15. **Simulador de Multitudes (Crowd Simulation)** 👥
- **Técnicas**: Boids avanzado, pathfinding, quadtree para optimización, ABM
- **Descripción**: Simulación de personas moviéndose en espacios, evitando obstáculos, formando filas
- **Factibilidad**: 5/10 - Pathfinding y optimización complejos
- **Entretenimiento**: 8/10 - Fascinante ver emergencia
- **Tiempo estimado**: 4 semanas

---

## 🏆 TOP 3 RECOMENDACIONES (Equilibrio Óptimo)

### 1. **Simulador de Acuario Interactivo** 🥇
**¿Por qué?** Combina múltiples técnicas del curso de forma natural, es visualmente atractivo, tiene ejemplos base (boids), y permite iteración incremental.

**Propuesta de párrafo para el profesor:**
> "Mi proyecto será un acuario virtual 3D interactivo que simula un ecosistema marino. Utilizará algoritmos de boids para el comportamiento de cardúmenes de peces, sistemas de partículas para burbujas y efectos de agua, deformación de mallas para plantas acuáticas que se mueven con corrientes simuladas, y técnicas de iluminación y texturizado para crear una atmósfera submarina realista. El usuario podrá navegar con la cámara libremente, alimentar a los peces (interacción), y ajustar parámetros del ecosistema."

---

### 2. **Simulador de Telas Interactivo** 🥈
**¿Por qué?** El curso ya tiene ejemplos base, la física es manejable, y los resultados son muy satisfactorios visualmente. Permite agregar complejidad gradualmente.

**Propuesta de párrafo para el profesor:**
> "Desarrollaré un simulador de telas interactivo que permita experimentar con diferentes propiedades físicas de materiales textiles. Basándome en los ejemplos del curso, implementaré simulación de telas usando integración de Verlet con mejoras en el realismo (rasgado, diferentes densidades de tela). Incluirá detección de colisiones con objetos 3D, viento simulado con campos de fuerza, y la posibilidad de sujetar/soltar puntos de la tela interactivamente. Aplicaré texturas realistas y shaders para mejorar la presentación visual."

---

### 3. **Juego de Billar Simplificado** 🥉
**¿Por qué?** Usa pymunk (ya en el curso), la física es manejable, tiene objetivo claro, y es muy satisfactorio visualmente. Buen balance entre complejidad técnica y resultado.

**Propuesta de párrafo para el profesor:**
> "Crearé un juego de billar 3D que simula la física realista de colisiones entre bolas usando pymunk. El proyecto incluirá detección de colisiones entre bolas y con los bordes de la mesa, fricción y amortiguamiento para movimiento realista, sistema de apuntado del taco usando ray-casting, y cámara con diferentes vistas (cenital y perspectiva). Aplicaré técnicas de texturizado para las bolas numeradas y la mesa, iluminación para resaltar el volumen de las esferas, y feedback visual para la trayectoria del tiro."

---

## 💡 Consejos Adicionales

### Para cualquier proyecto elegido:
1. **Empieza simple**: Versión mínima funcional primero
2. **Itera**: Agrega features incrementalmente
3. **Usa los ejemplos del curso**: `caja_de_juguetes.py` tiene excelentes bases
4. **Documenta**: Toma screenshots del progreso
5. **Performance**: Optimiza solo si es necesario (quadtree, frustum culling)

### Técnicas que dan mucho valor visual por poco esfuerzo:
- ✨ **Partículas**: Instantáneamente más dinámico
- 🎨 **Buenos colores y texturas**: Gran impacto visual
- 💡 **Iluminación básica**: Phong shading + sombras simples
- 📹 **Cámara suave**: Interpolación hace todo verse profesional
- 🎵 **Audio**: Efectos de sonido simples dan mucha vida

---

## 📊 Comparación Rápida

| Proyecto | Factibilidad | Entretenimiento | Tiempo | Técnicas |
|----------|--------------|-----------------|--------|----------|
| Acuario | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 2-3 sem | Boids, Partículas, Deformación |
| Billar | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 2 sem | Colisiones, Pymunk, Ray-casting |
| Visualizador Musical | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 2-3 sem | Partículas, Audio, Shaders |
| Árboles Procedurales | ⭐⭐⭐ | ⭐⭐⭐ | 2-3 sem | L-Systems, Curvas |
| Telas | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 2 sem | Deformación, Verlet, Colisiones |
| Mini Golf | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 3-4 sem | Física, Curvas, Colisiones |
| Sistema Solar+ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 2-3 sem | Grafos, Órbitas, Texturas |
| Fluidos | ⭐⭐ | ⭐⭐⭐⭐⭐ | 4 sem | Partículas, Shaders complejos |

---

**¿Necesitas más detalles sobre algún proyecto específico?** Puedo expandir la descripción técnica, sugerir recursos, o ayudarte a redactar la propuesta final.
