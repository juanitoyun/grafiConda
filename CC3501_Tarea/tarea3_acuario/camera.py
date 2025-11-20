"""
Sistema de cámara interactiva basado en Arcball.
Permite rotar la cámara con el mouse y hacer zoom con la rueda.

Este sistema es CRÍTICO según la retroalimentación del profesor.
"""

import numpy as np
from . import transformations as tr


class ArcballCamera:
    """
    Cámara orbital que permite rotar alrededor de un punto usando el mouse.
    
    Conceptos clave:
    - El usuario "arrastra" el mouse y la cámara rota alrededor del objeto
    - El scroll del mouse acerca/aleja la cámara
    - Siempre mira hacia un punto central (target)
    """
    
    # Estados de interacción
    STATE_ROTATE = 0   # Rotando alrededor del objeto
    STATE_PAN = 1      # Moviendo lateralmente
    STATE_ZOOM = 2     # Acercando/alejando
    
    def __init__(self, target, distance, windowSize):
        """
        Constructor de la cámara arcball.
        
        Parámetros:
        - target: punto hacia el que mira la cámara (array [x, y, z])
        - distance: distancia inicial desde el target
        - windowSize: tupla (ancho, alto) de la ventana
        """
        # Punto central que la cámara siempre mira
        self.target = np.array(target, dtype=np.float32)
        
        # Distancia desde el target (para zoom)
        self.distance = distance
        
        # Tamaño de la ventana (para mapear coordenadas del mouse)
        self.windowSize = np.array(windowSize, dtype=np.float32)
        
        # Ángulos de rotación (en radianes)
        self.theta = 0.0  # Ángulo horizontal (rotación alrededor de Y)
        self.phi = np.pi / 4.0  # Ángulo vertical (elevación)
        
        # Estado actual de interacción
        self.state = self.STATE_ROTATE
        
        # Última posición del mouse (para calcular deltas)
        self.lastMousePos = np.array([0, 0], dtype=np.float32)
        
        # Bandera para saber si estamos arrastrando
        self.isDragging = False
        
    def get_position(self):
        """
        Calcula la posición de la cámara en coordenadas esféricas.
        
        Usa los ángulos theta y phi para posicionar la cámara
        alrededor del target a una distancia fija.
        """
        # Convertir de coordenadas esféricas a cartesianas
        x = self.distance * np.sin(self.phi) * np.cos(self.theta)
        y = self.distance * np.cos(self.phi)
        z = self.distance * np.sin(self.phi) * np.sin(self.theta)
        
        # Sumar el target para obtener posición absoluta
        return self.target + np.array([x, y, z], dtype=np.float32)
    
    def get_view_matrix(self):
        """
        Genera la matriz de vista (View Matrix) para OpenGL.
        Esta matriz transforma coordenadas del mundo a coordenadas de cámara.
        """
        eye = self.get_position()  # Posición de la cámara
        at = self.target            # Punto al que mira
        up = np.array([0, 1, 0], dtype=np.float32)  # Vector "arriba"
        
        return tr.lookAt(eye, at, up)
    
    def on_mouse_press(self, x, y, button):
        """
        Manejador para cuando se presiona un botón del mouse.
        
        Parámetros:
        - x, y: posición del mouse en pixels
        - button: qué botón se presionó (LEFT=1, MIDDLE=2, RIGHT=4)
        """
        # Guardar posición inicial del mouse
        self.lastMousePos = np.array([x, y], dtype=np.float32)
        self.isDragging = True
        
        # Determinar qué acción realizar según el botón
        if button == 1:  # Botón izquierdo = rotar
            self.state = self.STATE_ROTATE
        elif button == 4:  # Botón derecho = pan (mover lateralmente)
            self.state = self.STATE_PAN
        elif button == 2:  # Botón central = zoom
            self.state = self.STATE_ZOOM
    
    def on_mouse_release(self, x, y, button):
        """Manejador para cuando se suelta un botón del mouse"""
        self.isDragging = False
    
    def on_mouse_drag(self, x, y, dx, dy):
        """
        Manejador para cuando se arrastra el mouse.
        
        Parámetros:
        - x, y: posición actual del mouse
        - dx, dy: cambio desde la última posición
        """
        if not self.isDragging:
            return
        
        # Sensibilidad del mouse (ajustar para hacer más rápido/lento)
        sensitivity = 0.005
        
        if self.state == self.STATE_ROTATE:
            # Rotar la cámara
            # dx afecta la rotación horizontal (theta)
            self.theta -= dx * sensitivity
            
            # dy afecta la rotación vertical (phi)
            self.phi -= dy * sensitivity
            
            # Limitar phi para evitar que la cámara se voltee
            # Mantener entre 0.1 y π - 0.1 radianes
            self.phi = np.clip(self.phi, 0.1, np.pi - 0.1)
            
        elif self.state == self.STATE_PAN:
            # Mover el target lateralmente
            # Calcular vectores derecha y arriba de la cámara
            viewDir = self.target - self.get_position()
            viewDir = viewDir / np.linalg.norm(viewDir)
            
            up = np.array([0, 1, 0], dtype=np.float32)
            right = np.cross(viewDir, up)
            right = right / np.linalg.norm(right)
            
            actualUp = np.cross(right, viewDir)
            
            # Mover el target
            panSensitivity = 0.01
            self.target += right * (-dx * panSensitivity)
            self.target += actualUp * (dy * panSensitivity)
        
        # Actualizar última posición del mouse
        self.lastMousePos = np.array([x, y], dtype=np.float32)
    
    def on_mouse_scroll(self, scrollX, scrollY):
        """
        Manejador para el scroll del mouse (rueda).
        Controla el zoom (acercar/alejar la cámara).
        
        Parámetros:
        - scrollY: dirección del scroll (positivo = hacia arriba)
        """
        # Sensibilidad del zoom
        zoomSensitivity = 0.5
        
        # Modificar la distancia según el scroll
        self.distance -= scrollY * zoomSensitivity
        
        # Limitar la distancia para evitar que la cámara entre al objeto
        # o se aleje demasiado
        self.distance = np.clip(self.distance, 1.0, 50.0)
    
    def reset(self):
        """Reinicia la cámara a su posición inicial"""
        self.theta = 0.0
        self.phi = np.pi / 4.0
        self.distance = 15.0
        self.target = np.array([0, 0, 0], dtype=np.float32)
