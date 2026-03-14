
TipoHabitacion=input("Ingrese el tipo de habitación, (1 = estándar, 2 = ejecutiva, 3 = suite)")
Noches=int(input("Ingrese el número de noches"))
Extranjero=input("¿Es extranjero? (s/n)")
if Extranjero == "s":
    Extranjero = True  
else:    Extranjero = False
Temporada=input("¿Es temporada alta? (s/n)")
if Temporada == "s":
    Temporada = True   
else:    Temporada = False
Frecuente=input("¿Es cliente frecuente? (s/n)")
if Frecuente == "s":
    frecuente = True
else:
    frecuente = False



    

PrecioEstandar=450
PrecioEjecutiva=700
PrecioSuite=1200
aumento15= False
aumento10= False
descuento12= False
precioEstandarB=PrecioEstandar
precioEjecutivaB=PrecioEjecutiva
precioSuiteB=PrecioSuite

if TipoHabitacion == "1":
    precio = PrecioEstandar
elif TipoHabitacion == "2":
    precio = PrecioEjecutiva
elif TipoHabitacion == "3":
    precio = PrecioSuite
    
    
if TipoHabitacion == "3" and Temporada == True:
    precio=precio*1.15
    aumento15= True
    
if Extranjero == True and Temporada == True:
    precio=precio*1.10
    aumento10= True
    
if frecuente == True and Noches > 3:
  precio=precio*0.88   
  descuento12= True
    


if Noches > 7:
        precio=precio*0.95


    

if TipoHabitacion =="1":
    print("El subtotal a pagar por noche es: ", precioEstandarB*Noches)
elif TipoHabitacion == "2":
    print("El subtotal a pagar por noche es: ", precioEjecutivaB*Noches)
elif TipoHabitacion == "3":
    print("El subtotal a pagar por noche es: ", precioSuiteB*Noches)

if aumento15 == True:
    print("Se aplicó un aumento del 15% por ser temporada alta en habitación suite")
if aumento10 == True:
    print("Se aplicó un aumento del 10% por ser extranjero en temporada alta")
if descuento12 == True:
    print("Se aplicó un descuento del 12% por ser cliente frecuente y hospedarse más de 3 noches")
if Noches > 7:
    print("Se aplicó un descuento adicional del 5%(acumulable) por hospedarse más de 7 noches")
elif Noches <= 7 and descuento12 == False and aumento10 == False and aumento15 == False:
    print("No se aplicó ningún descuento adicional")


if TipoHabitacion == "1":
   print(f"El precio total a pagar es: {precio * Noches:.2f}")
elif TipoHabitacion == "2":
    print(f"El precio total a pagar es: {precio * Noches:.2f}")
elif TipoHabitacion == "3":
    print(f"El precio total a pagar es: {precio * Noches:.2f}")
