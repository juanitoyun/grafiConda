@echo off
REM Script para ejecutar la Tarea 2
echo ============================================================
echo TAREA 2: Personaje Articulado y Poses Dramaticas
echo CC3501 - Computacion Grafica
echo ============================================================
echo.
echo Ejecutando el programa...
echo.

python -m 60910000-1

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: No se pudo ejecutar el programa.
    echo Verifica que tengas instaladas las dependencias:
    echo   pip install numpy pyglet PyOpenGL
    pause
)
