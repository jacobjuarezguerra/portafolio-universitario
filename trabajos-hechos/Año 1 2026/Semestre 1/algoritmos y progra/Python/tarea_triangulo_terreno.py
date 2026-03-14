# =============================================================================
# PSeudocódigo - Tarea: Triángulo Rectángulo y Terreno
# =============================================================================

# =============================================================================
# TAREA 1: Triángulo Rectángulo
# =============================================================================

"""
PSEUDOCÓDIGO - Triángulo Rectángulo

INICIO
    // Declarar variables
    DEFINIR base COMO ENTERO
    DEFINIR altura COMO ENTERO
    DEFINIR area COMO REAL
    
    // Solicitar dimensiones al usuario
    IMPRIMIR "Ingrese la base del triángulo rectángulo:"
    LEER base
    IMPRIMIR "Ingrese la altura del triángulo rectángulo:"
    LEER altura
    
    // Calcular el área
    area = (base * altura) / 2
    
    // Mostrar resultado
    IMPRIMIR "El área del triángulo rectángulo es: ", area
    
    // Dibujar con turtle
    // (Se implementa en Python)
    
FIN
"""

# =============================================================================
# TAREA 2: Terreno (Figura con dimensiones A, B, C)
# =============================================================================

"""
PSEUDOCÓDIGO - Área del Terreno

Se asume que la figura es un trapecio donde:
- A = base mayor
- B = base menor  
- C = altura

FÓRMULA: Área = ((A + B) / 2) * C

INICIO
    // Declarar variables
    DEFINIR A COMO ENTERO   // Base mayor
    DEFINIR B COMO ENTERO   // Base menor
    DEFINIR C COMO ENTERO   // Altura
    DEFINIR area COMO REAL
    
    // Asignar valores
    A = 400
    B = 200
    C = 300
    
    // Calcular el área del trapecio
    area = ((A + B) / 2) * C
    
    // Mostrar resultado
    IMPRIMIR "El área del terreno es: ", area
    
    // Dibujar con turtle
    // (Se implementa en Python)
    
FIN
"""

# =============================================================================
# IMPLEMENTACIÓN EN PYTHON - MÓDULO TURTLE
# =============================================================================

import turtle
import math

def dibujar_triangulo_rectangulo():
    """
    Dibuja un triángulo rectángulo y calcula su área
    """
    # Configuración de la ventana
    ventana = turtle.Screen()
    ventana.title("Triángulo Rectángulo - Cálculo de Área")
    ventana.bgcolor("white")
    
    # Crear la tortuga
    tortuga = turtle.Turtle()
    tortuga.speed(2)
    tortuga.pensize(3)
    tortuga.color("blue")
    
    # Dimensiones del triángulo
    base = 200
    altura = 150
    
    # Calcular el área
    area = (base * altura) / 2
    
    # Dibujar el triángulo rectángulo
    # vértice inferior izquierdo en el centro
    tortuga.penup()
    tortuga.goto(-100, -50)
    tortuga.pendown()
    
    # Lado 1: base (horizontal)
    tortuga.forward(base)
    
    # Lado 2: altura (vertical)
    tortuga.left(90)
    tortuga.forward(altura)
    
    # Lado 3: hipotenusa
    tortuga.goto(-100, -50)
    
    # Marcar el ángulo recto
    tortuga.penup()
    tortuga.goto(-100, -50)
    tortuga.pendown()
    tortuga.dot(10, "red")
    
    # Escribir el área en pantalla
    tortuga.penup()
    tortuga.goto(0, 100)
    tortuga.color("black")
    tortuga.write(f"Área del Triángulo Rectángulo: {area}", 
                  align="center", font=("Arial", 14, "bold"))
    
    # Información adicional
    tortuga.goto(0, 70)
    tortuga.write(f"Base: {base} | Altura: {altura}", 
                  align="center", font=("Arial", 10, "normal"))
    
    # Mantener la ventana abierta
    ventana.mainloop()


def dibujar_terreno():
    """
    Dibuja el terreno (trapecio) con A=400, B=300, C=200
    y calcula su área
    
    Nota: El terreno se dibuja como un trapecio donde:
    - A = 400 (base mayor)
    - B = 300 (base menor)  
    - C = 200 (altura)
    
    Según el enunciado: A=400, B=300, C=200
    """
    # Configuración de la ventana
    ventana = turtle.Screen()
    ventana.title("Terreno - Cálculo de Área")
    ventana.bgcolor("lightgreen")
    
    # Crear la tortuga
    tortuga = turtle.Turtle()
    tortuga.speed(3)
    tortuga.pensize(3)
    tortuga.color("darkgreen")
    
    # Dimensiones del terreno (según enunciado)
    A = 400  # Base mayor
    B = 300  # Base menor
    C = 200  # Altura
    
    # Calcular el área del trapecio
    # Fórmula: ((A + B) / 2) * C
    area = ((A + B) / 2) * C
    
    # Centrar el dibujo
    inicio_x = -A // 2
    inicio_y = 50
    
    # Dibujar el trapecio (terreno)
    tortuga.penup()
    tortuga.goto(inicio_x, inicio_y)
    tortuga.pendown()
    
    # Lado 1: base mayor (A)
    tortuga.forward(A)
    
    # Lado 2: lado inclinado derecho
    # Para hacer la figura más realista, dibujamos los lados inclinados
    tortuga.goto(inicio_x + (A - B) // 2 + B, inicio_y - C)
    
    # Lado 3: base menor (B)
    tortuga.forward(B)
    
    # Lado 4: lado inclinado izquierdo
    tortuga.goto(inicio_x, inicio_y)
    
    # Rellenar el terreno
    tortuga.fillcolor("lightgreen")
    tortuga.begin_fill()
    tortuga.goto(inicio_x + A, inicio_y)
    tortuga.goto(inicio_x + (A - B) // 2 + B, inicio_y - C)
    tortuga.goto(inicio_x + (A - B) // 2, inicio_y - C)
    tortuga.goto(inicio_x, inicio_y)
    tortuga.end_fill()
    
    # Escribir las dimensiones en el dibujo
    tortuga.penup()
    tortuga.color("black")
    
    # Etiqueta de la base mayor (A)
    tortuga.goto(inicio_x + A/2, inicio_y + 20)
    tortuga.write(f"A = {A}", align="center", font=("Arial", 10, "bold"))
    
    # Etiqueta de la base menor (B)
    tortuga.goto(inicio_x + (A - B) // 2 + B/2, inicio_y - C - 20)
    tortuga.write(f"B = {B}", align="center", font=("Arial", 10, "bold"))
    
    # Etiqueta de la altura (C)
    tortuga.goto(inicio_x + A + 30, inicio_y - C/2)
    tortuga.write(f"C = {C}", align="left", font=("Arial", 10, "bold"))
    
    # Escribir el área en pantalla (destacado)
    tortuga.goto(0, -200)
    tortuga.color("darkred")
    tortuga.write(f"ÁREA DEL TERRENO: {area} unidades²", 
                  align="center", font=("Arial", 16, "bold"))
    
    # Fórmula utilizada
    tortuga.goto(0, -230)
    tortuga.color("blue")
    tortuga.write(f"Fórmula: ((A + B) / 2) × C = (({A} + {B}) / 2) × {C}", 
                  align="center", font=("Arial", 12, "normal"))
    
    # Mantener la ventana abierta
    ventana.mainloop()


# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def menu_principal():
    """
    Muestra un menú para seleccionar qué figura dibujar
    """
    print("=" * 60)
    print("       MENÚ - DIBUJO DE FIGURAS CON TURTLE")
    print("=" * 60)
    print("1. Triángulo Rectángulo (con área)")
    print("2. Terreno (trapecio con A=400, B=300, C=200)")
    print("3. Ambas figuras")
    print("4. Salir")
    print("=" * 60)
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        print("\n--- TRIÁNGULO RECTÁNGULO ---")
        print("Base: 200, Altura: 150")
        print("Área: (200 × 150) / 2 = 15000/2 = 15000")
        print("Ejecutando dibujo...")
        dibujar_triangulo_rectangulo()
    elif opcion == "2":
        print("\n--- TERRENO ---")
        print("A = 400, B = 300, C = 200")
        print("Área: ((400 + 300) / 2) × 200 = (700/2) × 200 = 350 × 200 = 70000")
        print("Ejecutando dibujo...")
        dibujar_terreno()
    elif opcion == "3":
        print("\n--- AMBAS FIGURAS ---")
        print("Primero se mostrará el triángulo rectángulo...")
        dibujar_triangulo_rectangulo()
        print("Ahora se mostrará el terreno...")
        dibujar_terreno()
    else:
        print("¡Hasta luego!")


# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
