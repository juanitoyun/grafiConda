"""
Primitivas geométricas básicas.
Incluye cubos, esferas, cilindros y formas para el acuario.
"""

from OpenGL.GL import *
import numpy as np
import ctypes

class Mesh:
    """
    Clase base para mallas geométricas.
    Maneja la creación de VAO, VBO y EBO para renderizar con OpenGL.
    """
    
    def __init__(self, vertices, indices):
        """
        Constructor de Mesh.
        
        Parámetros:
        - vertices: array numpy con las posiciones (x,y,z) de los vértices
        - indices: array numpy con los índices de los triángulos
        """
        self.vertices = np.array(vertices, dtype=np.float32)
        self.indices = np.array(indices, dtype=np.uint32)
        self.numIndices = len(self.indices)
        self.setup_mesh()
        
    def setup_mesh(self):
        """
        Configura los buffers de OpenGL (VAO, VBO, EBO).
        VAO = Vertex Array Object (guarda configuración de atributos)
        VBO = Vertex Buffer Object (datos de vértices)
        EBO = Element Buffer Object (índices)
        """
        # Generar identificadores para los buffers
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)
        self.EBO = glGenBuffers(1)
        
        # Vincular VAO (todo lo siguiente se guardará en este VAO)
        glBindVertexArray(self.VAO)
        
        # Configurar VBO (buffer de vértices)
        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        
        # Configurar EBO (buffer de índices)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)
        
        # Especificar cómo interpretar los datos de vértices
        # Atributo 0: Posición (3 floats por vértice)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        
        # Desvincular VAO (buena práctica)
        glBindVertexArray(0)
        
    def draw(self):
        """Dibuja la malla usando los buffers configurados"""
        glBindVertexArray(self.VAO)
        glDrawElements(GL_TRIANGLES, self.numIndices, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)


def create_cube():
    """
    Crea un cubo unitario centrado en el origen.
    Tamaño: 1x1x1 (va de -0.5 a 0.5 en cada eje)
    """
    vertices = np.array([
        # Cara frontal (mirando hacia +Z)
        -0.5, -0.5,  0.5,  # 0: esquina inferior izquierda
         0.5, -0.5,  0.5,  # 1: esquina inferior derecha
         0.5,  0.5,  0.5,  # 2: esquina superior derecha
        -0.5,  0.5,  0.5,  # 3: esquina superior izquierda
        
        # Cara trasera (mirando hacia -Z)
        -0.5, -0.5, -0.5,  # 4
         0.5, -0.5, -0.5,  # 5
         0.5,  0.5, -0.5,  # 6
        -0.5,  0.5, -0.5,  # 7
    ], dtype=np.float32)
    
    # Índices: cada cara son 2 triángulos (6 índices)
    indices = np.array([
        # Cara frontal (+Z)
        0, 1, 2,  2, 3, 0,
        # Cara trasera (-Z)
        5, 4, 7,  7, 6, 5,
        # Cara izquierda (-X)
        4, 0, 3,  3, 7, 4,
        # Cara derecha (+X)
        1, 5, 6,  6, 2, 1,
        # Cara superior (+Y)
        3, 2, 6,  6, 7, 3,
        # Cara inferior (-Y)
        4, 5, 1,  1, 0, 4,
    ], dtype=np.uint32)
    
    return Mesh(vertices, indices)


def create_sphere(slices=20, stacks=20):
    """
    Crea una esfera usando coordenadas esféricas.
    
    Parámetros:
    - slices: divisiones horizontales (longitud)
    - stacks: divisiones verticales (latitud)
    
    La esfera tiene radio 0.5 (diámetro 1)
    """
    vertices = []
    indices = []
    
    # Generar vértices usando coordenadas esféricas
    # phi: ángulo desde el polo norte (0 a π)
    # theta: ángulo en el plano XZ (0 a 2π)
    for i in range(stacks + 1):
        phi = np.pi * i / stacks
        
        for j in range(slices + 1):
            theta = 2 * np.pi * j / slices
            
            # Convertir de esféricas a cartesianas
            x = np.sin(phi) * np.cos(theta)
            y = np.cos(phi)
            z = np.sin(phi) * np.sin(theta)
            
            # Escalar a radio 0.5
            vertices.extend([x * 0.5, y * 0.5, z * 0.5])
    
    # Generar índices para formar triángulos
    for i in range(stacks):
        for j in range(slices):
            # Vértices del "quad" actual
            first = i * (slices + 1) + j
            second = first + slices + 1
            
            # Primer triángulo del quad
            indices.extend([first, second, first + 1])
            # Segundo triángulo del quad
            indices.extend([second, second + 1, first + 1])
    
    return Mesh(np.array(vertices, dtype=np.float32), 
                np.array(indices, dtype=np.uint32))


def create_cylinder(slices=20):
    """
    Crea un cilindro con tapas.
    
    Parámetros:
    - slices: número de divisiones alrededor del círculo
    
    El cilindro tiene radio 0.5 y altura 1 (de -0.5 a 0.5 en Y)
    """
    vertices = []
    indices = []
    
    # Generar vértices de la pared lateral
    for i in range(slices + 1):
        theta = 2 * np.pi * i / slices
        x = np.cos(theta) * 0.5
        z = np.sin(theta) * 0.5
        
        # Para cada ángulo, crear dos vértices (arriba y abajo)
        vertices.extend([x, 0.5, z])   # Vértice superior
        vertices.extend([x, -0.5, z])  # Vértice inferior
    
    # Generar índices para la pared lateral
    for i in range(slices):
        base = i * 2
        # Primer triángulo de este segmento
        indices.extend([base, base + 1, base + 2])
        # Segundo triángulo de este segmento
        indices.extend([base + 1, base + 3, base + 2])
    
    # Agregar vértices centrales para las tapas
    center_top_idx = len(vertices) // 3
    vertices.extend([0, 0.5, 0])   # Centro de tapa superior
    
    center_bottom_idx = len(vertices) // 3
    vertices.extend([0, -0.5, 0])  # Centro de tapa inferior
    
    # Generar índices para las tapas
    for i in range(slices):
        base = i * 2
        
        # Tapa superior (triángulos que apuntan hacia arriba)
        indices.extend([center_top_idx, base, base + 2])
        
        # Tapa inferior (triángulos que apuntan hacia abajo)
        indices.extend([center_bottom_idx, base + 3, base + 1])
    
    return Mesh(np.array(vertices, dtype=np.float32), 
                np.array(indices, dtype=np.uint32))


def create_fish_simple():
    """
    Crea un pez simple usando formas geométricas básicas.
    Retorna una esfera (que luego se puede escalar para hacer forma de pez)
    """
    # Por ahora, un pez simple es una esfera escalada
    # Más adelante se puede hacer más elaborado
    return create_sphere(slices=12, stacks=8)


def create_aquarium_box(width=10.0, height=6.0, depth=8.0):
    """
    Crea una caja para el acuario (solo las aristas, sin caras completas).
    Retorna las líneas que definen las aristas del acuario.
    
    Parámetros:
    - width: ancho del acuario (eje X)
    - height: altura del acuario (eje Y)  
    - depth: profundidad del acuario (eje Z)
    """
    # Calcular dimensiones desde el centro
    w = width / 2.0
    h = height / 2.0
    d = depth / 2.0
    
    # Definir los 8 vértices de la caja
    vertices = np.array([
        # Cara frontal
        -w, -h,  d,  # 0: esquina inferior izquierda frontal
         w, -h,  d,  # 1: esquina inferior derecha frontal
         w,  h,  d,  # 2: esquina superior derecha frontal
        -w,  h,  d,  # 3: esquina superior izquierda frontal
        
        # Cara trasera
        -w, -h, -d,  # 4: esquina inferior izquierda trasera
         w, -h, -d,  # 5: esquina inferior derecha trasera
         w,  h, -d,  # 6: esquina superior derecha trasera
        -w,  h, -d,  # 7: esquina superior izquierda trasera
    ], dtype=np.float32)
    
    # Índices para las líneas (cada par define una arista)
    indices = np.array([
        # Aristas frontales
        0, 1,  1, 2,  2, 3,  3, 0,
        # Aristas traseras
        4, 5,  5, 6,  6, 7,  7, 4,
        # Aristas conectoras
        0, 4,  1, 5,  2, 6,  3, 7,
    ], dtype=np.uint32)
    
    return Mesh(vertices, indices)
