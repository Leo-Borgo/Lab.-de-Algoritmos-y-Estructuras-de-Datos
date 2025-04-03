import os, time, random
os.system("cls")
ciudades = {
    "París": {
        "país": "Francia",
        "población": "2.165.000 habitantes",
        "dato": "Es conocida como la 'Ciudad de la Luz' y es famosa por su Torre Eiffel."
    },
    "Kyoto": {
        "país": "Japón",
        "población": "1.460.000 habitantes",
        "dato": "Antigua capital de Japón, famosa por sus templos y jardines tradicionales."
    },
    "Venecia": {
        "país": "Italia",
        "población": "260.000 habitantes",
        "dato": "Es famosa por sus canales y la Plaza de San Marcos."
    }
}

for ciudad, datos in ciudades.items():
    print(ciudad)
    for clave, valor in datos.items():
        print(clave,":", valor)