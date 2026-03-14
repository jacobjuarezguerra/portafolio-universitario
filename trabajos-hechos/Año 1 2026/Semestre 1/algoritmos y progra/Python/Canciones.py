
num_canciones = int(input("¿Cuántas canciones escuchará hoy? "))
for i in range(num_canciones):
    nombre_cancion = input(f"Ingrese el nombre de la canción {i + 1}: ")
    print(f"Escuchando {nombre_cancion}")
print("sesion finalizada")