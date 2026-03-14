#Ejercicio 6
precio=float(input("Ingrese el precio del boleto"))
Dispo=float(input("Ingrese la cantidad de dinero disponible para comprar el boleto"))
Tipo=input("Ingrese el tipo de boleto (general o VIP)")
if Tipo=="VIP":
    precio=precio+precio*0.35
print(f"El precio del boleto es: {precio}")
descuento=("¿tiene descuento estudiantil? si/no")

if descuento=="si":
    descuento=0.2
else:
    descuento=0
    
    
falta = precio - Dispo
    
if Dispo>=precio:
        print("compra realizada")
else:
        print("No puedes comprar el boleto")
    
    
if falta > 0 and (falta / precio < 0.1):
        print("Te falta poco, considera ahorrar")
        
 #Ejercicio 7
nivel=int(input("Ingrese el nivel del jugador"))
misiones=int(input("Ingrese el número de misiones completadas"))
presicion=int(input("Ingrese el porcentaje de precisión en las misiones (0-100)"))
if nivel >= 20 and misiones >= 30 and presicion >= 80:
    print("Recompensa legendaria")
elif nivel >= 15 and misiones >= 20:
    print("Recompensa épica")
elif nivel >= 10:
    print("Recompensa basica")
else:
    print("Sigue entrenando")
    
#Ejercicio 8
edad=int(input("Ingrese su edad"))
Sub=input("Ingrese su suscripción (gratis,estandar o premium)")
Contparental=input("¿Tiene control parental? si/no")
if edad <13:
    print("solo puedes acceder a contenido para niños")
    
elif edad >=13 and edad <17 and Contparental=="si":
    print("Tu catalogo es PG13")
elif edad >=13 and edad <17 and Contparental=="no":
    print("Tienes catalogo infantil completo")
elif edad >=18 and Sub=="gratis":
    print("Tienes acceso limitado con anuncios")
elif edad >=18 and Sub=="estandar":
    print("Tienes acceso completo con anuncios")
elif edad >=18 and Sub=="premium":
    print("Tienes acceso completo sin restricciones")
    
#Ejercicio 9
promedio=float(input("Ingrese su promedio academico"))
Instrumento=input("Ingrese el instrumento que toca")
experiencia=int(input("Ingrese sus años de experiencia tocando el instrumento"))

if promedio< 80:
    print("No eres elegible")

if promedio >= 80 and (Instrumento=="guitarra" or Instrumento=="piano") and experiencia >= 3:
    print("Eres elegible para la banda principal")
elif promedio>=80 and Instrumento=="batería" and experiencia<3:
    print("Banda secundaria")

if promedio >= 80 and Instrumento=="bajo"or Instrumento=="batería" and experiencia >= 2:
    print("Eres elegible para la sección rítmica oficial")
elif promedio>=80 and Instrumento=="batería" and experiencia<2: 
    print("audicion adicional requerida")


if promedio >= 80 and Instrumento not in ["guitarra", "piano", "bajo", "batería"]:
    print("Eres elegible para la lista de espera")
#Ejercicio 10

puntaje=int(input("Ingrese su puntaje total"))
partidas=int(input("Ingrese el número de partidas"))
victorias=int(input("Ingrese el porcentaje de victorias"))
equipo=input("¿Pertenece a equipo profesional? (sí/no)")
if puntaje < 1500:
    print("Jugador amateur")
elif puntaje >= 1500:
    if partidas >= 20:
        if victorias >= 75:
            if equipo == "sí":
                print("Profesional élite")
            else:
                print("Profesional independiente")
        elif victorias >= 50:
            print("Competitivo avanzado")
        else:
            print("Jugador en desarrollo")
    else:
        print("Datos insuficientes")
        
