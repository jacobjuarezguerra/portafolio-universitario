
#Constantes y Variables para el cálculo de ingresos por reproducciones de canciones
pago=0.005
nombre=str(input("Ingrese el nombre de la cancion"))

numeror=int(input("Ingrese el numero de reproducciones"))

pagoporcentaje=float(input("Ingrese el porcentaje de pago al artista (en decimal)"))

#Cálculo de ingresos
ingresobruto=numeror*pago
ingresonetoart=ingresobruto*(pagoporcentaje)

#Resultados
print(f"El ingreso bruto por la canción '{nombre}' es: Q{ingresobruto:.2f}")
print(f"El ingreso neto para el artista por la canción '{nombre}' es: Q{ingresonetoart:.2f}")
#despedida xd asi es más amigable
print("Gracias por usar el programa de cálculo de ingresos por reproducciones de canciones.")