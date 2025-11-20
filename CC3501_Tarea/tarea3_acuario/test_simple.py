"""
VERSION DE PRUEBA ULTRA SIMPLIFICADA - SOLO PARA VER QUE FUNCIONA
Dibuja cubos grandes y coloridos para verificar que todo está bien
"""

import pyglet
from pyglet.window import key
from OpenGL.GL import *
import numpy as np
import os

from . import transformations as tr
from .geometry import create_cube, create_sphere


WIDTH = 1280
HEIGHT = 720


def load_compile_shaders():
    """Carga y compila shaders"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    with open(os.path.join(current_dir, "vertex_shader.glsl")) as f:
        vertex_src = f.read()
    with open(os.path.join(current_dir, "fragment_shader.glsl")) as f:
        fragment_src = f.read()
    
    # Vertex shader
    vs = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vs, vertex_src)
    glCompileShader(vs)
    
    # Fragment shader
    fs = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fs, fragment_src)
    glCompileShader(fs)
    
    # Program
    program = glCreateProgram()
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)
    
    glDeleteShader(vs)
    glDeleteShader(fs)
    
    return program


class TestApp(pyglet.window.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "TEST - Deberías ver CUBOS GRANDES")
        
        glClearColor(0.2, 0.2, 0.3, 1.0)
        glEnable(GL_DEPTH_TEST)
        
        self.program = load_compile_shaders()
        self.cube = create_cube()
        
        self.angle = 0.0
        
        # Cámara fija simple
        self.viewMat = tr.lookAt(
            np.array([5, 3, 5], dtype=np.float32),
            np.array([0, 0, 0], dtype=np.float32),
            np.array([0, 1, 0], dtype=np.float32)
        )
        
        self.projMat = tr.perspective(45, WIDTH/HEIGHT, 0.1, 100.0)
        
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        
        print("=" * 60)
        print("TEST: Deberías ver 3 CUBOS GRANDES rotando")
        print("Si ves esto, TODO FUNCIONA correctamente")
        print("ESC: Salir")
        print("=" * 60)
    
    def update(self, dt):
        self.angle += dt
    
    def on_draw(self):
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glUseProgram(self.program)
        
        # Uniforms globales
        glUniformMatrix4fv(glGetUniformLocation(self.program, "view"), 1, GL_FALSE, self.viewMat)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "projection"), 1, GL_FALSE, self.projMat)
        glUniform3f(glGetUniformLocation(self.program, "viewPos"), 5, 3, 5)
        glUniform3f(glGetUniformLocation(self.program, "lightPos"), 5, 5, 5)
        
        # CUBO 1 - ROJO (centro)
        model = tr.matmul([
            tr.rotationY(self.angle),
            tr.scale(1, 1, 1)
        ])
        glUniformMatrix4fv(glGetUniformLocation(self.program, "model"), 1, GL_FALSE, model)
        glUniform3f(glGetUniformLocation(self.program, "color"), 1.0, 0.0, 0.0)
        self.cube.draw()
        
        # CUBO 2 - VERDE (izquierda)
        model = tr.matmul([
            tr.translate(-2.5, 0, 0),
            tr.rotationY(self.angle * 0.7),
            tr.scale(0.8, 0.8, 0.8)
        ])
        glUniformMatrix4fv(glGetUniformLocation(self.program, "model"), 1, GL_FALSE, model)
        glUniform3f(glGetUniformLocation(self.program, "color"), 0.0, 1.0, 0.0)
        self.cube.draw()
        
        # CUBO 3 - AZUL (derecha)
        model = tr.matmul([
            tr.translate(2.5, 0, 0),
            tr.rotationY(self.angle * 1.3),
            tr.scale(0.8, 0.8, 0.8)
        ])
        glUniformMatrix4fv(glGetUniformLocation(self.program, "model"), 1, GL_FALSE, model)
        glUniform3f(glGetUniformLocation(self.program, "color"), 0.0, 0.0, 1.0)
        self.cube.draw()
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()


def main():
    app = TestApp()
    pyglet.app.run()


if __name__ == "__main__":
    main()
