import os, time, random
os.system("cls")

mascota1 = {
    "nombre": "Java",
    "tipo_animal": "perro",
    "dueño": "Eduardo"
}
mascota2 = {
    "nombre": "Ruby",
    "tipo_animal": "gato",
    "dueño": "Marta"
}
mascota3 = {
    "nombre": "Node",
    "tipo_animal": "lagarto",
    "dueño": "Carlos"
}

mascotas = [mascota1, mascota2, mascota3]

for diccionario in mascotas:
    print(diccionario)
