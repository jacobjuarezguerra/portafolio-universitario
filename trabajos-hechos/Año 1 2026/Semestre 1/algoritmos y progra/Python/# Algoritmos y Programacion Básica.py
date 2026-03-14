# Algoritmos y Programacion Básica
# fecha: 3 de febrero 2019
# descripcion: variables y expresiones en python
# Guardar distintos tipos de valores en las variables
numero_entero = 5
numeroReal = 99.99
texto = "Programar es divertido"
#Mostrar los tipos de las variables utilizando la funcion print()
print (""" "TIPOS DE DATOS" """)
print ("La variable numero_entero tiene el valor ", numero_entero)
print ("Su tipo es ", type(numero_entero))
print ("La variable numeroReal tiene el valor ", numeroReal)
print ("Su tipo es ", type(numeroReal))
print ("La variable texto tiene el valor ", texto)
print ("Su tipo es ", type(texto))
#Entrada de datos dentro del programa
num = int(input("Ingrese un numero entero: "))
print ("La variable num tiene el valor ",num)
print ("Su tipo es ", type(num))
#Convertir num al tipo float
num = float(num)
print ("La variable num tiene el valor ",num)
print ("Su tipo es ", type(num))
#Convertir num al tipo string o texto
num = str(num)
print ("La variable num tiene el valor ",num)
print ("Su tipo es ", type(num))
#Calcular el area de un cuadrilatero
print(""" "CALCULAR EL ÁREA DE UN CAUDRILATERO" """)
#pedir datos:
base = input("Ingrese el tamaño de la base: ")
base = float(base)
altura = input("Ingrese el tamaño de la altura: ")
altura = float(altura)
area = base * altura
#mostrar el resultado
print ("El area del cuadrilatero es: ",area)