menu = True

def hacer_album(nombre, titulo, canciones=None):
    album = {
        "artista": nombre,
        "titulo": titulo
    }
    if canciones is not None:
        album["canciones"] = canciones
    return album

while menu == True:
    print("Ingresa los siguientes datos que te solicitamos (salir para abandonar el programa): ")

    nombre = input("Ingrese el nombre del artista: ")
    if nombre.lower() == "salir":
        print("Usted ha abandonado el programa!")
        break
    titulo = input("Ingrese el titulo del artista: ")
    if titulo.lower() == "salir":
        print("Usted ha abandonado el programa!")
        break
    canciones = input("Ingrese la cantidad de canciones (opcional, enter para omitir): ")
    if canciones.lower() == "salir":
        print("Usted ha abandonado el programa!")
        break

    if canciones:
        album = hacer_album(nombre, titulo, int(canciones))
    else:
        album = hacer_album(nombre, titulo)

print("Album creado: ", album)
