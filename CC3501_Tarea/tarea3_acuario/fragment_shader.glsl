#version 330 core

// Variable de entrada desde el vertex shader
in vec3 fragPos;  // Posición del fragmento en coordenadas del mundo

// Variable de salida: color final del pixel
out vec4 FragColor;

// Uniformes: parámetros que podemos cambiar desde el código Python
uniform vec3 color;     // Color base del objeto
uniform vec3 lightPos;  // Posición de la luz
uniform vec3 viewPos;   // Posición de la cámara

void main()
{
    FragColor = vec4(1.0, 1.0, 1.0, 1.0); // SIEMPRE BLANCO
}
