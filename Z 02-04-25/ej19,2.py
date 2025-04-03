import os, time, random
os.system("cls")

menu = True
i = 0

while menu == True:
    os.system("cls")
    i += 1
    pal = input("Escriba salir o pulse enter: ")
    if i == 5:
        print("El bucle ha terminado!")
        menu = False
    if pal == "salir":
        print("Ha decidido romper el bucle!")
        break
