import os, time, random
os.system("cls")

# Escribí un programa que le pregunte a los usuarios sobre su destino de vacaciones soñado.
# Mostrá un mensaje como: Si pudieras visitar un lugar en el mundo, ¿a dónde irías? 
# Luego, incluí un bloque de código que imprima los resultados de la encuesta.

usuarios = ["Leo", "Jere", "Mario", "Jorge", "Ana"]
destinos_soñados = {}

for usuario in usuarios:
    destino_soñado = input(f"{usuario}, ¿cuál es tu destino soñado? ") 
    destinos_soñados[usuario] = destino_soñado  

print("\nResultados de la encuesta:")
for usuario, destino in destinos_soñados.items():
    print(f"{usuario} quiere ir a {destino}.")
