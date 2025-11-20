"""
Primitivas geométricas básicas
"""

from OpenGL.GL import *
import numpy as np

class Mesh:
    """Clase base para mallas geométricas"""
    
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices
        self.setup_mesh()
        
    def setup_mesh(self):
        """Configura los buffers de OpenGL"""
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.EBO = glGenBuffers(1)
        
        glBindVertexArray(self.VAO)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)
        
        # Posición
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        
        glBindVertexArray(0)
        
    def draw(self):
        """Dibuja la malla"""
        glBindVertexArray(self.VAO)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        glBindVertexArray(0)


def create_cube():
    """Crea un cubo unitario"""
    vertices = np.array([
        # Cara frontal
        -0.5, -0.5,  0.5,
         0.5, -0.5,  0.5,
         0.5,  0.5,  0.5,
        -0.5,  0.5,  0.5,
        # Cara trasera
        -0.5, -0.5, -0.5,
         0.5, -0.5, -0.5,
         0.5,  0.5, -0.5,
        -0.5,  0.5, -0.5,
    ], dtype=np.float32)
    
    indices = np.array([
        # Frontal
        0, 1, 2, 2, 3, 0,
        # Trasera
        5, 4, 7, 7, 6, 5,
        # Izquierda
        4, 0, 3, 3, 7, 4,
        # Derecha
        1, 5, 6, 6, 2, 1,
        # Superior
        3, 2, 6, 6, 7, 3,
        # Inferior
        4, 5, 1, 1, 0, 4,
    ], dtype=np.uint32)
    
    return Mesh(vertices, indices)


def create_sphere(slices=20, stacks=20):
    """Crea una esfera"""
    vertices = []
    indices = []
    
    for i in range(stacks + 1):
        phi = np.pi * i / stacks
        for j in range(slices + 1):
            theta = 2 * np.pi * j / slices
            
            x = np.sin(phi) * np.cos(theta)
            y = np.cos(phi)
            z = np.sin(phi) * np.sin(theta)
            
            vertices.extend([x * 0.5, y * 0.5, z * 0.5])
    
    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1
            
            indices.extend([first, second, first + 1])
            indices.extend([second, second + 1, first + 1])
    
    return Mesh(np.array(vertices, dtype=np.float32), 
                np.array(indices, dtype=np.uint32))


def create_cylinder(slices=20):
    """Crea un cilindro"""
    vertices = []
    indices = []
    
    # Vértices del cilindro
    for i in range(slices + 1):
        theta = 2 * np.pi * i / slices
        x = np.cos(theta) * 0.5
        z = np.sin(theta) * 0.5
        
        # Vértice superior
        vertices.extend([x, 0.5, z])
        # Vértice inferior
        vertices.extend([x, -0.5, z])
    
    # Índices para las caras laterales
    for i in range(slices):
        base = i * 2
        indices.extend([base, base + 1, base + 2])
        indices.extend([base + 1, base + 3, base + 2])
    
    # Índices para las tapas
    center_top = len(vertices) // 3
    vertices.extend([0, 0.5, 0])
    center_bottom = len(vertices) // 3
    vertices.extend([0, -0.5, 0])
    
    for i in range(slices):
        base = i * 2
        # Tapa superior
        indices.extend([center_top, base, base + 2])
        # Tapa inferior
        indices.extend([center_bottom, base + 3, base + 1])
    
    return Mesh(np.array(vertices, dtype=np.float32), 
                np.array(indices, dtype=np.uint32))
