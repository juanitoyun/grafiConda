# coding=utf-8
"""
Matrices de transformación para gráfica computacional.
Incluye funciones para rotación, traslación, escala y proyección.
"""

import numpy as np

def identity():
    """Matriz identidad 4x4"""
    return np.identity(4, dtype=np.float32)

def uniformScale(s):
    """Escala uniforme en todas las dimensiones"""
    return np.array([
        [s,0,0,0],
        [0,s,0,0],
        [0,0,s,0],
        [0,0,0,1]], dtype = np.float32)

def scale(sx, sy, sz):
    """Escala independiente en x, y, z"""
    return np.array([
        [sx,0,0,0],
        [0,sy,0,0],
        [0,0,sz,0],
        [0,0,0,1]], dtype = np.float32)

def rotationX(theta):
    """Rotación alrededor del eje X (en radianes)"""
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [1,0,0,0],
        [0,cos_theta,-sin_theta,0],
        [0,sin_theta,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)

def rotationY(theta):
    """Rotación alrededor del eje Y (en radianes)"""
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [cos_theta,0,sin_theta,0],
        [0,1,0,0],
        [-sin_theta,0,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)

def rotationZ(theta):
    """Rotación alrededor del eje Z (en radianes)"""
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [cos_theta,-sin_theta,0,0],
        [sin_theta,cos_theta,0,0],
        [0,0,1,0],
        [0,0,0,1]], dtype = np.float32)

def translate(tx, ty, tz):
    """Traslación en x, y, z"""
    return np.array([
        [1,0,0,tx],
        [0,1,0,ty],
        [0,0,1,tz],
        [0,0,0,1]], dtype = np.float32)

def matmul(mats):
    """
    Multiplica una lista de matrices en orden.
    Ejemplo: matmul([T, R, S]) = T * R * S
    """
    out = mats[0]
    for i in range(1, len(mats)):
        out = np.matmul(out, mats[i])
    return out

def perspective(fovy, aspect, near, far):
    """
    Crea matriz de proyección perspectiva.
    
    Parámetros:
    - fovy: campo de visión vertical en grados
    - aspect: relación de aspecto (ancho/alto)
    - near: plano cercano de recorte
    - far: plano lejano de recorte
    """
    halfHeight = np.tan(np.pi * fovy / 360) * near
    halfWidth = halfHeight * aspect
    return frustum(-halfWidth, halfWidth, -halfHeight, halfHeight, near, far)

def frustum(left, right, bottom, top, near, far):
    """Crea un frustum de proyección (utilizado por perspective)"""
    r_l = right - left
    t_b = top - bottom
    f_n = far - near
    return np.array([
        [ 2 * near / r_l,              0, (right + left) / r_l,                      0],
        [ 0             , 2 * near / t_b, (top + bottom) / t_b,                      0],
        [ 0             ,              0,  -(far + near) / f_n, -2 * near * far / f_n],
        [ 0             ,              0,                    -1,                      0]], 
        dtype = np.float32)

def lookAt(eye, at, up):
    """
    Crea matriz de vista (View Matrix).
    
    Parámetros:
    - eye: posición de la cámara (array de 3 elementos)
    - at: punto al que mira la cámara
    - up: vector "arriba" de la cámara
    """
    forward = (eye - at)
    forward = forward / np.linalg.norm(forward)
    
    side = np.cross(up, forward)
    side = side / np.linalg.norm(side)
    
    newUp = np.cross(forward, side)
    
    return np.array([
        [   side[0],    side[1],    side[2],    -np.dot(side, eye)],
        [  newUp[0],   newUp[1],   newUp[2],   -np.dot(newUp, eye)],
        [forward[0], forward[1], forward[2], -np.dot(forward, eye)],
        [         0,          0,          0,                      1]
    ], dtype = np.float32)
