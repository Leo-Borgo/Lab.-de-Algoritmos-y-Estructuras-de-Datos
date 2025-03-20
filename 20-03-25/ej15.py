import time, os

numeros = []

os.system("cls")

for i in range(1, 10000001):
    numeros.append(i)

maximo = max(numeros)
print("El numero maximo de esta lista es el: ", maximo, "\n"), time.sleep(1)
minimo = min(numeros)
print("El numero minimo de esta lista es el: ", minimo, "\n"), time.sleep(1)
suma = sum(numeros)
print("La suma de todos los numeros de la lista es: ", suma, "\n"), time.sleep(1)
