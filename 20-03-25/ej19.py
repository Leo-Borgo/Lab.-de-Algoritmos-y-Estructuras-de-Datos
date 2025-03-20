import time, os, random
os.system("cls")

colores = ["rojo", "amarillo", "verde", "blanco"]
eleccion = random.choice(colores)

time.sleep(1)

if eleccion == "verde":
    print("Has ganado 5 puntos!")
elif eleccion == "amarillo":
    print("Has ganado 10 puntos!")
elif eleccion == "rojo":
    print("Has ganado 15 puntos!")
else:
    print("No has ganado puntos!")
