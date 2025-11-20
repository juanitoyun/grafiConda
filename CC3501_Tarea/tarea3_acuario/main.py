"""
TAREA 3: ACUARIO VIRTUAL INTERACTIVO
Juan Ignacio Reyes Marchant

CONTROLES:
- Arrastrar mouse: Rotar cámara
- Scroll: Zoom
- ESPACIO: Pausar/reanudar
- ESC: Salir
"""

import pyglet
from pyglet.window import key
from OpenGL.GL import *
import numpy as np
import os

from . import transformations as tr
from .geometry import create_cube, create_sphere
from .boids import BoidSystem
from .particles import ParticleSystem


# Configuración
WIDTH = 1280
HEIGHT = 720


def load_shader(vertex_path, fragment_path):
    """Carga shaders desde archivos"""
    with open(vertex_path, 'r') as f:
        vertex_src = f.read()
    with open(fragment_path, 'r') as f:
        fragment_src = f.read()
    return vertex_src, fragment_src


def compile_shader(source, shader_type):
    """Compila un shader"""
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(shader).decode()
        print(f"Shader error: {error}")
        raise RuntimeError(error)
    
    return shader


def create_program(vertex_src, fragment_src):
    """Crea programa de shaders"""
    vertex_shader = compile_shader(vertex_src, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_src, GL_FRAGMENT_SHADER)
    
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(program).decode()
        print(f"Program error: {error}")
        raise RuntimeError(error)
    
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    
    return program


class SimpleCamera:
    """Cámara orbital simplificada"""
    
    def __init__(self):
        self.distance = 15.0
        self.theta = 0.0
        self.phi = np.pi / 4
        self.target = np.array([0, 0, 0], dtype=np.float32)
        self.dragging = False
        self.last_x = 0
        self.last_y = 0
    
    def get_position(self):
        x = self.distance * np.sin(self.phi) * np.cos(self.theta)
        y = self.distance * np.cos(self.phi)
        z = self.distance * np.sin(self.phi) * np.sin(self.theta)
        return self.target + np.array([x, y, z], dtype=np.float32)
    
    def get_view_matrix(self):
        eye = self.get_position()
        at = self.target
        up = np.array([0, 1, 0], dtype=np.float32)
        return tr.lookAt(eye, at, up)
    
    def on_mouse_press(self, x, y):
        self.dragging = True
        self.last_x = x
        self.last_y = y
    
    def on_mouse_release(self):
        self.dragging = False
    
    def on_mouse_drag(self, x, y):
        if not self.dragging:
            return
        
        dx = x - self.last_x
        dy = y - self.last_y
        
        self.theta -= dx * 0.005
        self.phi -= dy * 0.005
        self.phi = np.clip(self.phi, 0.1, np.pi - 0.1)
        
        self.last_x = x
        self.last_y = y
    
    def on_scroll(self, scroll_y):
        self.distance -= scroll_y * 0.5
        self.distance = np.clip(self.distance, 5.0, 30.0)


class AquariumApp(pyglet.window.Window):
    """Aplicación del acuario"""
    
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Acuario Virtual - Tarea 3")
        
        # OpenGL
        glClearColor(0.0, 0.1, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        
        # Shaders
        current_dir = os.path.dirname(os.path.abspath(__file__))
        vertex_src, fragment_src = load_shader(
            os.path.join(current_dir, "vertex_shader.glsl"),
            os.path.join(current_dir, "fragment_shader.glsl")
        )
        self.program = create_program(vertex_src, fragment_src)
        
        # Geometría
        self.sphere = create_sphere()
        
        # Cámara
        self.camera = SimpleCamera()
        self.projMat = tr.perspective(45, WIDTH / HEIGHT, 0.1, 100.0)
        
        # Sistemas
        bounds = (
            np.array([-5.0, -3.0, -4.0], dtype=np.float32),
            np.array([5.0, 3.0, 4.0], dtype=np.float32)
        )
        self.boids = BoidSystem(30, bounds)
        self.particles = ParticleSystem(5, bounds)
        
        # Estado
        self.paused = False
        self.light_pos = np.array([0, 5, 5], dtype=np.float32)
        
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        
        print("=" * 60)
        print("ACUARIO VIRTUAL - Tarea 3")
        print("=" * 60)
        print("Arrastrar mouse: Rotar cámara")
        print("Scroll:          Zoom")
        print("ESPACIO:         Pausar")
        print("ESC:             Salir")
        print("=" * 60)
    
    def update(self, dt):
        if not self.paused:
            self.boids.update(dt)
            self.particles.update(dt)
    
    def on_draw(self):
        self.clear()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glUseProgram(self.program)
        
        # Matrices
        viewMat = self.camera.get_view_matrix()
        
        # Uniforms globales
        glUniformMatrix4fv(glGetUniformLocation(self.program, "view"), 1, GL_FALSE, viewMat)
        glUniformMatrix4fv(glGetUniformLocation(self.program, "projection"), 1, GL_FALSE, self.projMat)
        glUniform3fv(glGetUniformLocation(self.program, "viewPos"), 1, self.camera.get_position())
        glUniform3fv(glGetUniformLocation(self.program, "lightPos"), 1, self.light_pos)
        
        # Dibujar
        self.draw_fish()
        self.draw_bubbles()
    
    def draw_fish(self):
        """Dibuja peces"""
        positions = self.boids.get_positions()
        velocities = self.boids.get_velocities()
        
        for i, pos in enumerate(positions):
            vel = velocities[i]
            
            translation = tr.translate(pos[0], pos[1], pos[2])
            scale = tr.scale(0.5, 0.3, 0.3)  # MÁS GRANDE para verlos mejor
            
            if np.linalg.norm(vel) > 0.001:
                angle = np.arctan2(vel[2], vel[0])
                rotation = tr.rotationY(angle)
            else:
                rotation = tr.identity()
            
            model = tr.matmul([translation, rotation, scale])
            
            glUniformMatrix4fv(glGetUniformLocation(self.program, "model"), 1, GL_FALSE, model)
            glUniform3f(glGetUniformLocation(self.program, "color"), 1.0, 0.5, 0.1)
            
            self.sphere.draw()
    
    def draw_bubbles(self):
        """Dibuja burbujas"""
        particles_data = self.particles.get_particles_data()
        
        for pos, size, alpha in particles_data:
            translation = tr.translate(pos[0], pos[1], pos[2])
            scale_mat = tr.uniformScale(size * 3)  # MÁS GRANDE para verlas
            model = tr.matmul([translation, scale_mat])
            
            glUniformMatrix4fv(glGetUniformLocation(self.program, "model"), 1, GL_FALSE, model)
            glUniform3f(glGetUniformLocation(self.program, "color"), 0.7, 0.8, 1.0)
            
            self.sphere.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        self.camera.on_mouse_press(x, y)
    
    def on_mouse_release(self, x, y, button, modifiers):
        self.camera.on_mouse_release()
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.camera.on_mouse_drag(x, y)
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.camera.on_scroll(scroll_y)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.paused = not self.paused
            print(f"{'PAUSADO' if self.paused else 'REANUDADO'}")
        elif symbol == key.ESCAPE:
            self.close()


def main():
    app = AquariumApp()
    pyglet.app.run()


if __name__ == "__main__":
    main()
