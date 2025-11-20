# ⚡ INICIO RÁPIDO - Usar Conda Prompt

## 🎯 LO QUE NECESITAS HACER AHORA

### 1. Abrir Anaconda Prompt

**IMPORTANTE:** NO uses PowerShell ni CMD normal. Usa **Anaconda Prompt**.

**Cómo abrir Anaconda Prompt:**
1. Presiona la tecla `Windows` (⊞)
2. Escribe: **"Anaconda Prompt"**
3. Click en **Anaconda Prompt** (icono negro con serpiente verde)

**Se abrirá una ventana** que dice algo como:
```
(base) C:\Users\56942>
```

---

### 2. Copiar y Pegar estos Comandos

**En Anaconda Prompt, ejecuta UNO POR UNO:**

#### Paso 1: Ir a la carpeta del curso
```bash
cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"
```

#### Paso 2: Crear el entorno (TARDA 5-10 min)
```bash
conda env create -n grafica -f environment.yml
```

**ESPERA** a que termine. Verás muchas descargas e instalaciones.

#### Paso 3: Activar el entorno
```bash
conda activate grafica
```

Verás que cambia de `(base)` a `(grafica)`:
```
(grafica) C:\Users\56942\Desktop\proyecto grafica\curso-cc3501>
```

---

### 3. Ejecutar Ejemplos

**Ahora puedes ejecutar cualquier ejemplo:**

#### Arcball (Tu cámara) ⭐
```bash
python caja_de_juguetes.py arcball_example
```
**Controles:** Arrastra mouse = rotar, Scroll = zoom

#### Boids (Tus peces) ⭐
```bash
python caja_de_juguetes.py boids_abm
```
**Observa:** Comportamiento de grupo

#### Partículas (Tus burbujas) ⭐
```bash
python caja_de_juguetes.py particulas
```
**Observa:** Spawn y física

---

## 📋 CHECKLIST

Marca cuando completes:

- [ ] Abrí **Anaconda Prompt** (NO PowerShell)
- [ ] Ejecuté `cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"`
- [ ] Ejecuté `conda env create -n grafica -f environment.yml`
- [ ] Esperé que termine (5-10 min)
- [ ] Ejecuté `conda activate grafica`
- [ ] Veo `(grafica)` al inicio de la línea ✅
- [ ] Ejecuté `python caja_de_juguetes.py arcball_example`
- [ ] ¡Vi el modelo 3D y lo pude rotar! 🎉

---

## 💡 RECUERDA

**SIEMPRE que quieras trabajar:**

1. Abrir **Anaconda Prompt** (no PowerShell)
2. `cd "C:\Users\56942\Desktop\proyecto grafica\curso-cc3501"`
3. `conda activate grafica`
4. `python caja_de_juguetes.py [ejemplo]`

---

## 🐛 SI ALGO FALLA

### "conda env create" da error
**Solución:** Intenta con `--force`:
```bash
conda env create -n grafica -f environment.yml --force
```

### No veo `(grafica)` después de activar
**Solución:** Activa de nuevo:
```bash
conda activate grafica
```

### "ModuleNotFoundError"
**Solución:** El entorno no está activado. Ejecuta:
```bash
conda activate grafica
```

---

## 📚 PRÓXIMO PASO DESPUÉS DE TESTEAR

1. **Testear los 3 ejemplos críticos** (30-45 min)
2. **Leer** `acuario_6W_analisis.md` (10 min)
3. **Enviar propuesta** al profesor (5 min)
4. **Empezar a programar** tu acuario (mañana)

---

**¡Ahora sí, abre Anaconda Prompt y ejecuta los comandos! 🚀**
