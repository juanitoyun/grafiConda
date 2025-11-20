# 🚀 Guía Rápida de Instalación (Sin Conda)
## Configurar entorno para testear ejemplos del curso

Como no tienes Conda instalado, usaremos `venv` (entorno virtual de Python) con `pip`.

---

## 📦 Pasos de Instalación

### 1. Crear entorno virtual

```powershell
# En: C:\Users\56942\Desktop\proyecto grafica\curso-cc3501
python -m venv venv_grafica
```

### 2. Activar el entorno

```powershell
.\venv_grafica\Scripts\Activate.ps1
```

**Nota:** Si te da error de permisos, ejecuta esto primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Instalar dependencias

```powershell
# Actualizar pip
python -m pip install --upgrade pip

# Instalar paquetes necesarios
pip install numpy pyopengl pillow matplotlib scipy click pyglet pymunk trimesh networkx shapely
```

### 4. Verificar instalación

```powershell
python caja_de_juguetes.py
```

Deberías ver la lista de ejemplos disponibles.

---

## 🎯 Ejemplos Clave a Testear

Una vez instalado, ejecuta en orden:

```powershell
# 1. Hello World (verificación básica)
python caja_de_juguetes.py hello_world

# 2. Arcball (TU CÁMARA)
python caja_de_juguetes.py arcball

# 3. Boids (TUS PECES)
python caja_de_juguetes.py boids-abm

# 4. Partículas (TUS BURBUJAS)
python caja_de_juguetes.py particles

# 5. Grafos de escena
python caja_de_juguetes.py scene_graphs

# 6. Transformaciones
python caja_de_juguetes.py transformations
```

---

## ❓ Si algo falla

**Error de OpenGL en Windows:**
Si `pyopengl` da problemas, instala la versión "informal":
```powershell
pip uninstall pyopengl
pip install PyOpenGL-3.1.7-cp311-cp311-win_amd64.whl
```
(Descarga desde: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl)

**Pyglet no abre ventana:**
Prueba versión específica:
```powershell
pip install pyglet==2.0.10
```

---

## ✅ Checklist

- [ ] Entorno virtual creado
- [ ] Entorno activado (ves `(venv_grafica)` en el prompt)
- [ ] Dependencias instaladas
- [ ] `python caja_de_juguetes.py` muestra lista de ejemplos
- [ ] `hello_world` funciona
- [ ] Listo para testear!

---

**Siguiente paso:** Ejecutar los comandos de arriba uno por uno.
