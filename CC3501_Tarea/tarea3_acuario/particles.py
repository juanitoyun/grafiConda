"""
Sistema de partículas para simular burbujas en el acuario.

Las burbujas:
- Nacen en el fondo del acuario
- Flotan hacia arriba (fuerza de flotación)
- Tienen movimiento oscilante (simulando corrientes)
- Desaparecen al llegar a la superficie o después de cierto tiempo
"""

import numpy as np


class Particle:
    """
    Una partícula individual (una burbuja).
    """
    
    def __init__(self, position, size=0.1):
        """
        Constructor de partícula.
        
        Parámetros:
        - position: posición inicial [x, y, z]
        - size: tamaño de la partícula
        """
        self.position = np.array(position, dtype=np.float32)
        
        # Velocidad inicial (pequeña variación aleatoria)
        self.velocity = np.array([
            np.random.uniform(-0.2, 0.2),  # Movimiento horizontal aleatorio
            np.random.uniform(0.5, 1.5),    # Flotación hacia arriba
            np.random.uniform(-0.2, 0.2)   # Movimiento en profundidad
        ], dtype=np.float32)
        
        # Tamaño de la burbuja
        self.size = size
        
        # Tiempo de vida (en segundos)
        self.lifetime = np.random.uniform(3.0, 6.0)
        self.age = 0.0
        
        # Fase para movimiento oscilante (cada burbuja oscila diferente)
        self.oscillationPhase = np.random.uniform(0, 2 * np.pi)
        
        # Está viva?
        self.alive = True
    
    def update(self, dt):
        """
        Actualiza la partícula.
        
        Parámetros:
        - dt: delta time
        """
        if not self.alive:
            return
        
        # Incrementar edad
        self.age += dt
        
        # Si superó su tiempo de vida, morir
        if self.age > self.lifetime:
            self.alive = False
            return
        
        # Aplicar fuerzas
        
        # 1. Fuerza de flotación (hacia arriba)
        buoyancy = np.array([0, 1.5, 0], dtype=np.float32)
        
        # 2. Resistencia del agua (frenar la burbuja)
        drag = -self.velocity * 0.1
        
        # 3. Movimiento oscilante (simula corrientes de agua)
        oscillation = np.array([
            0.3 * np.sin(self.age * 2.0 + self.oscillationPhase),
            0,
            0.3 * np.cos(self.age * 1.5 + self.oscillationPhase)
        ], dtype=np.float32)
        
        # Sumar todas las fuerzas
        acceleration = buoyancy + drag + oscillation
        
        # Actualizar velocidad y posición
        self.velocity += acceleration * dt
        self.position += self.velocity * dt


class ParticleSystem:
    """
    Sistema que maneja múltiples partículas (el sistema de burbujas completo).
    """
    
    def __init__(self, emissionRate, bounds):
        """
        Constructor del sistema de partículas.
        
        Parámetros:
        - emissionRate: partículas generadas por segundo
        - bounds: límites del acuario ((min_xyz), (max_xyz))
        """
        self.particles = []
        self.emissionRate = emissionRate
        self.bounds = bounds
        
        # Contador para emisión
        self.timeSinceLastEmission = 0.0
        
        # Intervalo entre emisiones (en segundos)
        self.emissionInterval = 1.0 / emissionRate if emissionRate > 0 else 0
    
    def update(self, dt):
        """
        Actualiza el sistema de partículas.
        
        Parámetros:
        - dt: delta time
        """
        # Actualizar partículas existentes
        for particle in self.particles:
            particle.update(dt)
        
        # Eliminar partículas muertas o fuera de límites
        self.particles = [p for p in self.particles if p.alive and self._is_in_bounds(p)]
        
        # Emitir nuevas partículas
        self.timeSinceLastEmission += dt
        
        if self.timeSinceLastEmission >= self.emissionInterval:
            self._emit_particle()
            self.timeSinceLastEmission = 0.0
    
    def _emit_particle(self):
        """
        Emite una nueva partícula desde el fondo del acuario.
        """
        minBounds, maxBounds = self.bounds
        
        # Posición aleatoria en el fondo del acuario
        position = np.array([
            np.random.uniform(minBounds[0] + 1, maxBounds[0] - 1),  # X aleatorio
            minBounds[1] + 0.5,  # En el fondo (Y mínimo)
            np.random.uniform(minBounds[1] + 1, maxBounds[2] - 1)   # Z aleatorio
        ], dtype=np.float32)
        
        # Tamaño aleatorio de burbuja
        size = np.random.uniform(0.05, 0.15)
        
        # Crear y agregar partícula
        particle = Particle(position, size)
        self.particles.append(particle)
    
    def _is_in_bounds(self, particle):
        """
        Verifica si una partícula está dentro de los límites del acuario.
        
        Parámetros:
        - particle: la partícula a verificar
        
        Retorna:
        - True si está dentro, False si salió
        """
        minBounds, maxBounds = self.bounds
        pos = particle.position
        
        # Verificar cada eje
        if pos[0] < minBounds[0] or pos[0] > maxBounds[0]:
            return False
        if pos[1] < minBounds[1] or pos[1] > maxBounds[1]:
            return False
        if pos[2] < minBounds[2] or pos[2] > maxBounds[2]:
            return False
        
        return True
    
    def get_particles_data(self):
        """
        Retorna datos de las partículas para renderizar.
        
        Retorna:
        - Lista de tuplas (posición, tamaño, alpha)
        """
        data = []
        
        for particle in self.particles:
            # Calcular transparencia basada en la edad
            # Las burbujas se vuelven más transparentes al envejecer
            alpha = 1.0 - (particle.age / particle.lifetime)
            
            data.append((particle.position, particle.size, alpha))
        
        return data
