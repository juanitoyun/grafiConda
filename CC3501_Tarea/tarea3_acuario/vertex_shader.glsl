#version 330 core

// Atributo de entrada: posición del vértice
layout (location = 0) in vec3 aPos;

// Matrices de transformación (uniformes = constantes para todos los vértices)
uniform mat4 model;       // Transformación del objeto (posición, rotación, escala)
uniform mat4 view;        // Transformación de la cámara
uniform mat4 projection;  // Proyección perspectiva

// Variable de salida que se pasa al fragment shader
out vec3 fragPos;  // Posición del fragmento en coordenadas del mundo

void main()
{
    // Calcular posición en coordenadas del mundo (aplicando solo model)
    fragPos = vec3(model * vec4(aPos, 1.0));
    
    // Posición final del vértice en coordenadas de pantalla
    // Se aplican todas las transformaciones: projection * view * model
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
