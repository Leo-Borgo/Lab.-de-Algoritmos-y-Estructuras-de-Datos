import os, time, random

Lista = []
i = 1

for i in range (10):
    i += i
    x = i
    y = x * 3
    if y == 10:
        print("Ha completado la mision")
        print("felicitaciones maquina".title()) #Reemplaza las inicilas de las palabras por letras mayusculas
    if y > 10:
        num = input("Seleccione un numero del 1 al 3\n")
        if num == "1":
            print("Numero 1")
        elif num == "2":
            print("Numero 2")
        elif num == "3":
            print("Numero 3")
        else: 
            print("Error, ERROR".removesuffix(", ERROR")) #Remueve el sufijo que uno desea