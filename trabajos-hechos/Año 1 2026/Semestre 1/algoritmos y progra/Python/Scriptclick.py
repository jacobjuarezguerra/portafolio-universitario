import pyautogui
import time
#script para clickear en la pantalla una cantidad de veces
num_clicks = int(input("¿Cuántos clicks desea realizar? "))
pyautogui.PAUSE = 0.1  # Pausa entre clicks para evitar problemas de velocidad
print("Tenga 5 segundos para posicionar el cursor en el lugar donde desea hacer los clicks.")
pyautogui.sleep(5)  # Espera 5 segundos para que el usuario pueda posicionar el cursor
for i in range(num_clicks):
    pyautogui.click()  # Realiza un click
print(f"Se han realizado {num_clicks} clicks.")
