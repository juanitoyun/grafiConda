# 🐍 Instalación con Conda Prompt (RECOMENDADO)
## Configuración oficial del curso CC3501

> **IMPORTANTE:** Esta es la forma oficial y recomendada por el curso.

---

## 📋 PASOS DE INSTALACIÓN

### 1️⃣ Abrir Anaconda Prompt

1. Presiona `Win + S` (buscar)
2. Escribe **"Anaconda Prompt"**
3. Click derecho → **Ejecutar como administrador** (opcional pero recomendado)

**IMPORTANTE:** Debe ser **Anaconda Prompt**, NO PowerShell ni CMD normal.

---

### 2️⃣ Navegar a la carpeta del curso

```bash
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
```

Verifica que estás en la carpeta correcta:
```bash
dir
```

Deberías ver: `environment.yml`, `caja_de_juguetes.py`, `examples`, etc.

---

### 3️⃣ Crear el entorno conda

```bash
conda env create -n grafica -f environment.yml
```

**Qué hace esto:**
- Lee el archivo `environment.yml` (configuración del curso)
- Crea un entorno llamado `grafica`
- Instala todas las dependencias automáticamente

**Tiempo estimado:** 5-10 minutos (descarga e instala paquetes)

**Salida esperada:**
```
Collecting package metadata...
Solving environment...
Downloading and Extracting Packages...
Preparing transaction...
Executing transaction...
#
# To activate this environment, use
#
#     $ conda activate grafica
#
```

---

### 4️⃣ Activar el entorno

```bash
conda activate grafica
```

**Sabrás que funcionó** cuando veas `(grafica)` al inicio de la línea:
```
(grafica) C:\Users\56942\Desktop\proyecto grafica\curso-cc3501>
```

---

### 5️⃣ Verificar instalación

```bash
python caja_de_juguetes.py
```

**Salida esperada:**
```
Usage: caja_de_juguetes.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  arcball_example
  boids_abm
  particulas
  solar_system
  ...
```

Si ves esto → ✅ **¡TODO FUNCIONA!**

---

## 🚀 EJECUTAR EJEMPLOS

**SIEMPRE** desde Anaconda Prompt con el entorno activado:

### Verificar que el entorno está activo
Verifica que veas `(grafica)` al inicio de la línea.

Si NO lo ves:
```bash
conda activate grafica
```

### Ejemplo 1: Arcball (Tu cámara) ⭐
```bash
python caja_de_juguetes.py arcball_example
```

### Ejemplo 2: Boids (Tus peces) ⭐
```bash
python caja_de_juguetes.py boids_abm
```

### Ejemplo 3: Partículas (Tus burbujas) ⭐
```bash
python caja_de_juguetes.py particulas
```

### Ejemplo 4: Sistema Solar (Grafos de escena)
```bash
python caja_de_juguetes.py solar_system
```

### Ejemplo 5: Transformaciones
```bash
python caja_de_juguetes.py transformed_bunny
```

---

## 📝 FLUJO DE TRABAJO DIARIO

Cada vez que quieras trabajar:

1. **Abrir Anaconda Prompt**
2. **Ir a la carpeta:**
   ```bash
   cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
   ```
3. **Activar entorno:**
   ```bash
   conda activate grafica
   ```
4. **Ejecutar ejemplos:**
   ```bash
   python caja_de_juguetes.py [nombre_ejemplo]
   ```

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Problema: "conda: command not found"
**Solución:** No estás en Anaconda Prompt. Cierra PowerShell/CMD y abre **Anaconda Prompt**.

### Problema: "environment.yml not found"
**Solución:** No estás en la carpeta correcta.
```bash
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
```

### Problema: "Solving environment: failed"
**Solución:** Conflicto de paquetes. Intenta:
```bash
conda env create -n grafica -f environment.yml --force
```

### Problema: El ejemplo no abre ventana
**Solución:** 
1. Espera 5-10 segundos (puede tardar en cargar)
2. Verifica errores en la consola
3. Asegúrate de tener drivers de GPU actualizados

### Problema: "ModuleNotFoundError: ..."
**Solución:** El entorno no está activado.
```bash
conda activate grafica
```

---

## 🔄 ACTUALIZAR ENTORNO

Si necesitas agregar paquetes después:

```bash
conda activate grafica
conda install [nombre_paquete]
```

O con pip (si no está en conda):
```bash
conda activate grafica
pip install [nombre_paquete]
```

---

## 🗑️ ELIMINAR Y RECREAR ENTORNO

Si algo sale mal, puedes eliminar y recrear:

```bash
# Desactivar primero
conda deactivate

# Eliminar entorno
conda env remove -n grafica

# Recrear desde cero
conda env create -n grafica -f environment.yml

# Activar
conda activate grafica
```

---

## 📊 COMANDOS ÚTILES

### Ver entornos disponibles
```bash
conda env list
```

### Ver paquetes instalados en el entorno
```bash
conda activate grafica
conda list
```

### Información del entorno
```bash
conda info --envs
```

---

## ✅ CHECKLIST DE INSTALACIÓN

- [ ] Anaconda Prompt abierto
- [ ] Navegado a `curso-cc3501/`
- [ ] Ejecutado `conda env create -n grafica -f environment.yml`
- [ ] Esperado 5-10 min (instalación)
- [ ] Ejecutado `conda activate grafica`
- [ ] Ves `(grafica)` al inicio de la línea
- [ ] Ejecutado `python caja_de_juguetes.py` → Ves lista de comandos
- [ ] ✅ ¡LISTO PARA TESTEAR!

---

## 🎯 SIGUIENTE PASO

**Ejecuta ahora en Anaconda Prompt:**

```bash
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
conda activate grafica
python caja_de_juguetes.py arcball_example
```

**Controles:**
- Arrastra con el mouse → Rotar
- Scroll → Zoom

**¡Disfruta explorando! 🐟💧✨**

---

## 💡 VENTAJAS DE USAR CONDA

✅ **Instalación automatizada** - Todo en un comando  
✅ **Dependencias resueltas** - Conda maneja conflictos  
✅ **Entorno aislado** - No afecta otros proyectos  
✅ **Exactamente como el curso** - Mismo setup que el profesor  
✅ **Fácil de compartir** - `environment.yml` tiene todo  

---

## 📚 REFERENCIA RÁPIDA

```bash
# Activar entorno
conda activate grafica

# Desactivar entorno
conda deactivate

# Ver ejemplos disponibles
python caja_de_juguetes.py --help

# Ejecutar ejemplo
python caja_de_juguetes.py [nombre_ejemplo]

# Ver paquetes instalados
conda list

# Actualizar paquete
conda update [nombre_paquete]
```

---

**¿Todo claro? ¡Ejecuta los comandos y empieza a explorar!** 🚀
