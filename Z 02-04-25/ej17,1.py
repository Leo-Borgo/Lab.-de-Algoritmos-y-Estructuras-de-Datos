import time, os, random
os.system("cls")

persona1 = {
    "nombre": "Mario",
    "apellido": "Borges",
    "edad": 61,
    "ciudad": "Villa Fiorito"
}
persona2 = {
    "nombre": "Diosito",
    "apellido": "Borges",
    "edad": 25,
    "ciudad": "Málaga"
}
persona3 = {
    "nombre": "Miguel",
    "apellido": "Palacios",
    "edad": 32,
    "ciudad": "La Plata"
}

gente = [persona1, persona2, persona3]

for diccionario in gente:
    print(diccionario)
