boleto = 750
patrocinio = 0.30

print("Elige ciudad:")
print("1. Ciudad de México")
print("2. Guadalajara")
print("3. Monterrey")

opcion = input("Opción: ")
presupuesto = float(input("Ingresa tu presupuesto: "))


if opcion == "1":
    vuelo = 250
    hotel = 130 * 3      
    comida = 35 * 4     
    ciudad = "Ciudad de México"

elif opcion == "2":
    vuelo = 300
    hotel = 45 * 3
    comida = 30 * 4
    ciudad = "Guadalajara"

elif opcion == "3":
    vuelo = 320
    hotel = 75 * 3
    comida = 35 * 4
    ciudad = "Monterrey"

else:
    print("Opción incorrecta")
    quit()


total = boleto + vuelo + hotel + comida


descuento = total * patrocinio


pago_final = total - descuento


porcentaje = (pago_final / presupuesto) * 100

print("\nCiudad:", ciudad)
print("Costo total antes del patrocinio:", total)
print("Monto del patrocinio:", descuento)
print("Total a pagar:", pago_final)
print("Porcentaje del presupuesto usado:", porcentaje, "%")
