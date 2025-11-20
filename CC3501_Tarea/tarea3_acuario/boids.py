"""
Sistema de Boids para simular comportamiento de cardumen de peces.

Los boids siguen 3 reglas simples que generan comportamiento emergente:
1. SEPARACIÓN: Evitar chocar con vecinos cercanos
2. COHESIÓN: Moverse hacia el centro del grupo
3. ALINEACIÓN: Igualar la velocidad/dirección de los vecinos

Basado en el algoritmo de Craig Reynolds (1986).
"""

import numpy as np


class Boid:
    """
    Un boid individual (un pez en nuestro caso).
    Cada boid tiene posición, velocidad y sigue las reglas del grupo.
    """
    
    def __init__(self, position, velocity, bounds):
        """
        Constructor de un boid.
        
        Parámetros:
        - position: posición inicial [x, y, z]
        - velocity: velocidad inicial [vx, vy, vz]
        - bounds: límites del espacio (min_xyz, max_xyz)
        """
        self.position = np.array(position, dtype=np.float32)
        self.velocity = np.array(velocity, dtype=np.float32)
        self.bounds = bounds  # Tupla ((min_x, min_y, min_z), (max_x, max_y, max_z))
        
        # Parámetros de comportamiento (se pueden ajustar)
        self.maxSpeed = 2.0          # Velocidad máxima
        self.maxForce = 0.05         # Fuerza máxima que puede aplicar
        
        # Radios de percepción
        self.separationRadius = 1.0  # Distancia mínima con otros peces
        self.alignRadius = 2.5       # Radio para alinearse con vecinos
        self.cohesionRadius = 2.5    # Radio para cohesión con el grupo
        
        # Pesos de las reglas (ajustar para cambiar el comportamiento)
        self.separationWeight = 1.5
        self.alignWeight = 1.0
        self.cohesionWeight = 1.0
    
    def update(self, dt, allBoids):
        """
        Actualiza la posición y velocidad del boid.
        
        Parámetros:
        - dt: delta time (tiempo transcurrido desde último frame)
        - allBoids: lista de todos los boids (para calcular vecinos)
        """
        # Encontrar vecinos cercanos
        neighbors = self._find_neighbors(allBoids)
        
        # Calcular fuerzas según las reglas de boids
        separation = self._separate(neighbors) * self.separationWeight
        alignment = self._align(neighbors) * self.alignWeight
        cohesion = self._cohere(neighbors) * self.cohesionWeight
        
        # Sumar todas las fuerzas
        acceleration = separation + alignment + cohesion
        
        # Aplicar fuerza de contención (mantener dentro del acuario)
        acceleration += self._contain_in_bounds()
        
        # Actualizar velocidad
        self.velocity += acceleration
        
        # Limitar velocidad máxima
        speed = np.linalg.norm(self.velocity)
        if speed > self.maxSpeed:
            self.velocity = (self.velocity / speed) * self.maxSpeed
        
        # Actualizar posición
        self.position += self.velocity * dt
    
    def _find_neighbors(self, allBoids):
        """
        Encuentra boids vecinos dentro del radio de percepción.
        
        Retorna:
        - Lista de boids cercanos (excluyendo a sí mismo)
        """
        neighbors = []
        maxRadius = max(self.separationRadius, self.alignRadius, self.cohesionRadius)
        
        for other in allBoids:
            if other is self:  # No incluirse a sí mismo
                continue
            
            distance = np.linalg.norm(self.position - other.position)
            
            # Solo considerar boids dentro del radio máximo
            if distance < maxRadius:
                neighbors.append(other)
        
        return neighbors
    
    def _separate(self, neighbors):
        """
        Regla 1: SEPARACIÓN
        Genera fuerza para alejarse de vecinos muy cercanos.
        Evita colisiones entre peces.
        """
        steer = np.zeros(3, dtype=np.float32)
        count = 0
        
        for other in neighbors:
            distance = np.linalg.norm(self.position - other.position)
            
            # Solo aplicar a vecinos MUY cercanos
            if distance < self.separationRadius and distance > 0:
                # Vector que apunta LEJOS del vecino
                diff = self.position - other.position
                diff = diff / distance  # Normalizar
                diff = diff / distance  # Ponderar por distancia (más cerca = más fuerza)
                
                steer += diff
                count += 1
        
        # Promediar
        if count > 0:
            steer = steer / count
        
        # Convertir a fuerza de dirección
        if np.linalg.norm(steer) > 0:
            steer = self._limit_force(steer)
        
        return steer
    
    def _align(self, neighbors):
        """
        Regla 2: ALINEACIÓN
        Igualar la velocidad/dirección con los vecinos.
        Hace que el grupo se mueva de forma coordinada.
        """
        avgVelocity = np.zeros(3, dtype=np.float32)
        count = 0
        
        for other in neighbors:
            distance = np.linalg.norm(self.position - other.position)
            
            if distance < self.alignRadius:
                avgVelocity += other.velocity
                count += 1
        
        if count > 0:
            # Calcular velocidad promedio de los vecinos
            avgVelocity = avgVelocity / count
            
            # Calcular fuerza necesaria para igualar esa velocidad
            steer = avgVelocity - self.velocity
            steer = self._limit_force(steer)
            return steer
        
        return np.zeros(3, dtype=np.float32)
    
    def _cohere(self, neighbors):
        """
        Regla 3: COHESIÓN
        Moverse hacia el centro de masa del grupo.
        Mantiene al grupo unido.
        """
        centerOfMass = np.zeros(3, dtype=np.float32)
        count = 0
        
        for other in neighbors:
            distance = np.linalg.norm(self.position - other.position)
            
            if distance < self.cohesionRadius:
                centerOfMass += other.position
                count += 1
        
        if count > 0:
            # Calcular centro de masa
            centerOfMass = centerOfMass / count
            
            # Calcular dirección hacia el centro
            desired = centerOfMass - self.position
            
            if np.linalg.norm(desired) > 0:
                # Normalizar y ajustar a velocidad máxima
                desired = (desired / np.linalg.norm(desired)) * self.maxSpeed
                
                # Calcular fuerza de dirección
                steer = desired - self.velocity
                steer = self._limit_force(steer)
                return steer
        
        return np.zeros(3, dtype=np.float32)
    
    def _contain_in_bounds(self):
        """
        Genera fuerzas para mantener al boid dentro del acuario.
        Cuando se acerca a los bordes, aplica una fuerza de repulsión.
        """
        force = np.zeros(3, dtype=np.float32)
        minBounds, maxBounds = self.bounds
        
        # Margen desde el borde donde empieza a repeler
        margin = 1.0
        
        # Fuerza de contención para cada eje
        for i in range(3):  # x, y, z
            # Si está muy cerca del límite inferior
            if self.position[i] < minBounds[i] + margin:
                distance = self.position[i] - minBounds[i]
                force[i] = (margin - distance) * 0.5
            
            # Si está muy cerca del límite superior
            elif self.position[i] > maxBounds[i] - margin:
                distance = maxBounds[i] - self.position[i]
                force[i] = -(margin - distance) * 0.5
        
        return force
    
    def _limit_force(self, force):
        """
        Limita la magnitud de una fuerza al máximo permitido.
        Evita cambios bruscos de dirección.
        """
        magnitude = np.linalg.norm(force)
        
        if magnitude > self.maxForce:
            return (force / magnitude) * self.maxForce
        
        return force


class BoidSystem:
    """
    Sistema que maneja múltiples boids (el cardumen completo).
    """
    
    def __init__(self, numBoids, bounds):
        """
        Constructor del sistema de boids.
        
        Parámetros:
        - numBoids: cantidad de peces a crear
        - bounds: límites del espacio ((min_xyz), (max_xyz))
        """
        self.boids = []
        self.bounds = bounds
        
        # Crear boids con posiciones y velocidades aleatorias
        minBounds, maxBounds = bounds
        
        for i in range(numBoids):
            # Posición aleatoria dentro de los límites
            position = np.array([
                np.random.uniform(minBounds[0], maxBounds[0]),
                np.random.uniform(minBounds[1], maxBounds[1]),
                np.random.uniform(minBounds[2], maxBounds[2])
            ], dtype=np.float32)
            
            # Velocidad aleatoria inicial
            velocity = np.array([
                np.random.uniform(-1, 1),
                np.random.uniform(-1, 1),
                np.random.uniform(-1, 1)
            ], dtype=np.float32)
            
            # Normalizar velocidad a una magnitud razonable
            if np.linalg.norm(velocity) > 0:
                velocity = (velocity / np.linalg.norm(velocity)) * 1.0
            
            self.boids.append(Boid(position, velocity, bounds))
    
    def update(self, dt):
        """
        Actualiza todos los boids del sistema.
        
        Parámetros:
        - dt: delta time
        """
        for boid in self.boids:
            boid.update(dt, self.boids)
    
    def get_positions(self):
        """
        Retorna las posiciones de todos los boids.
        Útil para renderizar.
        """
        return [boid.position for boid in self.boids]
    
    def get_velocities(self):
        """
        Retorna las velocidades de todos los boids.
        Útil para orientar los modelos de peces.
        """
        return [boid.velocity for boid in self.boids]
