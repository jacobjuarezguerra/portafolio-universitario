# Algoritmo para calcular el precio de impresión de páginas
# Precio por página: 0.5 centavos (quetzales)
# Descuento con tarjeta: 10%

PRECIO_POR_PAGINA = 0.5  # 0.5 centavos por página
DESCUENTO_TARJETA = 0.10  # 10% de descuento

def calcular_precio(cantidad_paginas, pago_tarjeta=False):
    """
    Calcula el precio total de impresión
    
    Args:
        cantidad_paginas: Número de páginas a imprimir
        pago_tarjeta: True si paga con tarjeta, False si paga en efectivo
    
    Returns:
        Diccionario con los detalles del cálculo
    """
    # Calcular precio base (sin descuento)
    precio_base = cantidad_paginas * PRECIO_POR_PAGINA
    
    # Aplicar descuento si paga con tarjeta
    if pago_tarjeta:
        descuento = precio_base * DESCUENTO_TARJETA
        precio_final = precio_base - descuento
    else:
        descuento = 0
        precio_final = precio_base
    
    return {
        "paginas": cantidad_paginas,
        "precio_por_pagina": PRECIO_POR_PAGINA,
        "precio_base": precio_base,
        "descuento": descuento,
        "precio_final": precio_final,
        "metodo_pago": "Tarjeta" if pago_tarjeta else "Efectivo"
    }

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo 1: 10 páginas, pago en efectivo
    resultado1 = calcular_precio(10, pago_tarjeta=False)
    print("=" * 40)
    print("CÁLCULO DE PRECIO DE IMPRESIÓN")
    print("=" * 40)
    print(f"Cantidad de páginas: {resultado1['paginas']}")
    print(f"Precio por página: Q{resultado1['precio_por_pagina']:.2f}")
    print(f"Método de pago: {resultado1['metodo_pago']}")
    print("-" * 40)
    print(f"Precio base: Q{resultado1['precio_base']:.2f}")
    print(f"Descuento (10%): -Q{resultado1['descuento']:.2f}")
    print(f"PRECIO FINAL: Q{resultado1['precio_final']:.2f}")
    print("=" * 40)
    
    print()  # Línea vacía
    
    # Ejemplo 2: 10 páginas, pago con tarjeta (con oferta)
    resultado2 = calcular_precio(10, pago_tarjeta=True)
    print("=" * 40)
    print("CÁLCULO DE PRECIO DE IMPRESIÓN")
    print("=" * 40)
    print(f"Cantidad de páginas: {resultado2['paginas']}")
    print(f"Precio por página: Q{resultado2['precio_por_pagina']:.2f}")
    print(f"Método de pago: {resultado2['metodo_pago']} (OFERTA APLICADA)")
    print("-" * 40)
    print(f"Precio base: Q{resultado2['precio_base']:.2f}")
    print(f"Descuento (10%): -Q{resultado2['descuento']:.2f}")
    print(f"PRECIO FINAL: Q{resultado2['precio_final']:.2f}")
    print("=" * 40)
    
    print()
    
    # Programa interactivo
    print("Programa interactivo de impresión")
    print("-" * 40)
    try:
        paginas = int(input("Ingrese la cantidad de páginas: "))
        if paginas < 0:
            print("Error: La cantidad de páginas no puede ser negativa")
        else:
            print("\nMétodo de pago:")
            print("1. Efectivo")
            print("2. Tarjeta (10% de descuento)")
            opcion = input("Seleccione opción (1/2): ")
            
            if opcion == "1":
                resultado = calcular_precio(paginas, pago_tarjeta=False)
            elif opcion == "2":
                resultado = calcular_precio(paginas, pago_tarjeta=True)
            else:
                print("Opción inválida, se cancela la operación")
            
            if opcion in ["1", "2"]:
                print("\n" + "=" * 40)
                print("RECIBO DE IMPRESIÓN")
                print("=" * 40)
                print(f"Cantidad de páginas: {resultado['paginas']}")
                print(f"Precio por página: Q{resultado['precio_por_pagina']:.2f}")
                print(f"Método de pago: {resultado['metodo_pago']}")
                print("-" * 40)
                print(f"Subtotal: Q{resultado['precio_base']:.2f}")
                if resultado['descuento'] > 0:
                    print(f"Descuento ({int(DESCUENTO_TARJETA*100)}%): -Q{resultado['descuento']:.2f}")
                print(f"TOTAL A PAGAR: Q{resultado['precio_final']:.2f}")
                print("=" * 40)
    except ValueError:
        print("Error: Por favor ingrese un número válido de páginas")
