
#comentario porque si
numPag=(int)(input("Ingrese el numero de paginas: "))
PrecioPag=(float)(input("Ingrese el precio por pagina: "))
CostoTotal=numPag*PrecioPag
print("El costo total es: ",CostoTotal)

TemperaturaF=(float)(input("Ingrese la temperatura en grados Fahrenheit: "))
TemperaturaC=(TemperaturaF-32)*5/9
print("La temperatura en grados Celsius es: ",TemperaturaC)

Montodelacompra=(float)(input("Ingrese el monto de la compra: "))
TipodePago=(int)(input("Ingrese el tipo de pago (1-efectivo, 2-tarjeta, 3-cheque): "))
if Montodelacompra>=150 and TipodePago==1:
    Descuento=0.15 
    print("El descuento es: ",Descuento*100,"%")
    print("El monto a pagar es: ",Montodelacompra*(1-Descuento))
elif Montodelacompra>=150 and TipodePago==2:
    Descuento=0.10
    print("El descuento es: ",Descuento*100,"%")
    print("El monto a pagar es: ",Montodelacompra*(1-Descuento))
elif Montodelacompra>=150 and TipodePago==3:
    Descuento=0
    print("No hay descuento")
    print("El monto a pagar es: ",Montodelacompra)
else:
    Descuento=0
    print("No hay descuento")
    print("El monto a pagar es: ",Montodelacompra)