"""
Tarea de Computación Gráfica (CC3501)
Basado en los ejemplos del repositorio:
https://github.com/PLUMAS-research/cc3501-computer-graphics
"""

import pyglet
from OpenGL.GL import *
import numpy as np

# Configuración de la ventana
WIDTH = 800
HEIGHT = 600

class TareaWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Tarea CC3501")
        
        # Configuración de OpenGL
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)
        
    def on_draw(self):
        """Método llamado para dibujar la escena"""
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aquí va tu código de dibujo
        # TODO: Implementar según los requisitos de la tarea
        
    def on_resize(self, width, height):
        """Método llamado cuando se redimensiona la ventana"""
        glViewport(0, 0, width, height)
        
    def update(self, dt):
        """Método para actualizar la lógica de la aplicación"""
        pass

if __name__ == "__main__":
    window = TareaWindow()
    
    # Programar actualización cada frame
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    
    pyglet.app.run()
