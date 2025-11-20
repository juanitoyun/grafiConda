"""
Scene Graph Node implementation
"""

import numpy as np
from OpenGL.GL import *
from . import transformations as tr

class SceneGraphNode:
    """Nodo del grafo de escena con transformaciones jerárquicas"""
    
    def __init__(self, name):
        self.name = name
        self.transform = tr.identity()
        self.children = []
        self.mesh = None
        self.color = [1.0, 1.0, 1.0]
        
    def add_child(self, child):
        """Agrega un nodo hijo"""
        self.children.append(child)
        return child
        
    def draw(self, shader_program, parent_transform=None):
        """Dibuja el nodo y sus hijos recursivamente"""
        if parent_transform is None:
            parent_transform = tr.identity()
            
        # Calcular la transformación acumulada
        current_transform = np.matmul(parent_transform, self.transform)
        
        # Si este nodo tiene geometría, dibujarla
        if self.mesh is not None:
            glUniformMatrix4fv(
                glGetUniformLocation(shader_program, "model"),
                1, GL_TRUE, current_transform
            )
            glUniform3f(
                glGetUniformLocation(shader_program, "color"),
                self.color[0], self.color[1], self.color[2]
            )
            self.mesh.draw()
        
        # Dibujar los hijos
        for child in self.children:
            child.draw(shader_program, current_transform)
