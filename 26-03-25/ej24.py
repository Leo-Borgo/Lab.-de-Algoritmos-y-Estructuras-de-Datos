import os, time, random

usuarios_actuales = ["Messi", "MacAllister", "Einstein", "Leo", "Ronaldo"]
usuarios_nuevos = ["Alvarez", "Leo", "MacAllister", "Dibu", "Enzo Fernandez"]

usuario_mayus = [usuario.capitalize() for usuario in usuarios_actuales]

for usuario in usuarios_nuevos:
    if usuario in usuario_mayus:
        print("El nombre", usuario, "YA ESTA EN USO.")
    else:
        print("El nombre", usuario, "ESTA DISPONIBLE.")
