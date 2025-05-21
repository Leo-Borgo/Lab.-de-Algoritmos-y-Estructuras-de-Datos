def hacer_album(nombre, album, canciones=None):
    album = {
        "artista": nombre,
        "titulo": album
    }
    if canciones is not None:
        album["canciones"] = canciones
    
    return album

print(hacer_album("Anuel AA", "Emmanuel (2020)"))
print(hacer_album("Bad Bunny", "YHLQMDLG (2020)"))
print(hacer_album("Trueno", "Bien o Mal (2022)"))

print(hacer_album("Duki", "Desde el fin del mundo", canciones=10))
