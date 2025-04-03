import os, time, random
os.system("cls")

prompt = "Hola"
prompt += "\nCual es tu nombre? "
nombre = input(prompt)
time.sleep(1)
print(f"Bienvenido {nombre}!")

cantidad = int(input("Cuantas personas son en su grupo? "))
time.sleep(0.5)
if cantidad > 8:
    print("Deberán de esperar por una mesa.")
else: 
    print("Tienen una mesa disponible.")
